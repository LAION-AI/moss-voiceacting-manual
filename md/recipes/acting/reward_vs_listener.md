# Does the local reward predict a listener? — measured

The casting agent ranks with a **local sensor stack only** (VoiceNet / EmoNet / genuineness /
blend / quality heads, ECAPA speaker similarity, the burst locator, Whisper WER). A Gemini
supervisor listens *afterwards* and scores the five shipped takes 0–10, purely so the two
orderings can be compared. This page answers the question that matters if you want to run this
pipeline **without** paying for an external judge:

> How much of the listener's verdict does the local reward actually capture?

**Short answer: on spoken scenes, a little — ρ ≈ 0.21, about 4 % of the variance. On non-verbal
scenes, nothing, and the sign is wrong. There is currently no configuration in which the local
stack can replace the listener.**

---

## 1. How this was measured

- **Unit of analysis: one round.** The supervisor scores five takes *of the same scene*, so the
  comparison must be made **within** a round. Pooling takes across rounds mixes in between-scene
  variance and washes the effect out — every pooled |r| in this corpus is below 0.17.
- **Statistic: Spearman ρ** between the metric and the supervisor's 0–10 score, computed per
  round and then averaged. Rank-based, because the supervisor emits integers.
- **Corpus: v7 + v8 only** — 54 rounds, 269 scored takes. Earlier generations are excluded because
  their supervisor was rating **presentation order**, not quality (see §5).
- 95 % CIs are bootstrap over rounds (4,000 resamples).

### The supervisor really does discriminate

Worth establishing before reading a near-zero correlation as "the judge is noise":

| | v7 | v8 |
|---|--:|--:|
| mean score | 6.29 | 6.54 |
| within-round sd | 1.37 | 1.39 |
| **within-round spread (max − min)** | **3.85** | **3.93** |
| rounds where all five takes got the same score | **0 / 27** | **0 / 27** |

The listener separates five takes of the same scene by nearly **four points out of ten**, every
single round. The near-zero correlations below are therefore a real failure of the local reward,
not an artefact of a judge that says nothing.

---

## 2. The headline table — spoken challenges

Seven briefs (C1_infidelity, C2_biggest_fear, C3_foreman, C4_last_priest, C5_third_wheel,
X3_birthday, X4_ice_water), 42 rounds. `*` marks a CI excluding zero.

| metric | mean ρ vs listener | 95 % CI | what it measures | read |
|---|--:|:--:|---|---|
| **`score`** (the composite) | **+0.207** * | [+0.04, +0.37] | the whole weighted reward | **the best proxy available — and it is weak** |
| **`emo_peak`** | **+0.179** * | [+0.00, +0.35] | strength of the target emotion (EmoNet) | the only *component* with a real signal |
| `pros_fit` | +0.110 | [−0.03, +0.25] | how close tempo/chunking landed to plan | plausible direction, not resolvable |
| `dur` | +0.098 | [−0.06, +0.25] | total length | longer takes are mildly preferred |
| `tempo` | +0.091 | [−0.08, +0.26] | VoiceNet tempo | — |
| `arc` | +0.049 | [−0.16, +0.27] | emotional movement between parts | no signal |
| `chunk` | +0.046 | [−0.12, +0.22] | VoiceNet chunking | — |
| `qual` | +0.041 | [−0.12, +0.21] | audio-quality heads | — |
| `spk_sim` | −0.037 | [−0.19, +0.12] | speaker similarity to the anchor | **no signal** — see §4 |
| `wps` | −0.048 | [−0.21, +0.12] | words per second | — |
| `pros_join` | −0.059 | [−0.21, +0.10] | prosodic seam quality | — |
| `runaway` | −0.084 | [−0.28, +0.12] | take sprinted | right direction, not resolvable |
| **`genu`** | **−0.143** | [−0.29, +0.01] | genuineness head | **points the wrong way** |
| **`blend`** | **−0.148** | [−0.30, +0.01] | vocal-burst blending | **points the wrong way** |
| **`wer`** | **−0.184** | [−0.37, +0.00] | word error rate | correct direction (lower WER → better) |

### What this says

- **The composite beats every one of its own components.** Aggregation helps, which is the one
  encouraging result here.
- **`emo_peak` is the only component pulling its weight.** If you must pick a single cheap signal,
  pick the strength of the target emotion.
- **`genu` and `blend` are mildly *anti*-correlated with the listener.** Genuineness carried the
  single largest weight in every generation up to v7. This is the most actionable finding on the
  page: the reward's biggest term is, if anything, pointing away from what a listener prefers.
- **`wer` at −0.184 is the strongest single component in magnitude**, and it is the term that
  already dominates the composite arithmetically (see [metrics](metrics.html) — the score
  correlates +0.91…+0.98 with the `(1 − WER)` multiplier). So most of the composite's modest
  +0.207 is probably *intelligibility*, not acting.

---

## 3. Per challenge

Composite `score` vs listener, mean within-round ρ over three rounds per generation.

| challenge | v7 | v8 | pooled | type |
|---|--:|--:|--:|---|
| C1_infidelity | +0.85 | +0.22 | **+0.53** | spoken |
| X4_ice_water | +0.13 | +0.63 | **+0.38** | spoken |
| C5_third_wheel | +0.38 | +0.30 | **+0.34** | spoken |
| C2_biggest_fear | +0.50 | +0.03 | +0.27 | spoken |
| X3_birthday | +0.23 | −0.16 | +0.04 | spoken |
| X1_horror_scream | −0.07 | +0.07 | +0.00 | non-verbal |
| C4_last_priest | +0.23 | −0.30 | −0.03 | spoken |
| C3_foreman | −0.59 | +0.45 | −0.07 | spoken |
| **X2_chainsaw** | −0.40 | −0.49 | **−0.45** | non-verbal |

**Treat the per-challenge column as unstable.** Each cell is a mean of three rounds of five takes;
the between-generation swings (C3_foreman −0.59 → +0.45, C1 +0.85 → +0.22) are larger than the
effect being measured. What survives aggregation is the **type** split, not the individual scene.

## 4. The subgroup that matters: spoken vs non-verbal

| subgroup | rounds | mean ρ | 95 % CI |
|---|--:|--:|:--:|
| **spoken scenes** (7 briefs) | 42 | **+0.207** | [+0.04, +0.37] |
| **non-verbal** (scream, chainsaw agony) | 12 | **−0.223** | [−0.55, +0.08] |

On non-verbal briefs the composite is **negatively** related to the listener's verdict. The CI
spans zero, so treat the magnitude as unproven — but there is no evidence of *any* usable signal,
and a point estimate on the wrong side of zero.

The mechanism is documented elsewhere in this tree and is consistent: on a scream,
**`nonverbal: true` forces WER to 0.0**, handing the take the dominant score multiplier for free;
**ECAPA has almost no voiced material to embed**, so `spk_sim` becomes noise; and the burst
locator's output stops being informative. Three of the reward's inputs degrade at once.

**Practical rule: do not use the local composite to rank non-verbal takes.** Rank them by
duration-fit and listen, or gate them separately.

## 5. Why earlier generations are excluded

The supervisor in v1/v2/v5 was largely rating **presentation order**:

| generation | favourite was take #4 or #5 | (chance = 40 %) |
|---|--:|---|
| v1 | **85 %** | 27 rounds |
| v2 | **89 %** | 27 rounds |
| v5 | **89 %** | 27 rounds |
| **v7** (rubric rewritten) | **48 %** | 27 rounds |
| **v8** (same rubric) | near chance | 27 rounds |

The v7 rubric — which asks for explicit `same_voice=<yes/no>` and `pacing=<organic/runaway/
disjointed>` verdicts before the score — removed most of the bias. **Any agreement figure computed
from v1, v2 or v5 measures the position bias and should be discarded**, and v7/v8 supervisor
scores are not comparable with the earlier ones on an absolute scale.

## 6. Can a fitted combination do better?

No. Leave-one-round-out cross-validation, twelve metrics, predicting the **within-round** deviation
of the supervisor score (both X and y centred per round, so this is exactly the "which of these
five is best" question):

| generation | takes | cross-validated r | r² |
|---|--:|--:|--:|
| v7 | 135 | **−0.164** | 0.027 |
| v8 | 134 | **+0.068** | 0.005 |

An optimally-weighted linear combination of everything the local stack measures explains **under
3 %** of the listener's within-round preference, and does not even hold its sign between
generations. **Re-weighting the existing terms cannot fix this** — the information is not in the
current feature set. Getting further needs a different signal (a learned preference model trained
on listener judgements, or a stronger local judge), not another weight sweep.

## 7. What to do with this

| you want to… | do this |
|---|---|
| rank spoken takes without an external judge | use the **composite**, expect ρ ≈ 0.2 — it will reliably reject the worst takes and will not reliably find the best |
| pick one cheap component | **`emo_peak`**; do not use `genu` or `blend` as a quality proxy |
| rank non-verbal takes | **do not use the composite.** Gate on duration-fit and listen |
| decide whether to pay for the judge | for final selection among near-equal takes, yes — nothing local substitutes yet |
| improve the local reward | collect listener judgements and *fit* a model; re-weighting the current terms is measurably a dead end (§6) |

*All numbers on this page recomputed from `out_v7` and `out_v8` `agent_log.json` (54 rounds,
269 scored takes). Bootstrap CIs over rounds, 4,000 resamples.*
