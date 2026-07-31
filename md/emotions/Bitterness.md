# Bitterness — conditioning guide

*Target metric:* EmoNet **Bitterness** strength (0–1). *Reward* = (genu + blend + 1.25·emo) / (1+WER).

**TL;DR.** Best reward comes decisively with the LoRA at 50% (0.622) — the strongest single condition across this emotion, well above BASE_P (0.518) and collapsing merges above 50% (LoRA100 0.407, LoRA150 0.388). Recommendation: run the evolved prompt plus the 50% LoRA and stop there. The win is driven by a big vocal-burst blend jump (0.485 to 0.591) and higher genuineness (0.151); the trade-off is a modest quality dip (0.549 to 0.485) and higher WER (0.246 to 0.319). Its most notable side-effect is that bitterness renders as weary sadness — LoRA50 correlates with Sadness, Fatigue and Helplessness and injects Emotional Numbness, while suppressing Concentration (-0.39).

## Without a LoRA (base model only)
Best: **evolved prompt, no LoRA** → reward **0.52** (emotion 0.00, WER 0.25).

```
GENERAL: A voice deeply expressing bitterness, a bitter, resentful voice, jaded and sardonic, dripping with disillusion, in every breath.
SCRIPT:
(bitterly, with jaded resentment) "<your neutral sentence>"
```
(sampling: temperature 0.9, top_p 0.95, top_k 25)

## With the emotion LoRA
LoRA: `Bitterness` (TTS-AGI/moss-emotion-loras-v3). Best merge: **50%** → reward **0.62** (emotion 0.00).
Dose: 50% → reward 0.62 (emo 0.00) · 100% → 0.41 (emo 0.00) · 150% → 0.39 (emo 0.01).

## Conditions
| condition | reward | emotion | genu | blend | quality | WER |
|---|---|---|---|---|---|---|
| neutral prompt, no LoRA | 0.49±0.27 | 0.00 | 0.11 | 0.45 | 0.63 | 0.27 |
| evolved prompt, no LoRA | 0.52±0.30 | 0.00 | 0.13 | 0.48 | 0.55 | 0.25 |
| evolved prompt + LoRA 50% | 0.62±0.33 | 0.00 | 0.15 | 0.59 | 0.49 | 0.32 |
| evolved prompt + LoRA 100% | 0.41±0.29 | 0.00 | 0.11 | 0.38 | 0.48 | 0.36 |
| evolved prompt + LoRA 150% | 0.39±0.27 | 0.01 | 0.12 | 0.33 | 0.46 | 0.57 |

## Side effects & correlations (LoRA @ 100%)
- **Pushed up** (vs base): Emotional Numbness (+0.84), Malevolence Malice (+0.37), Fatigue Exhaustion (+0.35)
- **Pushed down**: Concentration (-0.52), Mask Resonance (-0.22), Conversational Style (-0.21)
- **Positively correlated**: Fatigue Exhaustion (+0.36), Conversational Style (+0.35), Teasing (+0.34)
- **Negatively correlated**: Monologue Style (-0.54), Interest (-0.45), Narrator Style (-0.38)

## Conclusion
Best reward comes decisively with the LoRA at 50% (0.622) — the strongest single condition across this emotion, well above BASE_P (0.518) and collapsing merges above 50% (LoRA100 0.407, LoRA150 0.388). Recommendation: run the evolved prompt plus the 50% LoRA and stop there. The win is driven by a big vocal-burst blend jump (0.485 to 0.591) and higher genuineness (0.151); the trade-off is a modest quality dip (0.549 to 0.485) and higher WER (0.246 to 0.319). Its most notable side-effect is that bitterness renders as weary sadness — LoRA50 correlates with Sadness, Fatigue and Helplessness and injects Emotional Numbness, while suppressing Concentration (-0.39).

---
[← all emotions](index.md) · [human/audio version](../../site/emotions/Bitterness.html)