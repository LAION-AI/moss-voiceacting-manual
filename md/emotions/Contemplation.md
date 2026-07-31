# Contemplation — conditioning guide

*Target metric:* EmoNet **Contemplation** strength (0–1). *Reward* = (genu + blend + 1.25·emo) / (1+WER).

**TL;DR.** Best reward comes with the LoRA at 50% (0.623 vs 0.598 for the evolved prompt alone and 0.498 for BASE), so pair the evolved steering prompt with a 50% merge. The trade-off is intelligibility: emotion and blend edge up (blend 0.497, the highest of any condition) but quality dips (0.576 to 0.555) and WER climbs from 0.146 to 0.231. The main side-effect is a wistful, downcast color, LoRA50 correlates strongly with Longing (0.74), Sadness (0.73) and Pain (0.68) and pushes Emotional Numbness/Contentment up, so contemplation reads as calm and faintly melancholic. Do not push to 100/150%, WER doubles to ~0.52 and reward collapses to 0.41.

## Without a LoRA (base model only)
Best: **evolved prompt, no LoRA** → reward **0.60** (emotion 0.04, WER 0.15).

```
GENERAL: A voice to the extreme expressing contemplation, a slow, thoughtful voice, deep in contemplation, musing and reflective, in every breath.
SCRIPT:
(slowly, deep in contemplative thought) "<your neutral sentence>"
```
(sampling: temperature 1.1, top_p 0.95, top_k 25)

## With the emotion LoRA
LoRA: `Contemplation` (TTS-AGI/moss-emotion-loras-v3). Best merge: **50%** → reward **0.62** (emotion 0.05).
Dose: 50% → reward 0.62 (emo 0.05) · 100% → 0.47 (emo 0.06) · 150% → 0.41 (emo 0.03).

## Conditions
| condition | reward | emotion | genu | blend | quality | WER |
|---|---|---|---|---|---|---|
| neutral prompt, no LoRA | 0.50±0.27 | 0.01 | 0.11 | 0.45 | 0.63 | 0.27 |
| evolved prompt, no LoRA | 0.60±0.33 | 0.04 | 0.13 | 0.47 | 0.58 | 0.15 |
| evolved prompt + LoRA 50% | 0.62±0.35 | 0.05 | 0.14 | 0.50 | 0.55 | 0.23 |
| evolved prompt + LoRA 100% | 0.47±0.30 | 0.06 | 0.14 | 0.41 | 0.54 | 0.52 |
| evolved prompt + LoRA 150% | 0.41±0.25 | 0.03 | 0.13 | 0.37 | 0.49 | 0.52 |

## Side effects & correlations (LoRA @ 100%)
- **Pushed up** (vs base): Emotional Numbness (+0.58), Contentment (+0.32), Fatigue Exhaustion (+0.23)
- **Pushed down**: Dramatic Style (-0.21), Arousal (-0.19), Attack (-0.18)
- **Positively correlated**: Longing (+0.79), Affection (+0.72), Helplessness (+0.66)
- **Negatively correlated**: Formal Style (-0.49), Emphasis (-0.40), Pleasure Ecstasy (-0.36)

## Conclusion
Best reward comes with the LoRA at 50% (0.623 vs 0.598 for the evolved prompt alone and 0.498 for BASE), so pair the evolved steering prompt with a 50% merge. The trade-off is intelligibility: emotion and blend edge up (blend 0.497, the highest of any condition) but quality dips (0.576 to 0.555) and WER climbs from 0.146 to 0.231. The main side-effect is a wistful, downcast color, LoRA50 correlates strongly with Longing (0.74), Sadness (0.73) and Pain (0.68) and pushes Emotional Numbness/Contentment up, so contemplation reads as calm and faintly melancholic. Do not push to 100/150%, WER doubles to ~0.52 and reward collapses to 0.41.

---
[← all emotions](index.md) · [human/audio version](../../site/emotions/Contemplation.html)