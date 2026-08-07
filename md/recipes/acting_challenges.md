# Acting challenges: running an autonomous casting agent

Everything measured across seven generations of the casting harness (9 challenges × 3 rounds each,
~2,000 generations). Read this before writing an acting plan — most of it was learned the
expensive way, and several items are things a listener caught that no metric was watching.

The shape of the task: a ~30 s performance with a dramatic arc, written as **2–4 parts**, each
generated **best-of-16**, assembled as the best *combination* across parts, ranked by the local
sensor stack only. A supervisor listens afterwards and gives feedback for the next round.

> **This page is the summary. The full record is the [acting-challenge tree](acting/index.html).**
> Everything below is true and is the fastest way in; the tree has the per-challenge recipes with
> verbatim captions, the cross-version numbers, the scoring formulas each generation actually used,
> and the failures in full.

| page | what is in it |
|---|---|
| [Map & headline findings](acting/index.html) | what was run, in what order, and the five findings that are not on this page |
| [**Per challenge**](acting/per_challenge.html) | for each of the nine briefs: every round ever run, the recipe worth re-running, its full verbatim caption / adapters / doses / sampling, and why it won |
| [Version history](acting/versions.html) | generation by generation, with the cross-version tables |
| [What worked](acting/what_worked.html) · [partly worked](acting/what_partly_worked.html) · [failed](acting/what_failed.html) | the measurement behind each claim, and the boundary where it stops paying |
| [Metrics](acting/metrics.html) | the exact formulas, the thresholds, and the three scoring terms that carry no information |
| [Every prompt](acting/prompts.html) | all 351 part-captions, verbatim |
| [Edge-case swarm](acting/swarm_edgecases.html) | `T0001`–`T0008`: the recipes, and why half the reports should be read sceptically |

Three corrections the tree makes to this page: the "seven generations" are **four** complete runs
plus three aborted launches; **`out_v5_real`'s results are not paired with its plans** and must not
be used; and the **supervisor rankings from v1/v2/v5 measure presentation order**, not quality — the
listener picked the 4th or 5th take presented in 71 of 81 rounds.

---

## 0. The one-page checklist

- [ ] Part 0 with **no** reference; its best take becomes the **anchor**
- [ ] Later parts as **continuations** from **anchor + ~4 s tail** (§1)
- [ ] `GENERAL` voice description **byte-identical** across parts (§2)
- [ ] Seeds unique **per task**, and several sub-batches per part (§3)
- [ ] Every part **starts and ends on a word** — bursts go inside the line (§4)
- [ ] Cues written as **actions**, not tone descriptions (§5)
- [ ] `tempo_target` / `chunk_target` declared; `prosody_turn` only where intended (§6)
- [ ] Non-verbal parts sized by **duration**, not word count; not gated on speaker similarity (§7)
- [ ] Seams **level-matched** and crossfaded; assemblies ranked whole (§8)

---

## 1. Continuation, from an anchor

Reference conditioning keeps timbre roughly right but starts a *fresh utterance* with its own
level and attack — heard as a cut. `mode="continuation"` puts the previous audio in the
**assistant turn**, so new tokens continue real acoustic context.

Chaining from the *whole* previous part is worse than it sounds: drift compounds and the long
prefix drags the old mood forward.

| | part 1 | part 2 | part 3 |
|---|--:|--:|--:|
| chained from full previous part | 0.691 | 0.692 | **0.280** |
| **anchor + 4 s tail** | 0.777 | 0.787 | **0.835** |

Mechanics that each cost a debugging cycle: the assistant turn takes **codec codes `[T, 12]`**,
not a waveform; `encode_audios_from_wav` wants a **torch tensor**; `text` must be **cumulative**;
and the decode returns **only the continuation** — do not trim it.

## 2. Identity must be enforced, not ranked

Ranking the best of one batch is not enough: if a whole batch drifts, the least-bad take still
ships, which is how a listener ends up hearing a second actor mid-scene.

| control | value | action |
|---|--:|---|
| `spk_target` | 0.82 | **regenerate the part** with fresh seeds, merge pools |
| `vc_threshold` | 0.75 | attempt voice conversion as a repair |
| `spk_floor` | 0.68 | reject the take outright |
| assembly term | — | **½ mean + ½ worst part** |

Test the take that would actually be **kept**, not the best similarity available in the batch —
testing the maximum meant a batch containing one good take never resampled even when ranking then
chose a different one 0.3 lower.

Free textual levers: append an explicit *"the same speaker continues without interruption… no cut,
no new narrator"* sentence to `GENERAL` on every continuation part, and **keep the voice
description identical word-for-word** across parts. Re-describing the voice invites a new one.

**Result:** mean 0.662 → **0.784**; below 0.75 54 % → **17 %**. On spoken scenes alone,
**0.816 mean and 0 % below 0.55**.

## 3. Seeds must vary per task and per sub-batch

A listener noticed that *the same vocal burst opened the same part in unrelated challenges*. The
cause was arithmetic:

```python
seed = 7000 + 100 * rnd + 10 * pi + 3331 * att      # <-- no task term
```

Every one of nine challenges drew **seed 7110** for round 1 part 1. And with `cands == batch`
there was only ever one chunk, so `torch.manual_seed(seed + i)` set **one** RNG stream per part.

```python
seed = (zlib.crc32(task.encode()) % 100000) * 1000 + 7000 + 100*rnd + 10*pi + 3331*att
torch.manual_seed(seed + 7919 * (i // batch))       # several sub-batches per part
```

Correlated seeds do not just repeat artefacts across conditions — they make **best-of-16 explore
one neighbourhood**, so the selection is far weaker than the candidate count suggests. Keep
`batch < cands` so a part is drawn from several independent streams.

## 4. Never open or close a part with a vocal burst

A gasp, throat noise or sigh in the **first or last ~0.45 s** lands exactly **on the join** once
parts are concatenated, and reads as a glitch rather than as acting. Two defences:

- **Write it out.** Every part starts on a word and ends on a word; bursts go *inside* the line.
  The continuation caption also states this explicitly.
- **Measure it.** Count burst-locator spans overlapping the first/last 0.45 s and penalise them
  (`× (1 − 0.15·edge_bursts)` per candidate). Bursts inside the line are untouched — there a burst
  is usually the point.

### Weight the blend score, or you select against blending

Burst **blending** (0–10: does the burst grow out of the speech or sit on top of it) had weight
**0.00** in candidate ranking and 0.08 in the assembly score, while genuineness — which correlates
**−0.21** with blending — carried 0.34. The ranker was therefore mildly selecting *against* clean
blending, and **24 % of shipped assemblies scored below 3/10**. Blending is now 0.11 per candidate
and 0.12 in the assembly.

## 5. The narration failure — and how to write around it

The most common continuation failure is subtle: the voice stays correct but the model **stops
acting and reads the remaining words out**. It is measurable — VoiceNet's style heads give a
narration index:

```
narration = ½(S_NARR + S_NEWS) − ½(S_DRAM + S_CONV)      # positive = reading it out
```

The writing lever that matters: **make the cue an action the character performs, not a description
of a tone.** "The sentence collapses halfway and they have to start it again" is a direction;
"sad, resigned" is a label, and a label is an invitation to narrate.

## 6. Prosody: smooth, or changed for a stated reason

> Chunking, disfluency and tempo must **either flow smoothly** from part to part, **or change for
> a declared reason.**

Declare `tempo_target`, `chunk_target` and `prosody_turn` per part. Undeclared seams stay within
~1 point; a declared turn must actually move (1–3 points), not lurch. `runaway` (word rate above
~4.0/s, or an undeclared very high tempo) multiplies the score down rather than subtracting.

**The tempo dial saturates.** Measured over 77 parts:

| asked | 1 | 2 | 3 | 4 |
|---|--:|--:|--:|--:|
| measured | 2.97 | **2.07** | **2.84** | 2.82 |

Bias −0.16, mean absolute error 0.75 — plans *are* followed, but the usable range is ~2–3. Asking
for 4 buys nothing. Get urgency from the cue, the emotion adapter or the chunking.

**Chunking is the dial for fear, not tempo.** Real distress is held breath and short broken groups.
`chunk_target` 1–2 at ordinary tempo reads as genuine fear; `tempo_target` 5 reads as a caffeinated
narrator.

**Result:** seam jumps over 2 points 30 % → **12 %**; runaway 0.115 → **0.063**; words/sec over the
ceiling 47 % → **23 %**.

## 7. Non-verbal parts are a different regime

- **Size by duration, not word count.** `tokens` defaults to the word count, and a scream's text
  ("Aaaahh-! Kh-kh-!") has almost none — the model makes ~5 tokens and stops after 0.3 s. Use
  ~12.5 tokens per intended second.
- **Do not gate them on speaker similarity.** ECAPA needs voiced sustained material; a 1–3 s
  scream gives it almost none. Splitting the same run: spoken scenes **0.816 mean, 0 % below
  0.55**; non-verbal **0.610, 38 % below 0.55**. *Every* remaining identity failure is a scream.
  A 0.82 gate there burns resamples on something it cannot fix.
- **Watch for empty batches.** Non-verbal parts sometimes return 16 candidates that all decode to
  empty audio; continuing from an empty part poisons the next one (0.367 similarity downstream).
  Detect and regenerate rather than continuing.

## 8. Assembly hygiene

- **Level-match every part to part 0** over the loudest ~60 % of frames, then one gentle peak
  normalisation of the whole take.
- **25 ms equal-power crossfade** at each seam.
- **Rank whole assemblies**, not parts — keep top-K per part, score every combination.
- **Measure the arc continuously.** The original arc term counted whether the argmax EmoNet label
  changed; it saturated at **0.977 with 86 % of assemblies at exactly 1.0** while a listener heard
  no arc at all. Use cosine movement of the EmoNet profile plus peak swing.

## 9. Harness failures that each cost a run

- **Stale handshake files.** An interrupted archive left nine `STOP` files; every worker exited
  "after 0 rounds" while the drivers consumed the *previous* run's results — a whole "new" run that
  was old audio with new plans attached, reporting 27/27 complete. Clear `STOP` and
  `round_*.req/res.json` at worker startup.
- **A missing API key looks exactly like a bad model.** With the key unset every planner call
  returns `None` and the driver logs "unparsable plan" three times and gives up. Fail loudly at
  startup instead.
- **Launch from a script, with `setsid`.** Interrupted inline launches leave half-started runs that
  look fine from the outside.
- **A diagnostic must not be able to kill the run it diagnoses.** `min()` over an empty list in a
  log line took down a worker mid-run.

## 10. What is still open

- **Rounds do not reliably improve.** Only 4 of 9 challenges peaked in their final round, and two
  got monotonically worse. The gains so far come from mechanical fixes, not from the feedback loop.
- **Agent and listener disagree about ranking**, ρ from −0.53 to +0.90. The local sensor stack is
  not yet a reliable proxy for a listener's ordering of five near-equal takes.
- **`pros_fit` ≈ 0.62** is mostly model range, not disobedience (§6) — do not tune the planner
  against it.
