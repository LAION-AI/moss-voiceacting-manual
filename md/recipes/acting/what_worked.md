# What worked

Techniques that reproducibly helped, each with the measurement that supports it and the run it came
from. Part of the [acting-challenge tree](index.html). Things that helped only under some conditions
are on [what partly worked](what_partly_worked.html); negative results are on
[what failed](what_failed.html).

---

## 1. Continuation from an anchor plus a short tail

Three mechanisms were tried across four generations. Measured on later parts only (part 0 *is* the
anchor), as the mean over the four kept takes of each part:

| mechanism | generation | n | mean spk_sim | part 1 | part 2 | part 3 | < 0.75 | < 0.55 |
|---|---|--:|--:|--:|--:|--:|--:|--:|
| nothing — independent draws | v1 | — | not measured | | | | | |
| `reference=[anchor.wav]` | v2 | 61 | 0.625 | 0.638 | 0.629 | 0.557 | 69 % | 23 % |
| `mode="continuation"` chained from the **whole previous part** | v5 | 55 | 0.662 | 0.691 | 0.692 | **0.280** | 55 % | 25 % |
| `mode="continuation"` from **anchor + 4 s tail** | v7 | 51 | **0.784** | 0.755 | 0.811 | 0.820 | **12 %** | 4 % |

Reference conditioning keeps the timbre roughly right but starts a *fresh utterance* with its own
level and attack, which is heard as a cut. Continuation puts the previous audio in the **assistant
turn**, so the model believes it already produced it and predicts tokens that continue real acoustic
context. Chaining part-to-part is worse than it sounds: drift compounds, and the long prefix also
drags the old mood forward.

The prefix is `concat(anchor, last 4 s of the previous part)`: identity that cannot drift, plus just
enough prosodic context to join on.

Mechanics that each cost a debugging cycle, all confirmed by the crash logs in
[versions §1](versions.html#1):

- the assistant turn takes **codec codes `[T, 12]`**, not a waveform
  (`ValueError: audio code tensor must have shape [T, 12], got (652800,)`);
- `encode_audios_from_wav` wants a **torch tensor**, not a numpy array;
- `text` must carry **both** the words already spoken and the words still to come;
- the decode returns **only the continuation** and never echoes the prefix — measured over 77
  continuation batches in v7: 9.0 s mean prefix, 11.3 s mean decode. Do not trim it.

## 2. Enforce identity, do not merely rank it

Ranking the best of one batch is not enough: if a whole batch drifts, the least-bad take still
ships. v7 added three separate mechanisms:

| control | value | action |
|---|--:|---|
| `spk_target` | 0.82 | regenerate the part with a fresh seed (up to 2 extra batches), then rank the merged pool of 48 |
| `vc_threshold` | 0.75 | attempt Chatterbox S3Gen voice conversion; keep it only if ECAPA rose **and** DNSMOS did not fall > 0.15 |
| `spk_floor` | 0.68 | **exclude the take from ranking outright** (v2/v5 only multiplied its score by 0.25, which a high-genuineness take could out-earn) |
| assembly term | — | `0.5·mean + 0.5·min` over parts, weight 0.22 |

Test the take that would actually be **kept**, not the best similarity available in the batch:
testing the maximum meant a batch containing one good take never resampled even when the ranker then
chose a different one 0.3 lower.

Measured effect at the assembly level (mean over all parts of the shipped take):

| generation | mean | worst round | rounds below 0.75 |
|---|--:|--:|--:|
| v2 | 0.765 | 0.440 | 26 % |
| v5 | 0.777 | 0.361 | 37 % |
| v7 | **0.862** | 0.621 | **4 %** |

Cost: 9 of 56 v7 continuation parts triggered a resample, and wall-clock per round rose from 208 s
to 311 s.

**Free textual levers that ship with it.** Every continuation caption gets four sentences appended
to `GENERAL` before `SCRIPT:` — same speaker / still acting rather than narrating / begin straight
into speech with no onset burst / and, when `turn_from` is set, "across this passage the same voice
moves out of X into Y". And the planner is required to keep the `GENERAL` **byte-identical** across
parts: 27/27 v7 rounds do, 0/81 earlier rounds did.

## 3. Vary the seed per task **and** per sub-batch

A listener noticed that the same vocal burst opened the same part in unrelated challenges. The cause
was arithmetic:

```
seed = 7000 + 100 * rnd + 10 * pi + 3331 * att      # no task term
```

Every one of the nine challenges drew **seed 7110** for round 1, part 1. And with `cands == batch`
there was only ever one chunk, so `torch.manual_seed()` set **one** RNG stream per part — the 16
"candidates" explored a single neighbourhood, so best-of-16 was much weaker than the count suggests.

```
seed = (zlib.crc32(task.encode()) % 100000) * 1000 + 7000 + 100*rnd + 10*pi + 3331*att
torch.manual_seed(seed + 7919 * (i // batch))       # several sub-batches per part
```

v7 runs `--cands 16 --batch 8`, i.e. two independent streams per part.

## 4. Size non-verbal parts by duration, not by word count

`tokens` defaults to the number of words in `text`, and a scream's text — `"Aaaahh-! Kh-kh-!"` — has
almost none, so the model is told to make ~5 tokens and stops after 0.3 s. Use **~12.5 tokens per
intended second** and raise `max_new_frames` to match.

| generation | parts whose best take came back under 2 s | X2_chainsaw assembly durations |
|---|--:|---|
| v1 (bug present) | **13 / 88** | 12.7 s · 14.5 s · 13.2 s |
| v2 (fixed) | **0 / 88** | 26.6 s · 29.8 s · 36.6 s |
| v5 | 1 / 82 | 22.8 s · 26.6 s · 35.8 s |
| v7 | 3 / 76 | 14.4 s · 18.0 s · 23.9 s |

The same fix moved *all* assemblies onto target: the share of rounds landing within ±20 % of 30 s
went from **41 % (v1) to 78 % (v2)**.

## 5. Write the cue as an action, not as a tone

The most common continuation failure is that the voice stays correct but the model **stops acting
and reads the remaining words out**. It is measurable — VoiceNet's style heads give a narration
index:

```
narration = ½(S_NARR + S_NEWS) − ½(S_DRAM + S_CONV)      # positive = reading it out
```

The writing lever: make the cue something the character **does**. "The sentence collapses halfway
and they have to start it again" is a direction; "sad, resigned" is a label, and a label is an
invitation to narrate.

The best evidence in this corpus is C3_foreman, whose winning plan writes every line as an order
addressed to somebody — *"Nobody crowd him. Don't move him—do you hear me?"* … *"You, guide the
paramedics in. You, shut down the lift."* — and comes back with an ASR that matches the script
almost word for word at the **lowest adapter doses of any winner** (0.45 / 0.35 / 0.50) and the
**highest `emo_peak` of any winner** (2.815). Nothing about that plan is intense; everything about
it is specific.

The same lever shows up in C1's within-challenge ablation: across v2's three C1 rounds the adapters
were essentially constant (Anger 0.70 / 0.70 / 0.68) while the caption prose was rewritten each
round, and genuineness went 0.73 → 1.08 → **1.46** with blending 3.21 → 4.13 → **6.40**.

## 6. Bursts: inline, mid-line, and never next to a pause

Four rules, all of them measured, three of them elsewhere in this manual and one of them here.

**Merge the burst adapter.** Recomputed from the 1,512-generation `VB-control` grid (8 emotion
families × 60 burst classes, identical carriers and seeds):

| configuration | burst actually occurs | blend | genuineness | mean take duration |
|---|--:|--:|--:|--:|
| prompt only, no adapter | 23.5 % | 6.01 | 1.00 | 5.94 s |
| **emotion adapter @0.5 alone** | **16.4 %** | 6.30 | 1.15 | 5.34 s |
| burst adapter @1.0 | 71.4 % | 3.94 | 1.93 | 4.65 s |
| burst @1.0 + emotion @0.5 | 69.6 % | 3.80 | 1.83 | 5.38 s |

The emotion adapter **on its own suppresses the burst**, to below the no-adapter baseline. And the
dose curve, recomputed from the 2,304-generation `VB-dose` sweep:

| burst λ | burst occurs | blend | genuineness | mean take duration |
|---|--:|--:|--:|--:|
| 0.25 | 27.3 % | 5.73 | 1.48 | 5.73 s |
| 0.50 | 50.5 % | 4.76 | 1.89 | 5.69 s |
| **0.75** | **64.8 %** | 4.17 | **1.97** | 5.80 s |
| 1.00 | 71.4 % | 3.97 | 1.94 | **4.65 s** |

λ 0.75 is the knee: 91 % of full-merge presence at a materially better blend, and genuineness peaks
there. Note the duration column — at λ 1.00 the mean take is **1.1 s shorter**, which is the words
after the burst being eaten.

**Put the tag inside the line, never at an edge.** A gasp or throat noise in the first or last
~0.45 s lands exactly on the join once parts are concatenated and reads as a glitch. The two
cleanest examples in the corpus both do this:

- X1_horror_scream v7 r3: `"I feel—" (Gasp) "What was that? Don't move."` — the gasp interrupts a
  word mid-sentence.
- X3_birthday v2 r1: `"I do not know why I am even checking..." (Gasp) "What—" (Scream) "Oh my God,
  you are all here!"` — burst, then words immediately, **no pause**. A silence beat directly after a
  burst reliably triggers early truncation.

**Match the doses.** Across the corpus, 68 % of the 206 burst-adapter doses used were exactly 0.50,
and in 87 % of the 127 parts that carried both a burst and an emotion adapter the emotion dose was
at or below the burst dose.

## 7. Genuineness comes from the writing, not from the dose

Over 83 v7 parts, the emotion-adapter dose correlates **−0.226** with the measured `emo_peak` and
**+0.084** with genuineness. Bucketed:

| emotion λ | n parts | measured `emo_peak` | measured `genu` |
|---|--:|--:|--:|
| 0.30–0.45 | 11 | **1.98** | 1.04 |
| 0.45–0.55 | 32 | 1.79 | **1.69** |
| 0.55–0.65 | 11 | 1.58 | 1.41 |
| 0.65–0.80 | 29 | **1.32** | 1.57 |

*Inferred, and confounded:* the planner deliberately puts the **highest** doses on the parts that
have to swing hardest, and those are the parts that continuation resists most. So this is not
evidence that dose hurts — it is evidence that **dose is not what carries the result**, and that you
cannot buy a turn by raising λ.

What did produce the highest genuineness in the corpus (3.608, against a corpus mean of 1.62) was
X4_ice_water's loose, laughing, overlapping party delivery with `Amusement 0.5 + Chuckle 0.5`. Keep
emotion adapters in the **0.35–0.75** band — 98.6 % of the 492 doses used across the corpus were
inside it — and spend your effort on the line.

## 8. Rank whole assemblies, not parts

Keep the top-4 of each part and score every combination. It matters: the top-1 assembly used the
best candidate of *every* part in only **11 of 108 rounds (10.2 %)**. Two individually excellent
parts can join badly — a level jump, a tempo jump, or the same emotion twice where the script wanted
a turn.

But note how tight the field is: the score spread across the five shipped assemblies of a round is
**0.010 on average** (max 0.030). The ranker is choosing between near-identical candidates, which is
also why its ordering is so hard to validate against a listener.

## 9. Assembly hygiene

- **Level-match every part to part 0** over the loudest 60 % of 20 ms frames (`active_rms`), with a
  ±12 dB gain limit, then one gentle peak normalisation of the whole take to 0.95.
- **25 ms equal-power crossfade** at each seam. A hard concatenation leaves a click that the quality
  head reliably punishes, which would make every multi-part assembly look worse than it is.
- **Set `max_new_frames` per part**, not globally. X3_birthday's winning plan uses 180 / 150 / 240
  for a long-slow / short-burst / long-warm shape, and it is one of the very few rounds whose ASR
  matches its script on all three parts.

## 10. Resolve adapter names fuzzily — but log every resolution

The planner writes names from the manual and will say `Gratitude` for `Thankfulness_Gratitude` or
`Surprise` for `Astonishment_Surprise`. Silently dropping those would gut the plan. The resolver
scores shared **tokens**, not substrings, with an exact/stem weighting — a plain substring rule maps
`"painful moan"` to the *emotion* `Pain` and silently swaps a burst adapter for an emotion adapter.
Every fuzzy resolution is logged, because a silent wrong match changes what the plan does.

Adapters actually used across the 351 parts of the corpus:

| adapter | parts | dose min / mean / max |
|---|--:|---|
| `Fear` | 102 | 0.30 / 0.47 / 0.70 |
| `Scream` | 63 | 0.50 / 0.64 / 1.00 |
| `Amusement` | 63 | 0.35 / 0.44 / 0.60 |
| `Distress` | 59 | 0.30 / 0.50 / 0.72 |
| `Gasp` | 53 | 0.50 / 0.60 / 0.95 |
| `Anger` | 49 | 0.30 / 0.57 / 0.75 |
| `Astonishment_Surprise` | 49 | 0.35 / 0.48 / 0.75 |
| `Sadness` | 41 | 0.35 / 0.56 / 0.75 |
| `Gratitude` → `Thankfulness_Gratitude` | 40 | 0.35 / 0.46 / 0.70 |
| `Pain` | 39 | 0.35 / 0.50 / 0.75 |
| `Relief` | 37 | 0.35 / 0.57 / 0.75 |
| `Chuckle` | 28 | 0.50 / 0.62 / 0.90 |
| `Painful Moan` | 27 | 0.50 / 0.62 / 1.00 |
| `Elation` | 20 | 0.35 / 0.57 / 0.75 |
| `Sob` | 18 | 0.50 / 0.57 / 0.95 |
| `Whimper` | 18 | 0.50 / 0.63 / 0.90 |
| `Choking` | 6 | 0.80 / 0.88 / 0.95 |
| `Embarrassment` | 2 | 0.56 / 0.59 / 0.62 |
| `Sigh` | 1 | 0.50 |

Sampling was almost never varied: **130 of 351** parts used exactly
`temperature 1.0, top_p 0.95, top_k 30, max_new_frames 400`, and **94 %** (325 of 345 parts that
declare them) used `top_p 0.95, top_k 30`. The only systematic departures were non-verbal parts
(`temperature 1.4–1.45, top_p 0.98, top_k 40`).
