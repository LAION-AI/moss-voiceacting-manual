# Anger — conditioning guide

*Target metric:* EmoNet **Anger** strength (0–1). *Reward* = (genu + blend + 1.25·emo) / (1+WER).

**TL;DR.** Best reward comes without the LoRA via the evolved prompt (BASE_P, 0.553, vs 0.432/0.420/0.427 for LoRA50/100/150) — but be warned that this top-reward config is barely angry (emo only 0.016). If you actually need genuine anger, you must accept the LoRA at 100-150%, which pushes emo to 0.24-0.28 (huge Impatience +1.9, Triumph, Malevolence shifts). The cost is brutal: blend craters from 0.446 to 0.129, quality from 0.552 to 0.261, and WER more than doubles (0.202 to 0.570). Its most notable side-effect is that it drags in Malevolence and Contempt while stripping Warmth (-0.48) and articulation clarity, so the anger sounds cruel and slurred rather than heated.

## Without a LoRA (base model only)
Best: **evolved prompt, no LoRA** → reward **0.55** (emotion 0.02, WER 0.20).

```
GENERAL: A voice overwhelmingly expressing anger, a furious voice, seething and exploding into a rant, sharp, loud and cutting, building and building.
SCRIPT:
(furious, ranting, exploding with rage) "<your neutral sentence>"
```
(sampling: temperature 1.0, top_p 0.9, top_k 40)

## With the emotion LoRA
LoRA: `Anger` (TTS-AGI/moss-emotion-loras-v3). Best merge: **50%** → reward **0.43** (emotion 0.03).
Dose: 50% → reward 0.43 (emo 0.03) · 100% → 0.42 (emo 0.24) · 150% → 0.43 (emo 0.28).

## Conditions
| condition | reward | emotion | genu | blend | quality | WER |
|---|---|---|---|---|---|---|
| neutral prompt, no LoRA | 0.50±0.27 | 0.01 | 0.11 | 0.45 | 0.63 | 0.27 |
| evolved prompt, no LoRA | 0.55±0.36 | 0.02 | 0.14 | 0.45 | 0.55 | 0.20 |
| evolved prompt + LoRA 50% | 0.43±0.26 | 0.03 | 0.15 | 0.34 | 0.51 | 0.34 |
| evolved prompt + LoRA 100% | 0.42±0.25 | 0.24 | 0.16 | 0.13 | 0.26 | 0.57 |
| evolved prompt + LoRA 150% | 0.43±0.19 | 0.28 | 0.18 | 0.14 | 0.21 | 0.66 |

## Side effects & correlations (LoRA @ 100%)
- **Pushed up** (vs base): Impatience and Irritability (+1.90), Triumph (+1.43), Malevolence Malice (+1.35)
- **Pushed down**: Warmth (-0.48), Monologue Style (-0.41), Concentration (-0.39)
- **Positively correlated**: Malevolence Malice (+0.80), Disfluency (+0.77), Respiration (+0.74)
- **Negatively correlated**: Structure (-0.75), Articulation Clarity (-0.72), Formal Style (-0.72)

## Conclusion
Best reward comes without the LoRA via the evolved prompt (BASE_P, 0.553, vs 0.432/0.420/0.427 for LoRA50/100/150) — but be warned that this top-reward config is barely angry (emo only 0.016). If you actually need genuine anger, you must accept the LoRA at 100-150%, which pushes emo to 0.24-0.28 (huge Impatience +1.9, Triumph, Malevolence shifts). The cost is brutal: blend craters from 0.446 to 0.129, quality from 0.552 to 0.261, and WER more than doubles (0.202 to 0.570). Its most notable side-effect is that it drags in Malevolence and Contempt while stripping Warmth (-0.48) and articulation clarity, so the anger sounds cruel and slurred rather than heated.

---
[← all emotions](index.md) · [human/audio version](../../site/emotions/Anger.html)