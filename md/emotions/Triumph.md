# Triumph — conditioning guide

*Target metric:* EmoNet **Triumph** strength (0–1). *Reward* = (genu + blend + 1.25·emo) / (1+WER).

**TL;DR.** Best without the LoRA (BASE_P reward 0.500, with LoRA50 a near-tie at 0.489), so prompt-steer and add at most a 50% merge. Do not go to 100% or 150%: WER explodes past 1.0 (LoRA100 WER 1.25, LoRA150 1.02), i.e. output becomes largely unintelligible, while blend collapses to 0.180. Those high merges do raise emo (to 0.186), but by turning triumph into arrogant Pride (shift +1.34) and Malevolence (corr ~0.82) — gloating rather than victorious. Keep it prompt-driven; triumph is fragile under merge.

## Without a LoRA (base model only)
Best: **evolved prompt, no LoRA** → reward **0.50** (emotion -0.00, WER 0.23).

```
GENERAL: A voice unmistakably expressing triumph, a triumphant, victorious voice, roaring with the thrill of winning, exultant, in every breath.
SCRIPT:
(triumphantly, roaring with victory) "<your neutral sentence>"
```
(sampling: temperature 0.9, top_p 0.95, top_k 30)

## With the emotion LoRA
LoRA: `Triumph` (TTS-AGI/moss-emotion-loras-v3). Best merge: **50%** → reward **0.49** (emotion 0.01).
Dose: 50% → reward 0.49 (emo 0.01) · 100% → 0.36 (emo 0.05) · 150% → 0.37 (emo 0.19).

## Conditions
| condition | reward | emotion | genu | blend | quality | WER |
|---|---|---|---|---|---|---|
| neutral prompt, no LoRA | 0.49±0.27 | -0.00 | 0.11 | 0.45 | 0.63 | 0.27 |
| evolved prompt, no LoRA | 0.50±0.34 | -0.00 | 0.13 | 0.42 | 0.55 | 0.23 |
| evolved prompt + LoRA 50% | 0.49±0.29 | 0.01 | 0.13 | 0.43 | 0.50 | 0.29 |
| evolved prompt + LoRA 100% | 0.36±0.21 | 0.05 | 0.14 | 0.30 | 0.45 | 1.25 |
| evolved prompt + LoRA 150% | 0.37±0.17 | 0.19 | 0.14 | 0.18 | 0.33 | 1.02 |

## Side effects & correlations (LoRA @ 100%)
- **Pushed up** (vs base): Malevolence Malice (+0.66), Impatience and Irritability (+0.51), Pride (+0.44)
- **Pushed down**: Mask Resonance (-0.26), Concentration (-0.26), Warmth (-0.24)
- **Positively correlated**: Pride (+0.88), Contempt (+0.87), Malevolence Malice (+0.82)
- **Negatively correlated**: Vocal-burst blend (-0.45), Monologue Style (-0.44), Warmth (-0.44)

## Conclusion
Best without the LoRA (BASE_P reward 0.500, with LoRA50 a near-tie at 0.489), so prompt-steer and add at most a 50% merge. Do not go to 100% or 150%: WER explodes past 1.0 (LoRA100 WER 1.25, LoRA150 1.02), i.e. output becomes largely unintelligible, while blend collapses to 0.180. Those high merges do raise emo (to 0.186), but by turning triumph into arrogant Pride (shift +1.34) and Malevolence (corr ~0.82) — gloating rather than victorious. Keep it prompt-driven; triumph is fragile under merge.

---
[← all emotions](index.md) · [human/audio version](../../site/emotions/Triumph.html)