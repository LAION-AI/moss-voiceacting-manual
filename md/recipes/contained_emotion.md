# Contained / masked emotion — holding a strong feeling back

*Measured recipe page, added Aug 2026. Additive — nothing on the emotion, VoiceNet or
expressive/NSFW pages is retracted. This answers a target none of the other pages do:
how to make an **intense** emotion sound **held back** — contained, controlled, masked — rather
than simply **mild**. From a 4-round autonomous agent study on
`laion/moss-tts-local-transformer-4.55b-voice-acting-v2` (gpt-5.4 brain, Gemini judge).*

Mirrors of this page: [HTML](https://laion-ai.github.io/moss-voiceacting-manual/site/recipes/contained_emotion.html)
· [Markdown](https://github.com/LAION-AI/moss-voiceacting-manual/blob/main/md/recipes/contained_emotion.md).
The HTML is generated from the Markdown by [`tools/md2site.py`](https://github.com/LAION-AI/moss-voiceacting-manual/blob/main/tools/md2site.py),
so the two cannot drift apart.

---

## 0. Contained vs. free — and why "just turn it down" is the wrong instinct

A *free* (open) take lets the feeling out: an open outburst of rage, terror in every breath, grief
on the edge of tears. A *contained* (masked) take has the **same intensity underneath** but a
surface that is holding it in — cold level rage, forced calm over terror, grief swallowed and
deflected. The listener should hear a person **suppressing** a strong emotion, not a person feeling
a **weak** one.

The obvious first move — lower the emotion LoRA, or add "restrained / controlled / trying to hide
it" to the prompt — **does not work**, and the study proved it twice:

- **Round 1 (prompt cues) and Round 2 (heavy tension LoRAs) FAILED.** Both just **lowered the
  emotion output** — the take sounded *mild*, not *contained*. The feeling was gone, not held back.
- **VoiceNet *tension* did NOT separate contained from free.** Piling on `vn_TENS_high` reads as a
  tight, effortful voice, but a free scream is also tense. Tension alone is **not a suppression
  detector** (see §4 below).

## 1. The fix — emotional MASKING

The rounds that worked (3–4) keep the emotion LoRA **strong** and add a **thin masking layer** on
top. The feeling stays present; what drops is emotional **vulnerability** — the audible
touchability, the give in the voice that says the emotion is reaching the surface.

**The signature of a good contained take** — measured against a matched *free/open* take of the
same line (the free take uses `vn_VULN_high`):

- the **target emotion stays HIGH** (roughly equal to, or above, the free take — you have not
  merely turned it down), **and**
- the VoiceNet **VULN** (vulnerability) dimension drops **clearly below** the free take, **and**
- **Emotional_Numbness rises** (a cooler, more armoured surface).

That three-part contrast — *emotion held, VULN dropped, numbness up* — is the reliable read of
containment. A single number (tension, or even emotion alone) is not.

## 2. The general recipe (masking layer)

Start from the emotion's own best free recipe (see its per-emotion page), keep the emotion LoRA
strong, and add the masking layer. All doses are `λ` (merge strength); everything is **WER-gated**
— if a knob pushes WER up, back it off.

- **base emotion LoRA @ ~0.9–1.1** — keep the feeling strong; do **not** turn it down.
- **`vn_VULN_low` — the PRIMARY knob.** Reduces emotional touchability. This is what actually
  produces "held back". Tune it first; per-emotion best doses run **0.16 → 0.62**.
- **`Emotional_Numbness` LoRA @ ~0.1–0.3** — a cool, deadpan surface over the live feeling.
- **light `vn_TENS_high` @ ~0.1–0.4** — a little held muscular tension. **Light** — it is a garnish,
  not the mechanism (Round 2 proved tension alone fails).

Per-emotion specials layer on top of this (see §3.5, the masking toolbox):
distraction (`Concentration` / `vn_FOCS_high`), a lip-bite (`Pain` at a small dose), or "playing it
cool" casual/deadpan styles (`vn_S_CONV_high` / `vn_S_CASU_high`).

## 3. Per-emotion best recipes

Measured as the **contained − free gap** (matched line, matched voice; free take = same emotion with
`vn_VULN_high`). Emotion is *kept high*; VULN drops. Reward convention as elsewhere:
`(genu + blend + 1.25·emo)/(1+WER)`, WER-gated — but the *target* here is the contrast below, not a
single reward.

| emotion | contained recipe | emotion gap | **VULN gap** | other | verdict |
|---|---|--:|--:|---|---|
| **Anger** | `Anger@1.0 + vn_VULN_low@0.35 + Emotional_Numbness@0.3 + vn_TENS_high@0.4` | +0.13 | **−0.60** | TENS +0.22 | ✅ WORKS — cold, level, controlled rage instead of an open outburst |
| **Fear** | `Fear@1.02 + vn_VULN_low@0.16 + Emotional_Numbness@0.12 + vn_TENS_high@0.1` | +0.10 … +0.30 | **−0.42 … −0.55** | Numbness +0.11 | ✅ WORKS — forced-calm surface, terror alive underneath |
| **Sadness** | `Sadness@1.05 + vn_VULN_low@0.22 + Concentration@0.08` | ~kept | **−0.64 … −1.01** | biggest VULN effect | ✅ WORKS — grief held in, attention deflected outward |
| **Amusement** | `Amusement@0.98 + vn_VULN_low@0.62 + Emotional_Numbness + vn_TENS_high@0.32` | ~kept | **−0.79** | Numbness +0.25 | ⚠️ SEPARATES but damps the laugh; can read too tense/aggressive — being refined (Round 5) |

Notes per emotion:

- **Anger** — the cleanest result. A modest masking layer flips an open rant into cold, level,
  controlled rage: emotion actually goes **up** (+0.13) while VULN falls **−0.60**.
- **Fear** — a *very thin* layer is enough (VULN_low only 0.16). Gives a forced-calm surface with the
  terror still alive underneath; emotion is kept high (+0.10 to +0.30) and Numbness rises.
- **Sadness** — the biggest VULN drop of the four (**−0.64 to −1.01**), driven by adding
  **distraction** (`Concentration@0.08`): grief held in while the attention is deflected outward.
- **Amusement** — the **hardest**, because amusement intensity and the muscular effort of laughing
  are acoustically entangled — masking the effort tends to mask the laugh. **Weak masking failed
  (Round 3).** Only **strong** masking (`vn_VULN_low@0.62`) finally separated it (VULN −0.79,
  Numbness +0.25), but it damps the laugh more and can tip into sounding **too tense / aggressive**.
  See §5 (Round 5, in progress).

## 3.5 Specials — the masking toolbox

Reach for these on top of the general recipe:

- **`vn_VULN_low` — reduce emotional touchability. The PRIMARY knob.** If you tune one thing, tune
  this. It is what turns *mild* into *held back*.
- **`Emotional_Numbness` LoRA — cool / deadpan surface.** A thin armour over the live feeling; the
  reason Numbness *rises* in a good contained take.
- **`Concentration` / `vn_FOCS_high` — distraction.** "I'm focused on something else, not on how I
  feel." **Helped Sadness the most** — attention deflected outward reads as grief held in.
- **`Pain` LoRA at a small dose — biting the lip.** A trace of physical effort/discomfort reads as
  *suppression* rather than absence. **Helps Amusement** (holding a laugh in).
- **Casual / deadpan styles — `vn_S_CONV_high` / `vn_S_CASU_high` — "playing it cool."** A
  conversational, offhand register that flattens the emotional surface without killing the emotion.

## 4. Honest limits

- **VoiceNet *tension* alone is NOT a reliable suppression detector.** A held-back voice is tense —
  but so is a free scream. Do not score containment on tension, and do not try to *produce* it with
  tension alone (Round 2 failed exactly this way).
- **The reliable signal is the signature, not a single number:** target emotion **stays high** +
  **VULN drops** (vs a matched `vn_VULN_high` free take) + **Numbness up**. Always measure against a
  matched free take of the same line and voice — containment is a *contrast*, not an absolute.
- **Entangled emotions resist masking.** Where the emotion's intensity and its physical production
  share acoustics (Amusement ↔ effort of laughing), masking the surface also mutes the emotion, and
  you need a stronger layer — at the cost of blend and a tenser read.
- **Everything is WER-gated.** The masking layer stacks 3–4 adapters; watch intelligibility and back
  off any knob that pushes WER up. Keep lines short.

## 5. Further work — Round 5 (in progress)

Round 5 refinements are underway and extend the method:

- **To MODERATE intensity** — containment of a moderate, not only an extreme, feeling.
- **Optimising for higher genuineness + blend and lower WER**, so a contained take is not just
  separable but pleasant and intelligible.
- **Amusement specifically** is being re-worked toward a deadpan *"trying not to laugh"* that stays
  **genuine**: `Emotional_Numbness` + `Pain` (the lip-bite) + a **warm / soft** base + **LOW**
  tension — the opposite of the tense/aggressive read that Round 4's strong masking produced.

## See also

- Per-emotion conditioning manual (free/open recipes to start from): [../emotions/index.md](../emotions/index.md)
  — [Anger](../emotions/Anger.md) · [Fear](../emotions/Fear.md) · [Sadness](../emotions/Sadness.md) · [Amusement](../emotions/Amusement.md)
- VoiceNet dimension manual (VULN, TENS, FOCS, casual styles): https://laion-ai.github.io/moss-voicenet-manual/
- Emotional_Numbness page: [../emotions/Emotional_Numbness.md](../emotions/Emotional_Numbness.md) · Pain page: [../emotions/Pain.md](../emotions/Pain.md)
- The flagship intensity × containment study (6 voices × 40 emotions × 4 conditions): https://laion-ai.github.io/emotion-voice-conditions/

---
[← Manual hub](../index.md)
