# Interest — conditioning guide

*Target metric:* EmoNet **Interest** strength (0–1). *Reward* = (genu + blend + 1.25·emo) / (1+WER).

**TL;DR.** Best reward comes WITHOUT the LoRA — plain BASE tops the table at 0.690, edging out the evolved prompt (BASE_P, 0.679) and beating every merge (LoRA50 0.618, LoRA150 0.552). Interest is essentially a native emotion here: the base model already hits emo=0.187 with a neutral prompt, so just prompt plainly and skip the LoRA entirely. Adding the LoRA barely moves target strength (emo 0.187 to 0.227 only at 150%) while dragging blend down hard (0.453 to 0.274) and inflating WER (0.269 to 0.513 at 100%). The one thing the LoRA reliably drags along is a cartoonish, rough delivery (corr Cartoonish Style 0.82, Roughness 0.73 at 100%) — so higher merges buy you a caricatured voice, not more genuine interest.

## Without a LoRA (base model only)
Best: **neutral prompt, no LoRA** → reward **0.69** (emotion 0.19, WER 0.27).

```
GENERAL: A voice viscerally expressing interest, a keenly interested voice, leaning in, curious and engaged, with every word.
SCRIPT:
(keenly interested and curious) "<your neutral sentence>"
```
(sampling: temperature 1.15, top_p 0.95, top_k 40)

## With the emotion LoRA
LoRA: `Interest` (TTS-AGI/moss-emotion-loras-v3). Best merge: **50%** → reward **0.62** (emotion 0.19).
Dose: 50% → reward 0.62 (emo 0.19) · 100% → 0.54 (emo 0.20) · 150% → 0.55 (emo 0.23).

## Conditions
| condition | reward | emotion | genu | blend | quality | WER |
|---|---|---|---|---|---|---|
| neutral prompt, no LoRA | 0.69±0.30 | 0.19 | 0.11 | 0.45 | 0.63 | 0.27 |
| evolved prompt, no LoRA | 0.68±0.27 | 0.20 | 0.12 | 0.43 | 0.58 | 0.26 |
| evolved prompt + LoRA 50% | 0.62±0.29 | 0.19 | 0.10 | 0.37 | 0.58 | 0.20 |
| evolved prompt + LoRA 100% | 0.54±0.25 | 0.20 | 0.15 | 0.33 | 0.54 | 0.51 |
| evolved prompt + LoRA 150% | 0.55±0.20 | 0.23 | 0.15 | 0.27 | 0.53 | 0.36 |

## Side effects & correlations (LoRA @ 100%)
- **Pushed up** (vs base): Hope Enthusiasm Optimism (+0.38), Impatience and Irritability (+0.24), Elation (+0.17)
- **Pushed down**: Warmth (-0.15), Recording Quality (-0.14), Fullness (-0.13)
- **Positively correlated**: Cartoonish Style (+0.82), Roughness (+0.73), Metallic Character (+0.67)
- **Negatively correlated**: Chunking (-0.67), Smoothness (-0.61), Fatigue Exhaustion (-0.61)

## Conclusion
Best reward comes WITHOUT the LoRA — plain BASE tops the table at 0.690, edging out the evolved prompt (BASE_P, 0.679) and beating every merge (LoRA50 0.618, LoRA150 0.552). Interest is essentially a native emotion here: the base model already hits emo=0.187 with a neutral prompt, so just prompt plainly and skip the LoRA entirely. Adding the LoRA barely moves target strength (emo 0.187 to 0.227 only at 150%) while dragging blend down hard (0.453 to 0.274) and inflating WER (0.269 to 0.513 at 100%). The one thing the LoRA reliably drags along is a cartoonish, rough delivery (corr Cartoonish Style 0.82, Roughness 0.73 at 100%) — so higher merges buy you a caricatured voice, not more genuine interest.

---
[← all emotions](index.md) · [human/audio version](../../site/emotions/Interest.html)