# Fear — conditioning guide

*Target metric:* EmoNet **Fear** strength (0–1). *Reward* = (genu + blend + 1.25·emo) / (1+WER).

**TL;DR.** Best reward is WITH the LoRA at 50% (0.603 vs 0.527 for the evolved prompt). The 50% merge lifts the fear-adjacent signal (emo 0.040 to 0.085), genuineness (0.132 to 0.192) and blend (0.431 to 0.532), but intelligibility and quality pay for it: WER more than doubles (0.228 to 0.493) and quality drops from 0.514 to 0.387. Fear manifests mainly as distress and vulnerability with an emotional-numbness/fatigue undertone (corr Distress 0.70, shift up Emotional Numbness +0.92). Avoid 100/150% — pushing emo higher smears the voice into anger and pain (LoRA150 shift up Anger +2.4, Pain +2.4) and WER reaches 0.834.

## Without a LoRA (base model only)
Best: **evolved prompt, no LoRA** → reward **0.53** (emotion 0.04, WER 0.23).

```
GENERAL: A voice powerfully expressing fear, a terrified voice, trembling and breathless, shaking with fear, near screaming, in every breath.
SCRIPT:
(trembling, terrified, voice shaking with fear) "<your neutral sentence>"
```
(sampling: temperature 0.85, top_p 0.9, top_k 40)

## With the emotion LoRA
LoRA: `Fear` (TTS-AGI/moss-emotion-loras-v3). Best merge: **50%** → reward **0.60** (emotion 0.09).
Dose: 50% → reward 0.60 (emo 0.09) · 100% → 0.48 (emo 0.17) · 150% → 0.50 (emo 0.32).

## Conditions
| condition | reward | emotion | genu | blend | quality | WER |
|---|---|---|---|---|---|---|
| neutral prompt, no LoRA | 0.50±0.28 | 0.01 | 0.11 | 0.45 | 0.63 | 0.27 |
| evolved prompt, no LoRA | 0.53±0.33 | 0.04 | 0.13 | 0.43 | 0.51 | 0.23 |
| evolved prompt + LoRA 50% | 0.60±0.34 | 0.09 | 0.19 | 0.53 | 0.39 | 0.49 |
| evolved prompt + LoRA 100% | 0.48±0.24 | 0.17 | 0.22 | 0.39 | 0.25 | 0.86 |
| evolved prompt + LoRA 150% | 0.50±0.24 | 0.32 | 0.19 | 0.28 | 0.18 | 0.83 |

## Side effects & correlations (LoRA @ 100%)
- **Pushed up** (vs base): Pain (+1.25), Distress (+1.23), Helplessness (+1.08)
- **Pushed down**: Concentration (-0.65), Warmth (-0.48), Recording Quality (-0.43)
- **Positively correlated**: Distress (+0.85), Helplessness (+0.72), Malevolence Malice (+0.72)
- **Negatively correlated**: Mixed Resonance (-0.59), Interest (-0.55), Fullness (-0.52)

## Conclusion
Best reward is WITH the LoRA at 50% (0.603 vs 0.527 for the evolved prompt). The 50% merge lifts the fear-adjacent signal (emo 0.040 to 0.085), genuineness (0.132 to 0.192) and blend (0.431 to 0.532), but intelligibility and quality pay for it: WER more than doubles (0.228 to 0.493) and quality drops from 0.514 to 0.387. Fear manifests mainly as distress and vulnerability with an emotional-numbness/fatigue undertone (corr Distress 0.70, shift up Emotional Numbness +0.92). Avoid 100/150% — pushing emo higher smears the voice into anger and pain (LoRA150 shift up Anger +2.4, Pain +2.4) and WER reaches 0.834.

**Contained / masked delivery** (forced-calm surface with terror alive underneath): keep the LoRA strong and add a thin masking layer — `Fear@1.02 + vn_VULN_low@0.16 + Emotional_Numbness@0.12 + vn_TENS_high@0.1` (measured contained−free gap: emotion +0.10 to +0.30, **VULN −0.42 to −0.55**). See the [contained / masked emotion chapter](../recipes/contained_emotion.md).

---
[← all emotions](index.md) · [human/audio version](../../site/emotions/Fear.html)