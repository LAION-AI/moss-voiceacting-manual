# Hope Enthusiasm Optimism — conditioning guide

*Target metric:* EmoNet **Hope_Enthusiasm_Optimism** strength (0–1). *Reward* = (genu + blend + 1.25·emo) / (1+WER).

**TL;DR.** This is a no-LoRA emotion — best reward comes from the plain neutral BASE prompt (0.498); both the evolved steering prompt (0.429) and every LoRA merge reduce reward. The failure mode is that steering and the LoRA collapse vocal-burst blend (0.453 to 0.27-0.33) faster than they add any emotion, and the LoRA also fights intelligibility (LoRA150 corr neg Articulation Clarity -0.82). If you must inject audible enthusiasm, LoRA150 does raise target emotion to 0.168 (shift up Triumph +0.94, Elation +0.91), but reward (0.454) still trails BASE. Recommendation: keep this emotion neutral with minimal steering.

## Without a LoRA (base model only)
Best: **neutral prompt, no LoRA** → reward **0.50** (emotion 0.01, WER 0.27).

```
GENERAL: A voice deeply expressing hope enthusiasm optimism, a bright, hopeful voice, brimming with enthusiasm and optimism, uplifting, impossible to hide.
SCRIPT:
(brightly, full of hope and enthusiasm) "<your neutral sentence>"
```
(sampling: temperature 1.0, top_p 0.9, top_k 25)

## With the emotion LoRA
LoRA: `Hope_Enthusiasm_Optimism` (TTS-AGI/moss-emotion-loras-v3). Best merge: **150%** → reward **0.45** (emotion 0.17).
Dose: 50% → reward 0.39 (emo 0.02) · 100% → 0.35 (emo 0.04) · 150% → 0.45 (emo 0.17).

## Conditions
| condition | reward | emotion | genu | blend | quality | WER |
|---|---|---|---|---|---|---|
| neutral prompt, no LoRA | 0.50±0.27 | 0.01 | 0.11 | 0.45 | 0.63 | 0.27 |
| evolved prompt, no LoRA | 0.43±0.28 | 0.05 | 0.11 | 0.33 | 0.59 | 0.30 |
| evolved prompt + LoRA 50% | 0.39±0.21 | 0.02 | 0.13 | 0.29 | 0.54 | 0.20 |
| evolved prompt + LoRA 100% | 0.35±0.24 | 0.04 | 0.13 | 0.30 | 0.45 | 0.47 |
| evolved prompt + LoRA 150% | 0.45±0.31 | 0.17 | 0.11 | 0.27 | 0.41 | 0.43 |

## Side effects & correlations (LoRA @ 100%)
- **Pushed up** (vs base): Impatience and Irritability (+0.64), Emotional Numbness (+0.31), Anger (+0.26)
- **Pushed down**: Concentration (-0.35), Warmth (-0.30), Whisper-Talk Style (-0.23)
- **Positively correlated**: Confusion (+0.66), Elation (+0.56), Casual Style (+0.52)
- **Negatively correlated**: Throat Resonance (-0.53), Newsreader Style (-0.46), Chest Resonance (-0.45)

## Conclusion
This is a no-LoRA emotion — best reward comes from the plain neutral BASE prompt (0.498); both the evolved steering prompt (0.429) and every LoRA merge reduce reward. The failure mode is that steering and the LoRA collapse vocal-burst blend (0.453 to 0.27-0.33) faster than they add any emotion, and the LoRA also fights intelligibility (LoRA150 corr neg Articulation Clarity -0.82). If you must inject audible enthusiasm, LoRA150 does raise target emotion to 0.168 (shift up Triumph +0.94, Elation +0.91), but reward (0.454) still trails BASE. Recommendation: keep this emotion neutral with minimal steering.

---
[← all emotions](index.md) · [human/audio version](../../site/emotions/Hope_Enthusiasm_Optimism.html)