# MOSS-TTS-4.55B voice-acting-v2 — Conditioning Manual (agent skill)

A measured usage guide for `laion/moss-tts-local-transformer-4.55b-voice-acting-v2`. For each target: the best prompting strategy **with and without** a LoRA, the best merge %, the expected **reward** = (genuineness + vocal_burst_blend + 1.25·target_emotion)/(1+WER), and the **side-effects / correlations** on other EmoNet emotions, VoiceNet dimensions, genuineness, blend and speech quality.

## Manuals
- [Emotions (40)](emotions/index.md) — **ready**
- [Edge cases](https://laion-ai.github.io/moss-emotion-edgecase-evolution/) — **ready** (screaming, crying, laughter, groaning, shivering — reward-max prompt + λ, with/without LoRA)
- [VoiceNet dimensions](https://laion-ai.github.io/moss-voicenet-manual/) (57 × high/low, 25/50/75/100/125% sweep + side-effects, audio + prompting tips) — **ready**
- Character voices (per-voice merge sweep + correlations) — *planned*

## Related experiments & grids (all live)
- [40-emotion evolution](https://laion-ai.github.io/moss-emotion-evolution-all/)
- [Prompt × LoRA study](https://laion-ai.github.io/moss-emotion-prompt-lora-study/)
- [VoiceNet LoRA evolution](https://laion-ai.github.io/moss-voicenet-lora-evolution/)
- [VoiceNet high/low grid](https://laion-ai.github.io/moss-voicenet-highlow-grid/)
- [Emotion × Voice conditions](https://laion-ai.github.io/emotion-voice-conditions/)
- [Character-voice clusters](https://projects.laion.ai/character-voice-clusters/)
- [Character LoRA refinement grids](https://projects.laion.ai/moss-voiceacting-demos/refine_v2.html)

## Model & adapter repos
- [moss-tts…voice-acting-v2](https://huggingface.co/laion/moss-tts-local-transformer-4.55b-voice-acting-v2) · [emotion-loras-v3](https://huggingface.co/TTS-AGI/moss-emotion-loras-v3) · [voicenet-dimension-loras](https://huggingface.co/laion/moss-voicenet-dimension-loras) · [character-loras-refined](https://huggingface.co/TTS-AGI/moss-character-loras-refined)

Human/audio version: see the HTML pages.
