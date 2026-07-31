# Contempt — conditioning guide

*Target metric:* EmoNet **Contempt** strength (0–1). *Reward* = (genu + blend + 1.25·emo) / (1+WER).

**TL;DR.** Best reward is without any LoRA, use the evolved steering prompt (BASE_P 0.520, just ahead of BASE 0.492); every LoRA merge lowers reward (0.458 to 0.357 to 0.302). The LoRA nudges target emotion up only marginally (0.006 to 0.058) while WER explodes to 0.79 and blend/quality sink. Its worst side-effect is category drift: LoRA50 correlates almost perfectly with Disgust and Sourness (~1.0) and by 150% shifts hard into Anger, Malevolence and Impatience, so it stops sounding like contempt and becomes generic hostility. Note that actual contempt strength stays near zero (0.001) even with the prompt — this emotion is intrinsically hard to elicit, so lean on the prompt's low WER (0.134) and clean genuineness rather than chasing the emo score.

## Without a LoRA (base model only)
Best: **evolved prompt, no LoRA** → reward **0.52** (emotion 0.00, WER 0.13).

```
GENERAL: A voice to the extreme expressing contempt, a cold, sneering voice, full of contempt and disdain, looking down with scorn, pouring out.
SCRIPT:
(with cold, sneering contempt) "<your neutral sentence>"
```
(sampling: temperature 1.1, top_p 0.9, top_k 30)

## With the emotion LoRA
LoRA: `Contempt` (TTS-AGI/moss-emotion-loras-v3). Best merge: **50%** → reward **0.46** (emotion 0.01).
Dose: 50% → reward 0.46 (emo 0.01) · 100% → 0.36 (emo 0.02) · 150% → 0.30 (emo 0.06).

## Conditions
| condition | reward | emotion | genu | blend | quality | WER |
|---|---|---|---|---|---|---|
| neutral prompt, no LoRA | 0.49±0.27 | 0.00 | 0.11 | 0.45 | 0.63 | 0.27 |
| evolved prompt, no LoRA | 0.52±0.28 | 0.00 | 0.14 | 0.42 | 0.55 | 0.13 |
| evolved prompt + LoRA 50% | 0.46±0.35 | 0.01 | 0.14 | 0.39 | 0.49 | 0.30 |
| evolved prompt + LoRA 100% | 0.36±0.20 | 0.02 | 0.18 | 0.28 | 0.43 | 0.57 |
| evolved prompt + LoRA 150% | 0.30±0.18 | 0.06 | 0.16 | 0.26 | 0.38 | 0.79 |

## Side effects & correlations (LoRA @ 100%)
- **Pushed up** (vs base): Emotional Numbness (+0.59), Fear (+0.46), Malevolence Malice (+0.38)
- **Pushed down**: Mask Resonance (-0.30), Recording Quality (-0.27), Conversational Style (-0.23)
- **Positively correlated**: Disgust (+0.90), Malevolence Malice (+0.87), Pride (+0.79)
- **Negatively correlated**: Background Noise (-0.37), Structure (-0.36), Recording Quality (-0.34)

## Conclusion
Best reward is without any LoRA, use the evolved steering prompt (BASE_P 0.520, just ahead of BASE 0.492); every LoRA merge lowers reward (0.458 to 0.357 to 0.302). The LoRA nudges target emotion up only marginally (0.006 to 0.058) while WER explodes to 0.79 and blend/quality sink. Its worst side-effect is category drift: LoRA50 correlates almost perfectly with Disgust and Sourness (~1.0) and by 150% shifts hard into Anger, Malevolence and Impatience, so it stops sounding like contempt and becomes generic hostility. Note that actual contempt strength stays near zero (0.001) even with the prompt — this emotion is intrinsically hard to elicit, so lean on the prompt's low WER (0.134) and clean genuineness rather than chasing the emo score.

---
[← all emotions](index.md) · [human/audio version](../../site/emotions/Contempt.html)