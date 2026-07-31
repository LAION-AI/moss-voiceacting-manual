# Doubt — conditioning guide

*Target metric:* EmoNet **Doubt** strength (0–1). *Reward* = (genu + blend + 1.25·emo) / (1+WER).

**TL;DR.** Best reward comes without any LoRA and without heavy steering, plain BASE wins (0.495), with the evolved prompt just behind (0.473) and every LoRA strictly worse (0.436 to 0.324 to 0.269). The LoRA cannot move the target emotion at all (stays ~0.005) and simply degrades everything as the merge rises — WER balloons from 0.169 to 0.711. Its notable failure mode is drift: at 150% doubt collapses into Sourness, Contempt and Teasing (correlations ~0.92) rather than sounding uncertain. Skip the LoRA entirely; a light prompt is fine, but doubt is best conveyed through tension/hesitation cues (BASE_P correlates with Arousal, Stance and Tension) rather than any emotion-boosting merge.

## Without a LoRA (base model only)
Best: **neutral prompt, no LoRA** → reward **0.50** (emotion 0.01, WER 0.27).

```
GENERAL: A voice powerfully expressing doubt, a skeptical, uncertain voice, hedging and unconvinced, full of doubt, pouring out.
SCRIPT:
(doubtfully, deeply unconvinced) "<your neutral sentence>"
```
(sampling: temperature 1.15, top_p 0.9, top_k 25)

## With the emotion LoRA
LoRA: `Doubt` (TTS-AGI/moss-emotion-loras-v3). Best merge: **50%** → reward **0.44** (emotion 0.01).
Dose: 50% → reward 0.44 (emo 0.01) · 100% → 0.32 (emo 0.00) · 150% → 0.27 (emo 0.00).

## Conditions
| condition | reward | emotion | genu | blend | quality | WER |
|---|---|---|---|---|---|---|
| neutral prompt, no LoRA | 0.50±0.27 | 0.01 | 0.11 | 0.45 | 0.63 | 0.27 |
| evolved prompt, no LoRA | 0.47±0.26 | 0.00 | 0.13 | 0.43 | 0.58 | 0.24 |
| evolved prompt + LoRA 50% | 0.44±0.30 | 0.01 | 0.11 | 0.37 | 0.56 | 0.17 |
| evolved prompt + LoRA 100% | 0.32±0.20 | 0.00 | 0.12 | 0.29 | 0.52 | 0.42 |
| evolved prompt + LoRA 150% | 0.27±0.15 | 0.00 | 0.17 | 0.27 | 0.46 | 0.71 |

## Side effects & correlations (LoRA @ 100%)
- **Pushed up** (vs base): Emotional Numbness (+0.26), Fear (+0.25), Fatigue Exhaustion (+0.23)
- **Pushed down**: Contentment (-0.17), Vocal-burst blend (-0.17), Interest (-0.16)
- **Positively correlated**: Infatuation (+0.97), Affection (+0.93), Relief (+0.75)
- **Negatively correlated**: Velocity Flux (-0.55), Formal Style (-0.39), Chest Resonance (-0.39)

## Conclusion
Best reward comes without any LoRA and without heavy steering, plain BASE wins (0.495), with the evolved prompt just behind (0.473) and every LoRA strictly worse (0.436 to 0.324 to 0.269). The LoRA cannot move the target emotion at all (stays ~0.005) and simply degrades everything as the merge rises — WER balloons from 0.169 to 0.711. Its notable failure mode is drift: at 150% doubt collapses into Sourness, Contempt and Teasing (correlations ~0.92) rather than sounding uncertain. Skip the LoRA entirely; a light prompt is fine, but doubt is best conveyed through tension/hesitation cues (BASE_P correlates with Arousal, Stance and Tension) rather than any emotion-boosting merge.

---
[← all emotions](index.md) · [human/audio version](../../site/emotions/Doubt.html)