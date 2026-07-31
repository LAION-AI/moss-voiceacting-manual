# Sourness — conditioning guide

*Target metric:* EmoNet **Sourness** strength (0–1). *Reward* = (genu + blend + 1.25·emo) / (1+WER).

**TL;DR.** Best with the LoRA at 50% (reward 0.585), but note the plain neutral prompt (BASE, 0.494) beats the evolved steering prompt (0.470) — the steering prompt hurts here, so use BASE + 50% merge. Sourness never registers numerically (emo ~0 in every condition), so LoRA50's win comes entirely from higher blend (0.485) and lower WER (0.179), not added emotion. The price is quality: the proxy drops from 0.625 (BASE) to 0.489, and delivery leans on Disgust/Contempt/Embarrassment correlations, so let the text carry the sour meaning and use the LoRA only for delivery; avoid 100%+ (reward collapses to 0.32).

## Without a LoRA (base model only)
Best: **neutral prompt, no LoRA** → reward **0.49** (emotion 0.00, WER 0.27).

```
GENERAL: A voice intensely expressing sourness, a sour, grumbling voice, peevish and put-out, curdled with displeasure, with every word.
SCRIPT:
(sourly, grumbling and peevish) "<your neutral sentence>"
```
(sampling: temperature 1.2, top_p 0.9, top_k 30)

## With the emotion LoRA
LoRA: `Sourness` (TTS-AGI/moss-emotion-loras-v3). Best merge: **50%** → reward **0.58** (emotion -0.00).
Dose: 50% → reward 0.58 (emo -0.00) · 100% → 0.32 (emo 0.00) · 150% → 0.39 (emo 0.00).

## Conditions
| condition | reward | emotion | genu | blend | quality | WER |
|---|---|---|---|---|---|---|
| neutral prompt, no LoRA | 0.49±0.27 | 0.00 | 0.11 | 0.45 | 0.63 | 0.27 |
| evolved prompt, no LoRA | 0.47±0.25 | -0.00 | 0.13 | 0.44 | 0.58 | 0.30 |
| evolved prompt + LoRA 50% | 0.58±0.32 | -0.00 | 0.16 | 0.49 | 0.49 | 0.18 |
| evolved prompt + LoRA 100% | 0.32±0.28 | 0.00 | 0.11 | 0.28 | 0.48 | 0.31 |
| evolved prompt + LoRA 150% | 0.39±0.21 | 0.00 | 0.14 | 0.34 | 0.44 | 0.25 |

## Side effects & correlations (LoRA @ 100%)
- **Pushed up** (vs base): Impatience and Irritability (+0.91), Malevolence Malice (+0.30), Anger (+0.30)
- **Pushed down**: Concentration (-0.67), Fullness (-0.23), Warmth (-0.19)
- **Positively correlated**: Elation (+0.81), Hope Enthusiasm Optimism (+0.77), Teasing (+0.69)
- **Negatively correlated**: Contemplation (-0.45), Monologue Style (-0.33), Mixed Resonance (-0.25)

## Conclusion
Best with the LoRA at 50% (reward 0.585), but note the plain neutral prompt (BASE, 0.494) beats the evolved steering prompt (0.470) — the steering prompt hurts here, so use BASE + 50% merge. Sourness never registers numerically (emo ~0 in every condition), so LoRA50's win comes entirely from higher blend (0.485) and lower WER (0.179), not added emotion. The price is quality: the proxy drops from 0.625 (BASE) to 0.489, and delivery leans on Disgust/Contempt/Embarrassment correlations, so let the text carry the sour meaning and use the LoRA only for delivery; avoid 100%+ (reward collapses to 0.32).

---
[← all emotions](index.md) · [human/audio version](../../site/emotions/Sourness.html)