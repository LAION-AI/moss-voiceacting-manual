# Distress — conditioning guide

*Target metric:* EmoNet **Distress** strength (0–1). *Reward* = (genu + blend + 1.25·emo) / (1+WER).

**TL;DR.** Best reward is decisively without a LoRA, the evolved steering prompt is the standout (BASE_P 0.720, versus 0.539 for the best LoRA and 0.492 for BASE), driven by blend jumping to 0.555 and WER falling to 0.133. The LoRAs are powerful emotion dials (emo 0.031 to 0.341 at 100%, 0.361 at 150%, with Pain shifting up +2.0 to +2.3) but they demolish intelligibility (WER 0.81-0.95) and quality (down to 0.18), so reward drops. The side-effect is that distress escalates into raw screamed Pain, Fear and Helplessness (correlations ~0.9) with speech barely decodable. Use the prompt alone; only pick LoRA100 if you truly need extreme distress emotion and can tolerate WER 0.81 and quality of 0.226.

## Without a LoRA (base model only)
Best: **evolved prompt, no LoRA** → reward **0.72** (emotion 0.03, WER 0.13).

```
GENERAL: A voice powerfully expressing distress, a distressed, anguished voice, tight with panic and pain, on the verge of breaking, in every breath.
SCRIPT:
(in acute distress and anguish) "<your neutral sentence>"
```
(sampling: temperature 0.9, top_p 0.95, top_k 25)

## With the emotion LoRA
LoRA: `Distress` (TTS-AGI/moss-emotion-loras-v3). Best merge: **100%** → reward **0.54** (emotion 0.34).
Dose: 50% → reward 0.50 (emo 0.12) · 100% → 0.54 (emo 0.34) · 150% → 0.51 (emo 0.36).

## Conditions
| condition | reward | emotion | genu | blend | quality | WER |
|---|---|---|---|---|---|---|
| neutral prompt, no LoRA | 0.49±0.27 | 0.01 | 0.11 | 0.45 | 0.63 | 0.27 |
| evolved prompt, no LoRA | 0.72±0.40 | 0.03 | 0.17 | 0.55 | 0.52 | 0.13 |
| evolved prompt + LoRA 50% | 0.50±0.27 | 0.12 | 0.19 | 0.42 | 0.36 | 0.63 |
| evolved prompt + LoRA 100% | 0.54±0.24 | 0.34 | 0.23 | 0.28 | 0.23 | 0.81 |
| evolved prompt + LoRA 150% | 0.51±0.14 | 0.36 | 0.23 | 0.31 | 0.18 | 0.95 |

## Side effects & correlations (LoRA @ 100%)
- **Pushed up** (vs base): Pain (+2.03), Helplessness (+1.66), Fear (+1.63)
- **Pushed down**: Interest (-0.75), Concentration (-0.55), Warmth (-0.47)
- **Positively correlated**: Fear (+0.91), Helplessness (+0.89), Pain (+0.86)
- **Negatively correlated**: Mixed Resonance (-0.81), Narrator Style (-0.71), Fullness (-0.70)

## Conclusion
Best reward is decisively without a LoRA, the evolved steering prompt is the standout (BASE_P 0.720, versus 0.539 for the best LoRA and 0.492 for BASE), driven by blend jumping to 0.555 and WER falling to 0.133. The LoRAs are powerful emotion dials (emo 0.031 to 0.341 at 100%, 0.361 at 150%, with Pain shifting up +2.0 to +2.3) but they demolish intelligibility (WER 0.81-0.95) and quality (down to 0.18), so reward drops. The side-effect is that distress escalates into raw screamed Pain, Fear and Helplessness (correlations ~0.9) with speech barely decodable. Use the prompt alone; only pick LoRA100 if you truly need extreme distress emotion and can tolerate WER 0.81 and quality of 0.226.

---
[← all emotions](index.md) · [human/audio version](../../site/emotions/Distress.html)