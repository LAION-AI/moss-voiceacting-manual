# Awe — conditioning guide

*Target metric:* EmoNet **Awe** strength (0–1). *Reward* = (genu + blend + 1.25·emo) / (1+WER).

**TL;DR.** Best reward is a tie between the LoRA at 50% (0.537) and the evolved prompt with no LoRA (BASE_P, 0.535) — both far ahead of LoRA100 (0.402) and LoRA150 (0.282), so never exceed 50%. Either config works; pick LoRA50 if you want the intelligibility bonus, since it actually lowers WER (0.162 to 0.110) while holding blend high (0.436). Note that measured awe strength stays near zero in every condition (emo 0.0-0.009), so do not expect a numeric emotion spike — you are prompting for a texture, not a detectable burst. The notable correlate is that LoRA50 reads awe as Pride (corr 0.86) and trades against Recording Quality, so it can sound grand but slightly degraded.

## Without a LoRA (base model only)
Best: **evolved prompt, no LoRA** → reward **0.53** (emotion 0.01, WER 0.16).

```
GENERAL: A voice utterly expressing awe, a hushed voice filled with awe and wonder, breath taken away, reverent, impossible to hide.
SCRIPT:
(in hushed awe and wonder) "<your neutral sentence>"
```
(sampling: temperature 1.1, top_p 0.95, top_k 25)

## With the emotion LoRA
LoRA: `Awe` (TTS-AGI/moss-emotion-loras-v3). Best merge: **50%** → reward **0.54** (emotion 0.00).
Dose: 50% → reward 0.54 (emo 0.00) · 100% → 0.40 (emo 0.01) · 150% → 0.28 (emo 0.00).

## Conditions
| condition | reward | emotion | genu | blend | quality | WER |
|---|---|---|---|---|---|---|
| neutral prompt, no LoRA | 0.49±0.27 | 0.00 | 0.11 | 0.45 | 0.63 | 0.27 |
| evolved prompt, no LoRA | 0.53±0.34 | 0.01 | 0.14 | 0.44 | 0.56 | 0.16 |
| evolved prompt + LoRA 50% | 0.54±0.30 | 0.00 | 0.14 | 0.44 | 0.55 | 0.11 |
| evolved prompt + LoRA 100% | 0.40±0.24 | 0.01 | 0.15 | 0.30 | 0.53 | 0.24 |
| evolved prompt + LoRA 150% | 0.28±0.18 | 0.00 | 0.16 | 0.26 | 0.40 | 0.62 |

## Side effects & correlations (LoRA @ 100%)
- **Pushed up** (vs base): Emotional Numbness (+0.53), Fatigue Exhaustion (+0.43), Longing (+0.16)
- **Pushed down**: Interest (-0.20), Dramatic Style (-0.18), Concentration (-0.18)
- **Positively correlated**: Hope Enthusiasm Optimism (+0.52), Triumph (+0.36), Fear (+0.34)
- **Negatively correlated**: Storytelling Style (-0.41), Focus (-0.40), Recording Quality (-0.39)

## Conclusion
Best reward is a tie between the LoRA at 50% (0.537) and the evolved prompt with no LoRA (BASE_P, 0.535) — both far ahead of LoRA100 (0.402) and LoRA150 (0.282), so never exceed 50%. Either config works; pick LoRA50 if you want the intelligibility bonus, since it actually lowers WER (0.162 to 0.110) while holding blend high (0.436). Note that measured awe strength stays near zero in every condition (emo 0.0-0.009), so do not expect a numeric emotion spike — you are prompting for a texture, not a detectable burst. The notable correlate is that LoRA50 reads awe as Pride (corr 0.86) and trades against Recording Quality, so it can sound grand but slightly degraded.

---
[← all emotions](index.md) · [human/audio version](../../site/emotions/Awe.html)