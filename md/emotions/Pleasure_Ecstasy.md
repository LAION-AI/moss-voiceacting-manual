# Pleasure Ecstasy — conditioning guide

*Target metric:* EmoNet **Pleasure_Ecstasy** strength (0–1). *Reward* = (genu + blend + 1.25·emo) / (1+WER).

**TL;DR.** Best reward comes WITH the LoRA at 150% — reward climbs monotonically with merge strength (BASE 0.489 to LoRA100 0.521 to LoRA150 0.534), one of the few cases where the strongest merge wins. Use the evolved steering prompt plus the LoRA at 150%. Unusually, WER stays controlled at 150% (0.321, near baseline), so the trade-off is quality and blend, not intelligibility: quality drops 0.625 to 0.452 and blend 0.453 to 0.389. Be aware the reward gain is genuineness-driven, not emotion-driven — target strength stays low (emo ~0.048) while genuineness rises 0.110 to 0.200; the LoRA also shifts up Emotional Numbness and Fatigue, so you get a warmer, more sincere read rather than overt ecstatic intensity.

## Without a LoRA (base model only)
Best: **neutral prompt, no LoRA** → reward **0.49** (emotion -0.00, WER 0.27).

```
GENERAL: A voice intensely expressing pleasure ecstasy, a voice breathless with pleasure and ecstasy, rapturous and overwhelmed, with every word.
SCRIPT:
(breathless with pleasure and ecstasy) "<your neutral sentence>"
```
(sampling: temperature 1.15, top_p 0.9, top_k 25)

## With the emotion LoRA
LoRA: `Pleasure_Ecstasy` (TTS-AGI/moss-emotion-loras-v3). Best merge: **150%** → reward **0.53** (emotion 0.05).
Dose: 50% → reward 0.48 (emo 0.03) · 100% → 0.52 (emo 0.04) · 150% → 0.53 (emo 0.05).

## Conditions
| condition | reward | emotion | genu | blend | quality | WER |
|---|---|---|---|---|---|---|
| neutral prompt, no LoRA | 0.49±0.27 | -0.00 | 0.11 | 0.45 | 0.63 | 0.27 |
| evolved prompt, no LoRA | 0.49±0.26 | 0.01 | 0.13 | 0.45 | 0.57 | 0.31 |
| evolved prompt + LoRA 50% | 0.48±0.30 | 0.03 | 0.17 | 0.42 | 0.48 | 0.39 |
| evolved prompt + LoRA 100% | 0.52±0.33 | 0.04 | 0.19 | 0.40 | 0.43 | 0.37 |
| evolved prompt + LoRA 150% | 0.53±0.28 | 0.05 | 0.20 | 0.39 | 0.45 | 0.32 |

## Side effects & correlations (LoRA @ 100%)
- **Pushed up** (vs base): Emotional Numbness (+0.53), Fatigue Exhaustion (+0.49), Distress (+0.40)
- **Pushed down**: Concentration (-0.39), Fullness (-0.27), Interest (-0.25)
- **Positively correlated**: Elation (+0.72), Contentment (+0.62), Amusement (+0.58)
- **Negatively correlated**: Monologue Style (-0.60), Fullness (-0.47), Newsreader Style (-0.43)

## Conclusion
Best reward comes WITH the LoRA at 150% — reward climbs monotonically with merge strength (BASE 0.489 to LoRA100 0.521 to LoRA150 0.534), one of the few cases where the strongest merge wins. Use the evolved steering prompt plus the LoRA at 150%. Unusually, WER stays controlled at 150% (0.321, near baseline), so the trade-off is quality and blend, not intelligibility: quality drops 0.625 to 0.452 and blend 0.453 to 0.389. Be aware the reward gain is genuineness-driven, not emotion-driven — target strength stays low (emo ~0.048) while genuineness rises 0.110 to 0.200; the LoRA also shifts up Emotional Numbness and Fatigue, so you get a warmer, more sincere read rather than overt ecstatic intensity.

---
[← all emotions](index.md) · [human/audio version](../../site/emotions/Pleasure_Ecstasy.html)