# Writing the condition into the line: what works per dimension, and what does not

*Measured recipe page, added Aug 2026. Additive — nothing on the emotion, VoiceNet, burst or
NSFW pages is retracted. This adds one thing that had not been measured before: **for which
dimensions does manipulating the TEXT actually move the dimension**, and by how much.*

The [text-carries-the-condition](text_carries_the_condition.md) result showed that rewriting a
sentence so its *content* justifies the target emotion is the largest single lever on this
pipeline. The obvious next question is whether the same trick works for the *non-emotional*
dimensions — disfluency, chunking, explicitness — and for the edge cases.

**It does not generalise.** Two of the four families measured here get worse when you write the
condition into the line. That is the useful finding, and it is the opposite of what the
text-effect result would lead you to assume.

---

## 0. The ablation

One reference voice (`k325_age3_bg1`), **106 arms × 16 candidates = 1,696 generations**, zero
failures. Every arm is a real production group run through the ordinary generator, so the numbers
are directly comparable with the profile.

**The metric is not the same for every family, on purpose.** For a *level* dimension the goal is a
**ladder**, not a maximum: a recipe that pushes all four levels to "very high" has destroyed the
dimension. Those families are scored on monotonicity × span, with WER as a guard rail. Single-target
families (the explicitness LoRA, the edge cases) are scored on the manual's usual composite,
`(target + genuineness + blend/5) × (1 − WER)`.

---

## 1. Disfluency — **write it in**. Nearly 5× the span.

Ellipses, filled pauses (`uh`, `um`), explicit `[pause]` / `[long pause]` markers and a false start,
all scaled by level, plus a cue naming the behaviour.

| arm | ladder | span | WER | extremely low | mod. low | mod. high | very high |
|---|--:|--:|--:|--:|--:|--:|--:|
| base (adapter only) | 0.417 | 0.444 | **0.009** | 0.269 | 0.443 | 0.711 | 0.714 |
| ellipsis only | 0.271 | 1.132 | 0.179 | 0.299 | 0.266 | 1.549 | 1.430 |
| full recipe | 0.624 | 1.708 | 0.187 | 0.301 | 0.288 | 1.564 | 2.009 |
| **full + cue** | **0.970** | **2.084** | 0.187 | 0.255 | 0.295 | 1.747 | **2.339** |

The adapter alone spans 0.44 across the whole ladder — the top rung reaches 0.714, which is not a
disfluent voice by any reading. With the text written to match, the top rung reaches **2.339** and
the span is **2.084**, 4.7× wider. The cue on top of the text is worth another 0.22 of span, so
both matter.

**Cost: WER 0.009 → 0.187.** That is real and has to be accepted deliberately — a genuinely
disfluent take *is* harder to transcribe, so some of that rise is the effect working rather than a
defect. It stays inside the 0.25 guard rail.

> **Recipe.** Scale breaks by level: 0 breaks at *extremely low* (and strip any hesitation the
> source text already has — the low rung must be actively smooth, not merely default), ~1 at
> *moderately low*, ~3 plus a filled pause at *moderately high*, ~5 plus two filled pauses and one
> false start at *very high*. Put breaks at clause seams, never in the first two or last two words.
> Add a cue that names the behaviour.

---

## 2. Chunking — **do not**. The adapter is already better.

The same treatment applied to `CHNK`:

| arm | ladder | span | WER | extremely low | mod. low | mod. high | very high |
|---|--:|--:|--:|--:|--:|--:|--:|
| **base (adapter only)** | **0.446** | **0.480** | **0.088** | 2.193 | 2.279 | 2.375 | 2.673 |
| ellipsis only | 0.274 | 0.438 | 0.194 | 2.234 | 2.375 | 2.364 | 2.672 |
| full recipe | 0.150 | 0.229 | 0.179 | 2.176 | 2.455 | 2.365 | 2.405 |
| full + cue | 0.187 | 0.289 | 0.175 | 2.242 | 2.344 | 2.274 | 2.530 |

Every text arm is **worse** than the adapter alone, and WER roughly doubles for nothing.

**Why the asymmetry with disfluency is worth understanding**, because it predicts where else this
will fail: inserting `...` makes the model *hesitate*, which is what the disfluency head measures.
It does not make the model *restructure the line into distinct breath groups*, which is what the
chunking head measures. The two dimensions look similar on paper and respond to completely
different interventions. Do not assume a text trick transfers between dimensions that merely sound
related.

---

## 3. Explicitness (the VoiceNet dimension) — **write it in**, and the adapter alone does nothing

`EXPL` is a **register** axis: how unguarded and profane the speech is. It is not about sex.

| arm | ladder | span | WER | extremely low | mod. low | mod. high | very high |
|---|--:|--:|--:|--:|--:|--:|--:|
| base (adapter only) | 0.000 | **−0.006** | 0.128 | 0.161 | 0.218 | 0.161 | 0.155 |
| **vulgar-register ladder** | **0.399** | **0.691** | **0.079** | 0.420 | 0.069 | 0.419 | 1.110 |

**The adapter alone produces a completely flat line** — span −0.006 across all four levels. The
dimension was not being rendered at all. With the register written into the text the top rung
reaches 1.110, and **WER goes down** (0.128 → 0.079), because profanity is ordinary spoken
vocabulary and the model does not have to invent a register the words contradict.

> **Recipe.** Rewrite the seed per level: *extremely low* scrupulously polite and broadcast-safe;
> *moderately low* relaxed casual with mild slang; *moderately high* unguarded and blunt with
> ordinary swearing; *very high* raw and uncensored. Gemma-4-E4B is sufficient.

**Honest caveat:** the ladder is not monotonic — *moderately low* lands at 0.069, below
*extremely low* at 0.420. The span is what improved, not the ordering. The middle rungs need work
before this dimension can be claimed as a clean four-level scale.

---

## 4. The explicitness LoRA block — adult content yes, **bursts no**

A different target from the dimension: adult intimacy rather than vulgarity.

| arm | explicitness | blend | genuineness | WER | fitness |
|---|--:|--:|--:|--:|--:|
| base (corpus sentence) | **0.545** | 1.595 | 0.321 | 0.109 | 1.056 |
| **adult text** | 0.319 | **7.526** | 1.066 | **0.014** | **2.850** |
| adult text + bursts, no burst LoRA | 0.266 | 6.452 | 1.071 | 0.104 | 2.354 |
| adult text + bursts + burst LoRA @0.5 | 0.227 | 6.079 | 1.175 | 0.146 | 2.236 |

**Read the first column before concluding.** The explicitness *score* is highest for the baseline
(0.545) and drops with adult text (0.319) — the opposite of the intent. Everything else improves
enormously: blend 1.60 → 7.53, genuineness 0.32 → 1.07, WER 0.109 → **0.014**. The composite
favours adult text by a wide margin, but the explicitness head itself does not, and that
disagreement should be resolved by listening before this recipe is trusted. One plausible reading
is that the head keys on vulgarity, which the adult-intimacy rewrite deliberately avoids.

**Inline bursts made every metric worse here.** Unlike the edge cases, this block does not benefit
from them.

---

## 5. Edge cases — bursts raise intensity and cost blend and words

The eight `EDGE8` cases were receiving **no inline burst tags and no burst adapter at all** —
`caption_edge` passes tags only for the six GA hall-of-fame entries. So they were running at the
floor the [burst page](bursts_merging_evaluation.md) measures for prompt-free generation.

| arm | emotion | genuineness | blend | WER | fitness |
|---|--:|--:|--:|--:|--:|
| **base** (no tags, no burst LoRA) | 2.498 | 1.505 | **5.815** | **0.331** | **2.871** |
| + inline tags | 2.543 | 1.582 | 5.100 | 0.386 | 2.688 |
| + tags + burst LoRA @0.5 | 2.592 | 1.635 | 3.644 | 0.615 | 1.697 |
| + tags + LoRA + temp 1.4 | **2.683** | **1.738** | 4.079 | 0.543 | 2.116 |
| + tags + LoRA, emotion adapter dropped | 2.203 | 1.701 | 4.161 | 0.502 | 2.046 |

**Both readings are true and they disagree**, so state which one you are optimising:

- **On intensity alone, the intervention works and scales monotonically.** Emotion strength rises
  2.498 → 2.543 → 2.592 → 2.683 as you add tags, then the adapter, then heat. Genuineness rises
  1.505 → 1.738. If "not intense enough" is the complaint, `tags + LoRA + temp 1.4` is the answer.
- **On the composite, the baseline wins**, because blend falls 5.82 → 3.64 and WER nearly doubles
  0.331 → 0.615.

**Do not drop the emotion adapter on edge cases.** The burst page's rule — emotion@0.5 is the worst
cell when the burst is the point — **does not transfer here**: `tags_lora_noemo` has the *lowest*
emotion strength of any arm (2.203). On an edge case the emotion is also the point, so removing it
removes half the target.

> **Caveat on the composite.** `(1 − WER)` is doing heavy work in a family that is largely
> non-verbal. A scream or a sob has little transcribable material, so a WER of 0.6 may be measuring
> the absence of words rather than a defect. The ranking above should not be treated as settled
> until an edge-case-appropriate metric replaces WER in the composite.

---

## 6. Which dimensions to try this on next

Predicted from what the condition physically does to articulation, **not yet measured**:
Intoxication, Grief and Hesitancy at the strongest setting; Fatigue, Confusion, Embarrassment,
Shame, Distress, Fear, Sadness, Helplessness and Awkwardness below that. Fear has independent
support — the manual already finds chunking, not tempo, is its dial.

Given §2, expect this to work where the condition produces *hesitation* and to fail where it
produces *restructuring*. Measure before shipping any of them.

---

## 7. Bugs found while building this, worth avoiding

- `caption_edge` gives inline burst tags to `EDGE6` only; `EDGE8` gets a cue and nothing else, and
  no burst adapter is merged. Eight of the fourteen edge cases were running with no burst support.
- The stored explicitness sentence was a birthday message — *"...now that you're finally seventy
  and ready for some real fun."* No adapter can carry adult intimacy over that.
- An LLM rewrite that returns its seed **unchanged** is a failed rewrite, not a valid result.
  Unchecked, this produced a birthday greeting with `<breathing heavily>` and `<sighs>` added to
  it. Always compare the rewrite against the seed and retry on a no-op.
- `apply_breaks` hard-read `plan["pause"]`, which `CHNK_PLAN` does not define — so every call to
  `chunking_text()` raised `KeyError`. Optional plan keys must be read with `.get`.
