# Helplessness — conditioning guide

*Target metric:* EmoNet **Helplessness** strength (0–1). *Reward* = (genu + blend + 1.25·emo) / (1+WER).

**TL;DR.** Strong win WITH the LoRA at 50% (reward 0.755, well above the evolved prompt's 0.573). At 50% merge genuineness (0.142 to 0.205) and blend (0.457 to 0.576) both rise and WER stays controlled (0.262), so the only casualty is the quality proxy, which drops from 0.559 to 0.401. Helplessness rides a distress/sadness/disappointment cluster (corr Distress 0.82, Sadness 0.73) and it suppresses articulation clarity (corr neg -0.66). Stay at 50%: higher merges raise emo (0.26 at 150%) but WER jumps to 0.834 and reward falls back to 0.541.

## Without a LoRA (base model only)
Best: **evolved prompt, no LoRA** → reward **0.57** (emotion 0.02, WER 0.17).

```
GENERAL: A voice unmistakably expressing helplessness, a powerless, defeated voice, pleading and helpless, out of options, impossible to hide.
SCRIPT:
(helplessly, defeated and powerless) "<your neutral sentence>"
```
(sampling: temperature 0.9, top_p 0.9, top_k 25)

## With the emotion LoRA
LoRA: `Helplessness` (TTS-AGI/moss-emotion-loras-v3). Best merge: **50%** → reward **0.75** (emotion 0.07).
Dose: 50% → reward 0.75 (emo 0.07) · 100% → 0.56 (emo 0.21) · 150% → 0.54 (emo 0.26).

## Conditions
| condition | reward | emotion | genu | blend | quality | WER |
|---|---|---|---|---|---|---|
| neutral prompt, no LoRA | 0.50±0.27 | 0.01 | 0.11 | 0.45 | 0.63 | 0.27 |
| evolved prompt, no LoRA | 0.57±0.39 | 0.02 | 0.14 | 0.46 | 0.56 | 0.17 |
| evolved prompt + LoRA 50% | 0.75±0.42 | 0.07 | 0.20 | 0.58 | 0.40 | 0.26 |
| evolved prompt + LoRA 100% | 0.56±0.25 | 0.21 | 0.23 | 0.36 | 0.30 | 0.61 |
| evolved prompt + LoRA 150% | 0.54±0.17 | 0.26 | 0.22 | 0.44 | 0.23 | 0.83 |

## Side effects & correlations (LoRA @ 100%)
- **Pushed up** (vs base): Pain (+1.32), Distress (+1.20), Sadness (+1.16)
- **Pushed down**: Interest (-0.59), Concentration (-0.50), Warmth (-0.38)
- **Positively correlated**: Distress (+0.94), Fear (+0.85), Sadness (+0.84)
- **Negatively correlated**: Formal Style (-0.63), Interest (-0.61), Structure (-0.56)

## Conclusion
Strong win WITH the LoRA at 50% (reward 0.755, well above the evolved prompt's 0.573). At 50% merge genuineness (0.142 to 0.205) and blend (0.457 to 0.576) both rise and WER stays controlled (0.262), so the only casualty is the quality proxy, which drops from 0.559 to 0.401. Helplessness rides a distress/sadness/disappointment cluster (corr Distress 0.82, Sadness 0.73) and it suppresses articulation clarity (corr neg -0.66). Stay at 50%: higher merges raise emo (0.26 at 150%) but WER jumps to 0.834 and reward falls back to 0.541.

---
[← all emotions](index.md) · [human/audio version](../../site/emotions/Helplessness.html)