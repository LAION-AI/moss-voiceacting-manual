# Pain — conditioning guide

*Target metric:* EmoNet **Pain** strength (0–1). *Reward* = (genu + blend + 1.25·emo) / (1+WER).

**TL;DR.** Best reward comes WITHOUT the LoRA — BASE_P (0.533) narrowly tops LoRA50 (0.522) and crushes the higher merges (LoRA100 0.339). Use the evolved steering prompt for the best score; if you actually need an audible wince, LoRA50 nearly matches on reward while adding real pain (emo 0 to 0.049), but stop there. Beyond 50% the model becomes near-unusable for intelligibility: LoRA150 does deliver strong pain (emo 0.305) but with WER 0.899 and quality 0.269. The dominant side-effect is that pain renders as anguished distress/sobbing — every LoRA level shifts up Distress, Helplessness and Sadness (corr ~0.9) and suppresses Interest (-0.6), so the delivery reads as weeping despair rather than a sharp physical hurt.

## Without a LoRA (base model only)
Best: **evolved prompt, no LoRA** → reward **0.53** (emotion -0.00, WER 0.35).

```
GENERAL: A voice to the extreme expressing pain, a voice wracked with pain, gasping and groaning, near screaming in agony, raw and unfiltered.
SCRIPT:
(groaning, gasping in pain and agony) "<your neutral sentence>"
```
(sampling: temperature 1.0, top_p 0.9, top_k 25)

## With the emotion LoRA
LoRA: `Pain` (TTS-AGI/moss-emotion-loras-v3). Best merge: **50%** → reward **0.52** (emotion 0.05).
Dose: 50% → reward 0.52 (emo 0.05) · 100% → 0.34 (emo 0.13) · 150% → 0.45 (emo 0.30).

## Conditions
| condition | reward | emotion | genu | blend | quality | WER |
|---|---|---|---|---|---|---|
| neutral prompt, no LoRA | 0.49±0.27 | -0.00 | 0.11 | 0.45 | 0.63 | 0.27 |
| evolved prompt, no LoRA | 0.53±0.33 | -0.00 | 0.14 | 0.51 | 0.53 | 0.35 |
| evolved prompt + LoRA 50% | 0.52±0.31 | 0.05 | 0.17 | 0.44 | 0.40 | 0.40 |
| evolved prompt + LoRA 100% | 0.34±0.14 | 0.13 | 0.19 | 0.26 | 0.28 | 0.78 |
| evolved prompt + LoRA 150% | 0.45±0.13 | 0.30 | 0.21 | 0.26 | 0.27 | 0.90 |

## Side effects & correlations (LoRA @ 100%)
- **Pushed up** (vs base): Distress (+1.02), Helplessness (+1.00), Sadness (+0.88)
- **Pushed down**: Interest (-0.48), Concentration (-0.42), Recording Quality (-0.40)
- **Positively correlated**: Distress (+0.89), Helplessness (+0.89), Sadness (+0.85)
- **Negatively correlated**: Interest (-0.75), Arousal Shift (-0.59), Narrator Style (-0.58)

## Conclusion
Best reward comes WITHOUT the LoRA — BASE_P (0.533) narrowly tops LoRA50 (0.522) and crushes the higher merges (LoRA100 0.339). Use the evolved steering prompt for the best score; if you actually need an audible wince, LoRA50 nearly matches on reward while adding real pain (emo 0 to 0.049), but stop there. Beyond 50% the model becomes near-unusable for intelligibility: LoRA150 does deliver strong pain (emo 0.305) but with WER 0.899 and quality 0.269. The dominant side-effect is that pain renders as anguished distress/sobbing — every LoRA level shifts up Distress, Helplessness and Sadness (corr ~0.9) and suppresses Interest (-0.6), so the delivery reads as weeping despair rather than a sharp physical hurt.

---
[← all emotions](index.md) · [human/audio version](../../site/emotions/Pain.html)