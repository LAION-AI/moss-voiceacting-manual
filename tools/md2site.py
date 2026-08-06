#!/usr/bin/env python3
"""Render a manual Markdown page into the site's HTML style.

The manual keeps an agent-readable Markdown mirror of every page. Until now both halves were
written by hand, which is how they drift apart. This renders `md/**/x.md` -> `site/**/x.html`
in the existing dark style, so the mirror is generated rather than maintained.

Deliberately a small subset -- headings, tables, lists, blockquotes, hr, inline bold/code/links.
That is everything the pages actually use. It is not a general Markdown implementation and does
not try to be: anything it does not recognise passes through as a paragraph, which is visible
rather than silent.

  python3 tools/md2site.py md/recipes/foo.md site/recipes/foo.html "Page title"
"""
import html
import os
import re
import sys

CSS = """body{font-family:system-ui,Segoe UI,Arial;background:#0e1117;color:#e6edf3;margin:0 auto;
padding:30px;max-width:1000px;line-height:1.6}
a{color:#58a6ff}h1{margin:0 0 6px;font-size:27px}h2{margin:30px 0 8px;font-size:20px;
border-bottom:1px solid #21262d;padding-bottom:5px}h3{margin:20px 0 6px;font-size:16px;color:#c9d6e4}
.lead{color:#8b949e;font-size:14px}
code{background:#161b22;border:1px solid #30363d;padding:1px 5px;border-radius:4px;font-size:12.5px}
table{border-collapse:collapse;width:100%;font-size:13px;margin:10px 0;display:block;overflow-x:auto}
td,th{border:1px solid #30363d;padding:6px 9px;text-align:left;white-space:nowrap}
th{color:#8b949e;font-weight:600;background:#161b22}
td.n,th.n{text-align:right;font-variant-numeric:tabular-nums}
blockquote{background:#161b22;border-left:3px solid #58a6ff;border-radius:0 8px 8px 0;
margin:12px 0;padding:9px 15px;color:#c7cdda;font-size:13.5px}
ul{padding-left:22px}li{margin:6px 0;font-size:14px}
hr{border:0;border-top:1px solid #21262d;margin:26px 0}
em{color:#a9b6c6}
.dose-row{border:1px solid #30363d;border-radius:10px;padding:10px 12px;margin:12px 0;background:#12161d}
.dclass{font-weight:700;font-size:14px;margin-bottom:7px;color:#e6edf3}
.dcols{display:grid;grid-template-columns:repeat(4,1fr);gap:9px}
.dcol{border:1px solid #263041;border-radius:8px;padding:8px;background:#0f141b}
.dcol.rec{border-color:#2f6f4f;background:#101d16}
.dcol.bad{border-color:#6b3a3a;background:#1a1210}
.dh{font-size:12px;font-weight:700;color:#c9d6e4;margin-bottom:2px}
.dcol.rec .dh{color:#7fd8a4} .dcol.bad .dh{color:#ff9c9c}
.dm{font-size:10.5px;color:#8b949e;margin-bottom:6px;font-variant-numeric:tabular-nums}
.dcol audio{width:100%;height:28px;display:block;margin-top:4px}
.mm{font-size:10px;color:#8b949e;font-variant-numeric:tabular-nums}"""

INLINE = (
    (re.compile(r"`([^`]+)`"), lambda m: f"<code>{html.escape(m.group(1))}</code>"),
    (re.compile(r"\[([^\]]+)\]\(([^)]+)\)"), lambda m: f'<a href="{m.group(2)}">{m.group(1)}</a>'),
    (re.compile(r"\*\*([^*]+)\*\*"), lambda m: f"<b>{m.group(1)}</b>"),
    (re.compile(r"(?<!\*)\*([^*]+)\*(?!\*)"), lambda m: f"<em>{m.group(1)}</em>"),
)


def inline(s):
    # Escape first, then re-introduce markup, so raw < and & in the source stay literal.
    s = html.escape(s, quote=False)
    for pat, rep in INLINE:
        s = pat.sub(rep, s)
    return s


def is_sep(line):
    return bool(re.fullmatch(r"\|[\s:|-]+\|", line.strip()))


def cells(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def render(md):
    out, i, lines = [], 0, md.split("\n")
    while i < len(lines):
        ln = lines[i]
        s = ln.strip()

        if not s:
            i += 1
            continue

        # raw HTML passthrough: a line starting with <div/<audio/<table is emitted verbatim, so a
        # page can carry embedded audio players that Markdown cannot express (GitHub strips
        # <audio>, so the .md keeps links and the generated .html keeps the players)
        if s.startswith(("<div", "<audio", "<table", "<section", "<!--HTML")):
            buf = []
            while i < len(lines) and lines[i].strip():
                buf.append(lines[i])
                i += 1
            out.append("\n".join(buf))
            continue

        if s.startswith("#"):
            lvl = len(s) - len(s.lstrip("#"))
            out.append(f"<h{lvl}>{inline(s[lvl:].strip())}</h{lvl}>")
            i += 1
            continue

        if re.fullmatch(r"-{3,}", s):
            out.append("<hr>")
            i += 1
            continue

        # table: a header row followed by a |---|---| separator
        if s.startswith("|") and i + 1 < len(lines) and is_sep(lines[i + 1]):
            head = cells(s)
            # right-align a column when the markdown alignment marker says so
            aligns = ["n" if c.strip().endswith(":") and c.strip().startswith("-") is False
                      and ":" in c else "" for c in cells(lines[i + 1])]
            rows = []
            i += 2
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append(cells(lines[i]))
                i += 1
            th = "".join(f'<th class="{a}">{inline(c)}</th>' for c, a in zip(head, aligns))
            body = "".join(
                "<tr>" + "".join(f'<td class="{a}">{inline(c)}</td>'
                                 for c, a in zip(r, aligns + [""] * len(r))) + "</tr>"
                for r in rows)
            out.append(f"<table><tr>{th}</tr>{body}</table>")
            continue

        if s.startswith(">"):
            buf = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                buf.append(lines[i].strip().lstrip(">").strip())
                i += 1
            out.append(f"<blockquote>{inline(' '.join(buf))}</blockquote>")
            continue

        if re.match(r"^[-*] ", s):
            buf = []
            while i < len(lines):
                t = lines[i].strip()
                if re.match(r"^[-*] ", t):
                    buf.append(inline(t[2:]))
                elif t and lines[i].startswith(("  ", "\t")) and buf:
                    buf[-1] += " " + inline(t)          # continuation line
                else:
                    break
                i += 1
            out.append("<ul>" + "".join(f"<li>{b}</li>" for b in buf) + "</ul>")
            continue

        buf = []
        while i < len(lines) and lines[i].strip() and not re.match(
                r"^(#|\||>|[-*] |-{3,})", lines[i].strip()):
            buf.append(lines[i].strip())
            i += 1
        out.append(f"<p>{inline(' '.join(buf))}</p>")
    return "\n".join(out)


def main():
    src, dst = sys.argv[1], sys.argv[2]
    title = sys.argv[3] if len(sys.argv) > 3 else os.path.basename(src)
    depth = dst.count("/") - 1                  # site/x.html -> 0, site/recipes/x.html -> 1
    up = "../" * depth
    body = render(open(src).read())
    doc = (f'<!doctype html><html lang=en><head><meta charset=utf-8>'
           f'<meta name=viewport content="width=device-width,initial-scale=1">'
           f'<title>{html.escape(title)}</title><style>{CSS}</style></head><body>\n'
           f'<p><a href="{up}index.html">← Manual hub</a></p>\n{body}\n</body></html>\n')
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    open(dst, "w").write(doc)
    print(f"{src} -> {dst} ({len(doc)/1000:.1f} kB)")


if __name__ == "__main__":
    main()
