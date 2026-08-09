# Multi-part performances: keeping one actor across parts

*Measured page, added 2026-08-05. Written because the first multi-part run got this wrong and the
result was audible: a 30-second performance that sounded like three different people spliced
together.*

Mirrors: [HTML](https://laion-ai.github.io/moss-voiceacting-manual/site/recipes/multipart_and_voice_conversion.html)
· [Markdown](https://github.com/LAION-AI/moss-voiceacting-manual/blob/main/md/recipes/multipart_and_voice_conversion.md)

---

## 1. Why you need parts at all

A ~30 s performance with a dramatic arc cannot be generated in one call:

- **The truncation wall.** The model predicts EOS early on emotionally loaded scripts. Long takes
  come back cut off. (See the burst chapter, §2.5.)
- **One take holds one emotion.** A single generation conditioned on one caption does not turn
  from composure to collapse. The turn has to happen *between* generations.

So a performance is 2–4 **parts**, each generated best-of-N, assembled afterwards.

## 2. The mistake to avoid: parts with no shared speaker

**`build_user_message` takes a `reference` argument. Use it.**

```python
proc.build_user_message(text=..., instruction=..., language="English",
                        reference=["/path/to/part0.wav"],   # <-- the anchor voice
                        tokens=...)
```

If you omit it, **every part is an independent draw of an unspecified speaker.** The model has no
reason to pick the same voice twice, and it does not. A three-part assembly is then three
different actors, and no amount of crossfading hides it.

**The rule:**

1. **Part 0 chooses the voice.** Generate it with no reference, pick the best candidate, and
   treat that clip as the *anchor* for the whole performance.
2. **Every later part is generated with the anchor as `reference`.**
3. **Measure, do not assume.** Compute ECAPA cosine similarity of each candidate against the
   anchor. Reference conditioning improves continuity; it does not guarantee it, and emotional
   parts drift more than calm ones.
4. Make speaker similarity part of the score you rank assemblies with. Otherwise the ranker will
   happily pick a beautifully acted part that is a different person.

## 3. When conditioning is not enough: Chatterbox voice conversion

If a part still lands below your similarity threshold (**~0.45** — see §7 and the
[continuation page](voice_consistency_continuation.md) §5b for why this number is much lower than
it intuitively should be), convert it to the anchor's identity instead of throwing it away.

**Tool:** [`LAION-AI/chatterbox-voice-conversion`](https://github.com/LAION-AI/chatterbox-voice-conversion),
zero-shot VC on Resemble AI's Chatterbox S3Gen. Content tokens from the source, a 192-dim CAMPPlus
x-vector from the target, flow-matching decoder, HiFi-GAN vocoder, 24 kHz out.

```python
from chatterbox_vc.convert import VoiceConverter

vc = VoiceConverter(device="cuda")          # ~1.5 GB, ~7 s to load once
out = vc.convert(source_audio="part1.wav",   # the part whose identity is wrong
                 target_voice="anchor.wav",  # 6-10 s of the voice you want
                 output_path="part1_fixed.wav")   # returns float32 @ 24 kHz
```

Measured on this cluster: model load **~7 s** on GPU (27 s cold on CPU), conversion of a 6 s clip
**~20 s on CPU**, far faster on GPU. Weights are cached at
`$HF_HUB_CACHE/models--ResembleAI--chatterbox`.

**Chain it, do not fan it out.** Convert part 1 to part 0's identity, then part 2 to the
*already-aligned* part 0+1 identity, and so on. Converting everything to a moving target
reintroduces the drift you are trying to remove.

### VC is a repair, not a default

Conversion can flatten the emotion and add artefacts. **Check both sides before keeping it:**

| check | keep the conversion only if |
|---|---|
| ECAPA similarity to the anchor | it went **up** |
| **DNSMOS `ovrl_mos`** | it did **not drop** (a tolerance of ~0.15 is reasonable) |

```python
from speechmos import dnsmos
before = dnsmos.run(orig_16k, 16000)["ovrl_mos"]
after  = dnsmos.run(conv_16k, 16000)["ovrl_mos"]
```

A measured example from this stack: a 6 s casting part scored **3.345 → 3.358** overall MOS across
conversion — i.e. no damage, so the conversion was worth keeping. Do not assume that generalises;
emotional and non-verbal material is exactly where VC is most likely to cost you.

## 4. Assembling

- **Crossfade the seam.** A hard concatenation leaves a click that the quality head reliably
  punishes, which makes every multi-part assembly look worse than it is. 25 ms equal-power is
  enough.
- **Rank whole assemblies, not parts.** Two individually excellent parts can join badly — a level
  jump, a tempo jump, or the same emotion twice where the script wanted a turn. Keep the top-K of
  each part and score every combination.
- **Score the arc explicitly.** A take that holds one emotion beautifully for 30 s is not a
  dramatic performance. Include a term for whether the dominant emotion actually changes between
  parts.

## 5. Sizing the parts

`tokens` is derived from the **word count**. For a part that is deliberately **non-verbal**
(screaming, sobbing, agony), the text has almost no words — so the model is told to produce about
five tokens and dutifully stops after ~0.3 s. This produced a 13 s "30-second" performance in the
first run.

**For non-verbal parts, set `tokens` from the intended duration** (~12.5 per second) rather than
from the word count, and raise `max_new_frames` to match.

---

## 6. Continuation beats reference conditioning

Reference conditioning (§2) keeps the *timbre* roughly right but still starts a **fresh
utterance**, with its own level, register and attack. Listeners hear that as a cut between two
recordings even when ECAPA similarity looks acceptable.

The processor supports `mode="continuation"` natively, and it is the stronger fix: the previous
audio sits in the **assistant turn** as tokens the model believes it already produced, so the new
tokens are conditioned on real acoustic context rather than a summary of it.

```python
conv = [[proc.build_user_message(text=cumulative_text, instruction=caption,
                                 language="English", tokens=n_tokens),
         proc.build_assistant_message(audio_codes_list=[prefix_codes])]]
b = proc(conv, mode="continuation")
```

Four things that are easy to get wrong, all measured:

- The assistant turn takes **codec codes `[T, n_vq=12]`, not a waveform**. Passing the waveform
  raises `audio code tensor must have shape [T, 12]`.
- `proc.encode_audios_from_wav([...], 48000)` wants a **torch tensor**, not a numpy array — it
  calls `.unsqueeze()` internally.
- `text` must carry the **cumulative** script (words already spoken *and* words still to come),
  so the model knows where in the performance it is.
- **The decode returns ONLY the continuation, never the prefix.** Measured directly: a 9.3 s
  prefix returned 5.7–12.0 s of new audio. Do **not** trim the output — blind trimming left
  0.2 s stubs, and a "1.2×" guard then mis-trimmed the long candidates.

### Chain from an anchor, not from the previous part

Feeding each part the *whole* previous part lets drift compound and drags the old mood forward.
Measured across a 9-challenge run:

| | part 1 | part 2 | part 3 |
|---|--:|--:|--:|
| speaker similarity, chained | 0.691 | 0.692 | **0.280** |

Peak emotion also fell 2.29 → 2.05 against reference-only conditioning: a long prefix is a long
argument for staying in the previous emotion.

**Use anchor + short tail instead**: the fixed part-0 anchor (identity that cannot drift) plus
~4 s of the immediately preceding part (just enough prosodic context). After this change the same
challenge measured **0.791** and **0.805** on parts 2 and 3 — the compounding is gone.

---

## 7. Speaker identity: resample, do not settle

Ranking the best of one batch is not enough. If a whole batch drifts, the least-bad take still
ships, and the listener hears a second actor mid-scene. Three thresholds, applied in order:

| threshold | default | action |
|---|--:|---|
| `spk_target` | 0.82 | if no candidate reaches it, **generate the part again** with fresh seeds and merge the pools (up to 2 retries) |
| `vc_threshold` | 0.75 | attempt voice conversion as a repair |
| `spk_floor` | 0.68 | take is scored ×0.25 — effectively unusable however good the acting |

Then, when ranking whole assemblies, score speaker similarity as **half mean, half minimum**:

```python
spk = 0.5 * np.mean(sims) + 0.5 * min(sims)
```

A plain mean let assemblies containing a 0.28 part win on their other three parts. A listener does
not average identity across a take.

Measured over 9 challenges × 3 rounds (56 continuation parts):

| continuation parts | before | after |
|---|--:|--:|
| mean | 0.662 | **0.784** |
| below 0.75 | 54 % | **17 %** |
| part 1 → 2 → 3 | 0.691 → 0.692 → **0.280** | 0.777 → 0.787 → **0.835** |

### Do not apply this gate to non-verbal parts

Splitting the same run by challenge type:

| | n | mean | below 0.55 |
|---|--:|--:|--:|
| spoken scenes | 44 | **0.816** | **0 %** |
| screams / non-verbal agony | 8 | 0.610 | 38 % |

**Every failure left in the run is a non-verbal part.** ECAPA needs voiced, sustained material; a
1–3 s scream gives it almost none, so a low similarity there partly measures the absence of
anything to embed rather than a change of speaker. Gating screams at 0.82 burns resamples on parts
the threshold cannot fix. Watch also for batches where every candidate decodes to empty audio —
continuing from an empty part poisons the next one (0.367 similarity downstream of one).

### Prompt for it as well as measure it

Two textual levers, both cheap:

- **Append an explicit continuity sentence to `GENERAL`** on every continuation part: *"The same
  speaker from the preceding audio continues without interruption: identical voice, identical
  person, same microphone and same room — no cut, no new narrator, no change of casting."*
- **Keep the `GENERAL` voice description byte-identical across parts.** Describe the person once
  and repeat that description verbatim; vary only the delivery cue and the emotional state. A
  `GENERAL` that re-describes the voice differently is an invitation to cast a different voice.

---

## 8. Prosody discipline: tempo, chunking, disfluency

The failure a listener described as the actor *"getting carried away — too much into it"*: the
pace runs away inorganically, and phrasing changes between parts for no reason. It was never
measured, so nothing selected against it. Fear scenes were the worst offenders, because "terrified"
gets written as "fast".

Three VoiceNet heads cover exactly these axes, plus one arithmetic cross-check:

| signal | source | what it means |
|---|---|---|
| `TEMP` | VoiceNet, 0–6 | tempo: 3 ordinary conversation, 4 brisk, 5 compressed/urgent, 6 auctioneer |
| `CHNK` | VoiceNet, 0–6 | chunking: 0 shattered syllables, 2 short cautious groups, 3 sentence-length breath units, 6 unbroken wall |
| `DFLU` | VoiceNet, 0–6 | disfluency: fillers, restarts, stammers |
| words/sec | ASR hypothesis ÷ duration | independent check; **above ~4.0 w/s is a runaway** |

Use the continuous `reg` value, not the bucket — parts are compared to each other and you need
sub-bucket resolution.

### A rule that says "smooth unless declared" will make everything uniform

This is a mistake worth inheriting rather than repeating. The seam rule below was written as
*"prosody must either flow smoothly OR change for a stated reason"* — which sounds balanced. In
practice the planner rarely declared a change, so the rule reduced to **"stay uniform"**, and it
actively punished the variation that makes acting sound like acting.

The measurable consequence, between two runs: the spread of speaking rate across the parts of a
performance **fell 19 %** (sd 0.90 → 0.73) while the mean rose. A listener described the result
without seeing any numbers: *"too little variance in the style how they are talking."*

**Fix it in two places at once:**

- **Loosen the penalty.** Only mark down a genuine *lurch* (more than ~2.5 scale points between
  neighbouring parts). Ordinary movement should be free.
- **Add a positive reward for spread.** Score `max − min` of tempo, chunking and disfluency across
  the performance, targeting roughly one full scale point of movement. Variation must *earn*
  points, not merely avoid losing them.

A caution from doing exactly this: set the target high enough to bite. Our first attempt targeted
so little movement that the term sat at 0.975 — already satisfied by the flatness it was meant to
fix, and therefore pulling for nothing.

### Naturalness: reward the imperfections, and make the speed penalty two-sided

Nothing in the original scoring wanted a filler word, a restart or an audible breath, so none
appeared. Shipped parts averaged disfluency **2.31** where VoiceNet level 3 is defined as *"a
standard, entirely natural amount of fillers … the exact baseline of unscripted, everyday human
processing noise"*, and **32 %** sat below 2.0 — audibly cleaner than a real person. The listener
report was *"not with the imperfections that a real person would have"*.

Add an explicit naturalness term:

| component | target | notes |
|---|---|---|
| disfluency | full credit in **2.5–4.0** | below 1.8 reads as robotic; above 4.0 is a mess |
| words per second | full credit in **2.4–3.3** | penalise **both** sides |

**The two-sided band is the part to get right.** Our first version penalised only fast delivery
and gave arbitrarily slow speech full credit — which tripled the share of unnaturally slow parts
(3 % → 11 % below 2 words/second) in a single run. Both a listener and a model A/B comparison then
preferred the *faster* take. Dragging is a failure mode in its own right, not the safe direction.

### The governing rule

> Prosody must **either flow smoothly** from part to part, **or change for a stated reason**.

So the plan declares `tempo_target`, `chunk_target` and a boolean `prosody_turn` per part, and
both halves are scored:

- **Undeclared seam** — consecutive parts must stay within ~1 point; the penalty ramps beyond that.
- **Declared turn** — a change is now *required*: a declared turn that does not actually move
  scores ≤ 0.6, and a lurch beyond ~3 points is penalised too. A move, not a jump.
- **Runaway** is multiplicative, not a term (`× (1 − 0.35·runaway)`): a take that sprints is
  spoiled, not merely lower-scoring, and must not buy the loss back with genuineness.

### The tempo dial saturates — a bigger number does not buy more tempo

Measured over 77 parts with a declared `tempo_target`:

| asked | measured | n |
|--:|--:|--:|
| 1 | 2.97 | 3 |
| 2 | **2.07** | 26 |
| 3 | **2.84** | 36 |
| 4 | 2.82 | 12 |

Overall bias is only **−0.16** with mean absolute error **0.75**, so the plans are being followed.
But the model's usable range is roughly **2–3 measured**: asking for 4 lands at 2.8, asking for 1
lands at 3.0. **The extremes compress toward the middle.**

Two consequences:

- A `pros_fit` around 0.58 is *arithmetic*, not disobedience — mean error 0.75 against the ±2
  tolerance gives ≈0.63. Do not tune the planner to fix it; it is measuring model range.
- **To get real urgency, reach for a different lever** — the delivery cue, the emotion adapter, or
  chunking — not a larger integer. Which is the chunking finding below, arrived at from a second
  direction.

### Chunking is the dial for fear, not tempo

The single most useful correction. Real distress is more often held breath, short groups and
stalling than it is a sprint. **`chunk_target` 1–2 with `tempo_target` 3 reads as genuine fear;
`tempo_target` 5 reads as a caffeinated narrator.** Reserve 5 for a genuine loss of control, and
treat 6 as always wrong unless the brief is panic or auctioneering.

Plan prosody as a *shape* across the whole performance, e.g. tempo 3 → 2 → 4 with chunk 3 → 1 → 2,
declaring `prosody_turn` on the middle part (the character stalls) and the last (they break) —
and state the reason in the delivery cue so the writing and the numbers agree.

---

## 8b. Do not let the run quietly stop exploring

Two defects that a listener reports as *"the takes all sound the same"*, and that no metric flags,
because nothing is wrong with any individual take.

**Seed the task, not just the round and part.** A seed like
`7000 + 100*rnd + 10*pi` gives every challenge in a fleet the *same* seed for the same slot. That
does not produce the same voice (measured: mean ECAPA 0.344 between tasks), but it correlates the
sampling streams, so the same burst opens the same part across unrelated conditions and
best-of-N explores less than it appears to.

```python
sd = (zlib.crc32(task.encode()) % 100000) * 1000 + 7000 + 100*rnd + 10*pi + 3331*att
```

Give sub-batches a well-separated offset too — `seed + 7919*batch_index`, not `seed + i`.

**Select the top-K for spread, not for rank.** The K highest-scoring assemblies over a
combinatorial space are near-duplicates by construction: neighbouring combinations differ in one
part index, so three "different" takes share two thirds of the same audio files. Measured over 27
rounds, ranks 1-2-3 differed in a mean of **1.15** of 3 part slots. Greedy max-marginal-relevance
— best score minus an overlap penalty — raises that to **1.79** using takes that were already
rendered.

This generalises well past TTS: **any best-of-N ranker that hands a human "the top K" from a
combinatorial space should select them for diversity.**

## 8c. How to not fool yourself when measuring any of this

Four failures from building the above. Every one produced output that looked completely valid,
which is why they are worth naming.

**1. Optimising a proxy gives you the proxy, not the goal.** The identity threshold was raised
because stricter identity was wanted. It delivered exactly that number — and cost expressiveness,
because the metric mildly prefers flat delivery. Before tightening any filter, ask what *else*
that metric rewards.

**2. A cache keyed on a filename that does not encode its contents is a trap.** An A/B audio
builder skipped rewriting a file if one already existed. When the pair *selection* changed, the
audio did not, and every index silently pointed at the wrong clip. A model then judged the old
pairs while the results were labelled with the new metadata. **The analysis was coherent, and
every number in it was wrong — including two that reversed on rerun.** Either rewrite always, or
name files by a hash of their content.

**3. A ranking that can degrade to the identity permutation should be asserted against.** A
skipped scoring step left every candidate tied; the stable sort preserved input order, and "top 3
of 64" became "the first 3". Three items flagged, ranks filled 0…63, schema valid. A real ranking
is a permutation — check that it is one.

**4. `df.<name>` where the name is also a DataFrame method.** `d.rank != 0` compares the *bound
method* to 0, yielding the scalar `True`, and `d[True]` raises `KeyError: True`. This has now cost
time four separate times with `.take`, `.diff`, `.tail` and `.rank`. **Index columns with brackets
in analysis code.**

And one about evidence: when a model-judged result and a human listener disagree, **the listener
is the ground truth**, but check the plumbing before believing either — twice today a striking
result turned out to be a mislabelled join rather than a finding.

## 9. Checklist

- [ ] Part 0 generated with **no** reference; best candidate saved as the anchor
- [ ] Parts 1..n generated as **continuations** from **anchor + ~4 s tail**, not chained from the full previous part
- [ ] Continuation `text` carries the **cumulative** script; output **not** trimmed
- [ ] Explicit "same speaker continues" sentence appended to `GENERAL`; voice description identical across parts
- [ ] ECAPA similarity measured against the anchor for every candidate
- [ ] Part **regenerated** if no candidate reaches `spk_target` (**0.58**, not 0.82)
- [ ] VC applied only below **0.45**, kept only if similarity ↑ **and** DNSMOS not ↓
- [ ] Takes below `spk_floor` (**0.40**, not 0.68) rejected before ranking
- [ ] Identity **ranked** with meaningful weight (~0.19) but **never gated at a high threshold**
- [ ] `tempo_target` / `chunk_target` declared per part; `prosody_turn` set only where the change is intended
- [ ] Seams penalised only for a **lurch** (>2.5 points); variation **rewarded** separately
- [ ] Naturalness scored: disfluency in **2.5–4.0**, words/sec in **2.4–3.3** (penalise BOTH sides)
- [ ] Non-verbal parts sized by duration, not word count
- [ ] Seams crossfaded and **level-matched** to part 0
- [ ] Assemblies ranked as wholes, with speaker similarity (mean **and min**), arc and prosody in the score
