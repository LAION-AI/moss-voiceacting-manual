# Pride — conditioning guide

*Target metric:* EmoNet **Pride** strength (0–1). *Reward* = (genu + blend + 1.25·emo) / (1+WER).

**TL;DR.** Best reward comes WITHOUT the LoRA, and in fact without even the steering prompt — plain BASE (0.489) beats the evolved prompt (BASE_P 0.437) and every merge, which decline monotonically (LoRA50 0.403 to LoRA100 0.319). Pride is a failure case in this rig: both prompt-steering and the LoRA reduce reward, and emo never rises (max 0.018 at LoRA50), so keep a plain neutral prompt and leave both LoRA and steering prompt off. The LoRA's only real effect is to erode vocal-burst blend (0.453 to 0.263) for zero emotional payoff. When forced, its coloring is counterproductive: outputs correlate with Triumph, Contempt and Malevolence, collapsing dignified pride into an arrogant, contemptuous tone.

## Without a LoRA (base model only)
Best: **neutral prompt, no LoRA** → reward **0.49** (emotion 0.00, WER 0.27).

```
GENERAL: A voice overwhelmingly expressing pride, a proud, self-assured voice, chest swelling with pride, triumphantly boastful, impossible to hide.
SCRIPT:
(with swelling, self-assured pride) "<your neutral sentence>"
```
(sampling: temperature 1.05, top_p 0.95, top_k 25)

## With the emotion LoRA
LoRA: `Pride` (TTS-AGI/moss-emotion-loras-v3). Best merge: **50%** → reward **0.40** (emotion 0.02).
Dose: 50% → reward 0.40 (emo 0.02) · 100% → 0.32 (emo 0.00) · 150% → 0.33 (emo 0.01).

## Conditions
| condition | reward | emotion | genu | blend | quality | WER |
|---|---|---|---|---|---|---|
| neutral prompt, no LoRA | 0.49±0.27 | 0.00 | 0.11 | 0.45 | 0.63 | 0.27 |
| evolved prompt, no LoRA | 0.44±0.29 | 0.00 | 0.12 | 0.41 | 0.58 | 0.38 |
| evolved prompt + LoRA 50% | 0.40±0.27 | 0.02 | 0.11 | 0.34 | 0.58 | 0.30 |
| evolved prompt + LoRA 100% | 0.32±0.22 | 0.00 | 0.11 | 0.28 | 0.53 | 0.36 |
| evolved prompt + LoRA 150% | 0.33±0.23 | 0.01 | 0.12 | 0.26 | 0.52 | 0.28 |

## Side effects & correlations (LoRA @ 100%)
- **Pushed up** (vs base): Impatience and Irritability (+0.29), Fatigue Exhaustion (+0.19), Affection (+0.12)
- **Pushed down**: Concentration (-0.36), Fullness (-0.21), Vocal-burst blend (-0.17)
- **Positively correlated**: Malevolence Malice (+0.68), Contempt (+0.59), Amusement (+0.49)
- **Negatively correlated**: Chunking (-0.33), Focus (-0.29), Esthetics (-0.29)

## Conclusion
Best reward comes WITHOUT the LoRA, and in fact without even the steering prompt — plain BASE (0.489) beats the evolved prompt (BASE_P 0.437) and every merge, which decline monotonically (LoRA50 0.403 to LoRA100 0.319). Pride is a failure case in this rig: both prompt-steering and the LoRA reduce reward, and emo never rises (max 0.018 at LoRA50), so keep a plain neutral prompt and leave both LoRA and steering prompt off. The LoRA's only real effect is to erode vocal-burst blend (0.453 to 0.263) for zero emotional payoff. When forced, its coloring is counterproductive: outputs correlate with Triumph, Contempt and Malevolence, collapsing dignified pride into an arrogant, contemptuous tone.

---
[← all emotions](index.md) · [human/audio version](../../site/emotions/Pride.html)