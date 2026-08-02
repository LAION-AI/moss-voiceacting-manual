# MOSS Voice-Acting — Manual & Studies Hub

A measured, audio-backed usage guide for `laion/moss-tts-local-transformer-4.55b-voice-acting-v2` (4.55B expressive voice-acting TTS). For any target it gives the best prompt, which LoRA at which merge %, the expected reward, and measured side-effects. This is the agent-readable mirror of the [HTML hub](https://laion-ai.github.io/moss-voiceacting-manual/site/index.html).

**New (Aug 2026):** reward is `× (1 − WER)` (stops over-acted, unintelligible takes); at high energy add stabilizers `vn_ARSH_high@0.5 + vn_BRGT_high@0.5` (+`vn_S_NARR_high` for storytelling) to keep speech clear; a cheap API brain (gpt-5.6-luna) matches the local Gemma-4-31B (`google/gemma-4-31B-it-qat-w4a16-ct`) at cents/task. Favourite narrator recipe: `vn_S_STRY_high@0.65 + vn_ARSH_high@0.20 + vn_BRGT_low@0.20` → S_STRY 0.998, ESTH 0.59, WER 0.0, ~11s.

## 🚀 Start here — conditioning manuals
*How to drive the model: for a target (emotion, voice dimension, delivery), what prompt + which LoRA at which merge % — with measured side-effects. Each has an agent-readable Markdown mirror.*

- **[🎭 Emotion conditioning manual (40 emotions)](https://laion-ai.github.io/moss-voiceacting-manual/site/emotions/index.html)** · [MD](https://github.com/LAION-AI/moss-voiceacting-manual/tree/main/md/emotions) — Per emotion: the best prompting strategy **with and without** the emotion LoRA, the best merge λ, expected reward, and the top-3 ± correlations on other emotions / VoiceNet dims / genuineness / blend / quality. Start here to make a voice *feel* something.
- **[🎚️ VoiceNet dimension manual (57 dims × high/low)](https://laion-ai.github.io/moss-voicenet-manual/)** · [MD](https://github.com/LAION-AI/moss-voicenet-manual/tree/main/md) — Per speech dimension (tempo, warmth, arousal, roughness…): the dose-response across 25→125% merge, the best dose, the cost to genuineness/blend/quality, and the ± side-effects. The reference for *how a voice sounds*.
- **[🔁 Reinterpretation guide (procedural, at scale)](https://github.com/LAION-AI/voice-acting-search-agent/blob/main/REINTERPRETATION.md)** · [MD](https://github.com/LAION-AI/voice-acting-search-agent/blob/main/REINTERPRETATION.md) — A deterministic rule to pick LoRAs + scales + prompt from a clip's scores **without an LLM call**, so you can reinterpret a huge corpus (e.g. 1M DramaBox clips) — including the LoRA hot-swap / batch-bucketing answer.
- **[🔊 Edge-case delivery (screams, crying, laughter…)](https://laion-ai.github.io/moss-emotion-edgecase-evolution/)** — Reward-maximised recipes (prompt + λ + sampling) for hard non-speech-heavy deliveries — fear-scream, pain-scream/groan, sobbing, shivering, genuine laughter — evolved with and without the LoRA.

## 🔬 Interactive studies & audio grids
*Listen to the effects. Every clip is labelled with its recipe and scores.*

- **[⭐ Emotion × Voice conditions](https://laion-ai.github.io/emotion-voice-conditions/)** — 6 cloned voices × 40 emotions × 4 delivery conditions (intense/moderate × free/contained), best-of-32 with a speaker-similarity floor. The flagship study — shows that intensity, not containment, breaks a cloned voice.
- **[🧬 40-emotion evolution](https://laion-ai.github.io/moss-emotion-evolution-all/)** — Evolutionary search (10 generations, mean-of-8) for the best λ / prompt / sampling per emotion — the source of the per-emotion recipes used elsewhere.
- **[🎛️ Prompt × LoRA strength study](https://laion-ai.github.io/moss-emotion-prompt-lora-study/)** — Neutral vs prompt vs LoRA @50/100/150% for all 40 emotions, with a cross-steering heatmap — shows when the LoRA helps and when a good prompt alone wins.
- **[💥 Edge-case evolution](https://laion-ai.github.io/moss-emotion-edgecase-evolution/)** — The audio grid behind the edge-case recipes: screaming, crying, laughter, groaning, shivering, maximised with/without LoRA.
- **[🎚️ VoiceNet LoRA evolution (dose 0/50/100%)](https://laion-ai.github.io/moss-voicenet-lora-evolution/)** — Per-dimension controllability + best prompting at three doses — 50% already delivers most of the shift for most dimensions.
- **[↕️ VoiceNet high/low scaling grid](https://laion-ai.github.io/moss-voicenet-highlow-grid/)** — 57 dimensions × high/low × 5 merge doses (25→125%), 3 audio samples each — hear the full scaling sweep per dimension side by side.
- **[🗣️ Character-voice clusters](https://projects.laion.ai/character-voice-clusters/)** — VoiceNet-embedding clusters of the generated character voices with procedural captions — browse the space of distinct synthetic voices.
- **[♻️ Character LoRA refinement grids](https://projects.laion.ai/moss-voiceacting-demos/refine_v2.html)** — 120 character voices refined by SIDON self-distillation (generate → filter → restore → warm-start FT) — before/after quality per character.

## 🤖 Autonomous search agent
*An agent (local or API LLM brain) that *searches* for merge + prompt recipes on its own, guided by the manuals above and scored by the full perceptual stack.*

- **[📊 Results & model comparison](https://laion-ai.github.io/voice-acting-search-agent/)** — Single-dimension optimisation, the 4-brain comparison (gpt-5.6-luna vs Gemma-4 31B/12B/MoE, side by side with audio), the supervised edge-case swarm, and the corrected per-dimension runs.
- **[🏆 Which brain? (MODEL_COMPARISON.md)](https://github.com/LAION-AI/voice-acting-search-agent/blob/main/MODEL_COMPARISON.md)** · [MD](https://github.com/LAION-AI/voice-acting-search-agent/blob/main/MODEL_COMPARISON.md) — Gemini-judged, same-budget: gpt-5.6-luna (API) scored 9/9/10 — tied with the local Gemma-4 31B (9/10/9), ahead of 12B/MoE. Both independently found the stabilizer adapters.
- **[💸 Cost estimates (COSTS.md)](https://github.com/LAION-AI/voice-acting-search-agent/blob/main/COSTS.md)** · [MD](https://github.com/LAION-AI/voice-acting-search-agent/blob/main/COSTS.md) — Measured token/$ figures: an API brain runs a search for cents per task (luna: $0.31 for 4 missions, no GPU), and supervision is ~$0.007/verdict — see the 100/1000-task projections.
- **[🐝 Swarm design (SWARM_PLAN.md)](https://github.com/LAION-AI/voice-acting-search-agent/blob/main/SWARM_PLAN.md)** · [MD](https://github.com/LAION-AI/voice-acting-search-agent/blob/main/SWARM_PLAN.md) — The plan for scaling to a 32–64-agent self-improving swarm: two-tier hive-mind knowledge (raw experience vs. approved manual), task registry, supervisor loop, offline consolidation.
- **[🧠 What the agents have learned](https://github.com/LAION-AI/voice-acting-search-agent/blob/main/docs/experience-digest.md)** · [MD](https://github.com/LAION-AI/voice-acting-search-agent/blob/main/docs/experience-digest.md) — The distilled, validated learnings folded into every agent's context: winner recipes, the stabilizer adapters, the (1−WER) reward, and the task-difficulty map (what the TTS model can and cannot do).

## 📖 Taxonomies (definitions)
*The vocabularies everything is scored against.*

- **[VoiceNet taxonomy (base)](https://projects.laion.ai/Voice-Acting-Pipeline/voicenet_taxonomy.html)** — The 57 perceptual speech dimensions with 7-point anchor descriptions — what each VoiceNet score means.
- **[VoiceNet-Ext taxonomy](https://projects.laion.ai/Voice-Acting-Pipeline/voicenet_extension_taxonomy.html)** — The extended dimension set used by the predictor heads.
- **[Acting edge-cases / challenges](https://projects.laion.ai/Voice-Acting-Pipeline/path_ac_acting_challenge.html)** — 266 hard expressive-delivery situations, each expressed as VoiceNet/EmoNet/vocal-burst tokens — also mirrored (JSON + docs) in the [voice-taxonomies](https://github.com/LAION-AI/voice-taxonomies) repo.
- **[Situation taxonomy](https://projects.laion.ai/Voice-Acting-Pipeline/path_sit_situation.html)** — The scene/situation vocabulary behind the DramaBox reinterpretation prompts.

## 🤗 Models & adapters (Hugging Face)
*The checkpoints and LoRA collections referenced throughout.*

- **[Base model — moss-tts…voice-acting-v2](https://huggingface.co/laion/moss-tts-local-transformer-4.55b-voice-acting-v2)** — The 4.55B expressive voice-acting TTS model everything conditions on.
- **[Emotion LoRAs v3 (40)](https://huggingface.co/TTS-AGI/moss-emotion-loras-v3)** — One rank-64 LoRA per emotion (≤25% Got-Talent), the adapters behind the emotion manual.
- **[VoiceNet dimension LoRAs (114)](https://huggingface.co/laion/moss-voicenet-dimension-loras)** — 57 dimensions × high/low, the adapters behind the VoiceNet manual and the high/low grid.
- **[Character LoRAs — refined (120)](https://huggingface.co/TTS-AGI/moss-character-loras-refined)** — 120 SIDON-refined from-scratch character voices. (Private TTS-AGI repo — request access.)
