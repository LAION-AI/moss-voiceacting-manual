# Disappointment — conditioning guide

*Target metric:* EmoNet **Disappointment** strength (0–1). *Reward* = (genu + blend + 1.25·emo) / (1+WER).

**TL;DR.** Best reward is without a LoRA, use the evolved steering prompt (BASE_P 0.581, well above BASE 0.489 and every LoRA); LoRA150 is merely the best of the LoRAs (0.478), not the best overall. The LoRA is a genuine intensity dial, target emotion climbs 0.021 to 0.093 and genuineness 0.161 to 0.228, but blend collapses (0.450 to 0.281) and quality craters (0.534 to 0.331), which is why reward never catches the prompt. The key side-effect is that it drags in full-blown Sadness, Distress and Helplessness (all correlating ~0.85), so disappointment tips over into outright grief. Default to the prompt; only reach for LoRA150 when you specifically need audibly stronger, more genuine emotion and can accept the blend/quality loss.

## Without a LoRA (base model only)
Best: **evolved prompt, no LoRA** → reward **0.58** (emotion 0.02, WER 0.20).

```
GENERAL: A voice viscerally expressing disappointment, a deflated, let-down voice, heavy with disappointment, quietly crushed, in every breath.
SCRIPT:
(deeply disappointed, deflated) "<your neutral sentence>"
```
(sampling: temperature 1.1, top_p 0.9, top_k 40)

## With the emotion LoRA
LoRA: `Disappointment` (TTS-AGI/moss-emotion-loras-v3). Best merge: **150%** → reward **0.48** (emotion 0.09).
Dose: 50% → reward 0.46 (emo 0.02) · 100% → 0.45 (emo 0.07) · 150% → 0.48 (emo 0.09).

## Conditions
| condition | reward | emotion | genu | blend | quality | WER |
|---|---|---|---|---|---|---|
| neutral prompt, no LoRA | 0.49±0.27 | 0.00 | 0.11 | 0.45 | 0.63 | 0.27 |
| evolved prompt, no LoRA | 0.58±0.36 | 0.02 | 0.16 | 0.45 | 0.53 | 0.20 |
| evolved prompt + LoRA 50% | 0.46±0.33 | 0.02 | 0.16 | 0.42 | 0.51 | 0.43 |
| evolved prompt + LoRA 100% | 0.45±0.29 | 0.07 | 0.19 | 0.36 | 0.43 | 0.57 |
| evolved prompt + LoRA 150% | 0.48±0.25 | 0.09 | 0.23 | 0.28 | 0.33 | 0.43 |

## Side effects & correlations (LoRA @ 100%)
- **Pushed up** (vs base): Sadness (+0.60), Helplessness (+0.60), Distress (+0.60)
- **Pushed down**: Warmth (-0.30), Recording Quality (-0.28), Fullness (-0.28)
- **Positively correlated**: Sadness (+0.88), Bitterness (+0.84), Distress (+0.83)
- **Negatively correlated**: Interest (-0.66), Esthetics (-0.59), Structure (-0.53)

## Conclusion
Best reward is without a LoRA, use the evolved steering prompt (BASE_P 0.581, well above BASE 0.489 and every LoRA); LoRA150 is merely the best of the LoRAs (0.478), not the best overall. The LoRA is a genuine intensity dial, target emotion climbs 0.021 to 0.093 and genuineness 0.161 to 0.228, but blend collapses (0.450 to 0.281) and quality craters (0.534 to 0.331), which is why reward never catches the prompt. The key side-effect is that it drags in full-blown Sadness, Distress and Helplessness (all correlating ~0.85), so disappointment tips over into outright grief. Default to the prompt; only reach for LoRA150 when you specifically need audibly stronger, more genuine emotion and can accept the blend/quality loss.

---
[← all emotions](index.md) · [human/audio version](../../site/emotions/Disappointment.html)