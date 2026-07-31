# Fatigue Exhaustion — conditioning guide

*Target metric:* EmoNet **Fatigue_Exhaustion** strength (0–1). *Reward* = (genu + blend + 1.25·emo) / (1+WER).

**TL;DR.** Clear win WITH the LoRA at 50% — reward 0.844, far above the evolved prompt alone (0.634). This is the strongest LoRA case in the set: at 50% merge nearly every metric improves at once — emo 0.100 to 0.173, genuineness 0.159 to 0.198, blend 0.439 to 0.577, and WER even drops to 0.196. The only real trade-off is the quality proxy, which slips modestly from 0.529 to 0.475. The fatigue read pulls in a low-arousal longing/numbness color (corr Longing 0.62, Emotional Numbness 0.58, corr neg Arousal -0.72); higher merges regress (LoRA150 doubles emo to 0.29 but WER hits 0.666 and reward falls to 0.631).

## Without a LoRA (base model only)
Best: **evolved prompt, no LoRA** → reward **0.63** (emotion 0.10, WER 0.24).

```
GENERAL: A voice intensely expressing fatigue exhaustion, a weary, exhausted voice, heavy and dragging, barely able to stay awake, raw and unfiltered.
SCRIPT:
(utterly exhausted, weary and dragging) "<your neutral sentence>"
```
(sampling: temperature 1.1, top_p 0.95, top_k 25)

## With the emotion LoRA
LoRA: `Fatigue_Exhaustion` (TTS-AGI/moss-emotion-loras-v3). Best merge: **50%** → reward **0.84** (emotion 0.17).
Dose: 50% → reward 0.84 (emo 0.17) · 100% → 0.66 (emo 0.15) · 150% → 0.63 (emo 0.29).

## Conditions
| condition | reward | emotion | genu | blend | quality | WER |
|---|---|---|---|---|---|---|
| neutral prompt, no LoRA | 0.56±0.31 | 0.08 | 0.11 | 0.45 | 0.63 | 0.27 |
| evolved prompt, no LoRA | 0.63±0.41 | 0.10 | 0.16 | 0.44 | 0.53 | 0.24 |
| evolved prompt + LoRA 50% | 0.84±0.35 | 0.17 | 0.20 | 0.58 | 0.48 | 0.20 |
| evolved prompt + LoRA 100% | 0.66±0.31 | 0.15 | 0.24 | 0.39 | 0.48 | 0.34 |
| evolved prompt + LoRA 150% | 0.63±0.23 | 0.29 | 0.29 | 0.35 | 0.36 | 0.67 |

## Side effects & correlations (LoRA @ 100%)
- **Pushed up** (vs base): Emotional Numbness (+1.01), Longing (+0.48), Contemplation (+0.39)
- **Pushed down**: Mask Resonance (-0.27), Arousal Shift (-0.23), Formal Style (-0.22)
- **Positively correlated**: Disappointment (+0.57), Longing (+0.53), Helplessness (+0.52)
- **Negatively correlated**: Interest (-0.50), Articulation Clarity (-0.45), Arousal (-0.44)

## Conclusion
Clear win WITH the LoRA at 50% — reward 0.844, far above the evolved prompt alone (0.634). This is the strongest LoRA case in the set: at 50% merge nearly every metric improves at once — emo 0.100 to 0.173, genuineness 0.159 to 0.198, blend 0.439 to 0.577, and WER even drops to 0.196. The only real trade-off is the quality proxy, which slips modestly from 0.529 to 0.475. The fatigue read pulls in a low-arousal longing/numbness color (corr Longing 0.62, Emotional Numbness 0.58, corr neg Arousal -0.72); higher merges regress (LoRA150 doubles emo to 0.29 but WER hits 0.666 and reward falls to 0.631).

---
[← all emotions](index.md) · [human/audio version](../../site/emotions/Fatigue_Exhaustion.html)