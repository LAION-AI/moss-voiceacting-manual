# Acting challenges — the full record

Everything that was run on the nine casting challenges, consolidated so a new agent can warm-start
from it instead of rediscovering it. This tree is the *complete* record; the
[one-page playbook](../acting_challenges.html) is the short version of it.

**What exists.** Four complete casting runs (9 challenges × 3 rounds each), two aborted runs, two
smoke tests, plus an earlier eight-task edge-case swarm and two vocal-burst grids:

| body of work | when | what it is | usable rounds / generations |
|---|---|---|--:|
| edge-case swarm `T0001`–`T0008` | 2026-08-03/04 | evolutionary search, 8 hard delivery edge-cases, one agent each | 589 logged genomes |
| burst dose sweep `VB-dose` | 2026-08-04 | burst adapter λ 0.25–1.00 × emotion λ 0–0.50 | 2,304 generations |
| burst with/without control `VB-control` | 2026-08-05 | the missing λ = 0 baseline, 8 emotion families × 60 burst classes | 1,512 generations |
| **casting v1** `out_v1` | 08-05 14:20–15:00 | first multi-part casting run; **no** reference, **no** identity measurement | 27 rounds |
| **casting v2** `out_v2` | 08-05 21:42–22:03 | reference conditioning + ECAPA + voice conversion | 27 rounds |
| v3 / v4 attempts | 08-06 19:18–19:47 | continuation implementation; three crashes, one partial run | 9 round-1 results (`out_v4c_stub`) |
| **casting v5** `out_v5_real` | 08-06 19:51–20:07 | continuation chained from the full previous part | 27 rounds — **results not paired with their plans, do not use** |
| v6 | 08-06 22:21 | never generated anything — stale `STOP`, all 9 workers exited after 0 rounds | 0 |
| **casting v7** `out_v7` | 08-07 15:15–16:05 | anchor + 4 s tail, identity enforcement, prosody discipline | 27 rounds |
| v8 | running now | — | — |

> **Two pages added after this tree was first built:**
> [Does the local reward predict a listener?](reward_vs_listener.html) — the measured correlation
> between the agent's own composite reward and the Gemini supervisor, per metric, per challenge and
> per subgroup, and what it means for running this without an external judge.
> · [Keeping one voice across clips while the emotion changes](../voice_consistency_continuation.html)
> — the reference/continuation recipe extracted as a standalone guide for any character-consistency
> task, no acting-challenge context needed.

**Trustworthy plan → result pairs in the corpus: 82** (27 v1 + 27 v2 + 27 v7 + 1 smoke2), plus 9
round-1 results in `out_v4c_stub` with no supervisor verdict. 27 further rounds exist in
`out_v5_real` and must be discarded — see [what failed](what_failed.html#1).

---

## The pages

| page | what is in it |
|---|---|
| [Per challenge](per_challenge.html) | The nine briefs, every round ever run on each, and the plan worth re-running — full verbatim captions, adapters, doses, sampling, measured scores and the supervisor's verdict |
| [Version history](versions.html) | Generation by generation: what changed, what it bought, and the cross-version numbers |
| [What worked](what_worked.html) | Techniques that reproducibly helped, each with the measurement behind it |
| [What partly worked](what_partly_worked.html) | Things that helped under some conditions — with the boundary stated |
| [What failed](what_failed.html) | Negative results and harness failures, so nobody retries them |
| [Metrics](metrics.html) | What each number means, the exact scoring formulas each generation used, and which metrics turned out to be useless |
| [Every prompt](prompts.html) | All 351 part-captions, verbatim, grouped by challenge and generation |
| [Edge-case swarm](swarm_edgecases.html) | `T0001`–`T0008`: the recipes, and why half of them should be read sceptically |

---

## The headline finding of each generation

| gen | headline | measured |
|---|---|---|
| v1 | Multi-part assembly works at all; a 30 s arc can be built from 3 parts | 27/27 rounds completed, supervisor mean 7.14 |
| v1 | **Nobody kept the voice.** No `reference`, no speaker measurement — the parts are independent draws of an unspecified speaker | speaker similarity simply not measured |
| v1 | Non-verbal parts collapse: `tokens` defaults to word count, and a scream has no words | 13 of 88 parts came back under 2 s; X2 assemblies ran 12.7–14.5 s against a 30 s target |
| v2 | Reference conditioning is **not enough** | later parts at 0.625 mean similarity, 69 % below 0.75, 23 % below 0.55 |
| v2 | It fixed the length problem completely | 0 of 88 parts under 2 s; 78 % of assemblies within ±20 % of 30 s (v1: 41 %) |
| v5 | Chaining continuation from the *whole* previous part lets drift compound | part 1 0.691 → part 2 0.692 → part 3 **0.280** |
| v7 | Continuation from **anchor + 4 s tail**, with identity enforced rather than ranked | later parts 0.784 mean, 12 % below 0.75, 4 % below 0.55 |
| v7 | Prosody can be planned and measured; the tempo dial saturates at ~2–3 | asking 4 lands at 2.82, asking 1 lands at 2.97 (n = 83 parts) |
| v7 | Non-verbal parts are a **different regime** — every remaining identity failure is a scream | spoken parts 0.793 mean, non-verbal 0.561 |

## The five findings that matter most, and were not in the short playbook

1. **The casting score is a WER detector.** Across all four generations the `(1 − WER)` multiplier
   correlates **+0.91 to +0.98** with the final assembly score, while genuineness — nominally the
   largest single weight — correlates **+0.00 to +0.04**. Eight carefully-weighted terms, one of
   which does all the work. [→ metrics](metrics.html#3)
2. **Three of the eight scoring terms are dead.** `min(emo_peak, 1)` is saturated at its cap in
   **92.4 %** of assemblies (100 % in v2); `arc` sat at exactly 1.0 in **84 %** of the 81 shipped
   v1/v2/v5 assemblies and took only three distinct values ever; `qual` has a standard deviation of 0.21 on a mean of
   3.34 and contributes a near-constant **31 %** of a v2 score. [→ metrics](metrics.html#4)
3. **The supervisor was rating position, not performance.** In v1/v2/v5 the Gemini listener picked
   the take presented 4th or 5th as its favourite in **71 of 81 rounds** and the agent's top-ranked
   take in **3 of 108** (chance is 20 %). Within a round, the agent's score and the listener's score
   are **uncorrelated (r ≈ 0.00)** in every generation. The v7 supervisor prompt — which asks for
   explicit `same_voice` and `pacing` judgements — removed the bias (its position correlation is
   −0.12 against +0.32/+0.35). Every "rank agreement ρ" from v1/v2/v5 measures the bias, not
   quality. [→ what failed](what_failed.html#5)
4. **`out_v5_real` is the contaminated run, not `out_v4_failed`.** All 27 of its `res.json` files
   are 2.2–2.4 hours *older* than the `req.json` next to them: new plans were written into a
   directory that still held old results. Recomputing WER from the stored transcript against the
   stored script gives ≈0.95 for all 27 rounds against a reported 0.150.
   [→ what failed](what_failed.html#1)
5. **The scoring code on disk is v8, not v7.** `actworker_v7.py` was edited after the v7 run
   finished. The weights that actually produced `out_v7` were recovered by least-squares from the
   135 shipped assemblies (residual < 0.001) and differ from the file. Read the formulas from
   [metrics](metrics.html#2), not from the source. [→ metrics](metrics.html#2)

## What is still unsolved

- **X2_chainsaw** — sustained non-verbal agony. No generation produced a usable ~30 s take.
  [→ per challenge](per_challenge.html)
- **The feedback loop does not converge.** Pooling all four generations, the supervisor's best round
  was round 1 in **21 of 36** task-runs, round 3 in only 9. Every gain so far came from mechanical
  fixes to the harness, not from the round-to-round direction.
- **No local sensor predicts the listener.** Over 108 rounds the composite score correlates +0.13
  with the supervisor's mean, and within v7 alone +0.015.
