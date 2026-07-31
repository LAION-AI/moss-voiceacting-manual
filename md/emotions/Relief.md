# Relief — conditioning guide

*Target metric:* EmoNet **Relief** strength (0–1). *Reward* = (genu + blend + 1.25·emo) / (1+WER).

**TL;DR.** Best without the LoRA — the evolved steering prompt (BASE_P) tops the table at reward 0.624, ahead of the best merge (LoRA100, 0.517). Prompt-steer and stop there: the prompt alone lifts genuineness from 0.110 to 0.174 and blend to 0.499, whereas any merge trades a negligible emo gain (0.049 vs 0.039) for a large blend drop (0.499 to 0.369) and lower reward. Note the side-effect: relief reads as a weary exhale here, correlating with Fatigue/Exhaustion (0.41) and Vulnerability (0.37) rather than bright relief, so pair it with tired-sounding text.

## Without a LoRA (base model only)
Best: **evolved prompt, no LoRA** → reward **0.62** (emotion 0.04, WER 0.27).

```
GENERAL: A voice deeply expressing relief, a voice flooding with relief, exhaling the tension, grateful it is finally over, in every breath.
SCRIPT:
(exhaling in profound relief) "<your neutral sentence>"
```
(sampling: temperature 1.2, top_p 0.95, top_k 30)

## With the emotion LoRA
LoRA: `Relief` (TTS-AGI/moss-emotion-loras-v3). Best merge: **100%** → reward **0.52** (emotion 0.04).
Dose: 50% → reward 0.47 (emo 0.05) · 100% → 0.52 (emo 0.04) · 150% → 0.50 (emo 0.06).

## Conditions
| condition | reward | emotion | genu | blend | quality | WER |
|---|---|---|---|---|---|---|
| neutral prompt, no LoRA | 0.52±0.31 | 0.03 | 0.11 | 0.45 | 0.63 | 0.27 |
| evolved prompt, no LoRA | 0.62±0.33 | 0.04 | 0.17 | 0.50 | 0.53 | 0.27 |
| evolved prompt + LoRA 50% | 0.47±0.29 | 0.05 | 0.15 | 0.37 | 0.54 | 0.30 |
| evolved prompt + LoRA 100% | 0.52±0.34 | 0.04 | 0.16 | 0.39 | 0.51 | 0.23 |
| evolved prompt + LoRA 150% | 0.50±0.32 | 0.06 | 0.16 | 0.40 | 0.53 | 0.37 |

## Side effects & correlations (LoRA @ 100%)
- **Pushed up** (vs base): Fatigue Exhaustion (+0.36), Emotional Numbness (+0.35), Embarrassment (+0.20)
- **Pushed down**: Fullness (-0.20), Warmth (-0.18), Recording Quality (-0.17)
- **Positively correlated**: Affection (+0.89), Shame (+0.82), Thankfulness Gratitude (+0.75)
- **Negatively correlated**: Formal Style (-0.64), Articulation Clarity (-0.53), Stance (-0.52)

## Conclusion
Best without the LoRA — the evolved steering prompt (BASE_P) tops the table at reward 0.624, ahead of the best merge (LoRA100, 0.517). Prompt-steer and stop there: the prompt alone lifts genuineness from 0.110 to 0.174 and blend to 0.499, whereas any merge trades a negligible emo gain (0.049 vs 0.039) for a large blend drop (0.499 to 0.369) and lower reward. Note the side-effect: relief reads as a weary exhale here, correlating with Fatigue/Exhaustion (0.41) and Vulnerability (0.37) rather than bright relief, so pair it with tired-sounding text.

---
[← all emotions](index.md) · [human/audio version](../../site/emotions/Relief.html)