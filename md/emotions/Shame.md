# Shame — conditioning guide

*Target metric:* EmoNet **Shame** strength (0–1). *Reward* = (genu + blend + 1.25·emo) / (1+WER).

**TL;DR.** Best without the LoRA — the evolved prompt (BASE_P) leads at reward 0.553 with an excellent WER of 0.077, while every merge is worse (LoRA50 0.483, down to 0.371 at 150%). Prompt-steer only: shame never registers as a distinct emotion here (target emo stays ~0.009 in all conditions), so the LoRA buys no emotion but costs blend and intelligibility (WER 0.077 to 0.373 at 50%). Practically, shame surfaces as sadness — BASE_P correlates with Pain (0.999), Sadness (0.978) and Disappointment (0.95) — so write it as quiet, downcast lines.

## Without a LoRA (base model only)
Best: **evolved prompt, no LoRA** → reward **0.55** (emotion 0.01, WER 0.08).

```
GENERAL: A voice deeply expressing shame, a small, shame-filled voice, cringing and self-reproaching, unable to look up, building and building.
SCRIPT:
(with cringing shame and self-reproach) "<your neutral sentence>"
```
(sampling: temperature 0.9, top_p 0.95, top_k 25)

## With the emotion LoRA
LoRA: `Shame` (TTS-AGI/moss-emotion-loras-v3). Best merge: **50%** → reward **0.48** (emotion 0.00).
Dose: 50% → reward 0.48 (emo 0.00) · 100% → 0.38 (emo 0.00) · 150% → 0.37 (emo 0.00).

## Conditions
| condition | reward | emotion | genu | blend | quality | WER |
|---|---|---|---|---|---|---|
| neutral prompt, no LoRA | 0.49±0.27 | 0.00 | 0.11 | 0.45 | 0.63 | 0.27 |
| evolved prompt, no LoRA | 0.55±0.33 | 0.01 | 0.14 | 0.43 | 0.55 | 0.08 |
| evolved prompt + LoRA 50% | 0.48±0.30 | 0.00 | 0.21 | 0.40 | 0.48 | 0.37 |
| evolved prompt + LoRA 100% | 0.38±0.25 | 0.00 | 0.22 | 0.31 | 0.54 | 0.52 |
| evolved prompt + LoRA 150% | 0.37±0.27 | 0.00 | 0.17 | 0.32 | 0.50 | 0.54 |

## Side effects & correlations (LoRA @ 100%)
- **Pushed up** (vs base): Emotional Numbness (+0.29), ASMR Style (+0.14), Disfluency (+0.11)
- **Pushed down**: Perceived Gender (-0.21), Fullness (-0.17), Dramatic Style (-0.15)
- **Positively correlated**: Pain (+0.97), Distress (+0.56), Contemplation (+0.53)
- **Negatively correlated**: Tension (-0.38), Authoritative Style (-0.37), Attack (-0.36)

## Conclusion
Best without the LoRA — the evolved prompt (BASE_P) leads at reward 0.553 with an excellent WER of 0.077, while every merge is worse (LoRA50 0.483, down to 0.371 at 150%). Prompt-steer only: shame never registers as a distinct emotion here (target emo stays ~0.009 in all conditions), so the LoRA buys no emotion but costs blend and intelligibility (WER 0.077 to 0.373 at 50%). Practically, shame surfaces as sadness — BASE_P correlates with Pain (0.999), Sadness (0.978) and Disappointment (0.95) — so write it as quiet, downcast lines.

---
[← all emotions](index.md) · [human/audio version](../../site/emotions/Shame.html)