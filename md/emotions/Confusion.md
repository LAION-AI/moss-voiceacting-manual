# Confusion — conditioning guide

*Target metric:* EmoNet **Confusion** strength (0–1). *Reward* = (genu + blend + 1.25·emo) / (1+WER).

**TL;DR.** Best reward comes with the LoRA at 50% (0.521), beating BASE_P (0.496) and BASE (0.490), while higher merges fall apart (LoRA100 0.344, LoRA150 0.372). Recommendation: use the evolved prompt plus a 50% LoRA. The gain is a genuineness lift (0.140 to 0.172) with blend held roughly steady (~0.423); the trade-off is a small quality drop (0.551 to 0.503) and higher WER (0.196 to 0.302). One caution: the evolved prompt alone tends to make confusion sound irritated rather than doubtful (BASE_P correlates positively with Anger/Teasing and negatively with Doubt at -0.51), whereas the LoRA instead pulls in Fatigue and Fear and suppresses Concentration.

## Without a LoRA (base model only)
Best: **evolved prompt, no LoRA** → reward **0.50** (emotion 0.00, WER 0.20).

```
GENERAL: A voice powerfully expressing confusion, a baffled, disoriented voice, struggling to make sense of things, hesitant and lost, pouring out.
SCRIPT:
(confused, bewildered, thrown off) "<your neutral sentence>"
```
(sampling: temperature 1.0, top_p 0.9, top_k 30)

## With the emotion LoRA
LoRA: `Confusion` (TTS-AGI/moss-emotion-loras-v3). Best merge: **50%** → reward **0.52** (emotion 0.00).
Dose: 50% → reward 0.52 (emo 0.00) · 100% → 0.34 (emo 0.00) · 150% → 0.37 (emo 0.03).

## Conditions
| condition | reward | emotion | genu | blend | quality | WER |
|---|---|---|---|---|---|---|
| neutral prompt, no LoRA | 0.49±0.27 | 0.00 | 0.11 | 0.45 | 0.63 | 0.27 |
| evolved prompt, no LoRA | 0.50±0.28 | 0.00 | 0.14 | 0.43 | 0.55 | 0.20 |
| evolved prompt + LoRA 50% | 0.52±0.37 | 0.00 | 0.17 | 0.42 | 0.50 | 0.30 |
| evolved prompt + LoRA 100% | 0.34±0.20 | 0.00 | 0.13 | 0.31 | 0.47 | 0.33 |
| evolved prompt + LoRA 150% | 0.37±0.24 | 0.03 | 0.18 | 0.30 | 0.41 | 0.50 |

## Side effects & correlations (LoRA @ 100%)
- **Pushed up** (vs base): Impatience and Irritability (+0.38), Embarrassment (+0.28), Fear (+0.25)
- **Pushed down**: Concentration (-0.28), Fullness (-0.19), Structure (-0.18)
- **Positively correlated**: Shame (+0.39), Contemplation (+0.36), Doubt (+0.35)
- **Negatively correlated**: Harmonicity (-0.49), Articulation Clarity (-0.41), Attack (-0.35)

## Conclusion
Best reward comes with the LoRA at 50% (0.521), beating BASE_P (0.496) and BASE (0.490), while higher merges fall apart (LoRA100 0.344, LoRA150 0.372). Recommendation: use the evolved prompt plus a 50% LoRA. The gain is a genuineness lift (0.140 to 0.172) with blend held roughly steady (~0.423); the trade-off is a small quality drop (0.551 to 0.503) and higher WER (0.196 to 0.302). One caution: the evolved prompt alone tends to make confusion sound irritated rather than doubtful (BASE_P correlates positively with Anger/Teasing and negatively with Doubt at -0.51), whereas the LoRA instead pulls in Fatigue and Fear and suppresses Concentration.

---
[← all emotions](index.md) · [human/audio version](../../site/emotions/Confusion.html)