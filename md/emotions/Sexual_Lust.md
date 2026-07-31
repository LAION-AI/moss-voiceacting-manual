# Sexual Lust — conditioning guide

*Target metric:* EmoNet **Sexual_Lust** strength (0–1). *Reward* = (genu + blend + 1.25·emo) / (1+WER).

**TL;DR.** Best with the LoRA at 50%, and by a wide margin — reward 0.775 vs 0.521 prompt-only and 0.671/0.598 at higher merges. Run the evolved prompt + 50% merge; it nearly doubles reward mainly by boosting vocal-burst blend (0.430 to 0.635) at low WER cost (0.214). The trade-off is speech quality/clarity: qual dips 0.565 to 0.498 and Articulation Clarity correlates strongly negative (-0.46), so delivery turns breathy and less crisp. The emo strength stays modest (0.071) — this LoRA sells the emotion through breathy vocalizations, not lexical arousal — so don't push to 150% (emo rises to 0.18 but reward drops and WER hits 0.52).

## Without a LoRA (base model only)
Best: **evolved prompt, no LoRA** → reward **0.52** (emotion 0.01, WER 0.19).

```
GENERAL: A voice unmistakably expressing sexual lust, a husky, sultry voice, low and breathy, thick with desire and longing, pouring out.
SCRIPT:
(huskily, low and breathy with desire) "<your neutral sentence>"
```
(sampling: temperature 1.0, top_p 0.95, top_k 25)

## With the emotion LoRA
LoRA: `Sexual_Lust` (TTS-AGI/moss-emotion-loras-v3). Best merge: **50%** → reward **0.78** (emotion 0.07).
Dose: 50% → reward 0.78 (emo 0.07) · 100% → 0.60 (emo 0.10) · 150% → 0.67 (emo 0.18).

## Conditions
| condition | reward | emotion | genu | blend | quality | WER |
|---|---|---|---|---|---|---|
| neutral prompt, no LoRA | 0.49±0.28 | -0.00 | 0.11 | 0.45 | 0.63 | 0.27 |
| evolved prompt, no LoRA | 0.52±0.38 | 0.01 | 0.14 | 0.43 | 0.57 | 0.19 |
| evolved prompt + LoRA 50% | 0.78±0.37 | 0.07 | 0.17 | 0.63 | 0.50 | 0.21 |
| evolved prompt + LoRA 100% | 0.60±0.36 | 0.10 | 0.14 | 0.44 | 0.50 | 0.35 |
| evolved prompt + LoRA 150% | 0.67±0.33 | 0.18 | 0.19 | 0.50 | 0.46 | 0.52 |

## Side effects & correlations (LoRA @ 100%)
- **Pushed up** (vs base): Emotional Numbness (+0.87), Malevolence Malice (+0.66), Intoxication Altered States of Consciousness (+0.56)
- **Pushed down**: Mask Resonance (-0.38), Articulation Clarity (-0.29), Conversational Style (-0.28)
- **Positively correlated**: Infatuation (+0.62), Malevolence Malice (+0.58), Pleasure Ecstasy (+0.54)
- **Negatively correlated**: Oral Resonance (-0.59), Articulation Clarity (-0.58), Background Noise (-0.53)

## Conclusion
Best with the LoRA at 50%, and by a wide margin — reward 0.775 vs 0.521 prompt-only and 0.671/0.598 at higher merges. Run the evolved prompt + 50% merge; it nearly doubles reward mainly by boosting vocal-burst blend (0.430 to 0.635) at low WER cost (0.214). The trade-off is speech quality/clarity: qual dips 0.565 to 0.498 and Articulation Clarity correlates strongly negative (-0.46), so delivery turns breathy and less crisp. The emo strength stays modest (0.071) — this LoRA sells the emotion through breathy vocalizations, not lexical arousal — so don't push to 150% (emo rises to 0.18 but reward drops and WER hits 0.52).

---
[← all emotions](index.md) · [human/audio version](../../site/emotions/Sexual_Lust.html)