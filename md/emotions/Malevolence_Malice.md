# Malevolence Malice — conditioning guide

*Target metric:* EmoNet **Malevolence_Malice** strength (0–1). *Reward* = (genu + blend + 1.25·emo) / (1+WER).

**TL;DR.** Best reward comes WITHOUT the LoRA — the evolved prompt (BASE_P 0.590) beats every merge (LoRA50 0.564, LoRA100 0.468, LoRA150 0.415). For the best-scoring output, use the evolved steering prompt and no LoRA. The catch is that BASE_P leaves the emotion inaudible (emo 0.008); the LoRA is the only thing that makes malice actually register (emo 0.045 to 0.253 at 150%), but at a severe intelligibility and quality cost — WER explodes to 0.903 and quality falls to 0.245 at 150%, blend more than halves. If you genuinely need audible menace, cap at LoRA50 and accept the quality hit; the merged voice bleeds into Anger, Contempt, Fear and Pain rather than staying coldly malicious.

## Without a LoRA (base model only)
Best: **evolved prompt, no LoRA** → reward **0.59** (emotion 0.01, WER 0.23).

```
GENERAL: A voice deeply expressing malevolence malice, a menacing, malicious voice, cruel and threatening, savoring the harm, in every breath.
SCRIPT:
(with cruel, menacing malice) "<your neutral sentence>"
```
(sampling: temperature 1.05, top_p 0.9, top_k 40)

## With the emotion LoRA
LoRA: `Malevolence_Malice` (TTS-AGI/moss-emotion-loras-v3). Best merge: **50%** → reward **0.56** (emotion 0.05).
Dose: 50% → reward 0.56 (emo 0.05) · 100% → 0.47 (emo 0.20) · 150% → 0.41 (emo 0.25).

## Conditions
| condition | reward | emotion | genu | blend | quality | WER |
|---|---|---|---|---|---|---|
| neutral prompt, no LoRA | 0.50±0.27 | 0.01 | 0.11 | 0.45 | 0.63 | 0.27 |
| evolved prompt, no LoRA | 0.59±0.33 | 0.01 | 0.14 | 0.51 | 0.53 | 0.23 |
| evolved prompt + LoRA 50% | 0.56±0.30 | 0.05 | 0.20 | 0.45 | 0.40 | 0.40 |
| evolved prompt + LoRA 100% | 0.47±0.18 | 0.20 | 0.14 | 0.26 | 0.41 | 0.49 |
| evolved prompt + LoRA 150% | 0.41±0.20 | 0.25 | 0.18 | 0.24 | 0.25 | 0.90 |

## Side effects & correlations (LoRA @ 100%)
- **Pushed up** (vs base): Sexual Lust (+1.43), Emotional Numbness (+1.14), Intoxication Altered States of Consciousness (+1.12)
- **Pushed down**: Mask Resonance (-0.46), Articulation Clarity (-0.31), Conversational Style (-0.31)
- **Positively correlated**: Anger (+0.82), Contempt (+0.74), Sexual Lust (+0.74)
- **Negatively correlated**: Recording Quality (-0.58), Structure (-0.57), Mixed Resonance (-0.57)

## Conclusion
Best reward comes WITHOUT the LoRA — the evolved prompt (BASE_P 0.590) beats every merge (LoRA50 0.564, LoRA100 0.468, LoRA150 0.415). For the best-scoring output, use the evolved steering prompt and no LoRA. The catch is that BASE_P leaves the emotion inaudible (emo 0.008); the LoRA is the only thing that makes malice actually register (emo 0.045 to 0.253 at 150%), but at a severe intelligibility and quality cost — WER explodes to 0.903 and quality falls to 0.245 at 150%, blend more than halves. If you genuinely need audible menace, cap at LoRA50 and accept the quality hit; the merged voice bleeds into Anger, Contempt, Fear and Pain rather than staying coldly malicious.

---
[← all emotions](index.md) · [human/audio version](../../site/emotions/Malevolence_Malice.html)