# Version history — what each generation changed, and what it bought

Generation by generation, with the cross-version numbers recomputed from the run artifacts rather
than copied from any earlier write-up. Part of the
[acting-challenge tree](index.html).

---

## 1. Timeline

Reconstructed from file mtimes and Slurm logs in `act/logs/`, so it is checkable.

| when (2026) | job | directory | outcome |
|---|---|---|---|
| 08-05 14:20–15:00 | `act_1248197` | `out_v1` | **complete**, 27 rounds |
| 08-05 21:42–22:03 | `act_1252687` | `out_v2` | **complete**, 27 rounds |
| 08-06 19:18 | `act_1266716` | — | cancelled 6 s after start (interrupted launch) |
| 08-06 19:22 | `act_1266837` | `out_v4_failed` | crash: `audio code tensor must have shape [T, 12], got (652800,)` — a waveform was passed into the assistant turn instead of codec codes. 9 plans + 9 anchor wavs, **no results** |
| 08-06 19:34 | `act_1266996` | — | crash: `'numpy.ndarray' object has no attribute 'unsqueeze'` — `encode_audios_from_wav` wants a torch tensor |
| 08-06 19:39–19:49 | `act_1267180` | — | crash: `LibsndfileError: Error opening r1_anchor.wav: System error` |
| 08-06 19:37–19:47 | `act_1267259` | `out_v4c_stub` | first working continuation; cancelled part-way. 9 round-1 results, 1 supervisor verdict |
| 08-06 19:51–20:07 | `act_1267381` | `out_v5_real` | worker completed 3 rounds; the **results were later re-served to a new set of plans** — see [what failed](what_failed.html#1) |
| 08-06 22:08–22:15 | `act_1269132` | `out_smoke2` | 1-task smoke test, complete |
| 08-06 22:21:21 | `act_1269164` | — | **all 9 workers exited "after 0 rounds"** in the same second: a stale `STOP` file |
| 08-07 15:01–15:11 | `act_1276367` | — | cancelled |
| 08-07 15:15–16:05 | `act7_1276411` | `out_v7` | **complete**, 27 rounds (X2 re-run separately as `act7r_1276627` after a crash) |
| 08-07 23:56– | `act7_1283347` | `out/` | v8, running |

Wall-clock per round grew as the harness got stricter: v1 118 s mean, v2 185 s, v5 208 s,
v7 **311 s** (max 1,203 s — one X2 round with two resample passes).

---

## 2. What changed between generations

| | v1 | v2 | v5 | v7 |
|---|---|---|---|---|
| how later parts get the voice | nothing | `reference=[anchor.wav]` | `mode="continuation"`, prefix = **whole previous part**, chained | `mode="continuation"`, prefix = **anchor + 4 s tail** |
| ECAPA speaker similarity | not measured | measured | measured | measured |
| speaker in the assembly score | — | mean over parts, weight 0.20 | mean over parts, weight 0.20 | **½ mean + ½ worst part**, weight 0.22 |
| hard floor | — | `spk_floor` 0.60 (default), 0.25× penalty | 0.60, 0.25× penalty | **0.68, sub-floor takes excluded from ranking outright** |
| resample gate | — | — | — | **`spk_target` 0.82 on the take that would be kept**, up to 2 extra batches |
| voice conversion | — | `vc_threshold` **0.55** | **0.55** | **0.75** |
| seed | `7000+100·rnd+10·pi` | same | same | `crc32(task)·1000 + 7000+100·rnd+10·pi+3331·att`, plus `+7919` per sub-batch |
| sub-batches per part | 1 (`cands == batch`) | 1 | 1 | **2** (`--cands 16 --batch 8`) |
| prosody | — | — | — | `tempo_target`, `chunk_target`, `prosody_turn`; `pros`, `runaway`, `wps` measured and scored |
| `GENERAL` identical across parts | never (0/27) | never (0/27) | never (0/27) | **always (27/27)** — required by the planner prompt |
| planner asked for `turn_from` | no | yes | yes | yes |
| supervisor rubric | score + free comment | same | same | **+ `same_voice` + `pacing` verdicts** |

The continuation caption is also augmented by the harness in v5/v7 — the planner's `GENERAL` gets
four extra sentences appended before `SCRIPT:` (same speaker / still acting, not narrating / begin
straight into speech, no onset burst / and, when `turn_from` is set, an explicit "moves out of X
into Y"). The effective captions are recorded in `parts_run[].caption` in v7 and reproduced in
[prompts](prompts.html).

---

## 3. Speaker identity across generations — the central number

Measured on **later parts only** (part 0 is the anchor and is 1.000 by definition), as the mean over
the four kept takes of each part, read out of the worker logs so all four generations are measured
the same way.

| generation | mechanism | n parts | mean | part 1 | part 2 | part 3 | below 0.75 | below 0.55 |
|---|---|--:|--:|--:|--:|--:|--:|--:|
| v1 | nothing | — | *not measured* | — | — | — | — | — |
| v2 | `reference=[anchor]` | 61 | 0.625 | 0.638 | 0.629 | 0.557 | **69 %** | 23 % |
| v5 | continuation chained from the full previous part | 55 | 0.662 | 0.691 | 0.692 | **0.280** | 55 % | 25 % |
| v7 | continuation from anchor + 4 s tail, floor + resample + VC | 51 | **0.784** | 0.755 | 0.811 | 0.820 | **12 %** | 4 % |

Three things this table says that the shorter write-up does not:

- **Reference conditioning alone is barely better than nothing.** 0.625, with 23 % of later parts
  below 0.55 — i.e. audibly a different person. The `reference` argument is necessary but it does
  not solve the problem.
- **Chained continuation raised the mean and made the tail worse.** v5's mean is 0.037 higher than
  v2's, but part 3 collapses to 0.280 (n = 4) and the fraction below 0.55 goes *up*. Drift
  compounds when each part conditions on the last.
- **v7's gain is not just the prefix.** Anchor + tail, the 0.68 exclusion, the 0.82 resample and the
  VC repair all ship together; the run cannot separate them. *Inferred* from the resample log:
  9 of 56 continuation parts triggered a resample, so the gate is doing real work but is not the
  whole 0.12.

Measured on the **assembly** instead (mean over all parts of the shipped top-1 take, which is how a
listener hears it):

| generation | mean | median | worst round | rounds below 0.75 |
|---|--:|--:|--:|--:|
| v2 | 0.765 | 0.803 | 0.440 | 26 % |
| v5 | 0.777 | 0.810 | 0.361 | 37 % |
| v7 | **0.862** | 0.870 | 0.621 | **4 %** |

Note the v5 anomaly: its assembly mean is higher than v2's while the fraction of *bad* assemblies is
higher. Averaging hides a single collapsed part, which is exactly why v7 changed the assembly term
to ½ mean + ½ worst part.

---

## 4. The supervisor numbers are not comparable across generations

| generation | supervisor mean per round | supervisor best per round | rank agreement ρ | ρ > 0 |
|---|--:|--:|--:|--:|
| v1 | 7.14 | 9.00 | **−0.089** | 56 % |
| v2 | 7.05 | 8.93 | **−0.259** | 41 % |
| v5 | 6.95 | 8.81 | **−0.311** | 30 % |
| v7 | 6.29 | 8.19 | **+0.193** | 67 % |

The apparent decline from 7.14 to 6.29 is **not** a decline in quality. The v7 driver uses a
different supervisor prompt: it names the two known failure modes and requires a `same_voice` and
`pacing` verdict per take. Under that rubric the listener returned `same_voice=no` on **38 of 135**
v7 takes and `pacing=runaway` or `disjointed` on **64 of 135**. A stricter rubric produces lower
numbers. Do not compare v7 supervisor scores with v1/v2/v5 supervisor scores.

The same prompt change is what fixed the rank agreement — see
[what failed §5](what_failed.html#5) for why the v1/v2/v5 ρ values are measuring presentation order.

---

## 5. Everything else, side by side

Top-1 assembly of each round, all 27 rounds per generation.

| | v1 | v2 | v5 ⚠ | v7 |
|---|--:|--:|--:|--:|
| agent composite score (mean) | 0.734 | 0.748 | 0.750 | 0.701 |
| genuineness `genu` (0–6) | 1.77 | 1.54 | 1.72 | 1.52 |
| burst blending `blend` (0–10) | 4.47 | 4.42 | 4.48 | 3.96 |
| assemblies with blend < 3 | 19 % | 22 % | 33 % | 19 % |
| `emo_peak` | 2.13 | 2.27 | 2.02 | 1.60 |
| `arc` | 0.977 | 0.966 | 0.981 | 0.947 |
| `arc` exactly 1.0 | 85 % | 78 % | 89 % | 52 % |
| WER, C-challenges | 0.099 | 0.079 | — | 0.119 |
| WER, X-challenges | 0.343 | 0.236 | — | 0.159 |
| duration mean (s) | 26.5 | 30.4 | 31.9 | 30.3 |
| duration within 30 ± 20 % | 41 % | **78 %** | 59 % | 67 % |
| parts shorter than 2 s | 13/88 | **0/88** | 1/82 | 3/76 |
| rounds using voice conversion | — | 14/27 | 4/27 | 14/27 |
| seconds per round | 118 | 185 | 208 | 311 |

Reading it:

- **v2 fixed length, v7 fixed identity and intelligibility on the hard challenges.** X-challenge WER
  halved from v1's 0.343 to v7's 0.159 while C-challenge WER stayed flat — the gain is entirely in
  the scream/burst material.
- **v7 costs emotion.** `genu`, `blend` and `emo_peak` are all lowest in v7. Continuation from an
  anchor drags the opening mood forward, and the identity floor rejects the wildest takes, which
  are often the most genuine. This is a real trade, not a measurement artefact — the same trade is
  visible in the fall of `emo_peak` from 2.27 (v2, reference-only) to 1.60 (v7).
- **`arc` de-saturated but did not become useful.** The continuous replacement still returns exactly
  1.0 on 52 % of v7 assemblies. [→ metrics](metrics.html#4)

---

## 6. Rounds do not converge

Whether round 3 beat round 1 within the same run:

| generation | agent score r3 > r1 | supervisor mean r3 > r1 | supervisor's best round was r1 / r2 / r3 |
|---|--:|--:|---|
| v1 | 6/9 | 3/9 | 6 / 1 / 2 |
| v2 | 7/9 | 3/9 | 5 / 1 / 3 |
| v5 ⚠ | 5/9 | 2/9 | 6 / 1 / 2 |
| v7 | 5/9 | 3/9 | 4 / 3 / 2 |
| **pooled** | 23/36 | **11/36** | **21 / 6 / 9** |

The agent's own score usually improves — which is expected, because the planner is shown its own
score and optimises it. The listener's score usually does not. Pooled over all four generations the
best round by supervisor mean was **round 1 in 21 of 36** task-runs.

Part of the reason is that the feedback is nearly content-free: **71 %** of the 108 feedback strings
contain the word "transition" and **36 %** contain "gradual"; the two most common instructions the
supervisor ever gave were "make the transition more gradual" and "make X more Y".

---

⚠ **v5 columns are shown for completeness only.** The per-part identity figures in §3 come from the
worker log and are valid measurements of the audio v5 generated. The assembly rows in §5 are also
real measurements of that audio. What is *not* valid is attributing any of it to the plans stored in
`out_v5_real/*/round_NN.req.json` — see [what failed](what_failed.html#1).
