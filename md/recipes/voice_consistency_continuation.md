# Keeping one voice across clips while the emotion changes

**The problem this page solves.** You have a character. You need several clips of them — calm,
then frightened, then relieved — and they must sound like **the same person** throughout, matching
a reference recording you already have. Generate the clips independently and they will not: the
timbre wanders, the level and register jump, and a listener hears a cut between two recordings, or
two different actors.

This page is self-contained. It assumes only that you are driving
`laion/moss-tts-local-transformer-4.55b-voice-acting-v2` through its `AutoProcessor`, and nothing
about how it was worked out. Everything here is measured over ~2,000 generations; the underlying
experiments are in the [acting-challenge tree](acting/index.html) if you want the workings.

---

## 0. The short version

1. **Fix one anchor clip.** Either your reference recording, or generate clip 1 and keep the best
   take. Every later clip is measured against this one, never against its predecessor.
2. **Generate later clips in `mode="continuation"`**, with the assistant turn holding the
   **anchor + ~4 s of the previous clip** — not the whole previous clip.
3. **Keep the `GENERAL` voice description byte-identical** across clips. Change only the delivery
   cue and the emotional state.
4. **Append a continuity sentence** to `GENERAL` on every continuation clip.
5. **Measure ECAPA cosine similarity** against the anchor and *enforce* it: regenerate below 0.82,
   repair with voice conversion below 0.75, reject below 0.68.
6. **Do not apply step 5 to non-verbal clips** (screams, sobs, gasps). The metric stops working
   there.

Measured effect of doing this versus reference conditioning alone, over 9 scenes × 3 rounds:
mean similarity on later clips **0.662 → 0.799**, share below 0.75 **54 % → 22 %**, and — the part
that matters most — **share below 0.55 fell to 0 %**. Identity no longer collapses.

---

## 1. Why plain reference conditioning is not enough

`build_user_message(..., reference=[path])` conditions on your reference and gets the *timbre*
roughly right. But it still starts a **fresh utterance**: its own onset, its own level, its own
register. That is what a listener hears as a splice, and it happens at similarity values that look
perfectly acceptable on paper.

`mode="continuation"` is the stronger tool. It places real audio in the **assistant turn**, so the
model treats it as tokens it already produced and predicts what comes next — inheriting level,
register and speaking manner, not just timbre.

```python
conv = [[
    proc.build_user_message(text=cumulative_text, instruction=caption,
                            language="English", tokens=n_tokens),
    proc.build_assistant_message(audio_codes_list=[prefix_codes]),
]]
batch = proc(conv, mode="continuation")
out = model.generate(input_ids=batch["input_ids"].cuda(),
                     attention_mask=batch["attention_mask"].cuda(),
                     max_new_frames=400, do_sample=True,
                     audio_temperature=1.0, audio_top_p=0.95, audio_top_k=30)
```

### Four mechanics that each cost a debugging cycle

| | |
|---|---|
| the assistant turn takes **codec codes `[T, n_vq=12]`** | passing a waveform raises `audio code tensor must have shape [T, 12]` |
| `proc.encode_audios_from_wav([x], 48000)` wants a **torch tensor** | a numpy array fails on `.unsqueeze()` |
| `text` must be **cumulative** | the words already spoken *and* the words still to come, so the model knows where in the script it is |
| the decode returns **only the continuation** | measured: a 9.3 s prefix returned 5.7–12.0 s of *new* audio. **Do not trim the output.** Blind trimming left 0.2 s stubs; a "1.2× prefix length" guard then mis-trimmed exactly the good long takes |

In continuation mode the `reference=` slot is ignored — the prompt audio *is* the conditioning.

## 2. Anchor + tail — do not chain

The obvious thing is to feed each clip the whole previous clip. It is measurably wrong, for two
separate reasons:

| | clip 2 | clip 3 | clip 4 |
|---|--:|--:|--:|
| chained from the full previous clip | 0.691 | 0.692 | **0.280** |
| **anchor + 4 s tail** | 0.777 | 0.787 | **0.835** |

- **Drift compounds.** Each clip inherits the previous one's error as well as its voice, so a small
  wander becomes a different person by clip 4.
- **A long prefix drags the old emotion forward.** Peak emotion fell **2.29 → 2.05** under full
  chaining — exactly the opposite of what you want when the point is that the emotion *changes*.

So build the prefix from two pieces:

```python
tail = prev_clip[-int(4.0 * SR):]              # ~4 s of prosodic context
prefix = np.concatenate([anchor_wav, tail])    # identity that cannot drift, + context
```

The anchor supplies an identity that never degrades; the short tail supplies just enough recent
context to continue the delivery. **Always measure against the anchor**, never against the
previous clip — otherwise the reference drifts with the audio.

## 3. Getting the emotion to actually change

Continuation resists mood change: you are asking the model to continue an utterance *and* turn it.
Three levers, in order of effect.

**Write the cue as a CHANGE, not a state.** The single most effective textual lever.
"The composure finally breaks and it collapses into sobbing" works; "sad" does not. Name what the
delivery stops being as well as what it becomes.

**Write the cue as an ACTION, not a tone label.** The most common continuation failure is that the
voice stays right but the model stops acting and simply **reads the remaining words out**. A tone
label ("resigned, quiet") is an invitation to narrate; a physical direction ("the sentence
collapses halfway and they have to start it again") is not. This is measurable with the VoiceNet
style heads:

```
narration_index = ½(S_NARR + S_NEWS) − ½(S_DRAM + S_CONV)     # positive = reading it out
```

**Raise the emotion adapter on the clip that carries the turn.** The usable band is **0.35–0.75**;
above ~1.0 genuineness and intelligibility collapse. A clip that has to swing hard sits near the
top of the band; an opening clip can sit lower.

State the emotion the clip moves *out of* as well as into. A caption that says "moves out of
guarded composure and into open grief" outperforms one that only names the destination.

## 4. Prompting for identity — two free levers

**Append a continuity sentence to `GENERAL`** on every continuation clip:

> *"The same speaker from the preceding audio continues without interruption: identical voice,
> identical person, same microphone and same room — no cut, no new narrator, no change of
> casting."*

**Keep the `GENERAL` voice description byte-identical across clips.** Describe the person once and
repeat that description verbatim; vary only the delivery cue and the emotional state. A `GENERAL`
that re-describes the voice in different words is an invitation to cast a different voice.

Both cost nothing and both measurably help.

## 5. Enforce identity — do not merely rank it

Generating N candidates and keeping the best of one batch is not enough: **if the whole batch
drifts, the least-bad take still ships.** That is precisely how a second actor appears mid-scene.

| threshold | value | action |
|---|--:|---|
| `spk_target` | **0.82** | no candidate reaches it → **generate the clip again** with fresh seeds and merge the candidate pools |
| `vc_threshold` | **0.75** | attempt voice conversion to the anchor as a repair |
| `spk_floor` | **0.68** | reject the take outright — exclude it from ranking entirely |

Two details that turned out to matter:

- **Test the take that would actually be kept**, not the best similarity available in the batch.
  Testing the maximum meant a batch containing one good take never resampled, even when ranking
  then selected a different take 0.3 lower on other criteria.
- **A penalty is not a floor.** Multiplying a sub-floor take's score by 0.25 still let an
  excellent-sounding take from below the floor win. Exclude them.

When scoring a whole multi-clip sequence, use **½ mean + ½ minimum** similarity. A plain mean lets
a sequence containing one 0.28 clip win on the strength of the others; a listener does not average
identity across a performance.

### Voice conversion is a repair, not a default

Chatterbox VC to the anchor can flatten emotion and add artefacts, so run it only below threshold
and **keep it only if similarity rose *and* DNSMOS did not fall by more than 0.15**.

```python
conv = voice_converter().convert(src_path, anchor_path)   # float32 @ 24 kHz
keep = (sim_after > sim_before) and (dnsmos_after >= dnsmos_before - 0.15)
```

## 6. Seeds — a trap worth knowing about

If you generate N candidates per clip, make sure they are genuinely N draws:

```python
seed = (zlib.crc32(character_id.encode()) % 100000) * 1000 + base + 100*round + 10*clip
torch.manual_seed(seed + 7919 * (i // batch))     # several sub-batches per clip
```

Two failure modes, both observed:

- **A seed formula with no per-character/per-scene term** makes unrelated generations produce the
  *same artefact in the same place* — a listener spotted an identical vocal burst opening the same
  clip position across nine unrelated scenes before any metric did.
- **`candidates == batch_size`** means a single RNG stream per clip, so "best of 16" explores one
  neighbourhood and your selection is far weaker than the candidate count suggests. Keep
  `batch < candidates`.

## 7. Joining the clips

- **Level-match every clip to the anchor** over the loudest ~60 % of frames (a speech-active RMS),
  then normalise the whole join once. Independent generations vary audibly in loudness and a
  listener hears that as a badly cut scene.
- **25 ms equal-power crossfade** at each seam; a hard concatenation leaves a click.
- **Never let a clip open or close on a vocal burst.** A gasp or throat noise in the first or last
  ~0.45 s lands exactly *on* the join and reads as a glitch. Write each clip to start and end on a
  word; put bursts inside the line.
- **Watch burst loudness.** A burst more than ~6 dB above the speaker's own active level reads as a
  splice rather than as acting — unless the clip is *meant* to be a scream.

## 8. The non-verbal exception

Everything in §5 stops working on screams, sobs and non-verbal agony. Measured, splitting the same
run by clip type:

| | n | mean similarity | below 0.55 |
|---|--:|--:|--:|
| spoken clips | 44 | **0.816** | **0 %** |
| non-verbal clips | 8 | 0.610 | 38 % |

**Every** identity failure left in the corpus is a non-verbal clip. ECAPA needs voiced, sustained
material; a 1–3 s scream gives it almost none, so a low number there is substantially measuring
*the absence of anything to embed* rather than a change of speaker. Gating screams at 0.82 burns
regenerations on something the threshold cannot fix.

Two more non-verbal traps:

- **Size them by duration, not word count.** `tokens` defaults to the word count and a scream's
  text ("Aaaahh—! Kh—kh—!") has almost none, so the model produces ~5 tokens and stops after
  0.3 s. Use **~12.5 tokens per intended second** and raise `max_new_frames` to match.
- **Whole batches sometimes decode to empty audio.** Continuing from an empty clip poisons the next
  one (0.367 similarity downstream of one). Detect an empty batch and regenerate rather than
  continuing from it.

## 9. Checklist

- [ ] One **anchor** fixed up front; all similarity measured against it, never against the previous clip
- [ ] Later clips generated with `mode="continuation"`, prefix = **anchor + ~4 s tail**
- [ ] `text` **cumulative**; decode **not** trimmed; prefix passed as **codec codes** from a **torch tensor**
- [ ] `GENERAL` voice description **byte-identical** across clips
- [ ] Continuity sentence appended to every continuation caption
- [ ] Cues written as **changes** and as **actions**, never as tone labels
- [ ] Emotion adapter **0.35–0.75**, nearer the top on the clip that carries the turn
- [ ] Similarity **enforced**: regenerate < 0.82, VC < 0.75, reject < 0.68; sequence scored ½ mean + ½ min
- [ ] VC kept only if similarity ↑ **and** DNSMOS not ↓ by > 0.15
- [ ] Seeds vary per character/scene **and** per sub-batch; `batch < candidates`
- [ ] Clips start and end **on a word**; bursts inside the line, not louder than ~6 dB over speech
- [ ] Seams **level-matched** to the anchor and crossfaded
- [ ] Non-verbal clips: sized by duration, **not** gated on speaker similarity, empty batches retried
