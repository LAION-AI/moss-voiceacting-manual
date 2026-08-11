# Text-side recipes: make the WORDS carry the condition

*Measured recipe page, added Aug 2026. **Additive** — nothing on the emotion, VoiceNet, burst or
NSFW pages is retracted. This adds what was not previously measured: how much of a condition the
**text** can carry when the adapter alone is brittle, and one case where the obvious adapter fix
makes things actively worse.*

Ablation: **106 arms, 1,696 candidates**, one reference voice, everything held fixed except the
sentence and the adapter set. Regeneration: **89 groups, 2,848 candidates**.

---

## 0. The one-line summary

| target | winning recipe | effect |
|---|---|---|
| **Disfluency (DFLU)** | ellipses + filled pauses + a false start + a cue naming the behaviour | ladder span **0.44 → 2.07** |
| **Explicitness (EXPL dim)** | a written vulgarity ladder | ladder span **−0.006 → 0.43** |
| **Explicitness LoRA** | adult text + inline burst tags, **no** burst adapter | blend **1.60 → 7.82** |
| **Chunking (CHNK)** | **no change** — every recipe scored at or below base | negative result |
| **Edge cases** | inline tags on **laughter only**, **never** a burst adapter | see §4 |

---

## 1. Disfluency is a text property, not an adapter property

The adapter alone barely separates the top two levels: measured disfluency
**0.269 / 0.443 / 0.711 / 0.714** across the four levels — levels 2 and 3 are indistinguishable.

Writing the hesitation into the line fixes it:

| arm | ladder | span | extremely low → very high |
|---|--:|--:|---|
| base (adapter only) | 0.417 | 0.444 | 0.269 · 0.443 · 0.711 · 0.714 |
| ellipsis only | 0.544 | 1.146 | 0.299 · 0.266 · 1.143 · 1.445 |
| + filled pauses & false starts | 0.643 | 2.012 | 0.301 · 0.288 · 1.182 · 2.313 |
| **+ a cue naming the behaviour** | **0.968** | **2.066** | 0.255 · 0.295 · 1.302 · **2.321** |

**Recipe.** Scale the insertions by level: 0 breaks / 1 / 3 + one filler / 5 + two fillers + one
false start. At the **low** end do *negative* work — strip hesitation the source text already
contains, or level 0 is merely "the default" rather than a real contrast. Put breaks at commas and
clause boundaries first. Add a cue: *"very hesitant, stalling and restarting constantly"*.

**Cost:** WER +0.176. Some of that is real — a stalling speaker *is* harder to transcribe.

### 1b. It transfers to emotions whose delivery is physically broken speech

Applied to emotions selected by what the condition does to **articulation**, not by intensity:

| treatment | emotions | emotion Δ | genuineness Δ | disfluency Δ | WER Δ |
|---|---|--:|--:|--:|--:|
| **heavy (level 3)** | Intoxication, Grief, Hesitancy | **+0.703** | **+0.637** | +0.782 | +0.067 |
| moderate (level 2) | Fatigue, Confusion, Embarrassment, Shame, Distress, Fear, Sadness, Helplessness, Awkwardness | +0.037 | +0.131 | +0.304 | +0.148 |

**The heavy treatment on the most-broken emotions is the strongest single result on this page.**
The moderate treatment moves disfluency but barely moves emotion — apply it for the disfluency, not
expecting an emotion gain.

---

## 2. Chunking: a negative result, kept as one

Every recipe scored at or below base on the ladder, and all cost roughly **2.4× the WER**
(0.088 → 0.21). Base is monotonic with a tiny span (2.19 → 2.67); the recipes buy span but lose
monotonicity.

**Writing breaks into the line does not drive the chunking metric.** Either the metric measures
something else, or chunking is genuinely not text-drivable this way. Do not spend prompt budget on
it until that is resolved.

---

## 3. Explicitness: two different targets that had been conflated

The **EXPL dimension** is a *register* axis — polite → blunt → profane. The **explicitness LoRA**
is *adult intimacy*. They are not the same thing, and both had been handed ordinary neutral
sentences.

**The EXPL adapter does nothing on its own.** Measured base ladder: **0.161 / 0.218 / 0.161 /
0.155** — span **−0.006**. Flat. With a written vulgarity ladder: span **0.428**, and the target
metric rose **+0.584** on regeneration.

**For the LoRA block**, adult text with inline burst tags (`<moans>`, `<sharp inhale>`,
`<breathy giggle>`) and **no burst adapter**: blend **1.60 → 7.82**, genuineness **0.32 → 1.56**.
Adding the burst adapter *lowered* blend to 5.42 and raised WER to 0.287.

> ### ⚠️ Safety, from a real failure
> The adult rewrite silently returned its seed, and the seed was a corpus sentence — a birthday
> message. The pipeline produced *"Seventy years young, Paul. We want to celebrate you... with some
> real fun."* and the burst pass then added `<breathing heavily>` and `<sighs>`.
> **Seed adult register from a neutral adult scene between two unnamed adults — never from whatever
> the corpus supplied — and treat a rewrite that returns its seed verbatim as a FAILURE, not a
> result.** Nothing had been checking that.

---

## 4. Edge cases: the obvious fix makes them worse

The eight EDGE8 cases were getting **no inline burst tags and no burst adapter** —
`caption_edge` passes tags only for the six GA hall-of-fame entries. So they had been running at
the floor. The natural fix is to merge the fitting burst adapter. **Measured, that is harmful:**

| arm | emotion | WER | **speaker similarity** |
|---|--:|--:|--:|
| base | 2.501 | 0.329 | 0.365 |
| inline tags only | 2.723 | 0.511 | 0.334 |
| tags + burst adapter @0.5 | 2.671 | 0.697 | **0.176** |
| + temperature 1.4 | 2.666 | 0.666 | 0.185 |
| tags + adapter, emotion dropped | 2.278 | 0.643 | 0.230 |

**The burst adapter halves speaker identity for a 0.17 emotion gain.** The manual's λ=0.5 recipe
was measured for bursts inside *ordinary* sentences; an edge case is already at the extreme, and
stacking a burst adapter on top pushes it into unintelligibility.

**Inline tags alone win on only 6 of 12 cases, and the split is systematic:**

| gains | loses |
|---|---|
| amused_laughter **+1.024**, ga_amuse_laugh +0.522, cold_shiver +0.304 | tears **−0.546**, ga_sad_cry −0.183, sad_crying −0.048 |

Discrete laughter bursts land cleanly. Sobs smear into speech that is already sobbing.

**Recipe: inline tags on laughter/amusement edge cases; leave crying alone; never merge a burst
adapter into an edge case.**

---

## 5. What to take from this

- When a dimension's ladder is flat, suspect the **text** before the adapter dose. DFLU and EXPL
  were both nearly flat for that reason.
- **Score a ladder on monotonicity and span, not on the maximum.** A recipe that pushes every level
  high has destroyed the dimension.
- Strip hesitation at the low end. A contrast needs both ends built.
- Compute WER on **burst-stripped** text, or every burst take is charged for words it never
  contained.
- A rewrite that returns its input is a failure. Check.
