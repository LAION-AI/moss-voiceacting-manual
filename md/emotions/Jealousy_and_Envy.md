# Jealousy and Envy — conditioning guide

*Target metric:* EmoNet **Jealousy_&_Envy** strength (0–1). *Reward* = (genu + blend + 1.25·emo) / (1+WER).

**TL;DR.** Best reward comes WITH the LoRA at 50% — LoRA50 jumps to 0.770, well above the evolved prompt alone (BASE_P 0.596) and plain BASE (0.500). Use the evolved steering prompt plus the emotion LoRA merged at 50%, and do not go higher (LoRA100 0.672, LoRA150 0.548 with WER climbing to 0.400). Note the win is not from the target emotion itself — jealousy strength stays weak (emo 0.045) — it comes from a big surge in vocal-burst blend (0.453 to 0.629) and genuineness (0.110 to 0.173), traded against a quality dip (0.625 to 0.503). The side-effect: the LoRA drags in fatigue, longing and fear plus Shame/Teasing correlations, so the read is a bitter, weary undertone rather than sharp envy.

## Without a LoRA (base model only)
Best: **evolved prompt, no LoRA** → reward **0.60** (emotion 0.02, WER 0.13).

```
GENERAL: A voice intensely expressing jealousy and envy, a jealous, envious voice, seething with covetous resentment, bitter and possessive, in every breath.
SCRIPT:
(with jealous, envious resentment) "<your neutral sentence>"
```
(sampling: temperature 1.15, top_p 0.95, top_k 25)

## With the emotion LoRA
LoRA: `Jealousy_and_Envy` (TTS-AGI/moss-emotion-loras-v3). Best merge: **50%** → reward **0.77** (emotion 0.04).
Dose: 50% → reward 0.77 (emo 0.04) · 100% → 0.67 (emo 0.01) · 150% → 0.55 (emo 0.01).

## Conditions
| condition | reward | emotion | genu | blend | quality | WER |
|---|---|---|---|---|---|---|
| neutral prompt, no LoRA | 0.50±0.27 | 0.01 | 0.11 | 0.45 | 0.63 | 0.27 |
| evolved prompt, no LoRA | 0.60±0.33 | 0.02 | 0.14 | 0.49 | 0.56 | 0.13 |
| evolved prompt + LoRA 50% | 0.77±0.40 | 0.04 | 0.17 | 0.63 | 0.50 | 0.23 |
| evolved prompt + LoRA 100% | 0.67±0.35 | 0.01 | 0.18 | 0.56 | 0.45 | 0.22 |
| evolved prompt + LoRA 150% | 0.55±0.25 | 0.01 | 0.18 | 0.51 | 0.43 | 0.40 |

## Side effects & correlations (LoRA @ 100%)
- **Pushed up** (vs base): Fear (+1.05), Impatience and Irritability (+0.69), Embarrassment (+0.51)
- **Pushed down**: Concentration (-0.64), Mask Resonance (-0.33), Conversational Style (-0.23)
- **Positively correlated**: Shame (+0.58), Relief (+0.51), Sourness (+0.50)
- **Negatively correlated**: Interest (-0.36), Valence Shift (-0.36), Velocity Flux (-0.32)

## Conclusion
Best reward comes WITH the LoRA at 50% — LoRA50 jumps to 0.770, well above the evolved prompt alone (BASE_P 0.596) and plain BASE (0.500). Use the evolved steering prompt plus the emotion LoRA merged at 50%, and do not go higher (LoRA100 0.672, LoRA150 0.548 with WER climbing to 0.400). Note the win is not from the target emotion itself — jealousy strength stays weak (emo 0.045) — it comes from a big surge in vocal-burst blend (0.453 to 0.629) and genuineness (0.110 to 0.173), traded against a quality dip (0.625 to 0.503). The side-effect: the LoRA drags in fatigue, longing and fear plus Shame/Teasing correlations, so the read is a bitter, weary undertone rather than sharp envy.

---
[← all emotions](index.md) · [human/audio version](../../site/emotions/Jealousy_and_Envy.html)