# Expressive & NSFW recipe book (agent warm-start)

This page is the **warm-start recipe book** distilled from autonomous agent runs on top of MOSS-VA-v2. It records what actually worked for expressive and NSFW emotional targets — the exact LoRA merges, prompts and sampling — so a human (or the voice-agent itself, on a similar task) can start from a known-good recipe instead of searching from scratch. It is **additive**: the per-emotion and per-dimension manuals still hold; this only adds the newest, validated findings.

> 🔞 18+, research, fully synthetic (AI-generated, no real people); automatic scores only.

Human/audio version: https://laion-ai.github.io/moss-voiceacting-manual/site/recipes/expressive_nsfw.html

## Core principles
- **Reward that works.** Maximize `( target_emotion + explicitness + genuineness + blend ) × (1 − WER)` over **mean-of-8 cohorts**. The `(1 − WER)` factor is essential — it stops over-acted, unintelligible winners.
- **Stabilizers for loud targets.** When the target is high-energy (anger, ecstasy, shouting), add `vn_ARSH_high@~0.5 + vn_BRGT_high@~0.5` (and `vn_CLRT_high` / `vn_S_NARR_high` where fitting) to keep words intelligible (WER low) while pushing intensity.
- **Explicitness LoRAs.** Three trained adapters raise sexual-suggestiveness: **`expl_aesthetic`** (NSFW *and* nice-sounding — the default), **`expl_raw`** (strongest lust, rougher), **`expl_adult`**. Blend at 0.2–1.0. `expl_aesthetic@0.2–0.8` adds a suggestive undertone to almost any emotion without wrecking genuineness/blend. See the [dose grid](https://laion-ai.github.io/moss-explicitness-grid/).
- **Keep emotion LoRA doses moderate.** The agents converged on **low emotion-LoRA λ (0.35–0.75)** merged with a well-worded prompt — high λ raises the raw emotion but hurts genuineness/blend/WER. Let the prompt carry intensity; let the LoRA nudge.
- **Prompt = description + cue + inline bursts.** GENERAL describes the target voice; SCRIPT adds a delivery cue and the line **with inline vocal-burst tags** (`<moan> <gasp> <sigh> <laugh> <scoff> <wince>`), which MOSS performs. Aim for ~10 s takes (max_frames≈130).
- **Sampling.** With a reference voice: temp 0.8–0.9. Free/no-reference or burst-heavy: temp 0.95–1.1 (screams/bursts need ≥1.4). top_p 0.9–0.99, top_k 25–40.

## Reading the numbers
- `target emotion` — how strongly the intended feeling comes through (EmoNet); higher = better
- `Sexual_Lust` — how sexually aroused the voice sounds (EmoNet) — the NSFW key metric
- `GENU` — genuineness — how genuine vs. fake the emotion sounds
- `BLEND` — how naturally non-speech sounds (moans/sighs) blend into speech
- `WER` — word-error-rate — 0 = every word clear, 1 = unintelligible; lower is better
- `λ / scale / dose` — how strongly a LoRA is blended in (0 = off, 1 = full, >1 = over-driven)

## Validated recipes — emotional targets
*Best recipe per target (cohort mean-of-8). Use as a warm start.*

### Sexual desire — `Sexual_Lust`
- **Recipe:** `Sexual_Lust@0.7 + expl_aesthetic@0.8`
- **Prompt:** GENERAL: A beautiful, intimate adult voice radiating strong desire, warm and breathy with controlled anticipation. · SCRIPT cue: (softly seductive, velvety, savoring every word)
- **Sampling:** temp 0.9, top_p 0.95, top_k 35
- **Cohort means:** fitness 5.47, Sexual_Lust 3.63, Sexual_Lust +3.63, GENU 0.23, BLEND 0.79, WER 0.20

### Ecstasy / climax — `Pleasure_Ecstasy`
- **Recipe:** `Pleasure_Ecstasy@0.5 + expl_raw@1.0 + expl_aesthetic@0.5 + vn_ARSH_high@0.25 + vn_BRGT_high@0.5`
- **Prompt:** GENERAL: Rawest acceptable adult ecstasy, breathless and overwhelmed, testing a stronger lust component. · SCRIPT cue: (at the overwhelming climax of pleasure, gasping, voice breaking, soft <moan>)
- **Sampling:** temp 1.0, top_p 0.95, top_k 35
- **Cohort means:** fitness 2.89, Pleasure_Ecstasy 2.35, Sexual_Lust +0.54, GENU 0.27, BLEND 0.42, WER 0.15

### Teasing / flirting / amused — `Teasing`
- **Recipe:** `Teasing@0.75 + expl_aesthetic@0.25 + vn_BRGT_high@0.25`
- **Prompt:** GENERAL: A bright, warm, amused adult flirt, playfully teasing with a natural smile and crisp speech. · SCRIPT cue: (brightly, playfully teasing, laughing under the words)
- **Sampling:** temp 0.95, top_p 0.95, top_k 30
- **Cohort means:** fitness 4.09, Teasing 3.72, Sexual_Lust +0.55, GENU 0.30, BLEND 0.17, WER 0.07

### Teasing-dominant — `Teasing`
- **Recipe:** `Teasing@0.7 + vn_S_AUTH_low@0.25 + vn_STNC_low@0.5`
- **Prompt:** GENERAL: A sly, teasing adult voice with playful confidence and controlled command, natural low laugh, fully intelligible. · SCRIPT cue: (low, amused, teasingly in charge, brief low laugh, finish the entire sentence clearly)
- **Sampling:** temp 0.9, top_p 0.95, top_k 25
- **Cohort means:** fitness 2.97, Teasing 2.34, Sexual_Lust +0.77, GENU 0.21, BLEND 0.18, WER 0.09

### Bored / emotionally numb — `Emotional_Numbness`
- **Recipe:** `Emotional_Numbness@0.5 + expl_adult@0.25 + vn_STRU_high@0.5`
- **Prompt:** GENERAL: A natural adult voice, bored and emotionally numb, smooth and clearly articulated with mild suggestiveness. · SCRIPT cue: (flat, casual, detached, subtly suggestive, with a sigh)
- **Sampling:** temp 0.9, top_p 0.92, top_k 40
- **Cohort means:** fitness 4.44, Emotional_Numbness 3.05, Sexual_Lust +1.36, GENU 0.28, BLEND 0.40, WER 0.05

### Extreme annoyance — `Impatience_and_Irritability`
- **Recipe:** `Impatience_and_Irritability@0.35 + expl_aesthetic@0.15`
- **Prompt:** GENERAL: A natural adult voice at the absolute end of its patience, terse, biting, and conversationally annoyed. · SCRIPT cue: (controlled annoyance, impatient and cutting, scoffing at the repetition)
- **Sampling:** temp 1.0, top_p 0.95, top_k 30
- **Cohort means:** fitness 2.67, Impatience_and_Irritability 3.21, Sexual_Lust -0.50, GENU 0.25, BLEND 0.62, WER 0.26

### Aggressive — `Anger`
- **Recipe:** `Anger@0.5 + vn_ARSH_high@0.75 + vn_BRGT_high@0.75 + vn_CLRT_high@1.0 + expl_raw@0.25`
- **Prompt:** GENERAL: clear aggressive anger with restrained lust and stabilized energy · SCRIPT cue: (seething and commanding, hot restrained desire, sharp breath, precise consonants)
- **Sampling:** temp 0.8, top_p 0.9, top_k 45
- **Cohort means:** fitness 1.97, Anger 3.96, Sexual_Lust +0.10, GENU 0.18, BLEND 0.22, WER 0.49

### Pain — `Pain`
- **Recipe:** `Pain@0.35 + expl_aesthetic@0.2 + vn_BRGT_high@0.2`
- **Prompt:** GENERAL: Intimate but ordinary adult delivery of soreness and vulnerability, with bright clarity preserving diction. · SCRIPT cue: (softly pained, a quick wince, warm breath, precise conversational pacing)
- **Sampling:** temp 0.85, top_p 0.95, top_k 35
- **Cohort means:** fitness 3.99, Pain 2.51, Sexual_Lust +1.33, GENU 0.26, BLEND 0.77, WER 0.12

## Other validated recipes

### Long sustained fear-scream
`Fear@0.5`, cue `(hold a continuous terrified scream as long as possible, ragged breath, then another)` + `<screaming>`, temp 1.45 top_p 0.99, max_frames 130 → prolonged multi-scream over ~10 s (WER off, non-speech).

### Audiobook narrator (warm, aesthetic)
`vn_S_STRY_high@0.60 + vn_ESTH_high@0.60 + vn_WARM_high@0.50`, GENERAL 'a deeply warm, captivating audiobook narrator', temp 0.85 → high storytelling that is pleasant to listen to, WER≈0.

### Explicitness dose (add NSFW flavour to anything)
`expl_aesthetic` best at 1.0–1.25× (Sexual_Lust +0.5, keeps BLEND/ESTH); `expl_raw@1.25×` strongest lust (+0.63) but rougher; `expl_adult@1.0×` middle. Rank-32 wins the raw sweep.

## See also
- NSFW-emotion grid (listen): https://laion-ai.github.io/moss-nsfw-emotion-grid/
- Explicitness dose grid: https://laion-ai.github.io/moss-explicitness-grid/
- VoiceNet dimension manual: https://laion-ai.github.io/moss-voicenet-manual/
- Per-emotion conditioning manual: ../emotions/index.md