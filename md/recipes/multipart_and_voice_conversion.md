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

If a part still lands below your similarity threshold (~0.55 works), convert it to the anchor's
identity instead of throwing it away.

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

## 6. Checklist

- [ ] Part 0 generated with **no** reference; best candidate saved as the anchor
- [ ] Parts 1..n generated with `reference=[anchor]`
- [ ] ECAPA similarity measured against the anchor for every candidate
- [ ] VC applied only below threshold, kept only if similarity ↑ **and** DNSMOS not ↓
- [ ] Non-verbal parts sized by duration, not word count
- [ ] Seams crossfaded
- [ ] Assemblies ranked as wholes, with speaker similarity and arc in the score
