# Metrics — what each number means, and which ones are useless

The casting harness scores everything with a local sensor stack and never lets the LLM supervisor
touch the ranking. This page documents what each sensor measures, the exact formula each generation
used, the thresholds, and — the important part — which terms turned out to carry no information.
Part of the [acting-challenge tree](index.html).

---

## 1. The sensors

| name | range | source | what it measures |
|---|---|---|---|
| `genu` | 0–6 | `pp_scores_fast.FastScorer` → `genuineness_0_6` | does the emotion sound felt rather than performed |
| `blend` | 0–10 | `blend_0_10` | does a vocal burst grow out of the speech or sit on top of it |
| `qual` | ~0–5 | mean of the `quality` heads | production quality / cleanliness |
| `emo_peak` | unbounded, ~0–5 | EmoNet score of the part's declared `targets`, or the global argmax if none of them exist | how strongly the target emotion registers |
| `emo_argmax` | label | EmoNet | the dominant emotion |
| `wer` | 0–1 | `openai/whisper-small` + `jiwer`, against the part's `text` | intelligibility. **Forced to 0.0 when the part is `nonverbal`** |
| `dur` | s | waveform length | |
| `spk_sim` | −1…1 | `speechbrain/spkrec-ecapa-voxceleb` cosine against the anchor | is this the same actor |
| `n_bursts` | count | `Judge.loc.spans()` | located non-speech burst events |
| `tempo` / `chunk` / `dflu` / `vflx` | 0–6 | VoiceNet `TEMP` / `CHNK` / `DFLU` / `VFLX` continuous head | pace, breath-group length, disfluency, flexibility (v7 only) |
| `wps` | words/s | ASR word count ÷ duration | arithmetic cross-check on `tempo` (v7 only) |
| `narration` | ≈ −3…3 | `½(S_NARR + S_NEWS) − ½(S_DRAM + S_CONV)` | positive = reading it out instead of acting it (v7 only) |
| `edge_bursts` | count | burst spans overlapping the first/last 0.45 s | bursts that will land on a seam (v7 only) |
| `burst_db` | dB | loudest burst span RMS relative to speech-active RMS | a burst >6 dB over the speaker reads as a splice (v7 only) |
| `dnsmos` | ~1–5 | `speechmos.dnsmos` `ovrl_mos` | used **only** to decide whether to keep a voice conversion |

`active_rms` is taken over the loudest 60 % of 20 ms frames, not the whole clip, because plain RMS
is dominated by how much silence a take happens to contain.

---

## 2. The assembly score, per generation — verbatim

The weights below for v1 and v7 were **recovered by least squares from the shipped assemblies**
(135 per generation, residual < 0.0011), because the source files on disk have moved on:
`actworker.py` now contains a rewritten `arc` term that no v1/v2/v5 run ever used, and
`actworker_v7.py` was edited at 23:53 on 08-07 — after `out_v7` finished — and now contains the
**v8** formula. Read the formulas from here, not from the source. v2 and v5 reproduce the source
exactly (residual 0.0002).

**v1** — no speaker term at all:

```
core = 0.28·(genu/6) + 0.22·min(peak,1) + 0.20·arc + 0.14·(blend/10)
     + 0.10·qual + 0.06·dur_fit
score = core · (1 − min(wer,1))
```

**v2 and v5** — speaker similarity becomes a first-class term:

```
spk  = mean over parts of spk_sim
core = 0.24·(genu/6) + 0.18·min(peak,1) + 0.16·arc + 0.20·spk + 0.10·(blend/10)
     + 0.07·qual + 0.05·dur_fit
score = core · (1 − min(wer,1))
```

**v7** — prosody added, runaway made multiplicative, speaker made worst-case-sensitive:

```
spk  = 0.5·mean(spk_sim) + 0.5·min(spk_sim)
pros = 0.4·prosody_fit + 0.6·prosody_join
core = 0.20·(genu/6) + 0.15·min(peak,1) + 0.14·arc + 0.22·spk + 0.08·(blend/10)
     + 0.05·qual + 0.04·dur_fit + 0.12·pros
score = core · (1 − min(wer,1)) · (1 − 0.35·runaway)
```

**v8 (currently running, for reference)** — blend up, three further multiplicative penalties:

```
core = 0.18·(genu/6) + 0.14·min(peak,1) + 0.13·arc + 0.21·spk + 0.12·(blend/10)
     + 0.05·qual + 0.04·dur_fit + 0.13·pros
score = core · (1 − wer) · (1 − 0.35·runaway) · (1 − 0.12·min(edge_bursts,2))
      · (1 − 0.12·clip(narration/2,0,1)) · (1 − 0.12·clip((burst_db−6)/6,0,1))
```

Common to all: `dur_fit = max(0, 1 − |dur − target_dur| / target_dur)` with `target_dur = 30`.

### Candidate ranking (which 4 takes of the 16 are kept)

v1 / v2 / v5, from `actworker.py`:

```
sp     = spk_sim (1.0 if nan)
base_s = (genu/6·0.40 + min(peak,1)·0.25 + qual·0.10 + sp·0.25) · (1 − wer)
score  = base_s · (0.25 if sp < spk_floor else 1.0)
```

v7 — the two weights below are quoted from a traceback emitted by the running worker, the rest of
the v7 candidate formula is not recoverable from the artifacts:

```
base_s = (genu/6·0.34 + min(peak,1)·0.22 + … ) · (1 − wer)
score  = base_s · (0.25 if sp < floor) · (1 − 0.35·runaway) · edge_pen · narr_pen · loud_pen
```

and, critically, **v7's candidate ranking contains no `blend` term at all** — the v8 source says so
in a comment, and the consequence is in §5 below. v8 adds `blend/10·0.11` and `prosody_fit·0.10`.

### Thresholds

| knob | v1 | v2 / v5 | v7 | what happens |
|---|---|---|---|---|
| `spk_floor` | — | 0.60 (default) | **0.68** | v2/v5: score × 0.25. v7: the take is **excluded from ranking** unless nothing in the batch clears the floor |
| `spk_target` | — | — | **0.82** | v7 only: if the take that would be *kept* is below this, regenerate the part with a fresh seed, up to `spk_retries` = 2 extra batches, then rank the merged pool |
| `vc_threshold` | — | **0.55** | **0.75** | run Chatterbox S3Gen voice conversion on the candidate; keep it only if ECAPA similarity **rose** and DNSMOS did not fall by more than 0.15 |
| `WPS_CAP` | — | — | **4.0** | above this word rate, `runaway` starts accumulating |
| tempo runaway | — | — | measured > 5.0 with `tempo_target` < 5 | second `runaway` trigger |
| `topk` kept per part | 4 | 4 | 4 | assemblies = every combination of kept parts, capped at 256 |
| candidates per part | 16 | 16 | 16 (48 after 2 resamples) | |
| crossfade | 25 ms equal-power | same | same | |
| level match | to part 0's `active_rms`, ±12 dB max gain | same | same | |

---

## 3. The finding that matters: the score is a WER detector

Decomposing each generation's score into its terms across all 135 shipped assemblies. "Mean
contribution" is `weight × value`; "share" is that as a fraction of the mean score.

**v2 / v5** (mean score 0.745):

| term | weight | mean contribution | sd | share of score | corr. with final score |
|---|--:|--:|--:|--:|--:|
| `(1 − wer)` multiplier | × | 0.850 | 0.115 | — | **+0.975** |
| `qual` | 0.07 | 0.237 | 0.011 | 32 % | +0.825 |
| `spk` | 0.20 | 0.153 | 0.023 | 21 % | +0.879 |
| `peak` | 0.18 | 0.180 | **0.000** | 24 % | undefined (constant) |
| `arc` | 0.16 | 0.154 | 0.011 | 21 % | +0.283 |
| `genu` | 0.24 | 0.061 | 0.017 | 8 % | **+0.005** |
| `blend` | 0.10 | 0.043 | 0.018 | 6 % | +0.648 |
| `dur_fit` | 0.05 | 0.043 | 0.006 | 6 % | +0.141 |

**v7** (mean score 0.694):

| term | weight | mean contribution | sd | share of score | corr. with final score |
|---|--:|--:|--:|--:|--:|
| `(1 − wer)` multiplier | × | 0.861 | 0.130 | — | **+0.908** |
| `qual` | 0.05 | 0.170 | 0.007 | 25 % | −0.205 |
| `spk` | 0.22 | 0.178 | 0.021 | 26 % | +0.344 |
| `peak` | 0.15 | 0.144 | 0.021 | 21 % | +0.077 |
| `arc` | 0.14 | 0.131 | 0.015 | 19 % | +0.354 |
| `pros` | 0.12 | 0.088 | 0.013 | 13 % | −0.014 |
| `genu` | 0.20 | 0.051 | 0.019 | 7 % | **+0.027** |
| `blend` | 0.08 | 0.032 | 0.012 | 5 % | +0.228 |
| `dur_fit` | 0.04 | 0.031 | 0.009 | 5 % | +0.336 |

v1: `(1 − wer)` correlates **+0.973**, `genu` **−0.052**.

> Eight carefully weighted terms, and the `(1 − WER)` multiplier explains almost all of the
> variance in every generation. **Genuineness — the largest single weight in v1, v2 and v5 — has
> essentially zero correlation with the score it is supposed to dominate**, because its
> contribution varies by ±0.02 while the WER multiplier varies by ±0.13.

The high correlations of `qual` and `spk` are partly the same effect: an unintelligible take is
usually also a low-quality, drifting take, so those terms co-vary with WER. The honest reading is:
**the casting score ranks assemblies by intelligibility and speaker continuity, and is blind to
almost everything else it claims to measure.**

Consequence for anyone re-running this: if you want the ranker to select for acting rather than for
diction, you must either normalise the terms so their *variances* are comparable, or drop the
multiplicative WER form for a threshold ("reject above 0.35, then ignore").

---

## 4. Metrics that are useless, and why

### `arc` — the original label-flip version

The v1/v2/v5 `arc` term counted whether the argmax EmoNet **label** changed between consecutive
parts. Over 405 shipped assemblies it took exactly **three distinct values ever**:

| value | count | share |
|---|--:|--:|
| 1.000 | 326 | 80.5 % |
| 0.875 | 20 | 4.9 % |
| 0.833 | 59 | 14.6 % |

On the 81 top-ranked assemblies it is 1.000 in **84 %** of cases; on v1's 27 top-1 assemblies the
mean is **0.977 with 85 % at exactly 1.0** — while a listener reported hearing no arc at all. A
label can flip between neighbouring emotions with no audible change, so the metric fired on almost
everything. It carried 0.16–0.20 of the weight and 21–27 % of the score as an essentially constant
offset.

### `arc` — the continuous replacement, in v7

```
profile_move = mean over consecutive parts of (1 − cosine(EmoNet profile_a, profile_b))
swing        = max(emo_peak) − min(emo_peak) over parts
arc          = clip(0.6·min(profile_move/0.35, 1) + 0.4·min(swing/1.5, 1), 0, 1)
```

Better, but **still saturated**: mean 0.934, and **52 %** of v7 assemblies are still at exactly
1.000 (v1/v2/v5: 78–89 %). The correlation with the final score rose from +0.02/+0.10 to +0.354, so
it is now doing *something* — but a metric that is at its ceiling on half the population cannot
discriminate the top half of the distribution, which is exactly where casting decisions are made.
The 0.35 and 1.5 normalisers are too small.

### `min(emo_peak, 1)` — dead by clipping

`emo_peak` has a corpus mean of **2.01** and the score term is `min(peak, 1)`. Result:

| generation | assemblies at the cap |
|---|--:|
| v1 | 95.6 % |
| v2 | **100 %** |
| v5 | 93.3 % |
| v7 | 80.7 % |

In v2 the "emotional intensity" term is a literal constant (sd 0.0000, see §3). The clip was
presumably meant to stop one runaway part dominating; instead it removed the term. If you want
emotional intensity in the score, clip at ~3 or use a soft saturation.

### `qual` — an offset, not a discriminator

`qual` is the **unnormalised** mean of the quality heads: mean 3.338, sd 0.213, range 2.56–3.61
over 540 assemblies. Every other term is divided into 0–1 (`genu/6`, `blend/10`, `spk`, `arc`) but
`qual` is not, so a weight of 0.07 buys a contribution of **0.234** — a third of a typical score —
that barely moves. Two side effects:

- the "core" is **not bounded by 1**: two v1 assemblies scored above 1.0, the highest being
  **1.0093**. A score you cannot compare to 1 is a score nobody can calibrate against;
- the ranking is effectively over the remaining terms with a constant added.

### `n_bursts`

Counted and stored, never used in any score in v1–v7. v8 uses only the *edge* subset.

### The burst classifier's `identity`

Not part of the casting harness, but relevant if you extend it: on the `VB-control` grid the burst
classifier scored `identity` **0.000 on every one of the 32 cells** where bursts were plainly
audible, with a mean target probability of 0.0055. **Locator span timing is reliable; the class
label is not.** Score burst *presence*, and judge identity by listening.

---

## 5. Two ways the score actively selected against what it wanted

**Blending.** In v1–v7 `blend` had weight 0.00 in the *candidate* ranker and 0.08–0.14 in the
assembly score, while `genu` carried 0.34–0.40 per candidate. Pooled over 540 assemblies
`corr(genu, blend)` is −0.044, and within v7 it is **−0.207**. So the candidate ranker, which is
where takes are actually thrown away, was mildly selecting *against* clean burst blending.
Measured consequence: **23.1 %** of shipped top-1 assemblies (and 24.6 % of all top-5) score below
3/10 on blending. v8 gives blend 0.11 per candidate and 0.12 in the assembly.

**Non-verbal parts get the multiplier free.** `sense()` sets `wer = 0.0` unconditionally when a part
is marked `nonverbal`, on the reasonable ground that a scream has no words to get right. But since
the assembly score is essentially `(1 − WER) × constant` (§3), a `nonverbal` part contributes a
perfect intelligibility score by construction. An X2 assembly with two of three parts non-verbal is
being scored on one third of its content, which is how a chainsaw round posted WER 0.086 while its
middle part transcribed as the single word "you".

---

## 6. Prosody terms (v7)

```
prosody_fit(part)   = 1 − mean over {tempo, chunk} of min(|measured − target| / 2, 1)
runaway(part)       = min( max(0,(wps − 4.0)/1.5) + max(0,(tempo − 5)/1) if not declared , 1 )
prosody_join(a,b)   per dim in {tempo (tol 0.8), chunk (tol 0.8), dflu (tol 0.8)}:
      prosody_turn declared:  d < 0.8      → d/0.8·0.6      (asked for a change, didn't move)
                              0.8 ≤ d ≤ 3.5 → 1.0
                              d > 3.5      → max(0, 1 − (d−3.5)/2)   (lurched)
      not declared:           max(0, 1 − max(0, d − tol)/2)
pros = 0.4·mean(prosody_fit) + 0.6·mean(prosody_join)
```

Measured over v7's 27 rounds / 83 parts: `pros` 0.754 mean, `pros_join` 0.840, `pros_fit` **0.624**,
`runaway` 0.061. The low `pros_fit` is mostly the model's range, not disobedience — see the
saturating tempo dial in [what partly worked](what_partly_worked.html#1) — so do not tune the
planner against it.

`edge_bursts`, `narration` and `burst_db` are computed by the v7 worker but were **not** written
into `parts_run[].best` in the shipped `out_v7` artifacts (that field was added later, for v8), so
there is no v7 measurement of them in this corpus. Their multipliers are v8-only.

---

## 7. The supervisor's numbers

The Gemini supervisor gives each of the five presented takes a 0–10 score, an ordering, and two
sentences of feedback. Its distribution over 540 take-scores:

| score | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| count | 3 | 3 | 29 | 72 | 109 | 126 | 113 | 78 | 7 |

Compressed into 5–9, as an LLM judge on a 0–10 scale usually is. `sup_best` per round is 8 or 9 in
almost every round and therefore carries little information; **`sup_mean` is the usable summary**,
and even it should be read with [what failed §5](what_failed.html#5) in mind.

`agreement_spearman` is Spearman's ρ between the agent's ordering (which is always 1,2,3,4,5 by
construction) and the supervisor's ranking. Because the agent's ordering is the presentation order,
this statistic is **only** interpretable if the judge has no position bias — which it did not have
in v7, and did have in v1/v2/v5.
