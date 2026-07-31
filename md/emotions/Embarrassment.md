# Embarrassment — conditioning guide

*Target metric:* EmoNet **Embarrassment** strength (0–1). *Reward* = (genu + blend + 1.25·emo) / (1+WER).

**TL;DR.** Best reward comes WITH the LoRA at 50% (0.582 vs 0.498 for the plain BASE prompt, which is the best no-LoRA option here). Use the evolved steering prompt plus the 50% merge: the target-emotion signal stays weak (emo 0.026 — embarrassment resists direct elicitation), so the gain is actually driven by genuineness rising (0.110 to 0.161) and WER dropping sharply (0.269 to 0.112) while blend holds at 0.45. The trade-off is the speech-quality proxy, which falls from 0.625 to 0.475. Watch that the LoRA drags delivery toward a tired/sad register (shift up Fatigue +0.62, corr with Sadness 0.73 and Helplessness 0.71); don't exceed 50%, as LoRA100/150 both lose reward.

## Without a LoRA (base model only)
Best: **neutral prompt, no LoRA** → reward **0.50** (emotion 0.01, WER 0.27).

```
GENERAL: A voice unmistakably expressing embarrassment, a flustered, sheepish voice, cheeks burning with embarrassment, awkward and shrinking, impossible to hide.
SCRIPT:
(flustered and mortified with embarrassment) "<your neutral sentence>"
```
(sampling: temperature 1.05, top_p 0.9, top_k 30)

## With the emotion LoRA
LoRA: `Embarrassment` (TTS-AGI/moss-emotion-loras-v3). Best merge: **50%** → reward **0.58** (emotion 0.03).
Dose: 50% → reward 0.58 (emo 0.03) · 100% → 0.44 (emo 0.03) · 150% → 0.46 (emo 0.06).

## Conditions
| condition | reward | emotion | genu | blend | quality | WER |
|---|---|---|---|---|---|---|
| neutral prompt, no LoRA | 0.50±0.28 | 0.01 | 0.11 | 0.45 | 0.63 | 0.27 |
| evolved prompt, no LoRA | 0.49±0.31 | 0.02 | 0.12 | 0.42 | 0.56 | 0.25 |
| evolved prompt + LoRA 50% | 0.58±0.32 | 0.03 | 0.16 | 0.45 | 0.47 | 0.11 |
| evolved prompt + LoRA 100% | 0.44±0.27 | 0.03 | 0.11 | 0.34 | 0.50 | 0.17 |
| evolved prompt + LoRA 150% | 0.46±0.21 | 0.06 | 0.13 | 0.34 | 0.41 | 0.23 |

## Side effects & correlations (LoRA @ 100%)
- **Pushed up** (vs base): Impatience and Irritability (+0.46), Fear (+0.38), Fatigue Exhaustion (+0.27)
- **Pushed down**: Concentration (-0.49), Emotional Numbness (-0.26), Fullness (-0.23)
- **Positively correlated**: Amusement (+0.46), Pain (+0.44), Helplessness (+0.43)
- **Negatively correlated**: Velocity Flux (-0.45), Narrator Style (-0.43), Emphasis (-0.37)

## Conclusion
Best reward comes WITH the LoRA at 50% (0.582 vs 0.498 for the plain BASE prompt, which is the best no-LoRA option here). Use the evolved steering prompt plus the 50% merge: the target-emotion signal stays weak (emo 0.026 — embarrassment resists direct elicitation), so the gain is actually driven by genuineness rising (0.110 to 0.161) and WER dropping sharply (0.269 to 0.112) while blend holds at 0.45. The trade-off is the speech-quality proxy, which falls from 0.625 to 0.475. Watch that the LoRA drags delivery toward a tired/sad register (shift up Fatigue +0.62, corr with Sadness 0.73 and Helplessness 0.71); don't exceed 50%, as LoRA100/150 both lose reward.

---
[← all emotions](index.md) · [human/audio version](../../site/emotions/Embarrassment.html)