# Longing — conditioning guide

*Target metric:* EmoNet **Longing** strength (0–1). *Reward* = (genu + blend + 1.25·emo) / (1+WER).

**TL;DR.** Best reward comes WITH the LoRA at 50% (LoRA50 0.589, vs BASE_P 0.525 and BASE 0.505); higher merges backfire (LoRA100 drops to 0.413). Prompt with the evolved steering text and merge the LoRA at 50% — this lifts target emo modestly (0.016 to 0.060), raises genuineness (0.110 to 0.173) and roughly holds blend (0.469). The trade-off is intelligibility: WER rises from 0.193 (BASE_P) to 0.336, and quality slips to 0.522. The most notable coloring is that longing reads as tender and sorrowful — LoRA50 shifts up Emotional Numbness and Fatigue and correlates ~0.87 with Affection, Distress and Helplessness, so expect a wistful, near-grieving tone rather than hopeful yearning.

## Without a LoRA (base model only)
Best: **evolved prompt, no LoRA** → reward **0.53** (emotion 0.03, WER 0.19).

```
GENERAL: A voice unmistakably expressing longing, an aching, yearning voice, full of wistful longing, reaching for what is out of reach, with every word.
SCRIPT:
(with aching, wistful longing) "<your neutral sentence>"
```
(sampling: temperature 1.05, top_p 0.9, top_k 25)

## With the emotion LoRA
LoRA: `Longing` (TTS-AGI/moss-emotion-loras-v3). Best merge: **50%** → reward **0.59** (emotion 0.06).
Dose: 50% → reward 0.59 (emo 0.06) · 100% → 0.41 (emo 0.07) · 150% → 0.50 (emo 0.10).

## Conditions
| condition | reward | emotion | genu | blend | quality | WER |
|---|---|---|---|---|---|---|
| neutral prompt, no LoRA | 0.51±0.29 | 0.02 | 0.11 | 0.45 | 0.63 | 0.27 |
| evolved prompt, no LoRA | 0.53±0.37 | 0.03 | 0.14 | 0.41 | 0.55 | 0.19 |
| evolved prompt + LoRA 50% | 0.59±0.40 | 0.06 | 0.17 | 0.47 | 0.52 | 0.34 |
| evolved prompt + LoRA 100% | 0.41±0.26 | 0.07 | 0.13 | 0.34 | 0.53 | 0.49 |
| evolved prompt + LoRA 150% | 0.50±0.24 | 0.10 | 0.18 | 0.37 | 0.46 | 0.41 |

## Side effects & correlations (LoRA @ 100%)
- **Pushed up** (vs base): Emotional Numbness (+1.45), Concentration (+0.33), Contemplation (+0.31)
- **Pushed down**: Interest (-0.25), Mask Resonance (-0.18), Conversational Style (-0.17)
- **Positively correlated**: Helplessness (+0.92), Sadness (+0.86), Disappointment (+0.86)
- **Negatively correlated**: Astonishment Surprise (-0.61), Mixed Resonance (-0.61), Articulation Clarity (-0.60)

## Conclusion
Best reward comes WITH the LoRA at 50% (LoRA50 0.589, vs BASE_P 0.525 and BASE 0.505); higher merges backfire (LoRA100 drops to 0.413). Prompt with the evolved steering text and merge the LoRA at 50% — this lifts target emo modestly (0.016 to 0.060), raises genuineness (0.110 to 0.173) and roughly holds blend (0.469). The trade-off is intelligibility: WER rises from 0.193 (BASE_P) to 0.336, and quality slips to 0.522. The most notable coloring is that longing reads as tender and sorrowful — LoRA50 shifts up Emotional Numbness and Fatigue and correlates ~0.87 with Affection, Distress and Helplessness, so expect a wistful, near-grieving tone rather than hopeful yearning.

---
[← all emotions](index.md) · [human/audio version](../../site/emotions/Longing.html)