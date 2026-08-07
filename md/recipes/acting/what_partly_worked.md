# What partly worked

Things that helped under some conditions and not others. Each entry states the **boundary** — the
condition under which the technique stops paying. Part of the
[acting-challenge tree](index.html).

---

## 1. Declaring `tempo_target` — the dial is followed, but it saturates

The planner declares a target tempo per part on a 0–6 scale and the harness scores the distance to
it. Measured over all 83 v7 parts (best kept take of each):

| asked | n | measured mean | sd | measured min–max |
|---|--:|--:|--:|---|
| 1 | 3 | **2.97** | 1.27 | 1.31 – 4.39 |
| 2 | 29 | **2.05** | 0.81 | 0.36 – 3.97 |
| 3 | 39 | **2.79** | 0.81 | 0.55 – 4.31 |
| 4 | 12 | **2.82** | 1.20 | 0.30 – 4.41 |

Overall bias **−0.18**, mean absolute error **0.77**.

**Where it works:** 2 lands at 2.05 and 3 lands at 2.79 — those two requests are honoured almost
exactly, so the dial is usable for the difference between "unhurried" and "ordinary".

**Where it stops:** the model's real range is about **2–3**. Asking for 4 buys nothing over asking
for 3 (2.82 vs 2.79), and asking for 1 produces something *faster* than asking for 2. Above 4 the
`runaway` penalty starts firing on a take you asked for. Get urgency from the delivery cue, the
emotion adapter or the chunking — not from a bigger tempo number.

## 2. `chunk_target` — the better dial, within the same narrow range

| asked | n | measured mean | sd |
|---|--:|--:|--:|
| 1 | 11 | **1.05** | 0.76 |
| 2 | 38 | **2.14** | 0.75 |
| 3 | 34 | **2.44** | 0.70 |

Bias −0.16, MAE 0.65. Requests of 1 and 2 are tracked almost exactly, which makes chunking the
**most expressive dial available for fear and grief**: broken, gasping groups at ordinary tempo read
as genuine distress, whereas raising the tempo reads as a caffeinated narrator. X1_horror_scream's
best round declares `chunk_target 1` on the terror part and measures 0.86.

**Where it stops:** 3 lands at 2.44, so the top of the scale compresses the same way tempo does. The
dial is real between 1 and 3 and imaginary above it.

## 3. `prosody_turn` — only if the turn is actually written

Declaring `prosody_turn: true` tells the harness that a seam is *meant* to change, so a change of
0.8–3.5 points scores 1.0 and no change is penalised. That is the right shape — but declaring the
flag does not create the change.

- **Worked:** X1_horror_scream v7 r3 declares turns on parts 2 and 3 with a tempo shape of 3 → 1 → 4
  and a chunk shape of 3 → 1 → 2. Measured: tempo 3.03 → 1.31 → 3.71, chunk 3.01 → 0.86 → 1.62 →
  `pros_join` **1.000**, `pros_fit` 0.861, the best prosody of any v7 round.
- **Did not work:** X4_ice_water v7 r2 declares turns on parts 2 and 3 while holding `tempo_target`
  flat at 3 and stepping `chunk_target` 3 → 2 → 2 — i.e. it declares a change and asks for almost
  none. `pros_join` **0.610**, `pros_fit` 0.530, the second-worst prosody in the run.

**Boundary:** a declared turn must move roughly 1–3 points on at least one of tempo / chunk / dflu.
If the plan does not ask for the move, declaring the flag actively costs score.

Run-level effect of the whole prosody package, v7's 56 seams:

| |ΔPart| between consecutive parts | mean | median | max | over 2 points |
|---|--:|--:|--:|--:|
| tempo | 0.97 | 0.80 | 3.18 | 12.5 % |
| chunk | 0.92 | 0.68 | 2.71 | 10.7 % |
| dflu | 1.02 | 0.97 | 2.64 | 10.7 % |

## 4. Voice conversion as a repair

Chatterbox S3Gen VC, run only when a candidate falls below `vc_threshold`, kept only if ECAPA
similarity rose **and** DNSMOS `ovrl_mos` did not fall by more than 0.15.

| generation | `vc_threshold` | rounds whose shipped take contains ≥1 converted part | parts converted |
|---|--:|--:|--:|
| v2 | 0.55 | 14 / 27 | 22 |
| v5 | 0.55 | 4 / 27 | 7 |
| v7 | 0.75 | 14 / 27 | 20 |

**Where it works:** on ordinary spoken parts it is cheap insurance. The DNSMOS guard means a
conversion that damages the take is discarded automatically, and a measured example from this stack
went 3.345 → 3.358 overall MOS across conversion, i.e. no damage.

**Where it stops:** it did not rescue the failures that mattered. v2 shipped 22 converted parts and
still ended with 23 % of later parts below 0.55 similarity; X2_chainsaw's identity never recovered
in any generation despite the repair being available. Conversion can only align a take that has
content to align — a 0.1 s stub or a near-silent scream has nothing for it to work on. And at
`vc_threshold` 0.55, most of the drifting parts were never even offered to it: **54 % of v5's
continuation parts landed below 0.75 and most never triggered a repair.** Raising the threshold to
0.75 is what made the repair reachable.

## 5. Stacking several adapters on one part

**Where it works:** the "mixed feeling" briefs. X4_ice_water's brief asks for shock, draining
fright, amused delight and relief to be *audible at once*; its best part carries
`Relief 0.70 + Amusement 0.60 + Chuckle 0.50` simultaneously and it is the pattern that produced the
corpus's highest genuineness measurements. C2_biggest_fear crossfades
`Fear 0.5 → Fear 0.4 + Relief 0.4 → Relief 0.55 + Elation 0.65` so nothing is switched off at a
seam.

**Where it stops:** on **non-verbal** parts. Restricted to spoken continuation parts, the number of
adapters on a part correlates **+0.012** with speaker similarity — no effect at all:

| adapters on the part | n (spoken) | mean spk_sim |
|---|--:|--:|
| 1 | 23 | 0.800 |
| 2 | 14 | 0.770 |
| 3 | 12 | 0.802 |
| 4 | 1 | 0.847 |

But the two 5-adapter parts in the corpus — both X2_chainsaw non-verbal agony parts stacking
`Distress + Fear + Pain + Sob + Scream + Whimper + Painful Moan` at 0.5 each — averaged **0.561**.
The apparent "stacking hurts identity" correlation of −0.42 over all parts is entirely those two
parts, and they are non-verbal, where ECAPA is unreliable anyway. **Boundary: stack freely on spoken
parts; on non-verbal parts you are measuring nothing and the stack is a guess.**

## 6. Raising temperature above 1.0

| temperature | n (spoken continuation parts) | mean spk_sim |
|---|--:|--:|
| 1.00 | 36 | **0.817** |
| 1.05 | 9 | 0.775 |
| 1.10 | 1 | 0.827 |
| 1.15 | 1 | 0.762 |
| 1.20 | 2 | 0.756 |

Within spoken parts the correlation is −0.28, but that is dominated by a single part at temperature
1.08 that landed at 0.169. **Do not treat this as established.** The defensible statement is: 1.0 is
the well-sampled setting (36 of 50 spoken continuation parts), everything above it is n ≤ 9, and
there is no evidence in this corpus that raising temperature on a *spoken* part buys anything. The
model's own manual recommends 1.3–1.5 for pure non-verbal parts, and the corpus contains only four
such parts, all in X2_chainsaw, all of which failed for other reasons.

## 7. Breaking the burst-dose rule

The burst chapter's rule is that the emotion adapter must sit **at or below** the burst adapter's
dose, because they compete. Across the corpus, 16 of the 127 parts that carried both broke it.

**It sometimes works anyway.** X1_horror_scream v7 r3 — the best-measured X1 assembly in the corpus,
WER 0.052 — stacks `Fear 0.70` above `Scream 0.50` on its scream part, and that part measured
`emo_peak` 3.829, the highest single-part emotion measurement in v7.

**Boundary:** the rule is about *burst presence*, and that is not what X1's part needed. Its scream
is written as words (`"No!" (Scream) "No, no, no! Get away from him!"`) rather than as a non-verbal
event, so the part does not depend on the locator finding a burst. If you need the burst to *occur*,
follow the rule; if the burst is written into the line as shouted words, the emotion adapter can
lead.

## 8. Four parts instead of three

| parts | rounds | agent score | supervisor mean | WER | duration |
|---|--:|--:|--:|--:|--:|
| 3 | 88 | 0.732 | 6.86 | 0.163 | 28.8 s |
| 4 | 20 | 0.741 | 6.84 | 0.150 | 33.8 s |

No difference in quality; four parts just runs 5 s longer and costs another generation pass. The
planner chose four parts in 20 of 108 rounds and it was never the deciding factor.
