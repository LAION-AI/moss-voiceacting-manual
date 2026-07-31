# Elation — conditioning guide

*Target metric:* EmoNet **Elation** strength (0–1). *Reward* = (genu + blend + 1.25·emo) / (1+WER).

**TL;DR.** Best reward comes with the LoRA at 50% (0.561, above the evolved prompt's 0.520 and BASE's 0.491), so combine the evolved prompt with a 50% merge. Note it wins by improving delivery, not by raising the emotion — target-emo strength stays near zero (0.002) while WER drops to 0.162 and blend holds at 0.443; quality dips slightly (0.518 to 0.465). The side-effect is a high-energy, triumphant/prideful color — LoRA50 correlates with Triumph (0.93), Pain (0.94) and Pride (0.83). Keep it at 50%: at 100/150% the read degenerates into Impatient, ranting energy and reward collapses to ~0.32-0.36.

## Without a LoRA (base model only)
Best: **evolved prompt, no LoRA** → reward **0.52** (emotion 0.00, WER 0.26).

```
GENERAL: A voice utterly expressing elation, a soaring, jubilant voice, elated and euphoric, bursting with joy, in every breath.
SCRIPT:
(elated, euphoric, bursting with joy) "<your neutral sentence>"
```
(sampling: temperature 1.05, top_p 0.9, top_k 25)

## With the emotion LoRA
LoRA: `Elation` (TTS-AGI/moss-emotion-loras-v3). Best merge: **50%** → reward **0.56** (emotion 0.00).
Dose: 50% → reward 0.56 (emo 0.00) · 100% → 0.32 (emo 0.03) · 150% → 0.36 (emo 0.06).

## Conditions
| condition | reward | emotion | genu | blend | quality | WER |
|---|---|---|---|---|---|---|
| neutral prompt, no LoRA | 0.49±0.27 | 0.00 | 0.11 | 0.45 | 0.63 | 0.27 |
| evolved prompt, no LoRA | 0.52±0.35 | 0.00 | 0.14 | 0.45 | 0.52 | 0.26 |
| evolved prompt + LoRA 50% | 0.56±0.33 | 0.00 | 0.15 | 0.44 | 0.47 | 0.16 |
| evolved prompt + LoRA 100% | 0.32±0.23 | 0.03 | 0.12 | 0.27 | 0.40 | 0.41 |
| evolved prompt + LoRA 150% | 0.36±0.23 | 0.06 | 0.14 | 0.24 | 0.38 | 0.57 |

## Side effects & correlations (LoRA @ 100%)
- **Pushed up** (vs base): Emotional Numbness (+0.58), Impatience and Irritability (+0.55), Hope Enthusiasm Optimism (+0.32)
- **Pushed down**: Concentration (-0.61), Warmth (-0.29), Recording Quality (-0.26)
- **Positively correlated**: Content Appropriateness (3-point Scale) (+0.76), Ranting/Angry Style (+0.74), Casual Style (+0.63)
- **Negatively correlated**: Monologue Style (-0.73), Newsreader Style (-0.43), Formal Style (-0.42)

## Conclusion
Best reward comes with the LoRA at 50% (0.561, above the evolved prompt's 0.520 and BASE's 0.491), so combine the evolved prompt with a 50% merge. Note it wins by improving delivery, not by raising the emotion — target-emo strength stays near zero (0.002) while WER drops to 0.162 and blend holds at 0.443; quality dips slightly (0.518 to 0.465). The side-effect is a high-energy, triumphant/prideful color — LoRA50 correlates with Triumph (0.93), Pain (0.94) and Pride (0.83). Keep it at 50%: at 100/150% the read degenerates into Impatient, ranting energy and reward collapses to ~0.32-0.36.

---
[← all emotions](index.md) · [human/audio version](../../site/emotions/Elation.html)