# Disgust — conditioning guide

*Target metric:* EmoNet **Disgust** strength (0–1). *Reward* = (genu + blend + 1.25·emo) / (1+WER).

**TL;DR.** Best reward is without a LoRA (plain BASE 0.490, barely ahead of BASE_P 0.468 and LoRA50 0.474), but be aware the actual disgust signal is essentially zero (~0.001-0.003) in all of these — the model does not natively voice disgust. Only LoRA150 makes disgust audible (emo 0.236), at a punishing cost: WER 0.856 and quality down to 0.308. Its side-effect is that it doesn't produce clean disgust but shoves the delivery into Anger and Impatience (shift +1.31/+1.27) plus Fear, so you get an enraged read, not a revolted one. Recommendation: use the prompt for best reward if literal disgust isn't required; if it must be heard, accept LoRA150's near-total intelligibility loss.

## Without a LoRA (base model only)
Best: **neutral prompt, no LoRA** → reward **0.49** (emotion 0.00, WER 0.27).

```
GENERAL: A voice intensely expressing disgust, a revolted voice, curling with disgust, repulsed and sickened, in every breath.
SCRIPT:
(with revulsion and disgust, sickened) "<your neutral sentence>"
```
(sampling: temperature 1.05, top_p 0.95, top_k 30)

## With the emotion LoRA
LoRA: `Disgust` (TTS-AGI/moss-emotion-loras-v3). Best merge: **50%** → reward **0.47** (emotion 0.00).
Dose: 50% → reward 0.47 (emo 0.00) · 100% → 0.40 (emo 0.06) · 150% → 0.44 (emo 0.24).

## Conditions
| condition | reward | emotion | genu | blend | quality | WER |
|---|---|---|---|---|---|---|
| neutral prompt, no LoRA | 0.49±0.27 | 0.00 | 0.11 | 0.45 | 0.63 | 0.27 |
| evolved prompt, no LoRA | 0.47±0.29 | 0.00 | 0.11 | 0.43 | 0.56 | 0.23 |
| evolved prompt + LoRA 50% | 0.47±0.25 | 0.00 | 0.15 | 0.43 | 0.56 | 0.31 |
| evolved prompt + LoRA 100% | 0.40±0.20 | 0.06 | 0.18 | 0.29 | 0.46 | 0.47 |
| evolved prompt + LoRA 150% | 0.44±0.24 | 0.24 | 0.22 | 0.27 | 0.31 | 0.86 |

## Side effects & correlations (LoRA @ 100%)
- **Pushed up** (vs base): Impatience and Irritability (+0.57), Anger (+0.51), Fear (+0.38)
- **Pushed down**: Recording Quality (-0.22), Warmth (-0.20), Structure (-0.18)
- **Positively correlated**: Contempt (+0.76), Sourness (+0.66), Anger (+0.56)
- **Negatively correlated**: Concentration (-0.46), Structure (-0.45), Head Resonance (-0.44)

## Conclusion
Best reward is without a LoRA (plain BASE 0.490, barely ahead of BASE_P 0.468 and LoRA50 0.474), but be aware the actual disgust signal is essentially zero (~0.001-0.003) in all of these — the model does not natively voice disgust. Only LoRA150 makes disgust audible (emo 0.236), at a punishing cost: WER 0.856 and quality down to 0.308. Its side-effect is that it doesn't produce clean disgust but shoves the delivery into Anger and Impatience (shift +1.31/+1.27) plus Fear, so you get an enraged read, not a revolted one. Recommendation: use the prompt for best reward if literal disgust isn't required; if it must be heard, accept LoRA150's near-total intelligibility loss.

---
[← all emotions](index.md) · [human/audio version](../../site/emotions/Disgust.html)