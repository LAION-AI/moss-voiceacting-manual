# What failed

Negative results and harness failures, with enough detail that nobody has to rediscover them. Part
of the [acting-challenge tree](index.html).

The harness failures are first, because four of them each destroyed a whole run and three of them
are invisible from the outside — the run reports success.

---

## 1. `out_v5_real` — results silently paired with the wrong plans

**This is the contaminated run in the corpus.** Not `out_v4_failed`, which is a different and much
more honest failure (§3).

The evidence, in order of how conclusive it is:

1. **File times.** All 27 `round_NN.res.json` files in `out_v5_real` are **7,803 – 8,698 seconds
   (2.2 – 2.4 hours) older** than the `round_NN.req.json` beside them. In every other run in the
   project the result is 66–2,061 s *newer* than the request, which is simply the generation time.

   | run | n pairs | res − req, median | pairs where the result is older than the request |
   |---|--:|--:|--:|
   | `out_v1` | 27 | +141 s | 0 |
   | `out_v2` | 27 | +213 s | 0 |
   | `out_v4c_stub` | 10 | +303 s | 0 |
   | **`out_v5_real`** | 27 | **−8,378 s** | **27 / 27** |
   | `out_v7` | 27 | +226 s | 0 |

2. **The transcripts do not match the scripts.** Recomputing WER from the stored ASR of part 0
   against the stored `text` of part 0:

   | run | reported WER (3-part mean) | recomputed part-0 WER | rounds where the two differ by > 0.4 |
   |---|--:|--:|--:|
   | `out_v1` | 0.208 | 0.108 | 0 / 27 |
   | `out_v2` | 0.149 | 0.063 | 0 / 27 |
   | **`out_v5_real`** | **0.150** | **0.948** | **26 / 27** |
   | `out_v7` | 0.137 | 0.076 | 0 / 27 |

3. **Sequence.** Worker job `act_1267381` generated and served all 27 rounds between 19:51 and
   20:07 on 08-06. The `req.json` files sitting next to those results were written at **22:16–22:17**
   by a *new* driver launch, and `agent_log.json` for each task was written within ~60 s of the last
   request — far too fast for any generation to have happened. That launch's workers then all exited
   at 22:21:21 (§2). The plans of the run that *did* produce this audio were overwritten in place and
   are not preserved anywhere.

**What this means in practice.** The measurements in `out_v5_real` are real measurements of real
audio — the per-part speaker-similarity figures in [versions §3](versions.html#3) are valid and
useful. What is **not** valid is attributing any score to any plan in `out_v5_real`. All 27 of its
rounds are excluded from the recipe selection in [per_challenge](per_challenge.html).

**The fix**, now in the worker startup:

```
for stale in [f"{outdir}/STOP"] + glob.glob(f"{outdir}/round_*.req.json") + \
        glob.glob(f"{outdir}/round_*.res.json"):
    try:
        os.remove(stale)
    except OSError:
        pass
```

**How to detect it in any future run, in one line:** assert that every `res.json` is newer than its
`req.json`, and spot-check one recomputed WER per run against the reported one.

## 2. Stale `STOP` files — a run that generated nothing and reported nothing

On 2026-08-06 at **22:21:21**, all nine workers of job `act_1269164` logged, within the same second:

```
[22:21:21] [C1_infidelity] serving; waiting for round requests
[22:21:21] STOP
[22:21:21] [C1_infidelity] worker finished after 0 rounds
```

An interrupted archive step had left nine `STOP` files from the previous run in place. Every worker
saw one immediately and exited. This is the direct cause of §1: the drivers of that launch were
alive, wrote their plans into directories that still contained the previous run's `res.json`, read
them instantly, and produced a complete-looking `agent_log.json` for all nine tasks.

The failure is **completely silent from the outside** — the run reports 27/27 rounds complete with
plausible scores.

## 3. Three continuation implementation crashes, in three consecutive launches

All on 08-06, all in `_generate_continuation`, all recoverable in minutes once seen — but each one
cost a launch:

| job | error | cause |
|---|---|---|
| `act_1266837` → `out_v4_failed` | `ValueError: audio code tensor must have shape [T, 12], got (652800,)` | a **waveform** was placed in the assistant turn; the processor wants codec codes |
| `act_1266996` | `AttributeError: 'numpy.ndarray' object has no attribute 'unsqueeze'` | `proc.encode_audios_from_wav` wants a **torch tensor**, not a numpy array |
| `act_1267180` | `soundfile.LibsndfileError: Error opening 'r1_anchor.wav': System error` | the anchor written by a previous, killed worker was truncated / mid-write |

**What `out_v4_failed` actually contains:** 9 round-1 plans (written 19:18:36–41) and 9
`r1_anchor.wav` files (written 19:22:28–19:23:06), and nothing else — no `res.json`, no
`agent_log.json`, no `learnings.md`. It is an aborted run, not a misleading one. Treat it as **zero
usable results**, and do not attribute the stale-file failure to it.

`out_v4c_stub` (job `act_1267259`) is the first launch where continuation actually worked: 9
completed round-1 results in ~4 minutes, one task (X2_chainsaw) reaching round 2, then cancelled. It
carries only one supervisor verdict, so it is not usable for comparison — but it is real.

## 4. A diagnostic log line killed a worker mid-run

```
File "actworker_v7.py", line 374, in _generate_continuation
    f"{np.mean(raw_s):.1f}s (min {min(raw_s):.1f} max {max(raw_s):.1f}) -> kept "
ValueError: min() arg is an empty sequence
```

The line exists to *prove* that the decode returns only the continuation. When every candidate in a
batch decoded to empty audio — which happens on non-verbal parts — `raw_s` was empty and `min()`
raised, taking down the X2_chainsaw worker in the middle of v7. The whole task had to be re-run as a
separate job (`act7r_1276627`).

> A diagnostic must never be able to take down the thing it is diagnosing. Guard it, and log the
> all-empty case explicitly instead.

## 5. The supervisor was scoring **position**, not performance

This is the most consequential negative result on this page, because the entire feedback loop was
built on the supervisor's ranking.

The five assemblies are always presented to the listener in the agent's own rank order, 1 to 5. Mean
supervisor score by *presentation index*:

| run | idx 1 | idx 2 | idx 3 | idx 4 | idx 5 | corr(index, score within round) |
|---|--:|--:|--:|--:|--:|--:|
| v1 | 6.70 | 7.48 | 6.52 | **7.85** | 7.15 | +0.134 |
| v2 | 6.19 | 7.00 | 7.00 | **7.70** | 7.37 | **+0.322** |
| v5 | 6.22 | 6.93 | 6.78 | 7.00 | **7.81** | **+0.347** |
| v7 | **6.52** | 6.30 | 6.52 | 6.11 | 6.00 | −0.121 |

And which take the listener named as its favourite:

| run | favourite was idx 1 | 2 | 3 | 4 | 5 |
|---|--:|--:|--:|--:|--:|
| v1 | 0 | 0 | 4 | 13 | 10 |
| v2 | 0 | 1 | 2 | 13 | 11 |
| v5 | 0 | 0 | 3 | 9 | 15 |
| v7 | 3 | 4 | 7 | 6 | 7 |

In v1/v2/v5 the listener's favourite was the 4th or 5th take presented in **71 of 81 rounds**.
Across all 108 rounds it chose the agent's top-ranked take **3 times (2.8 %)** against a chance rate
of 20 %.

**Therefore every `agreement_spearman` value from v1, v2 and v5 is measuring presentation order, not
quality**, and the strongly *negative* mean ρ of those runs (−0.09, −0.26, −0.31) is exactly what a
late-position bias produces against a fixed presentation order.

Two further measurements make it worse:

- **Within a round, the agent's score and the listener's score are uncorrelated.** Subtracting the
  round mean, `corr(agent take score, supervisor take score)` is −0.003 (v1), −0.007 (v2), −0.007
  (v5), +0.006 (v7). Over all 540 takes: **+0.058 raw, −0.003 within-round.**
- **Across rounds, no sensor predicts the listener either.** Over 108 rounds, `corr` with the
  supervisor's mean score is +0.013 for genuineness, +0.233 for blend, +0.238 for `emo_peak`, +0.032
  for arc, +0.029 for WER, and **+0.129 for the composite casting score**. Within v7 alone the
  composite correlates **+0.015**.

**What fixed the position bias:** the v7 supervisor prompt, which names the two known failure modes
and requires a `same_voice` and `pacing` verdict per take. That alone flipped the index correlation
from +0.32/+0.35 to −0.12 and lifted the mean ρ from −0.31 to +0.19. A judge given concrete criteria
listens; a judge given "score 0–10" rates recency.

**Do not** re-use the v1/v2/v5 ρ numbers, and do not compare v7 supervisor scores to earlier ones.

## 6. The feedback loop does not improve anything

Pooled over all four generations, the supervisor's best round was **round 1 in 21 of 36 task-runs**,
round 2 in 6 and round 3 in 9. Round 3 beat round 1 on the listener's score in only **11 of 36**.
(The agent's *own* score improves in 23 of 36 — expected, since the planner is shown that score and
optimises against it.)

Part of the reason is that the feedback is nearly content-free. Of the 108 feedback strings:

| the feedback contains… | share |
|---|--:|
| "transition" | 71 % |
| "more" | 84 % |
| "gradual" | 36 % |
| "voice" | 28 % |
| "scream" | 14 % |
| "pacing" | 11 % |
| "pause" | 3 % |

The modal instruction across four generations and nine challenges was *"make the transition from X
to Y more gradual"*. All 108 strings are textually distinct, so it is not a caching bug — the judge
simply has one note.

## 7. Seed collisions across tasks

```
seed = 7000 + 100 * rnd + 10 * pi + 3331 * att      # no task term
```

Every one of the nine challenges drew **seed 7110** for round 1, part 1. A listener caught it by
ear: the same vocal burst opened the same part in unrelated challenges. Worse, with `cands == batch`
there was a single RNG stream per part, so "best of 16" explored one neighbourhood. Fixed in v7 with
a `crc32(task)` term and a per-sub-batch offset — see
[what worked §3](what_worked.html#3).

## 8. Non-verbal parts: an unsolved regime, and a scoring hole

X2_chainsaw is the only challenge that was never solved in any generation. Three separate mechanisms
fail on non-verbal material:

- **ECAPA has nothing to measure.** A 1–3 s scream gives the speaker encoder almost no voiced
  sustained material. In v7, spoken continuation parts averaged **0.793** similarity with 4 % below
  0.55; the non-verbal parts averaged **0.561**. Every remaining identity failure in the run is a
  scream. A 0.82 resample gate there burns candidate budget on something it cannot fix.
- **Empty batches poison the next part.** In the v7 X2 re-run, part 1 came back with a best take of
  **0.1 s**; part 2, continuing from it, could not get above **0.367** similarity in 48 candidates
  across three batches.
- **`nonverbal: true` sets WER to 0.0 unconditionally**, and the assembly score is essentially
  `(1 − WER) × constant` ([metrics §3](metrics.html#3)). A non-verbal part therefore earns a perfect
  intelligibility score by construction. One round posted WER **0.086** while its middle part
  transcribed as the single word "you" and its third part echoed part 1's words.

Best X2 durations by generation: v1 12.7 / 14.5 / 13.2 s, v2 26.6 / 29.8 / 36.6 s (at WER
0.358–0.422 and speaker similarity 0.440–0.562), v7 14.4 / 18.0 / 23.9 s. Either short, or
unintelligible, or a different actor.

## 9. Three of the eight scoring terms carry no information

Documented in full in [metrics §4](metrics.html#4). Summary:

- `arc` (v1–v5) took **three distinct values ever** across 405 assemblies and sat at exactly 1.0 in
  80.5 % of them — 0.977 mean with 85 % at 1.0 on v1's shipped takes — while a listener reported
  hearing no arc at all. Its continuous replacement in v7 is better but still at exactly 1.0 on
  **52 %** of assemblies.
- `min(emo_peak, 1)` is at its clip in **92.4 %** of assemblies and in **100 %** of v2's — a literal
  constant with weight 0.18.
- `qual` is fed in **unnormalised** (mean 3.34, sd 0.21), so a weight of 0.07 buys a near-constant
  0.23 of a ~0.75 score, and the "core" is not bounded by 1 — two v1 assemblies scored above 1.0.

And the ranker was **selecting against burst blending**: blend had weight 0.00 in the candidate
ranker while genuineness (which correlates −0.21 with blend within v7) carried 0.34. Result: **23 %
of shipped top-1 assemblies score below 3/10 on blending**.

## 10. Operational failures that each cost a launch

- **A missing API key looks exactly like a bad model.** With `HYPRLAB_API_KEY` unset, every planner
  call returns `None`, the driver logs "unparsable plan" three times and gives up — indistinguishable
  from a model that cannot follow the schema. Fail loudly at startup:
  `if not gclient.KEY: sys.exit("FATAL: HYPRLAB_API_KEY is empty")`.
- **Launch from a script, and use `setsid`.** Two interrupted inline launches killed most of the
  drivers half-way through the loop, leaving runs that look fine from the outside. Job
  `act_1266716` was cancelled 6 seconds after starting for exactly this reason.
- **Wait for the workers before starting the drivers.** The worker clears stale handshake files at
  startup, so a driver that writes its request *before* the worker is up has that request deleted
  and then waits forever. The launcher polls the worker logs for `serving; waiting for round
  requests` on all nine tasks first.

## 11. Things measured that turned out not to be true

- **"Five burst classes cannot be produced inside a sentence."** Recomputed from `VB-control`: at
  burst λ 1.0 with no emotion adapter, five of 63 classes produced no located burst — `Hiss`,
  `Kissing Noises`, `Lip Smack`, `Person Whistling Playfully`, `Slurping Noises`. But that is **6
  takes per class**, and in the burst @1.0 + emotion @0.5 cell a *different* set of four is dead
  (`Affirmative Grunt`, `Lip Smack`, `Smack One's Lips`, `Soft Whistle`). Only **`Lip Smack`** is
  dead in both. The honest statement is that quiet non-vocalic mouth sounds are unreliable
  mid-sentence, not that five specific classes are impossible.
- **"More burst dose is always more burst."** It holds for 6 of 8 emotion families.
  `Sexual_Lust` peaks at λ 0.75 (54.2 %) and **falls to 43.8 %** at full merge; `Pain` does the same
  mildly (77.1 % → 75.0 %). Both are quiet, sustained, speech-adjacent bursts.
- **The scoring source on disk is not the scoring source that ran.** `actworker_v7.py` was modified
  at 23:53 on 08-07, after `out_v7` finished, and now holds the v8 formula (blend 0.08 → 0.12 in the
  assembly, plus three new multiplicative penalties). `actworker.py` holds a rewritten `arc` term
  that no v1/v2/v5 run ever executed. If you need the formula a given run used, recover it from the
  artifacts — [metrics §2](metrics.html#2) does exactly that.
