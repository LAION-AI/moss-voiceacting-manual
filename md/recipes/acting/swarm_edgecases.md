# The edge-case swarm — `T0001`–`T0008`

Eight hard delivery edge-cases, one autonomous agent each, evolutionary search with a mandatory
supervisor review after every generation. This ran *before* the casting harness and is a different
shape of experiment: single takes optimised against a numeric fitness, not multi-part performances.
Part of the [acting-challenge tree](index.html).

**Read the recipes, distrust the verdicts.** Four of the eight agents reported success while their
own fitness was falling, and several "winning" hall-of-fame samples are under 1.5 seconds long.

---

## 1. The eight tasks

| task | edge case | reference voice | fitness targets | logged genomes | supervisor rounds |
|---|---|---|---|--:|--:|
| T0001 | Pretending angry while actually calm | none | maximise `Anger` ×2, `GENU` ×−1; constrain `AROU`, `TENS` ≤ baseline | 83 | 12 |
| T0002 | Tongue clicking during speech | `ref1.wav` | `BLEND` ×2, `CLRT` ×1, (1−WER) on | 90 | 11 |
| T0003 | Breaking down mid-eulogy | none | `S_FORM`, `Sadness` ×1.5, `Distress` ×1.5, `RESP`, `VOLT`; **(1−WER) off** | 90 | 11 |
| T0004 | Hoarse voice | `ref3.wav` | `ROUG` ×2, `RESP` ×1.5, `TENS`, `HARM` ×−2, `BRGT` ×−1, (1−WER) on | 64 | 8 |
| T0005 | Speaking while climbing | none | `BLEND` ×2, `RESP` ×2, `TENS` ×1.5, `VOLT` ×1.5; (1−WER) off | 104 | 12 |
| T0006 | Jump scare / sudden appearance | `ref5.wav` | `ARSH` ×2, `ATCK` ×2, `RESP` ×1.5, `GENU`; (1−WER) off | 89 | 12 |
| T0007 | Bomb-squad narration | none | `CLRT` ×2, `FOCS` ×2, `TEMP` ×−2, `RESP` ×−2, `VOLT` ×−2 | 33 | 4 |
| T0008 | Death scene / fading voice | `ref1.wav` | `DARC` ×−2, `AROU` ×−1, `RESP`, `CHNK` ×−1, (1−WER) on | 36 | 4 |

589 genomes in total, each evaluated mean-of-8.

## 2. The negative result nobody wrote down: half of them got worse

Best-of-generation fitness, first generation → last, straight out of `supervisor_log.jsonl`:

| task | gen 1 best | last gen best | direction | the agent's own report says |
|---|--:|--:|---|---|
| T0001 | 7.723 | **0.259** | ▼ −97 % | "MISSION COMPLETE" |
| T0002 | 1.069 | 2.285 | ▲ +114 % | "MISSION REPORT" (mixed) |
| T0003 | 2.061 | 5.641 | ▲ +174 % | admits the arc was not achieved |
| T0004 | 1.265 | **0.281** | ▼ −78 % | "MISSION ACCOMPLISHED … 9/10" |
| T0005 | 4.923 | 4.337 | ▼ −12 % | "MISSION COMPLETE" |
| T0006 | 4.312 | **2.793** | ▼ −35 % | "Partial Success / Technical Failure" |
| T0007 | 0.050 | 0.200 | ▲ ×4 | "MISSION COMPLETE … 9/10" |
| T0008 | 0.295 | 0.357 | ▲ +21 % | "MISSION SUCCESS" |

T0001's trajectory is monotone downhill after generation 4 — 7.72 → 6.19 → 2.96 → 0.79 → 2.53 →
1.27 → 1.05 → 0.53 → 0.63 → 0.26 — and it still reports a winning recipe. **The supervisor loop did
not protect against this**: the agent was choosing directions from the supervisor's *listening*
notes, and the fitness fell while the listener kept approving.

## 3. The hall-of-fame samples do not support the reports

Every saved best take, with its actual duration and WER:

| task | sample | dur | WER | GENU | BLEND | merge |
|---|---|--:|--:|--:|--:|---|
| T0002 | s0609 | **1.28 s** | 0.722 | 0.230 | 0.849 | `vn_S_CART_high@1.1; vn_TENS_high@0.6; vn_CLRT_high@0.5` |
| T0002 | s0671 | **1.20 s** | 0.722 | 0.167 | 0.371 | `vn_S_FORM_high@0.7; vn_S_PLAY_high@0.4; vn_CLRT_high@0.5` |
| T0002 | s0679 | **1.28 s** | 0.722 | 0.077 | 0.415 | `vn_S_NARR_high@0.7; vn_S_PLAY_high@0.4; vn_CLRT_high@0.5` |
| T0003 | s0660 | **1.12 s** | n/a | 0.247 | 0.605 | `vn_S_DRAM_high@0.8; Sadness@1.2; vn_S_WHIS_high@1.0` |
| T0003 | s0680 | **1.36 s** | n/a | 0.355 | 0.801 | `Sadness@1.5; vn_S_FORM_high@0.7; vn_RESP_high@1.0` |
| T0003 | s0700 | **0.56 s** | n/a | 0.290 | 0.619 | `vn_S_FORM_high@0.8; Sadness@0.8; vn_RESP_high@1.0; vn_S_WHIS_high@0.8` |
| T0004 | s0438 | 2.96 s | 0.758 | 0.402 | 0.681 | `char_genuine/gravelly-sinister-baritone@1.0; vn_HARM_low@1.0; vn_VULN_high@1.0` |
| T0004 | **s0456** | **16.16 s** | **0.000** | 0.286 | 0.142 | `char_genuine/gravelled-veteran-baritone@1.0; vn_HARM_low@1.2; vn_ROUG_high@1.0` |
| T0004 | s0475 | 3.44 s | 0.758 | 0.373 | 0.686 | `char_genuine/gravelly-sinister-baritone@1.0; vn_ROUG_high@0.8; vn_HARM_low@0.8; vn_VULN_high@0.8` |
| T0007 | s0202 | 14.64 s | 0.000 | 0.026 | **0.000** | `vn_SMTH_high@0.3; vn_WARM_high@0.4; vn_FOCS_high@0.4; vn_VOLT_low@0.4` |
| T0007 | s0217 | 12.32 s | 0.000 | 0.030 | **0.000** | `vn_SMTH_high@0.5; vn_VOLT_low@0.4; vn_RESP_low@0.4` |
| T0007 | s0270 | 3.52 s | 0.577 | 0.041 | 0.250 | `char_refined/human@1.0; vn_SMTH_high@0.4; vn_WARM_high@0.4; vn_FOCS_high@0.4; vn_VOLT_low@0.4; vn_CLRT_high@0.5` |
| T0008 | **s0240** | 15.28 s | 0.000 | 0.305 | 0.791 | `vn_S_WHIS_high@0.4` |
| T0008 | s0261 | 23.84 s | 0.056 | 0.244 | 0.673 | `vn_S_WHIS_high@0.3; emotion/Emotional_Numbness@0.3` |
| T0008 | s0271 | 10.40 s | 0.389 | 0.228 | 1.000 | `vn_S_WHIS_high@0.4; vn_RESP_high@0.4` |

Three specific contradictions between the reports and the artifacts:

- **T0002** declares a winning recipe with `<tsk>` tags in a full sentence, but all three saved
  samples are ~1.2 s long at WER 0.72 — the sentence did not survive.
- **T0003** ("breaking down mid-eulogy") saved a 0.56 s take as its best. The report is honest about
  it: *"the specific crack–pause–recovery arc remained elusive"*. This is the truncation wall.
- **T0004** reports the winner as `gravelled-veteran-baritone + HARM_low 1.2 + ROUG_high 1.0`, which
  matches exactly one of its three saved samples (**s0456**, 16.16 s, WER 0.000 — the only genuinely
  usable take in the whole hall of fame). The other two use a *different* character LoRA
  (`gravelly-sinister-baritone`) at WER 0.758.
- **T0007** reports `char_refined/human@1.0` as part of the winning merge; two of its three saved
  samples do not contain it, and both of those have `BLEND` 0.000 and `GENU` 0.026–0.030 — i.e.
  clean and empty.

**T0004 s0456 and T0008 s0240/s0261 are the only hall-of-fame entries in the swarm that are both
long enough to be a performance and intelligible.** Those three are worth listening to; the rest
are evidence of a search, not results.

## 4. What is genuinely reusable from the swarm

These are the findings that survived and were later confirmed by other work.

**The truncation wall (T0003, T0006).** The model predicts EOS immediately after the first phrase on
burst-heavy emotional scripts. Two mitigations found independently: **remove punctuation** from the
script and raise `max_frames`. And, decisively, **a silence beat in the script reliably triggers
early truncation** — never put a pause directly after a burst. This is the single most-repeated
finding across the swarm and it is why the casting harness splits performances into parts at all.

**Character LoRAs are structural, VoiceNet LoRAs are cosmetic (T0004).** For a *damaged* voice, the
model defaults to a "whisper fallback" — unvoiced air instead of voiced grit — when driven only by
`vn_ROUG`/`vn_TENS`. A character LoRA gives it a structure to damage. And the "bruised instrument"
quality comes from explicitly **breaking harmonicity** (`vn_HARM_low`) rather than adding noise
(`vn_ROUG_high`).

**The anchor-and-leak strategy (T0002).** A strong formal/narrator clamp (`vn_S_NARR_high@0.7`,
`vn_CLRT_high@0.5`) with a *low* dose of the burst-triggering LoRA (`vn_S_PLAY_high@0.4`) allowed
percussive transients through without the "fry and cartoonish distortion" that high-strength
percussive LoRAs produced. This is the same presence↔quality trade the dose sweep measured, found
independently. **It has still never been tested with the real vocal-burst adapters.**

**Burst tags inside the script text (T0005).** *"Placing burst tags (`<gasp>`, `<grunt>`) directly
inside the script text was critical for breaking repetitive patterns and forcing the model to
interleave speech with physical effort."* Consistent with the later control run: the inline tag
alone carries the burst ~24 % of the time, and the adapter **multiplies** that rather than replacing
it. Keep the tag.

**Two ways to destroy synthesis outright.**
- `vn_GEND_high` (pitch) stacked on a burst-heavy configuration → **whistling artefacts**, total
  failure (T0005).
- High-intensity onset LoRAs (`ARSH`/`ATCK`) combined with a **high-resonance reference voice** →
  **broadband static** (T0006). Directly relevant to "raise burst probability without wrecking the
  speaker".

**Scale discipline (T0007).** Generation 0 used VoiceNet merges at ≥1.0 and produced robotic,
metallic artefacts at WER ~0.65. Cutting every VoiceNet scale to **≤0.4** and adding one character
LoRA recovered intelligibility to WER ~0.28 and removed the artefacts. Across the swarm the pattern
is consistent: **many VoiceNet dimensions at 0.3–0.5 beats a few at 1.0+.**

**The bomb-squad recipe (T0007), for a voice that must not tremble:**
`char_refined/human@1.0 + vn_SMTH_high@0.4 + vn_WARM_high@0.4 + vn_FOCS_high@0.4 + vn_VOLT_low@0.4 +
vn_CLRT_high@0.5`, temp 0.8 / top_p 0.9 / top_k 40, with weighted pauses written as `...` inside the
script. `vn_SMTH_high` is what removes vocal fry and jitter.

**The death-scene recipe (T0008), the cleanest result in the swarm:**
`vn_S_WHIS_high@0.4 + vn_RESP_high@0.4`, temp 0.7 / top_p 0.9 / top_k 40, with the *prompt* doing
the work — "weakly, gradually losing volume phrase by phrase, widening pauses, ending in a long,
audible, smooth hiss of air that fades slowly to silence". Measured on s0240: dynamic arc 0.051,
arousal 0.084, WER 0.076 at 15.3 s. **Prompt steering, not the LoRA, was the primary driver of the
fading effect** — the agent's own conclusion, and the metrics support it.

## 5. Measurement traps found the expensive way

- **The burst classifier cannot name a burst embedded in speech.** `identity` scored **0.000 on all
  32 cells** of a grid where the bursts were plainly audible: no span found in 33 of 64 sentences,
  the rest labelled sigh/gasp/ahem, mean target probability 0.0055. Locator span *timing* is
  reliable; the class *label* is a weak prior. Score presence, judge identity by listening.
- **`Judge.judge()` takes the single longest located bout.** In a 6-second sentence the longest bout
  is the *speech*, so the cut handed to the classifier is speech. Classify **every** located span.
- **Score blend/genuineness on the whole sentence, burst identity on the cut.** Mixing those up made
  an earlier whole-corpus pass call 37 % of ordinary speech a burst.
- **Gemini's OpenAI-compatible endpoint silently drops audio.** Use the native
  `v1beta/models/<model>:generateContent` with `inline_data`. It was caught only because *real
  recordings* also scored 0 — i.e. because there was a ceiling control.

---

## 6. How this connects to the casting runs

The casting harness inherited four things from this swarm and rejected one.

Inherited: the truncation wall (hence multi-part performances), inline burst tags, the 0.35–0.75
usable dose band, and "never a silence beat after a burst".

Rejected: **the evolutionary loop itself.** The casting harness runs three fixed rounds with an LLM
planner instead of generations of genomes, because the swarm demonstrated that a supervised
evolutionary search can run for twelve generations while its own fitness falls by 97 % and still
report success. The casting harness's own version of the same disease is documented in
[what failed §6](what_failed.html#6): its rounds do not converge either — but at least it only
runs three of them.
