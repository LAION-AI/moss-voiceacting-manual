# MOSS-TTS-4.55B voice-acting-v2 — Conditioning Manual

A measured usage guide for `laion/moss-tts-local-transformer-4.55b-voice-acting-v2`.

- **Human / audio version (GitHub Pages):** https://laion-ai.github.io/moss-voiceacting-manual/
- **Agent-skill (Markdown, no audio):** [`md/index.md`](md/index.md)

For each target: the best prompting strategy **with and without** a LoRA, the best merge %, the expected
**reward** = (genuineness + vocal_burst_blend + 1.25·target_emotion) **× (1 − min(WER, 1))**, and the measured
**side-effects / correlations** on other EmoNet emotions, VoiceNet dimensions, genuineness, vocal-burst blend
and speech quality. Data: per target × 5 conditions × 32 samples on neutral sentences.

> The reward above was previously written as `/ (1 + WER)`. That form is **wrong** and has been
> corrected here: about three quarters of candidates have a *negative* core score, and dividing a
> negative number by a larger denominator makes it larger — so the division form rewards
> transcription errors on most of the pool. Confirmed twice, most recently on a 1,000-clip control
> set where a literal `WER × quality` filter put 602 of 1,000 candidates at exactly 0. Use
> `× (1 − min(WER, 1))` on sigmoid-squashed (strictly positive) components.

Sections: **Emotions (40) — ready** · Edge cases · VoiceNet dimensions · Character voices *(planned)*
· **[Vocal bursts, merge doses & how to evaluate a LoRA](md/recipes/bursts_merging_evaluation.md) — new**
· [Expressive & NSFW recipe book](md/recipes/expressive_nsfw.md).

`tools/md2site.py` renders `md/**.md` into the site's HTML style, so a page's Markdown mirror and
its HTML cannot drift apart.
