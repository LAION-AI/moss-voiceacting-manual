# Contentment — conditioning guide

*Target metric:* EmoNet **Contentment** strength (0–1). *Reward* = (genu + blend + 1.25·emo) / (1+WER).

**TL;DR.** Best reward comes with the LoRA at 50% (0.566, beating plain BASE 0.511), and importantly the evolved prompt alone underperforms neutral BASE (0.470 < 0.511), so use evolved-prompt + 50% merge and don't run the steering prompt without the LoRA. LoRA50 roughly triples target emotion (0.069) and cuts WER to 0.167, but blend drops (0.453 to 0.402) and quality falls (0.625 to 0.543). The dominant side-effect is a sleepy, relaxed tone — it suppresses Concentration sharply (-0.48) and raises Fatigue, Emotional Numbness and Relief, so contentment reads as drowsy calm; keep the merge at 50% since 100/150% only add WER without more reward.

## Without a LoRA (base model only)
Best: **neutral prompt, no LoRA** → reward **0.51** (emotion 0.02, WER 0.27).

```
GENERAL: A voice utterly expressing contentment, a relaxed, satisfied voice, at peace and content, easy and unhurried, in every breath.
SCRIPT:
(calmly content and at ease) "<your neutral sentence>"
```
(sampling: temperature 1.0, top_p 0.9, top_k 40)

## With the emotion LoRA
LoRA: `Contentment` (TTS-AGI/moss-emotion-loras-v3). Best merge: **50%** → reward **0.57** (emotion 0.07).
Dose: 50% → reward 0.57 (emo 0.07) · 100% → 0.42 (emo 0.04) · 150% → 0.43 (emo 0.03).

## Conditions
| condition | reward | emotion | genu | blend | quality | WER |
|---|---|---|---|---|---|---|
| neutral prompt, no LoRA | 0.51±0.27 | 0.02 | 0.11 | 0.45 | 0.63 | 0.27 |
| evolved prompt, no LoRA | 0.47±0.28 | 0.02 | 0.11 | 0.41 | 0.58 | 0.23 |
| evolved prompt + LoRA 50% | 0.57±0.28 | 0.07 | 0.12 | 0.40 | 0.54 | 0.17 |
| evolved prompt + LoRA 100% | 0.42±0.28 | 0.04 | 0.10 | 0.37 | 0.55 | 0.36 |
| evolved prompt + LoRA 150% | 0.43±0.22 | 0.03 | 0.11 | 0.38 | 0.53 | 0.34 |

## Side effects & correlations (LoRA @ 100%)
- **Pushed up** (vs base): Emotional Numbness (+0.60), Fatigue Exhaustion (+0.26), Contemplation (+0.19)
- **Pushed down**: Concentration (-0.38), Conversational Style (-0.19), Interest (-0.17)
- **Positively correlated**: Awe (+0.87), Contemplation (+0.77), Pleasure Ecstasy (+0.65)
- **Negatively correlated**: Dramatic Style (-0.48), Tension (-0.42), Shame (-0.39)

## Conclusion
Best reward comes with the LoRA at 50% (0.566, beating plain BASE 0.511), and importantly the evolved prompt alone underperforms neutral BASE (0.470 < 0.511), so use evolved-prompt + 50% merge and don't run the steering prompt without the LoRA. LoRA50 roughly triples target emotion (0.069) and cuts WER to 0.167, but blend drops (0.453 to 0.402) and quality falls (0.625 to 0.543). The dominant side-effect is a sleepy, relaxed tone — it suppresses Concentration sharply (-0.48) and raises Fatigue, Emotional Numbness and Relief, so contentment reads as drowsy calm; keep the merge at 50% since 100/150% only add WER without more reward.

---
[← all emotions](index.md) · [human/audio version](../../site/emotions/Contentment.html)