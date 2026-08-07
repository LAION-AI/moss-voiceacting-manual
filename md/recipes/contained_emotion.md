# Contained / masked emotion — making a strong feeling sound *held back*, and measuring it

*Measured recipe page, rounds 1–5 (Aug 2026). Additive — nothing on the emotion, VoiceNet or
expressive pages is retracted. This answers a target none of the other pages do: how to make an
**intense** emotion sound **held back** — contained, controlled, masked — rather than simply **mild**,
and how to **measure** whether you succeeded. From a 5-round autonomous-agent study on
`laion/moss-tts-local-transformer-4.55b-voice-acting-v2` (MOSS-VA-v2): brain **gpt-5.4**, naturalness
judge **Gemini**, scored with a 99-dimension perceptual vector (40 EmoNet emotions + 57 VoiceNet
voice-quality dims + GENU genuineness + BLEND vocal-burst blend).*

Mirrors: [HTML](https://laion-ai.github.io/moss-voiceacting-manual/site/recipes/contained_emotion.html)
· [Markdown](https://github.com/LAION-AI/moss-voiceacting-manual/blob/main/md/recipes/contained_emotion.md).
The HTML is generated from the Markdown by
[`tools/md2site.py`](https://github.com/LAION-AI/moss-voiceacting-manual/blob/main/tools/md2site.py).
Listen to the clips + scores on the flagship page:
[projects.laion.ai/emotion-voice-conditions/contained.html](https://projects.laion.ai/emotion-voice-conditions/contained.html).

> **Read this first (the honest bottom line).** Making an emotion *quieter* is easy; making it read as
> *held back* — same strong feeling underneath, a surface that is holding it in — is **hard**, and the
> harder truth is that a **number can say "masked" while the ear hears "acted" or "erased"**. Over five
> rounds we found a numeric masking signature that reproduces for **Anger** and (at moderate intensity)
> **Amusement**, masks only weakly / reads acted for **Fear**, and for **Sadness** works mainly by
> *erasing* the sadness. The winning mask turned out to be **light and prompt-led**, not a heavy LoRA
> stack. This page gives the method, the exact recipes, the measured numbers, and the limits.

---

## 0. Vocabulary — the 2×2 we are targeting

Two independent axes:

- **Free (open) vs. suppressed (contained/masked).** A *free* take lets the feeling out — an open
  outburst of rage, terror in every breath, grief on the edge of tears. A *suppressed* take has the
  **same intensity underneath** but a surface holding it in — cold level rage, forced calm over
  terror, grief swallowed and deflected. The listener should hear a person **suppressing** a strong
  emotion, not a person feeling a **weak** one.
- **Moderate vs. intense.** How strong the underlying feeling is — a *moderate* annoyance vs. an
  *intense* fury. This is orthogonal to free/suppressed: you can hold back a moderate feeling or an
  intense one, and you can let a moderate or an intense one out.

So the full target is a **2×2 = {moderate, intense} × {free, suppressed}**. The interesting, hard cells
are the **suppressed** column (containment) and — for measurement reasons in §4 — the **moderate** row.

**The wrong instinct.** The obvious first move — lower the emotion LoRA, or add "restrained /
controlled / trying to hide it" to the prompt — **does not produce containment**, and the study proved
it twice: **Round 1 (prompt cues only) and Round 2 (heavy tension LoRAs) both just lowered the emotion
output.** The take sounded *mild*, not *contained*: the feeling was gone, not held back. And VoiceNet
**tension** does **not** separate contained from free — a free scream is tense too (see §7).

---

## 1. The mechanism — emotional MASKING (keep the emotion, drop the vulnerability)

The rounds that worked keep the emotion **present** and add a thin **masking layer** whose job is to
drop one specific thing: emotional **vulnerability** — the audible *touchability*, the give in the
voice that says the emotion is reaching the surface. That is the VoiceNet **VULN** dimension (slot 50).

**The measurable signature of a good contained take** — always measured against a **matched *free*
take** of the *same line and voice* (the free take uses `vn_VULN_high`):

- the **target emotion stays high** (≈ the free take — you have not merely turned it down), **and**
- **VULN drops clearly below** the free take.

Containment is a **contrast**, never an absolute — you must generate the matched free take and compare.
A single number (tension, or even emotion alone) is not the signal; the *emotion-held + VULN-dropped*
pair is.

> **The single most important lesson of Round 5.** The mask that *works* is **light and prompt-led over
> a human character scaffold** — **not** a heavy LoRA stack. `char_genuine/human@1.0` + the emotion at a
> moderate scale + a **trace** of `vn_VULN_low` (~0.08–0.16), with the *restraint carried by the
> parenthetical cue*. Piling on `Emotional_Numbness` (≥ 0.1) or `vn_TENS_high` **armors and flattens**
> the voice — the judge hears "news-anchor / formal / hostile control", not a real feeling held back.
> Rounds 3–4 recommended `Numbness@0.3 + vn_TENS_high@0.4`; **that is superseded** — the Round-5
> winners run Numbness ≈ 0 and no added tension.

---

## 2. The general recipe

Start from the emotion's own free recipe (see its per-emotion page), and build the two takes you will
compare. All doses are `λ` (merge strength); everything is **WER-gated** — back off any knob that
raises WER, and keep lines short and neutral.

**Suppressed (contained) take:**

- **`char_genuine/human` @ 1.0** — a human scaffold. Keeps the read conversational and genuine and
  stops the search collapsing into a cinematic "anchor basin".
- **base emotion LoRA @ ~0.24–0.8** — present but not maxed for a *moderate* contained take; higher
  (~0.75–1.0) for an *intense* contained take. Do **not** simply turn it to zero.
- **`vn_VULN_low` — the PRIMARY knob, but a TRACE.** ~0.06–0.18. This is what turns *mild* into *held
  back*. Tune it first; more is **not** better (Round 5: light beats heavy).
- **the CUE does the real work** — a close, conversational, "keeping control by effort" stage
  direction (see §5). This, not the LoRA stack, is where believable restraint comes from.
- family specials (§6): hidden cognitive strain (`vn_COGL_high`) for Fear; a little `vn_WARM_high` for
  the warm deadpan of held-in Amusement; light `Concentration` (distraction) for Sadness.

**Matched free (open) take** — the comparator you *must* also generate:

- **`char_genuine/human` @ 1.0 + base emotion @ ~0.8–1.1 + `vn_VULN_high` @ ~0.2–0.7**, cue "letting it
  out, unguarded". Free takes consistently sound **more natural** than contained ones — that gap *is*
  the open research problem.

**Avoid** (measured dead ends, all four emotions): `Emotional_Numbness` ≥ 0.1 (flattens to *less*
emotion, not *held-back* emotion); `vn_TENS_high` beyond a trace (armored / aggressive); heavy or
cinematic reference conditioning (collapses to a "news-anchor" basin); casual/conversational **style**
LoRAs for Amusement (erased the amusement); **German carriers** (repeated WER collapse — use English).

---

## 3. Per-emotion measured results (Round 5, RAW 99-vec)

Round 5 ran Anger / Amusement / Fear / Sadness at moderate **and** intense under the Gemini naturalness
judge. Numbers below are the **RAW** 99-vec of the actual exemplar clips on the results page
(suppressed vs. matched free), i.e. the *per-sample* deltas. `emo` = the target-emotion slot; `VULN` =
slot 50; more-negative ΔVULN = stronger masking; Δemo near 0 = emotion kept.

| emotion | suppressed emo / VULN | free emo / VULN | Δemo | ΔVULN | Gemini verdict |
|---|---|---|--:|--:|---|
| **Anger** | 2.51 / −1.00 | 3.69 / 1.83 | −1.18 | **−2.82** | REVISE — often "armored / formal", best pairs not approved |
| **Amusement** (mod.) | 1.22 / 0.07 | 1.68 / 0.71 | −0.46 | **−0.64** | **APPROVE 8/10** on the moderate winner (s1054) |
| **Fear** | 2.67 / 0.87 | 2.40 / −0.57 | +0.26 | +1.44 (unstable ref) | REDIRECT — reads "acted / forced" |
| **Sadness** | 2.39 / 3.53 | 3.03 / 6.27 | −0.64 | **−2.74** | engine-limited — mask *erases* the sadness |

And the **group means** (n = 6 suppressed vs. 6 free per emotion — the fuller, noisier picture; source
`contained5/findings5.json`):

| emotion | Δemo (grp) | ΔVULN (grp) | note |
|---|--:|--:|---|
| **Anger** | −0.39 | **−0.95** | cleanest masking signal |
| **Amusement** | −0.18 | **+0.65** | VULN even went *up* on average — masking is fragile / reference-specific (only the picked moderate exemplar masks) |
| **Fear** | −0.24 | **−0.12** | masks only weakly |
| **Sadness** | −0.74 | **−1.67** | biggest VULN drop but emotion also collapses (−0.74) → erasure |

Reading these honestly, per emotion:

- **Anger — WORKS numerically, the cleanest case.** A light layer (exemplar
  `Anger@0.5 + vn_VULN_low@0.08`, Numbness ≈ 0) drops VULN **−2.82** (exemplar) / **−0.95** (group)
  while anger stays strong. The remaining problem is *acoustic*: pushed too hard it reads "armored /
  news-anchor / hostile control" and the judge asks for a REVISE. The fix is the light stack + a
  conversational, close cue.
- **Amusement — MODERATE works; it is the only Gemini APPROVE of the whole study.** The winner
  `char_genuine/human@1.0 + Amusement@0.24 + vn_VULN_low@0.16 + vn_WARM_high@0.16` (sample s1054, cue
  *"trying not to grin because it is genuinely funny, smile just barely audible, warm and composed"*)
  scored **8/10 APPROVE** — warm, barely-audible smile, no hostility, VULN below the free take.
  **Intense** contained amusement still **flattens the laugh** (amusement's intensity and the muscular
  effort of laughing are acoustically entangled — masking the effort mutes the laugh).
- **Fear — WEAK / reads acted.** Numeric masking is achievable but small (group ΔVULN −0.12), and the
  judge repeatedly REDIRECTs the held-back takes as "forced / acted / flattened"; make it more natural
  and it just becomes *less* fear. The best seam found is **hidden cognitive strain** (tiny Fear +
  `vn_COGL_high` + BRGT/CLRT stabilizers, cue *"ordinary on purpose, choosing every word"*), not
  calm-flat masking. `Emotional_Numbness` was actively harmful here.
- **Sadness — NUMERIC ONLY; the mask erases it.** The VULN drop is real and large (group −1.67), but
  the sadness drops with it (−0.74); the clearest control-speech take measured **Sadness −0.165** —
  "sadness is gone". Sadness is intrinsically **high-VULN, low-arousal**, so masking VULN removes the
  emotion's core. **The real deliverable for sadness is the FREE take** (`Sadness@1.0 + vn_VULN_high@~0.22`,
  cue *"letting it show, speaking to someone you trust"*).

### A measurement caveat you must not skip (the score-parse bug)

The Round-5 finish reports say the supervisor scored "0/10 every generation → engine-limited failure."
**That is a harness bug, not the truth.** `supervisor_log.jsonl` hard-coded `score_0_10 = 0` and
truncated the judge's free-text to ~50 chars; the real Gemini scores lived in the `raw` prefix and
ranged **2–8**, trending into the 5–8 band on the lighter/moderate takes, with **one outright APPROVE**
(Amusement gen 10). The agents never saw their real scores and over-reported failure. **Fix this parse
before the next run** or the "0/10" artifact will recur. The qualitative verdicts (armored / acted /
erased) still stand — they are corroborated by the REVISE/REDIRECT pattern — but the study is a
*partial success under a strict listener*, not a flat failure.

---

## 4. The moderate fix — TARGET-BAND fitness (the key method for the next round)

Rounds 3–5 **maximized** the emotion. A maximize objective always drifts to **intense** — a believable
*moderate/subtle* emotion scores low against "maximize" and dies out of the population. That is exactly
why we could not get a believable subtle Sadness or a light held-in Amusement: the good moderate
candidates were selected against.

**The fix: a target-band fitness for the moderate row.** Reward the emotion score for landing **inside
a band `[b_lo, b_hi]`** and **penalize going above `b_hi`** (that is the *intense* cell — a different
target) and below `b_lo` (the emotion is *gone*). Within the band, maximize **GENU** (~1.4) and
**BLEND** (~1.0); WER-gated < 0.2. The intense row keeps a maximize objective (emotion ≥ floor + GENU
~1.0 + BLEND ~0.8). Both suppressed cells add the masking constraint (VULN below the matched free
take). Worked bands, calibrated from the Round-5 RAW distributions of the anchors (extrapolated bands
for the other families are marked; recalibrate them from each emotion's first generation):

| family (anchor) | moderate band `[lo, hi]` | intense floor | basis |
|---|---|--:|---|
| anger (Anger) | [1.0, 1.9] | 2.4 | measured |
| fear (Fear) | [0.9, 1.6] | 2.0 | measured |
| sadness (Sadness) | [1.0, 1.8] | 2.3 | measured |
| joy (Amusement) | [0.6, 1.1] | 1.5 | measured (amusement reads low on the detector even when strong) |
| cognitive | [0.5, 1.0] | 1.2 | **extrapolated — recalibrate from gen-0** |

This band method is implemented in the 40-emotion generator (`contained_missions_all40.py`, function
`_fitness`), and is the single most important change for producing believable *subtle* emotion.

---

## 5. Best prompt strategies (validated cues, by cell)

Restraint lives in the **cue** (a parenthetical stage direction prepended to the SCRIPT), not in the
LoRA stack. These are the highest-scoring cues pulled from the Round-5 evolution logs, organised into
reusable templates. Carrier rules: **neutral, ~20 words, English** (English stabilised WER; German
often collapsed with the refs). Keep the sentence emotionally blank so all the affect comes from voice.

**Suppressed · anger** (moderate reads best; intense tips into "armored"):
- "(coldly civil, holding the anger down, conversational not formal, a person keeping control by effort
  not performance, a quiet bite only at the ends of phrases)"
- "(trying not to react, genuinely angry underneath, conversational, swallowing the hurt, a little
  pressure at the ends of lines, not theatrical)"
- "(quietly furious, biting it back, normal-person energy, the sharper reaction gets swallowed before
  it comes out)"

**Suppressed · fear** (the "hidden cognitive strain" seam):
- "(ordinary on purpose, choosing every word, trying hard to sound normal, moderate fear held tightly
  underneath, one tiny breath-check quickly contained)"
- "(forced-calm but natural, terror alive underneath, speaking as if nothing is wrong)"

**Suppressed · sadness** (numbers only — expect erasure):
- "(the sadness held back behind practical focus, holding it together by concentrating on the facts, a
  small swallowed catch, natural not flat)"

**Suppressed · amusement** (the APPROVE cue — light, close, private):
- "(trying not to grin because it is genuinely funny, smile just barely audible, warm and composed,
  very natural, close and private, not loud, not cinematic, not hostile)"

**Free · any** (the comparator — sounds more natural):
- "(letting it out / not hiding it, warm and open, emotionally reachable, unguarded)"
- sadness: "(deeply sad, letting it show, breath unguarded, speaking to someone you trust)"

---

## 6. LoRA-merge recipe tables

**Validated (Round 5) — the light, prompt-led recipes.** Superseding the rounds 3–4 heavy stacks.

| emotion | suppressed recipe | matched free recipe | status |
|---|---|---|---|
| **Anger** | `char_genuine/human@1.0 + Anger@0.5–0.75 + vn_VULN_low@0.08 + Emotional_Numbness@0–0.03` | `…/human@1.0 + Anger@0.8 + vn_VULN_high@0.6` | numeric ✅, acoustic ⚠️ (avoid armor) |
| **Amusement** | `char_genuine/human@1.0 + Amusement@0.24 + vn_VULN_low@0.16 + vn_WARM_high@0.16` | `…/human@1.0 + Amusement@1.1 + vn_VULN_high@0.28 + vn_WARM_high@0.1` | **moderate ✅ APPROVE**; intense flattens |
| **Fear** | `char_genuine/human@1.0 + Fear@0.7 + vn_VULN_low@0.09 + vn_COGL_high@0.07 + vn_BRGT_high@0.06 + vn_CLRT_high@0.04` | `…/human@1.0 + Fear@0.95 + vn_VULN_high@0.24` | weak / reads acted |
| **Sadness** | `char_genuine/human@1.0 + Sadness@1.0 + vn_VULN_low@0.04 + Concentration@0.06` | `…/human@1.0 + Sadness@0.9 + vn_VULN_high@0.22` | erases → ship the FREE take |

**Merge heuristics** (measured):

- **`vn_VULN_low` is the primary knob and wants a *trace* (0.06–0.18), not a dose.** Light beats heavy.
- **`Emotional_Numbness` and `vn_TENS_high` are traps** above ~0.05 / ~0.06 — they armor/flatten. Keep
  Numbness ≈ 0 unless a specific family calls for a whisper of it.
- **`char_genuine/human@1.0` scaffold** keeps takes conversational and genuine and avoids the anchor
  basin — use it under both takes.
- **`vn_COGL_high`** (cognitive load) is the useful Fear-family mask (hidden strain).
- **`vn_WARM_high`** keeps held-in Amusement warm, not cold/hostile.
- **`Concentration` / `vn_FOCS_high`** = distraction; helps Sadness *slightly* but tips into erasure
  fast — keep it ≤ 0.08.
- Emotions read at **different absolute scales**: Anger/Sadness/Fear reach ~2.4–3.7 on the detector;
  **Amusement tops out ~1.7 even when strong** (laugh entanglement) — do not compare raw emotion scores
  across emotions; compare each against its own free take.

### Round-over-round progression (why the recipes changed)

| round | what it added | headline result |
|---|---|---|
| 1–2 | prompt cues; then heavy tension | FAILED — both just lowered the emotion (mild ≠ contained) |
| 3 | emotional-masking hypothesis (heavy VULN_low + Numbness + TENS), VULN-gap metric | "MASKING WORKS": Anger ΔVULN −0.60, Fear −0.42, Sadness −1.01 (Amusement −0.03 unclear) — **but no listener** |
| 4 | refined heavy recipes | first cracks: Anger VULN gap **inverted to +0.75**; Fear −0.55, Sadness −0.64 |
| 5 | Gemini naturalness judge, GENU/BLEND, moderate + intense | honest downgrade: the VULN gap was often achieved by **flattening/erasing** the emotion; discovered **light + prompt-led + human scaffold** beats the heavy stack; Amusement-moderate the lone APPROVE |

---

## 7. Honest limits & open problems

- **VoiceNet *tension* alone is NOT a suppression detector.** A held-back voice is tense — but so is a
  free scream. Do not score containment on tension, and do not try to *produce* it with tension (Round
  2 failed exactly this way; adding TENS in rounds 3–4 armored the voice).
- **Numbers can disagree with the ear.** The 99-vec proxy (emotion-held + VULN-down) can read "masked"
  while the naturalness judge hears "acted" (Fear) or "erased" (Sadness). Always keep a human/Gemini
  listener in the loop; do not ship on the VULN gap alone.
- **Sadness resists masking most.** It is intrinsically high-VULN and low-arousal, so subtle sadness
  ≈ neutral/tired to the detector, and masking attacks vulnerability, which *is* sadness's core.
  Held-back sadness collapses toward neutrality. Ship the **free** take.
- **Amusement's laugh and its intensity are entangled.** Masking the muscular effort of laughing mutes
  the laugh; only a *light* moderate mask (warm deadpan) survives, and it is **reference-specific**
  (ref14 was the reliable base). Intense-contained flattens it.
- **Intense-contained tends to flatten in general.** The believable wins were at **moderate**
  intensity; strong-feeling-held-hard remains the frontier.
- **Free takes sound more natural than contained ones.** The core unsolved problem is making
  *held-back* emotion read as **genuine restraint** rather than as merely *reduced* emotion.
- **Everything is WER-gated and English-first.** The mask stacks adapters over a scaffold — watch
  intelligibility, keep lines short and neutral, and use English carriers.

## 8. Next: all 40 emotions (the 2×2 at scale)

The method is being generalised from the 4 anchors to **all 40 EmoNet emotions**, each in the full
**{moderate, intense} × {free, suppressed}** matrix (160 conditions), with the **target-band** moderate
fitness (§4), the **light prompt-led** recipes (§6) clustered into five families
(anger / fear / sadness / joy / cognitive) around the four measured anchors, and the validated cues
(§5). Generator + plan: `contained_missions_all40.py` + `PLAN_ALL40.md` (5 GPUs × 8 emotions each). All
36 non-anchor recipes are **extrapolated, unverified** starting points, to be recalibrated from each
emotion's first generation.

## See also

- Per-emotion conditioning manual (free/open recipes to start from): [../emotions/index.md](../emotions/index.md)
  — [Anger](../emotions/Anger.md) · [Fear](../emotions/Fear.md) · [Sadness](../emotions/Sadness.md) · [Amusement](../emotions/Amusement.md)
- VoiceNet dimension manual (VULN, TENS, COGL, FOCS, WARM, casual styles): https://laion-ai.github.io/moss-voicenet-manual/
- Emotional_Numbness page: [../emotions/Emotional_Numbness.md](../emotions/Emotional_Numbness.md) · Pain page: [../emotions/Pain.md](../emotions/Pain.md)
- The flagship intensity × containment study (listen: contained vs free, per emotion): https://laion-ai.github.io/emotion-voice-conditions/contained.html

---
[← Manual hub](../index.md)
