# Sadness — conditioning guide

*Target metric:* EmoNet **Sadness** strength (0–1). *Reward* = (genu + blend + 1.25·emo) / (1+WER).

**TL;DR.** Best with the LoRA at 100% (reward 0.629, just above the prompt-only 0.604). Use the evolved prompt plus the 100% merge when you need genuine sadness — it pushes target-emotion strength from 0.007 to 0.152 and genuineness to 0.238. The cost is steep on intelligibility and quality: WER jumps 0.146 to 0.515 and the quality proxy falls 0.546 to 0.348, so keep lines short. It also drags in Distress and Helplessness (both corr ~0.93), so the voice sounds despairing rather than merely melancholy; if you need clean, intelligible sadness, prompt-only BASE_P (WER 0.146) is nearly as rewarding.

## Without a LoRA (base model only)
Best: **evolved prompt, no LoRA** → reward **0.60** (emotion 0.01, WER 0.15).

```
GENERAL: A voice powerfully expressing sadness, a soft, grief-worn voice, heavy and slow, on the edge of tears, impossible to hide.
SCRIPT:
(quietly, grief-stricken, near tears) "<your neutral sentence>"
```
(sampling: temperature 1.0, top_p 0.95, top_k 40)

## With the emotion LoRA
LoRA: `Sadness` (TTS-AGI/moss-emotion-loras-v3). Best merge: **100%** → reward **0.63** (emotion 0.15).
Dose: 50% → reward 0.57 (emo 0.06) · 100% → 0.63 (emo 0.15) · 150% → 0.58 (emo 0.23).

## Conditions
| condition | reward | emotion | genu | blend | quality | WER |
|---|---|---|---|---|---|---|
| neutral prompt, no LoRA | 0.49±0.27 | 0.00 | 0.11 | 0.45 | 0.63 | 0.27 |
| evolved prompt, no LoRA | 0.60±0.33 | 0.01 | 0.16 | 0.49 | 0.55 | 0.15 |
| evolved prompt + LoRA 50% | 0.57±0.30 | 0.06 | 0.20 | 0.51 | 0.45 | 0.42 |
| evolved prompt + LoRA 100% | 0.63±0.33 | 0.15 | 0.24 | 0.43 | 0.35 | 0.52 |
| evolved prompt + LoRA 150% | 0.58±0.26 | 0.23 | 0.23 | 0.36 | 0.23 | 0.62 |

## Side effects & correlations (LoRA @ 100%)
- **Pushed up** (vs base): Distress (+0.80), Helplessness (+0.77), Longing (+0.73)
- **Pushed down**: Structure (-0.35), Formal Style (-0.34), Mask Resonance (-0.33)
- **Positively correlated**: Distress (+0.93), Helplessness (+0.93), Disappointment (+0.89)
- **Negatively correlated**: Formal Style (-0.61), Articulation Clarity (-0.57), Structure (-0.57)

## Conclusion
Best with the LoRA at 100% (reward 0.629, just above the prompt-only 0.604). Use the evolved prompt plus the 100% merge when you need genuine sadness — it pushes target-emotion strength from 0.007 to 0.152 and genuineness to 0.238. The cost is steep on intelligibility and quality: WER jumps 0.146 to 0.515 and the quality proxy falls 0.546 to 0.348, so keep lines short. It also drags in Distress and Helplessness (both corr ~0.93), so the voice sounds despairing rather than merely melancholy; if you need clean, intelligible sadness, prompt-only BASE_P (WER 0.146) is nearly as rewarding.

---
[← all emotions](index.md) · [human/audio version](../../site/emotions/Sadness.html)