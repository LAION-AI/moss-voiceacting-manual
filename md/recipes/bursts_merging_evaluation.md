# Vocal bursts, merge doses & how to evaluate a LoRA

*Measured recipe page, added Aug 2026. Additive — nothing on the emotion, VoiceNet or
expressive/NSFW pages is retracted. This adds three things that had not been measured before:
how hard to merge a **vocal-burst** adapter when the burst has to land **inside** a sentence,
what happens when you **stack** a burst adapter with an emotion adapter, and what a LoRA
evaluation has to contain before its numbers mean anything.*

Mirrors of this page: [HTML](https://laion-ai.github.io/moss-voiceacting-manual/site/recipes/bursts_merging_evaluation.html)
· [Markdown](https://github.com/LAION-AI/moss-voiceacting-manual/blob/main/md/recipes/bursts_merging_evaluation.md).
The HTML is generated from the Markdown by [`tools/md2site.py`](https://github.com/LAION-AI/moss-voiceacting-manual/blob/main/tools/md2site.py),
so the two cannot drift apart.

---

## 1. Vocal-burst adapters: the merge-dose curve

**Setup.** 64 vocal-burst adapters ([`laion/vocal-burst-lora-adapters`](https://huggingface.co/laion/vocal-burst-lora-adapters)),
grouped into 8 emotion families, one autonomous agent per family. Each generation is a
**natural sentence that must contain the burst mid-utterance** — not a bare burst. 1,536
generations for the dose sweep, 768 more for the stacking sweep, 2,304 total.

`presence` = fraction of takes where a burst span was actually located in the audio.
`blend` = how naturally the non-speech event sits inside the speech (0–10).
`genu` = genuineness (0–6).

| burst LoRA dose λ | burst present | blend | genuineness | burst duration | composite |
|---|--:|--:|--:|--:|--:|
| 0.25 | 27.3 % | 5.73 | 1.48 | 0.38 s | 0.080 |
| 0.50 | 50.5 % | 4.76 | 1.89 | 0.46 s | 0.146 |
| **0.75** | **64.8 %** | **4.17** | **1.97** | 0.49 s | 0.199 |
| 1.00 | 71.4 % | 3.97 | 1.94 | 0.57 s | 0.226 |

95 % bootstrap CIs on presence: 0.25 → [0.229, 0.320]; 0.50 → [0.456, 0.555];
0.75 → [0.599, 0.695]; 1.00 → [0.669, 0.758]. n = 384 per dose. The ladder is monotone and
every step is separated.

**What this says:**

- **You buy burst presence with blend, roughly one-for-one.** Presence rises 27 % → 71 % while
  blend falls 5.73 → 3.97. There is no dose that gives you both. Decide which you are optimising
  before you pick λ.
- **λ = 0.75 is the knee.** It delivers **91 % of the presence** of full merge at a
  **noticeably better blend**, and it is where **genuineness peaks** (1.97). Full merge buys
  6.6 more points of presence for another 0.2 of blend.
- **Bursts get longer with dose** (0.38 s → 0.57 s). If you want a *brief* burst inside a line,
  low dose is not just weaker — it is shorter, which is often what you actually want.
- **λ = 0.25 is not worth using.** Three quarters of takes contain no burst at all; you are
  paying generation time for nothing.

> This contrasts with the **bare-burst** sweep in the earlier vocal-burst run, where λ = 1.0 beat
> λ = 0.5 in every class. That result was measured on isolated bursts with no carrier sentence.
> **Bursts embedded in connected speech behave differently** — there the blend cost is real,
> because there is speech for the burst to be badly glued to. Do not carry the bare-burst
> prior into sentence generation.

### Five classes never fire, at any dose

At λ = 1.0, **5 of 64** burst classes produced no located burst in any take:
`Hiss`, `Kissing Noises`, `Lip Smack`, `Person Whistling Playfully`, `Slurping Noises`.

These are all quiet, short, non-vocalic mouth sounds. Whether the model cannot make them or the
locator cannot find them is not separated by this experiment — but either way, **do not rely on
these five inside a sentence**. Generate them as isolated events if you need them.

### Per-emotion-family variation

The dose response is not uniform. Presence at λ = 0.25 → 1.00:

| family | 0.25 | 0.50 | 0.75 | 1.00 | Δ |
|---|--:|--:|--:|--:|--:|
| Fear | 0.333 | 0.729 | 0.750 | **0.896** | +0.563 |
| Sadness | 0.271 | 0.458 | 0.750 | 0.812 | +0.541 |
| Pain | 0.396 | 0.646 | **0.771** | 0.750 | +0.354 |
| Anger | 0.208 | 0.583 | 0.604 | 0.729 | +0.521 |
| Teasing | 0.146 | 0.438 | 0.688 | 0.729 | +0.583 |
| Malevolence_Malice | 0.333 | 0.396 | 0.562 | 0.688 | +0.355 |
| Fatigue_Exhaustion | 0.250 | 0.479 | 0.521 | 0.667 | +0.417 |
| **Sexual_Lust** | 0.250 | 0.312 | **0.542** | 0.438 | +0.188 |

- **Fear is the easiest family** — 90 % presence at full merge. Screams, gasps and shudders are
  loud and long, so they both generate and detect well.
- **Sexual_Lust is the exception that matters**: it *peaks at λ = 0.75* (0.542) and gets
  **worse** at 1.0 (0.438), and it has the flattest curve overall. Moans and sighs are quiet and
  slide into the speech rather than punctuating it. For this family, use 0.75 and do not push.
- **Pain also peaks at 0.75**. Two of eight families are non-monotone — enough that "more is
  more" is not a safe default.

---

## 2. Stacking a burst adapter with an emotion adapter

The obvious use is a burst inside emotional speech: `Pain` + `Painful Moan`, `Fear` + `Scream`.
768 generations across burst dose × emotion dose:

| burst λ | emotion λ | burst present | blend | genuineness | composite |
|--:|--:|--:|--:|--:|--:|
| 0.50 | 0.00 | 0.505 | 4.76 | 1.89 | 0.146 |
| 0.50 | 0.25 | 0.569 | 4.90 | 1.91 | 0.148 |
| 0.50 | 0.50 | **0.441** | 4.45 | 1.57 | 0.114 |
| 0.75 | 0.25 | 0.650 | 3.92 | 1.95 | 0.223 |
| 0.75 | 0.50 | 0.558 | 4.13 | 1.79 | 0.205 |
| 1.00 | 0.00 | 0.714 | 3.97 | 1.94 | 0.226 |
| 1.00 | 0.25 | 0.787 | 3.96 | 2.07 | 0.271 |
| **1.00** | **0.50** | **0.824** | 3.81 | 1.97 | **0.299** |

**The two adapters interact, and the sign of the interaction flips with burst dose.**

- At **burst λ ≤ 0.75**, adding emotion at 0.5 **suppresses the burst** (0.505 → 0.441 at burst
  0.5; 0.650 → 0.558 at burst 0.75). The emotion adapter is competing for the same capacity and
  the weaker burst adapter loses.
- At **burst λ = 1.0**, emotion at 0.5 **helps** (0.714 → 0.824) and produces the best cell in
  the entire 2,304-generation sweep: **composite 0.299, 82 % burst presence, genuineness 1.97**.

**Recipe — burst inside emotional speech: `burst@1.0 + emotion@0.5`.**
If you want to run the emotion adapter harder than 0.5, run the burst adapter at full merge
first, or the burst will simply stop happening. Never pair a half-merged burst adapter with a
half-merged emotion adapter — that is the worst cell in the table.

This is consistent with the emotion-manual guidance (*keep emotion λ moderate, 0.35–0.75*) and
sharpens it: **when a burst adapter is stacked underneath, the emotion adapter must sit at or
below half of the burst adapter's dose.**

---

## 3. Identity vs. dose: the ceiling on all of this

Merge dose does not only trade blend for presence — with a **reference voice** it destroys the
voice. ECAPA speaker similarity of a generation to its reference clip:

| dose λ | speaker similarity |
|---|--:|
| 0.0 (no adapter) | **0.62** |
| 0.5 | 0.57 |
| 1.0 | 0.50 |
| **1.5** | **−0.03** |

Anchors from the same encoder: a reference against **itself** = 1.000, two **different** speakers
= 0.105. So λ = 1.5 lands *below the unrelated-speaker floor* — no relationship to the reference
at all.

**Combine this with §1 and §2 and the picture is a genuine three-way trade:**

| what you care about most | dose |
|---|---|
| **reference voice identity** | λ ≤ 0.5, and accept ~50 % burst presence |
| **the burst actually happening** | λ = 1.0 (+ emotion@0.5), and accept losing the cloned voice |
| **a natural-sounding blend** | λ = 0.75, the knee for everything except Sexual_Lust/Pain, which also want 0.75 |

There is no dose that satisfies all three. If you need a specific cloned voice **and** a
reliable burst, generate more candidates at λ ≤ 0.5 and select, rather than pushing the dose.

---

## 4. Best-of-N is nearly free — use it

- **Generation time is flat from batch 16 to 32** (20.34 s → 20.54 s on a GH200): the decode
  loop is latency-bound, not throughput-bound. **32 candidates cost the same wall time as 16.**
  Batch 16 wastes half the GPU. Peak VRAM at batch 32 ≈ 23 GB.
- Going **16 → 32** is worth **+4.5 % reward** and **−9 % duration error**, measured by
  subsampling real 64-candidate groups.
- Going **32 → 64** costs **3.4×** more for the same size of increment. 32 is the sweet spot.
- For ranking at scale, transcribe with **Parakeet v3**, not CrisperWhisper: ASR was **66 %** of
  a 32-candidate group's cost with CrisperWhisper and **12 %** with Parakeet. Rank on Parakeet,
  then re-transcribe only the top 3 with the good model — that is **+182 GPU-hours** on a
  40 × 3,000-group run instead of **+1,804**.

---

## 5. How to evaluate a LoRA so the number means something

This section is the expensive lesson. A sports-commentator adapter was trained, swept over
13 rank × epoch configurations, and evaluated — and the evaluation is what saved it from being
published as a success it is not.

### 5.1 Always include a real-audio ceiling control

Judge scores on a 0–2 "does this sound like live sports commentary" scale:

| | mean |
|---|--:|
| best adapter cell | 1.969 |
| **real human broadcast commentary** | **1.775** |
| **base model, no LoRA** | **1.750** |

The base model and *real human recordings* are statistically the same. **The metric's ceiling
is ≈1.8 and the un-adapted model was already at it** — so there was nothing for the adapter to
add. Without the real-audio row, "1.97 vs 1.75, p = 0.027" reads like a win.

**Every LoRA evaluation should contain a real-recording row.** If real audio does not clearly
beat your base model on your metric, your metric cannot rank your adapters.

### 5.2 Correct for the number of comparisons

13 cells means 12 comparisons against base. Two cells clear p < 0.05 raw; the Bonferroni
threshold is **p < 0.0042** and **none survive**. Sweeping a grid and reporting the best cell's
raw p-value is how a null result gets published as a positive one.

### 5.3 An absolute rating scale saturates — use pairwise preference

Every cell landed between 1.75 and 1.97, with 75–97 % of clips at the top score. The scale was
compressed against its ceiling and could not separate configurations. **Use A/B preference
against base** when the base model is already competent at the task.

### 5.4 Validation loss does not rank checkpoints — three times running

At rank 64 the val loss went **4.4237 (epoch 1) → 5.4369 (epoch 8)**, a 0.905 regression that
looks like severe overfitting. Listeners rate **epoch 1 and epoch 8 identically (1.969 both)**.
The same disagreement appeared twice before on this stack.

**Rank checkpoints by generating audio and scoring it.** Val loss tells you the run did not
diverge; it does not tell you which checkpoint sounds better.

### 5.5 The burst classifier cannot name a burst inside a sentence

The vocal-burst *classifier* scored identity 0.00 on all 32 cells of a grid where the bursts
were plainly audible: it found no span in 33 of 64 sentences and labelled the rest
sigh/gasp/ahem, mean target probability 0.0055. **Span timing from the locator is reliable; the
class label is a weak prior** and is unusable for bursts embedded in continuous speech. Judge
embedded bursts by listening (a capable audio LLM works), not with the classifier.

### 5.6 Never divide quality by `(1 + WER)`

Confirmed independently twice now. Roughly three quarters of candidates have a **negative** core
score, and dividing a negative number by a larger denominator makes it **larger** — so the
division form *rewards* transcription errors on most of the pool. On a 1,000-clip control set a
literal `WER × quality` filter put **602 of 1,000 candidates at exactly 0** (60 % had WER 0.00)
and selected the half with *worse* WER.

Use `(sigmoid-squashed components) × (1 − min(WER, 1))`. Squashing first makes the core strictly
positive, so the gate is monotone decreasing in WER for every candidate.

---

## 6. Cross-lingual reference voices — a good source of *new* characters

20 Japanese anime reference clips ([`joujiboi/japanese-anime-speech-v2`](https://huggingface.co/datasets/joujiboi/japanese-anime-speech-v2),
verified different speakers) were used as reference audio for **German and English** generation.
**1,280 generations, all 20 references scored.**

| | speaker similarity |
|---|--:|
| reference against **itself** | 1.000 |
| **all generations** (n = 1,280) | **0.188** |
| best of 8 candidates per group | 0.294 |
| neutral, **no** emotion adapter | 0.226 |
| `Anger@0.5` | 0.250 |
| `Sadness@1.0` | 0.202 |
| `Amusement@1.5` | **0.072** |
| two **unrelated** speakers | **0.105** |

**The voice does not transfer.** At 0.188 the average generation sits barely above the
unrelated-speaker floor. English carries slightly more than German (0.217 vs 0.158, n = 640
each), and `Amusement@1.5` falls to 0.072 — *below* the floor, consistent with §3.

The average hides a wide spread: **ref00 reaches 0.622 and ref14 0.497**, while the median
reference sits near 0.16. A few source voices land in the model's range and genuinely carry;
most do not. Selecting best-of-8 on similarity lifts the mean to 0.294 — worth doing, not enough
to make it a clone.

### Pitch tracks the reference, but gets pulled toward the middle

Median F0, reference vs generation, all 20 pairs:

| | median F0 |
|---|--:|
| references | **182 Hz** (110–302) |
| generations | **157 Hz** |
| Pearson r(ref, gen) | **0.591** |
| above 200 Hz | references **7/20**, generations **1/20** |

So pitch is **correlated** with the reference — a high-pitched source does produce a
higher-pitched generation — but it is **compressed toward the model's own register**. The 250–302 Hz
anime voices come out at 149–181 Hz; the 110–125 Hz voices come out slightly *higher*. Relative
ordering survives; the extremes do not.

**Practical reading:** the generations sound bright and high *relative to the model's default*,
and they sound good, which is why they are useful. But do not expect the source's extreme
register to reproduce — if you need a genuinely very high voice, prompt for it explicitly rather
than relying on the reference to carry it.

**Recipe — mining new character voices:** take reference audio from a corpus in a *different*
language with a distinctive vocal register, generate in your target language at **dose 0** (no
emotion adapter), generate **8+ candidates**, and treat the output as a **new voice** rather than
a transfer. You get a usable, distinctive character voice that is not a copy of the source
speaker. This is a cheap way to populate a character-voice bank from any expressive corpus, and
it sidesteps the identity question entirely — you are not trying to preserve identity.

If you *are* trying to preserve identity across languages, this method does not do it. The best
single reference reached 0.622 and that was not predictable in advance.

---

## 7. Checkpoints referenced on this page

| | |
|---|---|
| Base model | [`laion/moss-tts-local-transformer-4.55b-voice-acting-v2`](https://huggingface.co/laion/moss-tts-local-transformer-4.55b-voice-acting-v2) |
| 64 vocal-burst adapters | [`laion/vocal-burst-lora-adapters`](https://huggingface.co/laion/vocal-burst-lora-adapters) |
| 40 emotion adapters (v3) | [`TTS-AGI/moss-emotion-loras-v3`](https://huggingface.co/TTS-AGI/moss-emotion-loras-v3) |
| Sports-commentator adapters | [`laion/moss-sports-commentator-lora`](https://huggingface.co/laion/moss-sports-commentator-lora) |
| DramaBox reinterpretations (top-3 of 64) | [`laion/dramabox-reinterpretations-top3`](https://huggingface.co/datasets/laion/dramabox-reinterpretations-top3) |
| DramaBox edge-case top-3 | [`laion/dramabox-edge-top3-voice`](https://huggingface.co/datasets/laion/dramabox-edge-top3-voice) |

**Listening pages:** [vocal-burst LoRAs (77 classes)](https://projects.laion.ai/laion-moss-local-1.5-voice-acting-4.55b/vocal_burst_loras.html) ·
[sports-commentator evaluation](https://projects.laion.ai/laion-moss-local-1.5-voice-acting-4.55b/sports_commentator_lora.html) ·
[Japanese→DE/EN reference transfer](https://projects.laion.ai/laion-moss-local-1.5-voice-acting-4.55b/jpref_grid.html) ·
[DramaBox reinterpretations](https://projects.laion.ai/laion-moss-local-1.5-voice-acting-4.55b/reinterpretations_25.html)

Full experimental record with code:
[`Voice-Acting-Pipeline-WIP/docs/18`](https://github.com/LAION-AI/Voice-Acting-Pipeline-WIP/blob/main/docs/18_burst_merging_sports_and_evaluation.md).
