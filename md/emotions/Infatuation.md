# Infatuation — conditioning guide

*Target metric:* EmoNet **Infatuation** strength (0–1). *Reward* = (genu + blend + 1.25·emo) / (1+WER).

**TL;DR.** Best reward is WITH the LoRA at 50% (0.616 vs 0.488 for BASE). Note the infatuation target dimension stays essentially zero in every condition (emo ~0.01 — the model cannot score direct infatuation), so the reward win comes entirely from richer vocal-burst blend (0.453 to 0.540), higher genuineness (0.110 to 0.150) and lower WER (0.269 to 0.198), not from any measured emotion. The LoRA colors delivery toward a sexual-lust/longing register (corr Sexual Lust 0.81, Longing 0.51). The trade-off is a quality dip (0.625 to 0.515); higher merges (100/150%) keep the blend but add no emotion and lose reward.

## Without a LoRA (base model only)
Best: **neutral prompt, no LoRA** → reward **0.49** (emotion -0.00, WER 0.27).

```
GENERAL: A voice to the extreme expressing infatuation, a dreamy, smitten voice, lovestruck and breathless with infatuation, impossible to hide.
SCRIPT:
(dreamily infatuated, lovestruck) "<your neutral sentence>"
```
(sampling: temperature 1.1, top_p 0.95, top_k 40)

## With the emotion LoRA
LoRA: `Infatuation` (TTS-AGI/moss-emotion-loras-v3). Best merge: **50%** → reward **0.62** (emotion 0.01).
Dose: 50% → reward 0.62 (emo 0.01) · 100% → 0.55 (emo -0.00) · 150% → 0.53 (emo 0.02).

## Conditions
| condition | reward | emotion | genu | blend | quality | WER |
|---|---|---|---|---|---|---|
| neutral prompt, no LoRA | 0.49±0.27 | -0.00 | 0.11 | 0.45 | 0.63 | 0.27 |
| evolved prompt, no LoRA | 0.45±0.25 | 0.00 | 0.13 | 0.41 | 0.56 | 0.30 |
| evolved prompt + LoRA 50% | 0.62±0.34 | 0.01 | 0.15 | 0.54 | 0.51 | 0.20 |
| evolved prompt + LoRA 100% | 0.55±0.25 | -0.00 | 0.13 | 0.56 | 0.58 | 0.33 |
| evolved prompt + LoRA 150% | 0.53±0.22 | 0.02 | 0.16 | 0.51 | 0.55 | 0.39 |

## Side effects & correlations (LoRA @ 100%)
- **Pushed up** (vs base): Emotional Numbness (+0.44), Sexual Lust (+0.32), Cartoonish Style (+0.23)
- **Pushed down**: Mask Resonance (-0.34), Conversational Style (-0.26), Brightness (-0.19)
- **Positively correlated**: Respiration (+0.41), Ranting/Angry Style (+0.33), Contempt (+0.33)
- **Negatively correlated**: Embarrassment (-0.26), Smoothness (-0.22), Formal Style (-0.20)

## Conclusion
Best reward is WITH the LoRA at 50% (0.616 vs 0.488 for BASE). Note the infatuation target dimension stays essentially zero in every condition (emo ~0.01 — the model cannot score direct infatuation), so the reward win comes entirely from richer vocal-burst blend (0.453 to 0.540), higher genuineness (0.110 to 0.150) and lower WER (0.269 to 0.198), not from any measured emotion. The LoRA colors delivery toward a sexual-lust/longing register (corr Sexual Lust 0.81, Longing 0.51). The trade-off is a quality dip (0.625 to 0.515); higher merges (100/150%) keep the blend but add no emotion and lose reward.

---
[← all emotions](index.md) · [human/audio version](../../site/emotions/Infatuation.html)