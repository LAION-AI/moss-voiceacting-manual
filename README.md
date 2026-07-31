# MOSS-TTS-4.55B voice-acting-v2 — Conditioning Manual

A measured usage guide for `laion/moss-tts-local-transformer-4.55b-voice-acting-v2`.

- **Human / audio version (GitHub Pages):** https://laion-ai.github.io/moss-voiceacting-manual/
- **Agent-skill (Markdown, no audio):** [`md/index.md`](md/index.md)

For each target: the best prompting strategy **with and without** a LoRA, the best merge %, the expected
**reward** = (genuineness + vocal_burst_blend + 1.25·target_emotion) / (1 + WER), and the measured
**side-effects / correlations** on other EmoNet emotions, VoiceNet dimensions, genuineness, vocal-burst blend
and speech quality. Data: per target × 5 conditions × 32 samples on neutral sentences.

Sections: **Emotions (40) — ready** · Edge cases · VoiceNet dimensions · Character voices *(planned)*.
