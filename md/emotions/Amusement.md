# Amusement — conditioning guide

*Target metric:* EmoNet **Amusement** strength (0–1). *Reward* = (genu + blend + 1.25·emo) / (1+WER).

**TL;DR.** Best reward is essentially a tie between no LoRA (neutral BASE, 0.504) and the LoRA at 150% (0.502); notably the evolved prompt (BASE_P, 0.459) actually hurts here, so prefer the plain base prompt for safe quality. If you need audibly perceptible amusement, only the LoRA delivers it — target-emotion strength climbs from ~0.01 (both no-LoRA conditions) to 0.259 at 150%, driving huge Teasing (+1.56) and Pleasure/Elation shifts. The trade-off is severe: vocal-burst blend collapses (0.453 to 0.175), speech quality drops (0.625 to 0.405) and WER rises (0.269 to 0.472). Its signature side-effect is that it strongly suppresses Concentration (-0.78) and Warmth, trading composure for giddiness.

## Without a LoRA (base model only)
Best: **neutral prompt, no LoRA** → reward **0.50** (emotion 0.01, WER 0.27).

```
GENERAL: A voice overwhelmingly expressing amusement, a voice bubbling with amusement, on the edge of laughter, playful and delighted, impossible to hide.
SCRIPT:
(chuckling, highly amused, barely holding back laughter) "<your neutral sentence>"
```
(sampling: temperature 1.1, top_p 0.95, top_k 30)

## With the emotion LoRA
LoRA: `Amusement` (TTS-AGI/moss-emotion-loras-v3). Best merge: **150%** → reward **0.50** (emotion 0.26).
Dose: 50% → reward 0.43 (emo 0.06) · 100% → 0.50 (emo 0.14) · 150% → 0.50 (emo 0.26).

## Conditions
| condition | reward | emotion | genu | blend | quality | WER |
|---|---|---|---|---|---|---|
| neutral prompt, no LoRA | 0.50±0.28 | 0.01 | 0.11 | 0.45 | 0.63 | 0.27 |
| evolved prompt, no LoRA | 0.46±0.24 | 0.01 | 0.14 | 0.38 | 0.58 | 0.23 |
| evolved prompt + LoRA 50% | 0.43±0.18 | 0.06 | 0.14 | 0.35 | 0.55 | 0.23 |
| evolved prompt + LoRA 100% | 0.50±0.25 | 0.14 | 0.17 | 0.29 | 0.45 | 0.29 |
| evolved prompt + LoRA 150% | 0.50±0.29 | 0.26 | 0.20 | 0.17 | 0.40 | 0.47 |

## Side effects & correlations (LoRA @ 100%)
- **Pushed up** (vs base): Pleasure Ecstasy (+0.64), Teasing (+0.56), Elation (+0.39)
- **Pushed down**: Concentration (-0.69), Fatigue Exhaustion (-0.32), Warmth (-0.28)
- **Positively correlated**: Pleasure Ecstasy (+0.82), Teasing (+0.79), Contentment (+0.73)
- **Negatively correlated**: Background Noise (-0.72), Smoothness (-0.67), Recording Quality (-0.66)

## Conclusion
Best reward is essentially a tie between no LoRA (neutral BASE, 0.504) and the LoRA at 150% (0.502); notably the evolved prompt (BASE_P, 0.459) actually hurts here, so prefer the plain base prompt for safe quality. If you need audibly perceptible amusement, only the LoRA delivers it — target-emotion strength climbs from ~0.01 (both no-LoRA conditions) to 0.259 at 150%, driving huge Teasing (+1.56) and Pleasure/Elation shifts. The trade-off is severe: vocal-burst blend collapses (0.453 to 0.175), speech quality drops (0.625 to 0.405) and WER rises (0.269 to 0.472). Its signature side-effect is that it strongly suppresses Concentration (-0.78) and Warmth, trading composure for giddiness.

---
[← all emotions](index.md) · [human/audio version](../../site/emotions/Amusement.html)