# Thankfulness Gratitude — conditioning guide

*Target metric:* EmoNet **Thankfulness_Gratitude** strength (0–1). *Reward* = (genu + blend + 1.25·emo) / (1+WER).

**TL;DR.** Best without the LoRA — the evolved prompt (BASE_P) tops out at reward 0.532 and the LoRA only hurts, sliding monotonically from 0.442 (50%) to 0.287 (150%). Prompt-steer and skip the merge entirely: gratitude never registers as a measurable emotion (emo stays ~0.006-0.020 everywhere), so the LoRA adds no feeling while steadily draining blend (0.456 to 0.244) and reward. BASE_P is also the safe choice for clean audio — it holds the quality proxy high (0.583) and WER low (0.182) — so express the gratitude lexically rather than expecting the model to color it.

## Without a LoRA (base model only)
Best: **evolved prompt, no LoRA** → reward **0.53** (emotion 0.01, WER 0.18).

```
GENERAL: A voice intensely expressing thankfulness gratitude, a warm, heartfelt voice, full of gratitude and thanks, deeply touched, raw and unfiltered.
SCRIPT:
(warmly, full of heartfelt gratitude) "<your neutral sentence>"
```
(sampling: temperature 1.05, top_p 0.9, top_k 40)

## With the emotion LoRA
LoRA: `Thankfulness_Gratitude` (TTS-AGI/moss-emotion-loras-v3). Best merge: **50%** → reward **0.44** (emotion 0.01).
Dose: 50% → reward 0.44 (emo 0.01) · 100% → 0.38 (emo 0.02) · 150% → 0.29 (emo 0.01).

## Conditions
| condition | reward | emotion | genu | blend | quality | WER |
|---|---|---|---|---|---|---|
| neutral prompt, no LoRA | 0.50±0.27 | 0.01 | 0.11 | 0.45 | 0.63 | 0.27 |
| evolved prompt, no LoRA | 0.53±0.30 | 0.01 | 0.14 | 0.46 | 0.58 | 0.18 |
| evolved prompt + LoRA 50% | 0.44±0.24 | 0.01 | 0.13 | 0.41 | 0.56 | 0.36 |
| evolved prompt + LoRA 100% | 0.38±0.19 | 0.02 | 0.11 | 0.34 | 0.53 | 0.28 |
| evolved prompt + LoRA 150% | 0.29±0.15 | 0.01 | 0.14 | 0.24 | 0.50 | 0.49 |

## Side effects & correlations (LoRA @ 100%)
- **Pushed up** (vs base): Emotional Numbness (+0.84), Concentration (+0.30), Pride (+0.26)
- **Pushed down**: Interest (-0.16), Amusement (-0.15), Recording Quality (-0.15)
- **Positively correlated**: Contentment (+0.67), Confusion (+0.67), Pleasure Ecstasy (+0.60)
- **Negatively correlated**: Elation (-0.77), Concentration (-0.46), Harmonicity (-0.43)

## Conclusion
Best without the LoRA — the evolved prompt (BASE_P) tops out at reward 0.532 and the LoRA only hurts, sliding monotonically from 0.442 (50%) to 0.287 (150%). Prompt-steer and skip the merge entirely: gratitude never registers as a measurable emotion (emo stays ~0.006-0.020 everywhere), so the LoRA adds no feeling while steadily draining blend (0.456 to 0.244) and reward. BASE_P is also the safe choice for clean audio — it holds the quality proxy high (0.583) and WER low (0.182) — so express the gratitude lexically rather than expecting the model to color it.

---
[← all emotions](index.md) · [human/audio version](../../site/emotions/Thankfulness_Gratitude.html)