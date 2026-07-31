# Teasing — conditioning guide

*Target metric:* EmoNet **Teasing** strength (0–1). *Reward* = (genu + blend + 1.25·emo) / (1+WER).

**TL;DR.** Essentially a tie — LoRA at 50% barely edges plain BASE (0.503 vs 0.499), and the evolved steering prompt actually lowers reward (0.470), so use a neutral prompt with at most a 50% merge. Emotion strength stays tiny at 50% (emo 0.008); pushing to 150% raises emo to 0.109 but craters blend to 0.155 and reward to 0.364. The tell-tale side-effect: at high merge teasing collapses into overt Amusement (shift +2.02) — it becomes laughter, not sly teasing. Across all levels teasing shares acoustic space with Sourness/Anger/Contempt (corr ~0.9), so it can read as mocking; keep the merge low and let playful wording set the tone.

## Without a LoRA (base model only)
Best: **neutral prompt, no LoRA** → reward **0.50** (emotion 0.01, WER 0.27).

```
GENERAL: A voice to the extreme expressing teasing, a playful, teasing voice, sing-song and mischievous, poking fun, pouring out.
SCRIPT:
(playfully teasing, mischievous) "<your neutral sentence>"
```
(sampling: temperature 1.2, top_p 0.95, top_k 30)

## With the emotion LoRA
LoRA: `Teasing` (TTS-AGI/moss-emotion-loras-v3). Best merge: **50%** → reward **0.50** (emotion 0.01).
Dose: 50% → reward 0.50 (emo 0.01) · 100% → 0.35 (emo 0.03) · 150% → 0.36 (emo 0.11).

## Conditions
| condition | reward | emotion | genu | blend | quality | WER |
|---|---|---|---|---|---|---|
| neutral prompt, no LoRA | 0.50±0.27 | 0.01 | 0.11 | 0.45 | 0.63 | 0.27 |
| evolved prompt, no LoRA | 0.47±0.26 | 0.01 | 0.12 | 0.45 | 0.57 | 0.30 |
| evolved prompt + LoRA 50% | 0.50±0.33 | 0.01 | 0.14 | 0.44 | 0.56 | 0.24 |
| evolved prompt + LoRA 100% | 0.35±0.23 | 0.03 | 0.13 | 0.27 | 0.51 | 0.29 |
| evolved prompt + LoRA 150% | 0.36±0.20 | 0.11 | 0.19 | 0.16 | 0.47 | 0.53 |

## Side effects & correlations (LoRA @ 100%)
- **Pushed up** (vs base): Amusement (+0.41), Pleasure Ecstasy (+0.30), Malevolence Malice (+0.26)
- **Pushed down**: Concentration (-0.61), Fullness (-0.23), Perceived Gender (-0.19)
- **Positively correlated**: Amusement (+0.83), Pleasure Ecstasy (+0.76), Contempt (+0.69)
- **Negatively correlated**: Monologue Style (-0.64), Narrator Style (-0.50), Formal Style (-0.46)

## Conclusion
Essentially a tie — LoRA at 50% barely edges plain BASE (0.503 vs 0.499), and the evolved steering prompt actually lowers reward (0.470), so use a neutral prompt with at most a 50% merge. Emotion strength stays tiny at 50% (emo 0.008); pushing to 150% raises emo to 0.109 but craters blend to 0.155 and reward to 0.364. The tell-tale side-effect: at high merge teasing collapses into overt Amusement (shift +2.02) — it becomes laughter, not sly teasing. Across all levels teasing shares acoustic space with Sourness/Anger/Contempt (corr ~0.9), so it can read as mocking; keep the merge low and let playful wording set the tone.

---
[← all emotions](index.md) · [human/audio version](../../site/emotions/Teasing.html)