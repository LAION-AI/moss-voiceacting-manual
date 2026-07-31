# Affection — conditioning guide

*Target metric:* EmoNet **Affection** strength (0–1). *Reward* = (genu + blend + 1.25·emo) / (1+WER).

**TL;DR.** Best reward comes without the LoRA — the evolved steering prompt (BASE_P, reward 0.513) narrowly beats neutral BASE (0.493) and every LoRA merge (LoRA50 0.418, dropping to 0.366 at 100%). Recommendation: use the evolved Affection prompt and skip the LoRA entirely. The LoRA does climb genuineness (0.122 to 0.229 at 150%) but at a steep cost: blend falls (0.411 to 0.340) and WER nearly quadruples (0.196 to 0.674). Its most telling side-effect is that it injects massive Emotional Numbness (shift up ~0.89-0.93) rather than warmth, so it flattens the voice instead of making it tender.

## Without a LoRA (base model only)
Best: **evolved prompt, no LoRA** → reward **0.51** (emotion 0.03, WER 0.20).

```
GENERAL: A voice intensely expressing affection, a warm, tender voice overflowing with affection, soft and caring, a gentle smile in every word, impossible to hide.
SCRIPT:
(warmly, tenderly, full of affection) "<your neutral sentence>"
```
(sampling: temperature 0.9, top_p 0.95, top_k 25)

## With the emotion LoRA
LoRA: `Affection` (TTS-AGI/moss-emotion-loras-v3). Best merge: **50%** → reward **0.42** (emotion 0.03).
Dose: 50% → reward 0.42 (emo 0.03) · 100% → 0.37 (emo 0.02) · 150% → 0.38 (emo 0.02).

## Conditions
| condition | reward | emotion | genu | blend | quality | WER |
|---|---|---|---|---|---|---|
| neutral prompt, no LoRA | 0.49±0.27 | 0.01 | 0.11 | 0.45 | 0.63 | 0.27 |
| evolved prompt, no LoRA | 0.51±0.38 | 0.03 | 0.12 | 0.41 | 0.54 | 0.20 |
| evolved prompt + LoRA 50% | 0.42±0.29 | 0.03 | 0.13 | 0.37 | 0.54 | 0.51 |
| evolved prompt + LoRA 100% | 0.37±0.25 | 0.02 | 0.16 | 0.37 | 0.53 | 0.64 |
| evolved prompt + LoRA 150% | 0.38±0.25 | 0.02 | 0.23 | 0.34 | 0.50 | 0.67 |

## Side effects & correlations (LoRA @ 100%)
- **Pushed up** (vs base): Emotional Numbness (+0.86), Relief (+0.42), Fatigue Exhaustion (+0.40)
- **Pushed down**: Stance (-0.18), Dramatic Style (-0.18), Arousal Shift (-0.18)
- **Positively correlated**: Impatience and Irritability (+0.68), Longing (+0.68), Helplessness (+0.66)
- **Negatively correlated**: Throat Resonance (-0.39), Formal Style (-0.32), Authoritative Style (-0.31)

## Conclusion
Best reward comes without the LoRA — the evolved steering prompt (BASE_P, reward 0.513) narrowly beats neutral BASE (0.493) and every LoRA merge (LoRA50 0.418, dropping to 0.366 at 100%). Recommendation: use the evolved Affection prompt and skip the LoRA entirely. The LoRA does climb genuineness (0.122 to 0.229 at 150%) but at a steep cost: blend falls (0.411 to 0.340) and WER nearly quadruples (0.196 to 0.674). Its most telling side-effect is that it injects massive Emotional Numbness (shift up ~0.89-0.93) rather than warmth, so it flattens the voice instead of making it tender.

---
[← all emotions](index.md) · [human/audio version](../../site/emotions/Affection.html)