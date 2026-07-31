# Emotional Numbness — conditioning guide

*Target metric:* EmoNet **Emotional_Numbness** strength (0–1). *Reward* = (genu + blend + 1.25·emo) / (1+WER).

**TL;DR.** Best reward is WITH the LoRA at 50% (0.583, beating BASE 0.519). This is the one setting that actually delivers real target strength — emo jumps from 0.029 (prompt-only) to 0.235 — while keeping vocal-burst blend intact at 0.45. The cost is intelligibility and quality: WER roughly doubles (0.269 to 0.558) and quality drops to 0.445. Numbness surfaces as flattened arousal and emphasis (corr neg Arousal -0.79, Emphasis -0.80) plus rising disfluency (corr 0.77); do NOT push to 100/150%, where emo climbs but WER explodes to ~1.0 and reward collapses.

## Without a LoRA (base model only)
Best: **neutral prompt, no LoRA** → reward **0.52** (emotion 0.03, WER 0.27).

```
GENERAL: A voice utterly expressing emotional numbness, a flat, hollow, emotionally numb voice, detached and empty, drained of all feeling, in every breath.
SCRIPT:
(flatly, hollow and emotionally numb) "<your neutral sentence>"
```
(sampling: temperature 0.8, top_p 0.9, top_k 40)

## With the emotion LoRA
LoRA: `Emotional_Numbness` (TTS-AGI/moss-emotion-loras-v3). Best merge: **50%** → reward **0.58** (emotion 0.23).
Dose: 50% → reward 0.58 (emo 0.23) · 100% → 0.52 (emo 0.45) · 150% → 0.48 (emo 0.39).

## Conditions
| condition | reward | emotion | genu | blend | quality | WER |
|---|---|---|---|---|---|---|
| neutral prompt, no LoRA | 0.52±0.29 | 0.03 | 0.11 | 0.45 | 0.63 | 0.27 |
| evolved prompt, no LoRA | 0.51±0.28 | 0.03 | 0.13 | 0.45 | 0.56 | 0.22 |
| evolved prompt + LoRA 50% | 0.58±0.26 | 0.23 | 0.14 | 0.45 | 0.44 | 0.56 |
| evolved prompt + LoRA 100% | 0.52±0.19 | 0.45 | 0.14 | 0.34 | 0.26 | 0.99 |
| evolved prompt + LoRA 150% | 0.48±0.22 | 0.39 | 0.13 | 0.34 | 0.28 | 1.07 |

## Side effects & correlations (LoRA @ 100%)
- **Pushed up** (vs base): Pain (+0.97), Pleasure Ecstasy (+0.94), Sexual Lust (+0.79)
- **Pushed down**: Interest (-0.80), Concentration (-0.69), Impatience and Irritability (-0.53)
- **Positively correlated**: Playful Style (+0.64), Nasal Resonance (+0.63), Disfluency (+0.60)
- **Negatively correlated**: Interest (-0.79), Authoritative Style (-0.71), Smoothness (-0.68)

## Conclusion
Best reward is WITH the LoRA at 50% (0.583, beating BASE 0.519). This is the one setting that actually delivers real target strength — emo jumps from 0.029 (prompt-only) to 0.235 — while keeping vocal-burst blend intact at 0.45. The cost is intelligibility and quality: WER roughly doubles (0.269 to 0.558) and quality drops to 0.445. Numbness surfaces as flattened arousal and emphasis (corr neg Arousal -0.79, Emphasis -0.80) plus rising disfluency (corr 0.77); do NOT push to 100/150%, where emo climbs but WER explodes to ~1.0 and reward collapses.

---
[← all emotions](index.md) · [human/audio version](../../site/emotions/Emotional_Numbness.html)