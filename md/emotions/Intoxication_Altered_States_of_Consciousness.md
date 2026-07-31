# Intoxication Altered States of Consciousness — conditioning guide

*Target metric:* EmoNet **Intoxication_Altered_States_of_Consciousness** strength (0–1). *Reward* = (genu + blend + 1.25·emo) / (1+WER).

**TL;DR.** Best reward is WITHOUT the LoRA (BASE 0.485; BASE_P 0.465, LoRA50 0.468). This target is effectively unlearnable in this rig — emo sits at or below zero at baseline (-0.004) and even LoRA150 only reaches 0.084, so use a plain neutral prompt and don't expect audible intoxication. Pushing the LoRA does lift genuineness (0.110 to 0.265 at 150%) but collapses blend (0.453 to 0.254), quality (0.625 to 0.342) and WER (up to 0.579), a net reward loss. Worse, the merged model doesn't render intoxication at all — it shifts up Triumph, Amusement and Malevolence and correlates with Confusion/Fear, i.e. you get slurred, degraded audio miscolored as other high-arousal states.

## Without a LoRA (base model only)
Best: **neutral prompt, no LoRA** → reward **0.49** (emotion -0.00, WER 0.27).

```
GENERAL: A voice overwhelmingly expressing intoxication altered states of consciousness, a woozy, slurring voice, intoxicated and untethered, in an altered haze, impossible to hide.
SCRIPT:
(woozy, slurring, intoxicated) "<your neutral sentence>"
```
(sampling: temperature 1.0, top_p 0.9, top_k 30)

## With the emotion LoRA
LoRA: `Intoxication_Altered_States_of_Consciousness` (TTS-AGI/moss-emotion-loras-v3). Best merge: **50%** → reward **0.47** (emotion -0.00).
Dose: 50% → reward 0.47 (emo -0.00) · 100% → 0.43 (emo 0.04) · 150% → 0.45 (emo 0.08).

## Conditions
| condition | reward | emotion | genu | blend | quality | WER |
|---|---|---|---|---|---|---|
| neutral prompt, no LoRA | 0.49±0.27 | -0.00 | 0.11 | 0.45 | 0.63 | 0.27 |
| evolved prompt, no LoRA | 0.46±0.28 | -0.00 | 0.12 | 0.47 | 0.58 | 0.31 |
| evolved prompt + LoRA 50% | 0.47±0.26 | -0.00 | 0.14 | 0.39 | 0.55 | 0.17 |
| evolved prompt + LoRA 100% | 0.43±0.25 | 0.04 | 0.24 | 0.29 | 0.43 | 0.58 |
| evolved prompt + LoRA 150% | 0.45±0.30 | 0.08 | 0.26 | 0.25 | 0.34 | 0.53 |

## Side effects & correlations (LoRA @ 100%)
- **Pushed up** (vs base): Amusement (+0.62), Emotional Numbness (+0.48), Hope Enthusiasm Optimism (+0.32)
- **Pushed down**: Recording Quality (-0.26), Mask Resonance (-0.26), Warmth (-0.22)
- **Positively correlated**: Jealousy & Envy (+0.50), Emotional Numbness (+0.48), Confusion (+0.48)
- **Negatively correlated**: Focus (-0.64), Authoritative Style (-0.58), Tempo (-0.54)

## Conclusion
Best reward is WITHOUT the LoRA (BASE 0.485; BASE_P 0.465, LoRA50 0.468). This target is effectively unlearnable in this rig — emo sits at or below zero at baseline (-0.004) and even LoRA150 only reaches 0.084, so use a plain neutral prompt and don't expect audible intoxication. Pushing the LoRA does lift genuineness (0.110 to 0.265 at 150%) but collapses blend (0.453 to 0.254), quality (0.625 to 0.342) and WER (up to 0.579), a net reward loss. Worse, the merged model doesn't render intoxication at all — it shifts up Triumph, Amusement and Malevolence and correlates with Confusion/Fear, i.e. you get slurred, degraded audio miscolored as other high-arousal states.

---
[← all emotions](index.md) · [human/audio version](../../site/emotions/Intoxication_Altered_States_of_Consciousness.html)