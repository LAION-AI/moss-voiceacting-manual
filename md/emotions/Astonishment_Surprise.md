# Astonishment Surprise — conditioning guide

*Target metric:* EmoNet **Astonishment_Surprise** strength (0–1). *Reward* = (genu + blend + 1.25·emo) / (1+WER).

**TL;DR.** Best reward comes without the LoRA — the evolved prompt (BASE_P, 0.496) edges out BASE (0.491) and all LoRA merges (best LoRA is 150% at 0.475). Recommendation: rely on the evolved prompt, which already injects surprise cues (Hope/Enthusiasm +0.36, Interest +0.21); reach for LoRA150 only when you need a stronger emo signal (0.033 to 0.145). The trade-off at 150% is a large intelligibility and quality hit (WER 0.296 to 0.621, quality 0.558 to 0.376). Its key side-effect is that the LoRA leaks surprise into Impatience/Irritability (+1.09) and Anger/Disgust rather than delight, and it suppresses Concentration (-0.66).

## Without a LoRA (base model only)
Best: **evolved prompt, no LoRA** → reward **0.50** (emotion 0.03, WER 0.30).

```
GENERAL: A voice unmistakably expressing astonishment surprise, a voice struck with astonishment, gasping, utterly surprised, eyes wide, pouring out.
SCRIPT:
(gasping, astonished, taken completely by surprise) "<your neutral sentence>"
```
(sampling: temperature 1.0, top_p 0.95, top_k 25)

## With the emotion LoRA
LoRA: `Astonishment_Surprise` (TTS-AGI/moss-emotion-loras-v3). Best merge: **150%** → reward **0.47** (emotion 0.14).
Dose: 50% → reward 0.45 (emo 0.02) · 100% → 0.39 (emo 0.03) · 150% → 0.47 (emo 0.14).

## Conditions
| condition | reward | emotion | genu | blend | quality | WER |
|---|---|---|---|---|---|---|
| neutral prompt, no LoRA | 0.49±0.27 | 0.00 | 0.11 | 0.45 | 0.63 | 0.27 |
| evolved prompt, no LoRA | 0.50±0.25 | 0.03 | 0.15 | 0.42 | 0.56 | 0.30 |
| evolved prompt + LoRA 50% | 0.45±0.30 | 0.02 | 0.14 | 0.38 | 0.53 | 0.32 |
| evolved prompt + LoRA 100% | 0.39±0.22 | 0.03 | 0.14 | 0.31 | 0.48 | 0.39 |
| evolved prompt + LoRA 150% | 0.47±0.19 | 0.14 | 0.16 | 0.39 | 0.38 | 0.62 |

## Side effects & correlations (LoRA @ 100%)
- **Pushed up** (vs base): Impatience and Irritability (+1.09), Anger (+0.43), Dynamic Arc (+0.26)
- **Pushed down**: Concentration (-0.40), Warmth (-0.30), Fullness (-0.21)
- **Positively correlated**: Elation (+0.78), Disgust (+0.78), Amusement (+0.77)
- **Negatively correlated**: Smoothness (-0.55), Monologue Style (-0.54), Formal Style (-0.51)

## Conclusion
Best reward comes without the LoRA — the evolved prompt (BASE_P, 0.496) edges out BASE (0.491) and all LoRA merges (best LoRA is 150% at 0.475). Recommendation: rely on the evolved prompt, which already injects surprise cues (Hope/Enthusiasm +0.36, Interest +0.21); reach for LoRA150 only when you need a stronger emo signal (0.033 to 0.145). The trade-off at 150% is a large intelligibility and quality hit (WER 0.296 to 0.621, quality 0.558 to 0.376). Its key side-effect is that the LoRA leaks surprise into Impatience/Irritability (+1.09) and Anger/Disgust rather than delight, and it suppresses Concentration (-0.66).

---
[← all emotions](index.md) · [human/audio version](../../site/emotions/Astonishment_Surprise.html)