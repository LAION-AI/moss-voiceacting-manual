# Prompt notation — brackets, capitals, and how long a line has to be

**New (Aug 2026).** Four notation rules that are not style preferences: each one was violated in a
shipped run and each violation was measurable. If you write prompts for
`moss-tts-local-transformer-4.55b-voice-acting-v2`, this page is the shortest thing in the manual
that will stop you losing a run.

> **The rules, in one block.**
>
> ```
> GENERAL: <the standing description of the voice and the situation>
> SCRIPT:
> (delivery cue) "the spoken line, (burst) with tags inline, [pause] and pauses in squares"
> ```
>
> 1. **Round brackets** carry delivery cues *and* vocal bursts: `(quietly, with lethal control)`,
>    `(screams)`. This is the only inline notation the model was trained on.
> 2. **Square brackets** carry pauses: `[pause]`, `[long pause]`. Never put one directly after a
>    burst — that is the truncation shape (see
>    [bursts & merging](bursts_merging_evaluation.html)).
> 3. **Never capitalise a tag.** `(SCREAM)` is read out as "ess see arr ee ay em". Lowercase
>    everything inside brackets.
> 4. **Give the line enough words.** At ~2.8 words/s a line under 8 words cannot fill three
>    seconds however slowly it is read. Ten words is the working minimum.

---

## 1. Round brackets, not angle brackets

Every worked example in this manual —
[all 351 verbatim captions](acting/prompts.html) — uses round brackets:

```
SCRIPT:
(a broken breath turning into a controlled eruption) "Don't you dare touch me." (screams) "You
don't get to cry now."
```

A pipeline of ours emitted `<sobs>` instead for one full round of the voice-profile corpus. That
was wrong twice over, and the second way is the expensive one:

- **The model does not act on it.** The angle form is not the trained notation, so the tag is at
  best ignored and at worst spoken.
- **It corrupted the SCORING.** The WER reference strips `\([^)]*\)` — round brackets — before
  comparing against ASR. An angle-bracket tag therefore stayed *in* the reference string, so every
  burst-tagged take was charged word-error for failing to pronounce "sobs". Reward is multiplied
  by `(1 − WER)`, so the ranker was actively selecting **against** exactly the takes the tags had
  been added to improve. An ablation of "inline tags vs no tags" run in that state showed tags
  winning on only 6 of 12 edge cases; that result is not trustworthy and was re-run.

**If you change the tag notation, change the WER stripper in the same commit.** The regex must
cover every notation the text can contain:

```python
BURST_TAG_RE = re.compile(r"\([^)]*\)|\[[^\]]*\]|<[^>]{1,40}>")
```

## 2. Square brackets for pauses — a different mechanism from "..."

`...` and `[pause]` are not two spellings of one thing. The ellipsis is a written cue the model may
or may not honour; the pause tag is an explicit instruction. They can be swapped at a **fixed break
count**, which is the only way to ask "which notation works" without also asking "how many breaks
work" — the two questions get confounded otherwise, because a plan that emits three pause tags and
eight ellipses is comparing three breaks against eight.

The disfluency ladder that shipped after this correction escalates `0 / 1 / 4 / 8` breaks across the
four levels and, at the top level only, is allowed to break **mid-phrase** rather than at clause
seams. Breaking only at seams reads as *thoughtful*; heavy intoxication and grief break inside the
phrase. See [text carries the condition](text_carries_the_condition.html) for the measured ladder.

## 3. Never capitalise inside a tag

The model spells capitalised tokens out letter by letter. `(SCREAM)`, `(Sobs)` and `AAAH` are all
failure modes; `(screams)`, `(sobs)` and a written-out `aaah` are not. This applies to the
`GENERAL:` block too — write `a shivering voice`, not `A SHIVERING VOICE`.

### Measured, because this rule was written and then not applied

**Aug 2026.** This page shipped the rule in round 3 and *nothing enforced it on the 808 texts that
already existed*. Thirty of them carried an all-caps run in the spoken line — `WSA`, `GUI`, `FDA`,
`RTR`, and one that mattered:

```
k325_age3_bg1|X|pain_scream   "My leg... god, it hurts! I can't... move it! AGH!"
```

The single clip in the corpus whose entire purpose was to be a scream was the single clip where the
model stopped acting and read an initialism. Four candidates, four transcripts:

| what the ASR heard |
|---|
| …I can't move it. **Age.** |
| …move it. **Atch! Itch!** |
| …I can't move it. **Akish.** |
| …I can't move it. **Age each.** |

It is pronouncing the letter names *ay-gee-aitch*, and ASR then re-spells that as ordinary words —
which is why a naive detector looking for separated single characters (`a g h`) finds nothing. If
you are checking a corpus for this, match letter-*name* phonetics and read the transcripts.

**Two implementation notes that cost time here:**

- Enforce it at the point where candidates are built, not where texts are authored. Authored text
  is only one of the sources; a paraphraser will happily reintroduce an acronym.
- Do **not** run the fix over the whole caption. `GENERAL:` and `SCRIPT:` are format keywords the
  model was trained on, and a first version of our guard lowercased both in all 808 groups. Only
  the quoted line is spoken, so only the quoted line gets normalised.

An acronym is a genuine ambiguity rather than a bug — "the WSA program" *should* arguably be
spelled out. But a paraphrase of a news sentence has no business putting one in an actor's mouth;
rewrite it to what a person would say.

## 4. Long enough to be a reference clip

A clip that represents a condition has to be long enough to hear the condition in. Two independent
things enforce that:

- **Text side.** Every line ≥ 10 words. The explicitness dimension was previously driven by a
  single six-word line — *"That wasn't love. Not even close."* — reused for **all four levels**, so
  the ladder had no room to move and the winning takes came out at 2.4–2.6 s.
- **Ranking side.** A duration multiplier `clip(dur / 3.0, 0, 1) ** 2` on the score. It *crushes*
  short takes rather than banning them, so a group where every candidate is short still resolves to
  its best member instead of ranking arbitrarily.

Without the duration term nothing in the score preferred a longer take, and short takes had a
perverse advantage: fewer words means fewer chances to misread, so WER trends to zero and the
z-scored perceptual terms are computed over a nearly silent clip.

### The publishing trap that hid all of this

Worth stating separately, because it wasted a listening session. The page builder exported the
winning take by matching `audio_key`, which is only `<gid>.cNNN.mp3` — **not unique across runs**.
With several run directories passed in, whichever tar was scanned first won. The result: the scores
on the page came from the current run and the audio came from an older one, and *all 89 regenerated
groups played their pre-regeneration take underneath a "NEW, improved" badge*. The metadata said
5.76 s; the clip served was 0.24 s.

Match on `(source directory, audio_key)`, clear the output directory before writing, and assert
that each exported file's size is consistent with the duration its metadata claims. A page that
serves the wrong audio is worse than a page with no audio, because it invalidates the listening
that follows it.

---

## 5. Measured — 124 arms, 3,968 candidates

**Round brackets beat angle brackets**, on the six GA hall-of-fame genomes where the angle form was
deliberate and evolved:

| notation | emotion | blend | genuineness |
|---|--:|--:|--:|
| angle `<screams>` (as evolved) | 2.535 | 6.77 | 1.600 |
| **round `(screams)`** | **2.603** | **7.06** | **1.731** |

**`...` and `[pause]` do different jobs.** Held at a fixed break count per level (0 / 1 / 4 / 8):

| notation | ladder | span | top level | WER |
|---|--:|--:|--:|--:|
| **both together** | **0.635** | **1.850** | **2.154** | 0.198 |
| `...` only | 0.608 | 1.537 | 1.876 | 0.238 |
| `[pause]` only | 0.526 | 1.067 | 1.396 | **0.122** |
| adapter alone, no written breaks | 0.337 | 0.351 | 0.669 | 0.005 |

Read that as a choice, not a ranking: **ellipses drive the disfluency head harder, pause tags are
far gentler on intelligibility** (WER 0.122 vs 0.238, nearly half). Use ellipses when the condition
must be audible, pause tags when the words must survive, both when you want the widest ladder.

**Carrier length is a separate axis from notation.** Lengthening the 4–9 word GA carriers took
takes under three seconds from 12.0 % to 2.1 % and raised emotion, at the cost of blend halving
(7.06 → 3.89) — a burst is simply a smaller fraction of a longer line.

**Dose is not linear.** Writing *heavy* hesitation into a line wins in both languages
(disfluency +0.72; the intoxication/grief/hesitancy emotions +0.58 EN / +0.68 DE). Writing
*moderate* hesitation is a **negative result in English** (−0.224 over 32 emotion groups, across
two independent rounds) while working in German (+0.113). A little written hesitation appears to
cost more than it buys; a lot changes the delivery enough to register.

---

*Part of the [MOSS voice-acting manual](../index.html). See also
[text carries the condition](text_carries_the_condition.html) for what to write, and
[bursts, merge doses & evaluation](bursts_merging_evaluation.html) for how hard to merge a burst
adapter.*
