# Concentration — conditioning guide

*Target metric:* EmoNet **Concentration** strength (0–1). *Reward* = (genu + blend + 1.25·emo) / (1+WER).

**TL;DR.** Best reward comes without any LoRA and without the evolved prompt — plain neutral BASE wins outright (0.605), ahead of BASE_P (0.520), LoRA50 (0.486) and the rest. This emotion is native to the base model: BASE already shows the highest target-emotion strength (0.107), and both the evolved prompt and the LoRA reduce emo (LoRA drops it to 0.081 then 0.044). Recommendation: just use the neutral prompt; adding steering or LoRA only lowers reward, blend and intelligibility. The telltale side-effect of the LoRA is that it floods in Emotional Numbness (+1.18 at 100%) and suppresses Interest and Conversational style, turning focused attention into flat detachment.

## Without a LoRA (base model only)
Best: **neutral prompt, no LoRA** → reward **0.61** (emotion 0.11, WER 0.27).

```
GENERAL: A voice intensely expressing concentration, a focused, deliberate voice, fully concentrated, measured and precise, raw and unfiltered.
SCRIPT:
(intensely focused and concentrated) "<your neutral sentence>"
```
(sampling: temperature 0.9, top_p 0.95, top_k 25)

## With the emotion LoRA
LoRA: `Concentration` (TTS-AGI/moss-emotion-loras-v3). Best merge: **50%** → reward **0.49** (emotion 0.08).
Dose: 50% → reward 0.49 (emo 0.08) · 100% → 0.40 (emo 0.06) · 150% → 0.37 (emo 0.04).

## Conditions
| condition | reward | emotion | genu | blend | quality | WER |
|---|---|---|---|---|---|---|
| neutral prompt, no LoRA | 0.61±0.30 | 0.11 | 0.11 | 0.45 | 0.63 | 0.27 |
| evolved prompt, no LoRA | 0.52±0.26 | 0.13 | 0.11 | 0.37 | 0.60 | 0.33 |
| evolved prompt + LoRA 50% | 0.49±0.35 | 0.08 | 0.10 | 0.37 | 0.55 | 0.26 |
| evolved prompt + LoRA 100% | 0.40±0.26 | 0.06 | 0.11 | 0.35 | 0.47 | 0.47 |
| evolved prompt + LoRA 150% | 0.37±0.26 | 0.04 | 0.10 | 0.33 | 0.48 | 0.50 |

## Side effects & correlations (LoRA @ 100%)
- **Pushed up** (vs base): Emotional Numbness (+1.18), Fear (+0.21), Distress (+0.18)
- **Pushed down**: Interest (-0.30), Mask Resonance (-0.21), Conversational Style (-0.21)
- **Positively correlated**: Voice Age (+0.55), Interest (+0.47), Warmth (+0.45)
- **Negatively correlated**: Playful Style (-0.54), Dynamic Arc (-0.51), Casual Style (-0.47)

## Conclusion
Best reward comes without any LoRA and without the evolved prompt — plain neutral BASE wins outright (0.605), ahead of BASE_P (0.520), LoRA50 (0.486) and the rest. This emotion is native to the base model: BASE already shows the highest target-emotion strength (0.107), and both the evolved prompt and the LoRA reduce emo (LoRA drops it to 0.081 then 0.044). Recommendation: just use the neutral prompt; adding steering or LoRA only lowers reward, blend and intelligibility. The telltale side-effect of the LoRA is that it floods in Emotional Numbness (+1.18 at 100%) and suppresses Interest and Conversational style, turning focused attention into flat detachment.

---
[← all emotions](index.md) · [human/audio version](../../site/emotions/Concentration.html)