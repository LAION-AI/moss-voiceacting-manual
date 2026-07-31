# Impatience and Irritability — conditioning guide

*Target metric:* EmoNet **Impatience_and_Irritability** strength (0–1). *Reward* = (genu + blend + 1.25·emo) / (1+WER).

**TL;DR.** Best reward is WITHOUT any LoRA — the plain BASE prompt wins at 0.543, with the evolved prompt essentially tied (0.539); the baseline already carries meaningful irritability (emo 0.058). Every LoRA merge only costs reward, decreasing monotonically (LoRA50 0.466 to LoRA150 0.421). The LoRAs do crank the target hard (LoRA150 emo 0.279, shift up Anger +2.1, Triumph +1.9), but blend collapses (0.453 to 0.193), quality tanks to 0.282 and WER hits 0.767. If you genuinely need overt anger-tinged irritation, use LoRA50 (emo 0.098, WER still low at 0.200) and accept the blend/quality hit; otherwise stay at BASE.

## Without a LoRA (base model only)
Best: **neutral prompt, no LoRA** → reward **0.54** (emotion 0.06, WER 0.27).

```
GENERAL: A voice utterly expressing impatience and irritability, a tense, irritable voice, snapping with impatience, on a short fuse, pouring out.
SCRIPT:
(impatiently, irritable and snappy) "<your neutral sentence>"
```
(sampling: temperature 1.0, top_p 0.9, top_k 25)

## With the emotion LoRA
LoRA: `Impatience_and_Irritability` (TTS-AGI/moss-emotion-loras-v3). Best merge: **50%** → reward **0.47** (emotion 0.10).
Dose: 50% → reward 0.47 (emo 0.10) · 100% → 0.45 (emo 0.17) · 150% → 0.42 (emo 0.28).

## Conditions
| condition | reward | emotion | genu | blend | quality | WER |
|---|---|---|---|---|---|---|
| neutral prompt, no LoRA | 0.54±0.31 | 0.06 | 0.11 | 0.45 | 0.63 | 0.27 |
| evolved prompt, no LoRA | 0.54±0.46 | 0.06 | 0.12 | 0.39 | 0.58 | 0.25 |
| evolved prompt + LoRA 50% | 0.47±0.28 | 0.10 | 0.12 | 0.29 | 0.52 | 0.20 |
| evolved prompt + LoRA 100% | 0.45±0.25 | 0.17 | 0.12 | 0.27 | 0.43 | 0.45 |
| evolved prompt + LoRA 150% | 0.42±0.19 | 0.28 | 0.15 | 0.19 | 0.28 | 0.77 |

## Side effects & correlations (LoRA @ 100%)
- **Pushed up** (vs base): Anger (+0.57), Triumph (+0.51), Pride (+0.40)
- **Pushed down**: Concentration (-0.55), Warmth (-0.31), Monologue Style (-0.25)
- **Positively correlated**: Arousal Shift (+0.58), Content Appropriateness (3-point Scale) (+0.57), Chunking (+0.55)
- **Negatively correlated**: Contemplation (-0.33), Throat Resonance (-0.31), Concentration (-0.31)

## Conclusion
Best reward is WITHOUT any LoRA — the plain BASE prompt wins at 0.543, with the evolved prompt essentially tied (0.539); the baseline already carries meaningful irritability (emo 0.058). Every LoRA merge only costs reward, decreasing monotonically (LoRA50 0.466 to LoRA150 0.421). The LoRAs do crank the target hard (LoRA150 emo 0.279, shift up Anger +2.1, Triumph +1.9), but blend collapses (0.453 to 0.193), quality tanks to 0.282 and WER hits 0.767. If you genuinely need overt anger-tinged irritation, use LoRA50 (emo 0.098, WER still low at 0.200) and accept the blend/quality hit; otherwise stay at BASE.

---
[← all emotions](index.md) · [human/audio version](../../site/emotions/Impatience_and_Irritability.html)