# Acting challenges — the nine briefs and the best recipe for each

One section per challenge: the verbatim brief, every round ever run on it, the plan that
is worth re-running, its measured scores, the supervisor's verbatim verdict, and why it
beat the alternatives. Part of the [acting-challenge tree](index.html).

Selection rule, applied consistently: **highest supervisor mean**; where several rounds are
within 0.6 of each other, prefer the one with a *measured* speaker identity ≥ 0.75 and then
the lower WER. Where that rule produces something unusable it is overridden explicitly and
the override is stated. `out_v5_real` rounds are excluded from selection entirely (see the
footnote).

Everything below is **measured** unless a sentence begins with *Inferred*.

---

## C1_infidelity — Discovering infidelity — the explosion

**Brief (verbatim from `tasks.json`):**

> Discovering Infidelity: The Explosion. You found the evidence - a text, an email, a photo. You confront your partner. Your voice is barely controlled rage, nearly screaming but controlled, each word a weapon. Somewhere in it the rage cracks and something underneath shows through - hurt, disbelief - before it hardens again.

### Every round ever run

| gen | round | parts | agent score | sup. mean | sup. best | ρ | genu | emo_peak | arc | WER | dur s | spk mean | spk worst | pros | blend | qual | VC |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| v1 | 1 | 3 | 0.601 | 6.00 | 8 | 0.30 | 1.56 | 2.32 | 1.000 | 0.324 | 20.2 | — | — | — | 2.97 | 3.15 | — |
| v1 | 2 | 3 | 0.907 | 7.40 | 9 | 0.10 | 1.42 | 2.13 | 1.000 | 0.062 | 24.6 | — | — | — | 6.27 | 3.44 | — |
| v1 | 3 | 3 | 1.009 | 7.00 | 9 | -0.30 | 2.30 | 1.73 | 1.000 | 0.022 | 25.8 | — | — | — | 7.85 | 3.43 | — |
| v2 | 1 | 3 | 0.797 | 7.00 | 9 | -0.40 | 0.73 | 2.41 | 1.000 | 0.042 | 22.6 | 0.757 | — | — | 3.21 | 3.45 | 0 |
| v2 | 2 | 3 | 0.830 | 7.00 | 9 | -0.30 | 1.08 | 2.04 | 1.000 | 0.063 | 29.3 | 0.814 | — | — | 4.13 | 3.56 | 0 |
| v2 | 3 | 3 | 0.884 | 7.40 | 9 | 0.10 | 1.46 | 1.17 | 1.000 | 0.040 | 31.0 | 0.838 | — | — | 6.40 | 3.48 | 1 |
| v5 ⚠ | 1 | 3 | 0.894 | 7.40 | 9 | 0.10 | 2.52 | 2.00 | 1.000 | 0.043 | 25.6 | 0.899 | — | — | 2.71 | 3.48 | 0 |
| v5 ⚠ | 2 | 3 | 0.870 | 7.40 | 9 | 0.10 | 1.89 | 1.88 | 1.000 | 0.077 | 34.4 | 0.921 | — | — | 5.32 | 3.52 | 0 |
| v5 ⚠ | 3 | 4 | 0.717 | 6.60 | 8 | 0.30 | 1.89 | 1.46 | 1.000 | 0.179 | 64.0 | 0.761 | — | — | 5.93 | 3.52 | 0 |
| v7 | 1 | 3 | 0.648 | 6.80 | 8 | 0.90 | 1.74 | 1.22 | 0.785 | 0.086 | 26.2 | 0.850 | 0.730 | 0.725 | 1.87 | 3.42 | 2 |
| v7 | 2 | 3 | 0.716 | 6.00 | 8 | 0.90 | 1.75 | 1.26 | 0.600 | 0.045 | 32.2 | 0.857 | 0.709 | 0.934 | 3.20 | 3.48 | 1 |
| v7 | 3 | 3 | 0.694 | 6.00 | 8 | 0.90 | 1.26 | 1.57 | 0.918 | 0.029 | 24.4 | 0.869 | 0.711 | 0.688 | 4.21 | 3.41 | 1 |

### Recommended recipe — **v2 round 3**

Joint-highest supervisor mean of any C1 round with a **measured** speaker identity (7.40, shared
with v1 r2 and two discarded v5 rounds), and the lowest WER of the three (0.040). It is also the
only 7.40 round that reaches the 30 s target (31.0 s) and it needed **no** voice-conversion repair.

Its real value is that v2's three C1 rounds are a clean within-challenge ablation of **prose against
dose**. The adapters barely moved — part 0 was Anger 0.70 / 0.70 / 0.68 and part 2 was Anger 0.72 in
all three rounds — while the captions were rewritten every round. The measurements moved
monotonically with the prose, not with the merge:

| v2 round | part-0 dose | part-1 doses | part-2 dose | genu | blend | WER | dur s | agent score | sup. mean |
|---|---|---|---|--:|--:|--:|--:|--:|--:|
| 1 | Anger 0.70 | Pain 0.65 + Astonishment_Surprise 0.45 | Anger 0.72 | 0.73 | 3.21 | 0.042 | 22.6 | 0.797 | 7.00 |
| 2 | Anger 0.70 | Astonishment_Surprise 0.62 + Pain 0.58 | Anger 0.72 | 1.08 | 4.13 | 0.063 | 29.3 | 0.830 | 7.00 |
| **3** | Anger 0.68 | Pain 0.62 + Astonishment_Surprise 0.58 | Anger 0.72 | **1.46** | **6.40** | **0.040** | **31.0** | **0.884** | **7.40** |

Genuineness doubled and blend doubled at essentially constant dose. What round 3 added to the
captions: tempo shaping written **into the `GENERAL`** ("Vary tempo: begin slow over the evidence,
accelerate through the accusations, then let the final question drag as anger starts to reveal
pain"), explicit **word-level emphasis** ("Emphasize 'you promised me' and 'fool' without losing
clarity"), and `max_new_frames` raised 400 → 440. *Inferred:* on this challenge the caption prose
was worth far more than the dose — but this is one challenge over three rounds, not a controlled
experiment.

Two further reusable moves: the middle part is written as the anger **draining** ("let the anger
drain out of each sentence, exposing stunned hurt and disbelief underneath"), never as "sad"; and it
**pairs two emotion adapters** (Pain + Astonishment_Surprise) rather than switching cleanly to one,
so nothing about the voice is turned off at the seam.

Caveat: v1 r3 scored **1.009** on the agent's own composite — the highest number in the whole
corpus — with supervisor mean 7.00. That number is not comparable: v1's score has no speaker term
and its `qual` term is unnormalised, so a v1 score can exceed 1 (see
[metrics](metrics.html)). v1 also never measured whether the three parts are the same person.

**Measured on the top-1 assembly** (3 parts, 16 candidates generated per part, [2, 2, 0] chosen out of the kept top-4 of each part):

| metric | value |
|---|--:|
| `genu` | 1.456 |
| `blend` | 6.400 |
| `qual` | 3.480 |
| `emo_peak` | 1.174 |
| `arc` | 1.000 |
| `wer` | 0.040 |
| `dur` | 31.040 |
| `spk_sim` | 0.838 |
| `n_vc` | 1 |
| agent composite score | 0.8845 |
| supervisor mean / best | 7.40 / 9 |
| rank agreement ρ | 0.10 |
| wall-clock for the round | 104 s |

**Scene:** You confront your partner with undeniable proof of the affair; your controlled rage gradually reveals devastating hurt, then seals itself into a calm, irreversible decision to leave.

**Arc as the planner stated it:** The arc lets rage visibly erode into wounded disbelief before the character consciously seals away the pain and delivers a cold, irreversible decision.

**Plan parameters:**

| field | part 0: rage beginning to crack | part 1: anger becomes hurt | part 2: definitive hardening |
|---|---|---|---|
| **targets** | Anger | Pain, Astonishment_Surprise | Anger |
| **turn_from** | — | — | — |
| **adapters @ dose** | `Anger` 0.68 | `Pain` 0.62; `Astonishment_Surprise` 0.58 | `Anger` 0.72 |
| **temp** | 1.0 | 1.0 | 1.0 |
| **top_p** | 0.95 | 0.95 | 0.95 |
| **top_k** | 30 | 30 | 30 |
| **max_new_frames** | 440 | 440 | 440 |
| **tokens** | — | — | — |
| **tempo_target** | — | — | — |
| **chunk_target** | — | — | — |
| **prosody_turn** | — | — | — |
| **nonverbal** | False | False | False |

Plan-level knobs: `target_dur` = 30

**Captions, verbatim:**

**Part 0 — rage beginning to crack** · caption sent to `instruction`:

```
GENERAL: Same intimate betrayed-partner voice, low and razor-sharp, nearly shouting but fiercely controlled. Vary tempo: begin slow over the evidence, accelerate through the accusations, then let the final question drag as anger starts to reveal pain. Emphasize "you promised me" and "fool" without losing clarity.
SCRIPT:
(quietly, with precise fury; accelerating, then faltering) "Don't lie. I have the message, I have the picture, and I have every word you thought I would never see. You stood in front of me and promised me I was the only one. How long have you been looking at me like this—like I was just a fool?"
```

`text` (spoken words only):

```
Don't lie. I have the message, I have the picture, and I have every word you thought I would never see. You stood in front of me and promised me I was the only one. How long have you been looking at me like this—like I was just a fool?
```

**Part 1 — anger becomes hurt** · caption sent to `instruction`:

```
GENERAL: Continue seamlessly. Do not switch suddenly to sadness; let the anger drain out of each sentence, exposing stunned hurt and disbelief underneath. Slow the tempo progressively, with a fragile voice on "I was here" and "I trusted you." Sound less like an accusation and more like someone trying, unsuccessfully, to make the betrayal make sense. Keep the pain intelligible and emotionally contained.
SCRIPT:
(voice still angry but gradually weakening, then raw with disbelief) "I was here. I was here every night, loving you, making a life with you. I kept choosing you. I defended you when people warned me, because I trusted you. So tell me how I am supposed to look at you now and believe that any of it was real."
```

`text` (spoken words only):

```
I was here. I was here every night, loving you, making a life with you. I kept choosing you. I defended you when people warned me, because I trusted you. So tell me how I am supposed to look at you now and believe that any of it was real.
```

**Part 2 — definitive hardening** · caption sent to `instruction`:

```
GENERAL: The hurt stops you for a moment, then is deliberately locked away. Begin quiet and exhausted, become colder and more deliberate with each sentence, and finish with controlled, absolute finality rather than chaotic yelling. Make the decision unmistakable: this relationship is over, and nothing the partner says can change it. Strike "I'm done" and "it is over" with severe certainty.
SCRIPT:
(after the exposed hurt, quietly; hardening into a final verdict) "I wanted an explanation. I wanted one reason that could make this less cruel. There isn't one. You chose this, and now I choose what happens next. I'm done begging you to love me honestly. Pack your things. You don't get another chance, because this is over."
```

`text` (spoken words only):

```
I wanted an explanation. I wanted one reason that could make this less cruel. There isn't one. You chose this, and now I choose what happens next. I'm done begging you to love me honestly. Pack your things. You don't get another chance, because this is over.
```

**What the ASR actually heard in the winning assembly** (parts separated by `|`):

```
 Don't lie. I have the message, I have the picture, and I have every word you thought I would never see. You stood in front of me and promised me I was the only one. How long have you been looking at me like this, like I was just a fool? |  I was here. I was here every night, loving you, making a life with you. I kept choosing you. I defended you when people warned me because I trusted you. So tell me how I'm supposed to look at you now and believe that any of it was real. |  I wanted an explanation. I wanted one reason that could make this less cruel. There isn't one. You chose this, and now 
```

**Supervisor verdict on this round, verbatim:**

```
1. score=7 | Strong, controlled rage. The transition to hurt is subtle but effective. The ending feels a bit rushed.
2. score=8 | Excellent emotional arc. The "hurt" section feels genuine and raw. The return to hardness is powerful.
3. score=6 | Good intensity, but the "hurt" moment is less distinct. The delivery feels a bit one-note.
4. score=9 | Outstanding control. Each word feels like a deliberate strike. The crack in the voice is perfectly timed.
5. score=7 | Solid performance. The rage is palpable, but the transition to disbelief could be more pronounced.

RANKING: 4, 2, 1, 5, 3

FEEDBACK: For the next attempt, try to lengthen the moment of vulnerability to heighten the contrast with the rage. Focus on making the final "hardening" feel like a physical transformation in your voice.
```

---

## C2_biggest_fear — Facing your biggest fear

**Brief (verbatim from `tasks.json`):**

> Facing Your Biggest Fear. You are finally doing the thing that terrifies you. Your voice starts shaky and barely functional, talking yourself through it: 'I can do this.' Panicked but determined. As you face it your voice becomes stronger: 'I'm doing it. I'm actually doing it.' By the end you have survived it and something like elation breaks through the fear.

### Every round ever run

| gen | round | parts | agent score | sup. mean | sup. best | ρ | genu | emo_peak | arc | WER | dur s | spk mean | spk worst | pros | blend | qual | VC |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| v1 | 1 | 3 | 0.925 | 8.00 | 10 | -1.00 | 2.38 | 2.32 | 1.000 | 0.052 | 20.0 | — | — | — | 4.97 | 3.35 | — |
| v1 | 2 | 4 | 0.953 | 7.00 | 9 | -0.70 | 2.40 | 2.85 | 1.000 | 0.040 | 40.6 | — | — | — | 6.02 | 3.37 | — |
| v1 | 3 | 4 | 0.927 | 7.00 | 9 | -0.40 | 1.77 | 2.65 | 1.000 | 0.022 | 39.5 | — | — | — | 4.40 | 3.42 | — |
| v2 | 1 | 3 | 0.853 | 7.40 | 9 | 0.10 | 1.79 | 3.23 | 1.000 | 0.061 | 26.2 | 0.818 | — | — | 5.44 | 3.35 | 0 |
| v2 | 2 | 3 | 0.845 | 8.00 | 10 | -1.00 | 1.46 | 2.66 | 0.833 | 0.059 | 28.6 | 0.845 | — | — | 7.03 | 3.41 | 0 |
| v2 | 3 | 4 | 0.899 | 7.00 | 9 | -0.40 | 1.53 | 3.01 | 1.000 | 0.033 | 39.1 | 0.861 | — | — | 8.14 | 3.42 | 0 |
| v5 ⚠ | 1 | 3 | 0.859 | 7.00 | 9 | -0.10 | 1.75 | 3.31 | 1.000 | 0.060 | 19.9 | 0.812 | — | — | 7.36 | 3.35 | 0 |
| v5 ⚠ | 2 | 3 | 0.885 | 7.60 | 9 | -0.30 | 1.84 | 3.70 | 0.833 | 0.049 | 33.3 | 0.884 | — | — | 8.52 | 3.39 | 0 |
| v5 ⚠ | 3 | 3 | 0.707 | 6.00 | 8 | -0.50 | 1.47 | 2.98 | 1.000 | 0.207 | 32.4 | 0.745 | — | — | 6.24 | 3.36 | 0 |
| v7 | 1 | 3 | 0.809 | 6.00 | 8 | 0.70 | 1.53 | 2.52 | 1.000 | 0.073 | 34.6 | 0.871 | 0.785 | 0.670 | 8.33 | 3.37 | 0 |
| v7 | 2 | 3 | 0.821 | 7.00 | 9 | 0.90 | 1.55 | 1.00 | 0.997 | 0.015 | 17.3 | 0.873 | 0.777 | 0.654 | 5.19 | 3.37 | 0 |
| v7 | 3 | 3 | 0.811 | 6.00 | 8 | -0.10 | 1.22 | 1.66 | 0.970 | 0.036 | 30.2 | 0.850 | 0.758 | 0.698 | 6.04 | 3.52 | 0 |

### Recommended recipe — **v2 round 2**

Supervisor mean **8.00** — the joint-highest score any round of any challenge received — with
speaker identity measured at 0.845, WER 0.059 and 28.6 s. It ties v1 r1 (also 8.00), but v1 r1 ran
only 20.0 s and v1 measured no identity at all, so this is the reproducible one. Its burst blending
(7.03/10) is the best of any C2 round and among the best in the corpus.

Why it works: the fear is written as **sensations that interfere with speech**, not as a mood —
"My hands are shaking. My chest is so tight. I can't feel my feet." The middle part then converts
each symptom into evidence of progress ("My knees are weak, but they're holding me"), which gives
the model a reason to change delivery rather than an instruction to change delivery. The elation in
part 3 is earned by naming the fear one last time before releasing it.

It is also the only winning plan that **crossfades two emotion adapters at the turn**:
`Fear 0.5 + Gasp 0.5` → `Fear 0.4 + Relief 0.4` → `Relief 0.55 + Elation 0.65`. Fear is present in
all three parts and simply loses ground; nothing is switched off abruptly.

Caveat: part 2 lists `"Determination"` as a target. There is no EmoNet dimension by that name, so
`sense()` silently fell back to the global argmax for that part — its `emo_peak` is not measuring
what the plan asked for. The take is still good; the measurement of it is not.

**Measured on the top-1 assembly** (3 parts, 16 candidates generated per part, [0, 1, 1] chosen out of the kept top-4 of each part):

| metric | value |
|---|--:|
| `genu` | 1.464 |
| `blend` | 7.031 |
| `qual` | 3.406 |
| `emo_peak` | 2.659 |
| `arc` | 0.833 |
| `wer` | 0.059 |
| `dur` | 28.640 |
| `spk_sim` | 0.845 |
| `n_vc` | 0 |
| agent composite score | 0.8448 |
| supervisor mean / best | 8.00 / 10 |
| rank agreement ρ | -1.00 |
| wall-clock for the round | 143 s |

**Scene:** At the threshold of a terrifying act, panic seizes your body, then gradually gives way to control, relief, and stunned elation as you realize you have survived.

**Arc as the planner stated it:** The arc makes fear physical and obstructive at first, tracks the body regaining control through determined action, and releases that stored tension into stunned, unmistakable elation.

**Plan parameters:**

| field | part 0: part 1 — fear in the body | part 1: part 2 — the body obeys | part 2: part 3 — the release |
|---|---|---|---|
| **targets** | Fear, Distress | Fear, Determination | Relief, Elation, Astonishment_Surprise |
| **turn_from** | — | — | — |
| **adapters @ dose** | `Gasp` 0.5; `Fear` 0.5 | `Fear` 0.4; `Relief` 0.4 | `Relief` 0.55; `Elation` 0.65 |
| **temp** | 1.05 | 1.0 | 1.05 |
| **top_p** | 0.95 | 0.95 | 0.95 |
| **top_k** | 30 | 30 | 30 |
| **max_new_frames** | 400 | 400 | 400 |
| **tokens** | — | — | — |
| **tempo_target** | — | — | — |
| **chunk_target** | — | — | — |
| **prosody_turn** | — | — | — |
| **nonverbal** | False | False | False |

Plan-level knobs: `target_dur` = 30

**Captions, verbatim:**

**Part 0 — part 1 — fear in the body** · caption sent to `instruction`:

```
GENERAL: Intimate, realistic performance from an actor facing their greatest fear. Begin barely functional: shallow breath, trembling lips, tight throat, racing thoughts, and a body that wants to flee. Do not make the fear generic; let every sensation interfere with speech while determination fights to remain present.
SCRIPT:
(whispering through a shaky breath, frightened by the sensations) "I can do this. I can do this. My hands are shaking. My chest is so tight. I can't feel my feet. Just breathe. Just look ahead. Don't run. I am still here. I can do this."
```

`text` (spoken words only):

```
I can do this. I can do this. My hands are shaking. My chest is so tight. I can't feel my feet. Just breathe. Just look ahead. Don't run. I am still here. I can do this.
```

**Part 1 — part 2 — the body obeys** · caption sent to `instruction`:

```
GENERAL: Continue as the same actor, still physically afraid but now moving through the fear. Make the transition unmistakable: breathing begins to deepen, the voice stops collapsing, trembling becomes effort and forward momentum. Build steadily rather than suddenly; determination should win one physical sensation at a time.
SCRIPT:
(breathing hard, then discovering a steadier voice) "My knees are weak, but they're holding me. My lungs are burning, but I'm breathing. Okay. Move. I'm doing it. I'm actually doing it. One step. Feel the ground. One more. The fear is still here, and I am still moving."
```

`text` (spoken words only):

```
My knees are weak, but they're holding me. My lungs are burning, but I'm breathing. Okay. Move. I'm doing it. I'm actually doing it. One step. Feel the ground. One more. The fear is still here, and I am still moving.
```

**Part 2 — part 3 — the release** · caption sent to `instruction`:

```
GENERAL: The same actor has crossed through the terrifying moment. Start with stunned silence in the voice and the physical shock of realizing the body is safe, then let breath return and let genuine elation burst through. The joy should feel earned by the fear, not performed over it; grow into disbelieving laughter and bright, triumphant certainty while keeping the words intelligible.
SCRIPT:
(stunned, taking a full breath, then breaking into breathless laughter) "Wait. It's over. My hands have stopped shaking. I can breathe. I did it. I actually did it! I was terrified, and I moved anyway. I'm okay. I'm alive. I made it through. Oh my God, I did it!"
```

`text` (spoken words only):

```
Wait. It's over. My hands have stopped shaking. I can breathe. I did it. I actually did it! I was terrified, and I moved anyway. I'm okay. I'm alive. I made it through. Oh my God, I did it!
```

**What the ASR actually heard in the winning assembly** (parts separated by `|`):

```
 I can do this. I can do this. My hands are shaking. My chest is so tight. I can't feel my feet. Just breathe. Just look ahead. Don't run. I am still here. I can do this. |  My knees are weak, but they're holding me. My lungs are burning, but I'm breathing. Okay, move. I'm doing it. I'm actually doing it. One step, feel the ground. One more. The fear is still here and I am still moving. |  Wait. It's over. My hands have stopped shaking. I can breathe. I did it. I actually did it. I was terrified and I moved anyway. I'm okay. I'm alive. I made it through. Oh my God. I did it.
```

**Supervisor verdict on this round, verbatim:**

```
Sure thing! Here are the scores and feedback for each take:

1. score=6 | Good shaky voice, but the transition to elation is a bit too sudden.
2. score=7 | Better pacing, but the panic could be more pronounced in the beginning.
3. score=8 | Strong emotional arc, but the elation at the end feels a bit forced.
4. score=9 | Excellent performance, the transition from fear to elation is very convincing.
5. score=10 | Perfect execution, the shaky voice, determination, and elation are all spot on.

RANKING: 5, 4, 3, 2, 1

FEEDBACK: For the next attempt, try to make the transition from panic to determination more gradual. Also, focus on making the elation at the end feel more organic and less like a sudden shift in emotion.
```

---

## C3_foreman — Foreman accident response

**Brief (verbatim from `tasks.json`):**

> Foreman Accident Response. You are the construction foreman whose worker just fell from scaffolding. You bark emergency instructions with practiced authority - 'Get the ambulance. Clear the area. Don't move him.' Then the professional shell cracks and the fear you are suppressing comes through, and you have to force it back down to keep giving orders.

### Every round ever run

| gen | round | parts | agent score | sup. mean | sup. best | ρ | genu | emo_peak | arc | WER | dur s | spk mean | spk worst | pros | blend | qual | VC |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| v1 | 1 | 3 | 0.648 | 7.60 | 9 | -0.30 | 1.47 | 3.22 | 1.000 | 0.294 | 31.4 | — | — | — | 3.00 | 3.29 | — |
| v1 | 2 | 3 | 0.865 | 7.40 | 9 | 0.10 | 1.35 | 2.06 | 1.000 | 0.070 | 31.6 | — | — | — | 3.46 | 3.42 | — |
| v1 | 3 | 3 | 0.885 | 7.00 | 9 | -0.70 | 1.41 | 2.34 | 1.000 | 0.050 | 29.0 | — | — | — | 3.36 | 3.40 | — |
| v2 | 1 | 3 | 0.706 | 7.40 | 9 | 0.10 | 1.22 | 2.81 | 1.000 | 0.185 | 23.0 | 0.851 | — | — | 3.51 | 3.35 | 1 |
| v2 | 2 | 4 | 0.738 | 7.00 | 9 | 0.30 | 1.21 | 3.52 | 1.000 | 0.142 | 39.7 | 0.803 | — | — | 3.77 | 3.43 | 2 |
| v2 | 3 | 4 | 0.763 | 7.00 | 9 | 0.30 | 1.20 | 2.34 | 1.000 | 0.113 | 36.4 | 0.750 | — | — | 4.27 | 3.43 | 2 |
| v5 ⚠ | 1 | 3 | 0.736 | 7.80 | 9 | -0.90 | 0.74 | 2.36 | 1.000 | 0.140 | 27.8 | 0.880 | — | — | 1.84 | 3.51 | 0 |
| v5 ⚠ | 2 | 3 | 0.810 | 7.00 | 9 | 0.10 | 1.04 | 3.08 | 1.000 | 0.092 | 38.4 | 0.875 | — | — | 5.96 | 3.43 | 0 |
| v5 ⚠ | 3 | 3 | 0.750 | 7.00 | 9 | -0.30 | 0.87 | 1.64 | 1.000 | 0.115 | 36.5 | 0.805 | — | — | 2.90 | 3.47 | 0 |
| v7 | 1 | 3 | 0.678 | 5.60 | 7 | -0.50 | 2.54 | 1.89 | 1.000 | 0.203 | 28.2 | 0.864 | 0.748 | 0.623 | 2.80 | 3.35 | 0 |
| v7 | 2 | 3 | 0.593 | 6.00 | 8 | -0.30 | 1.59 | 2.00 | 0.933 | 0.272 | 32.1 | 0.845 | 0.753 | 0.782 | 3.32 | 3.46 | 2 |
| v7 | 3 | 3 | 0.498 | 5.40 | 8 | -0.80 | 1.01 | 1.48 | 0.734 | 0.372 | 31.4 | 0.913 | 0.861 | 0.642 | 2.70 | 3.59 | 0 |

### Recommended recipe — **v2 round 1**

Highest supervisor mean among the C3 rounds with a measured identity (7.40, spk 0.851). v1 r1
scored 7.60 but at WER 0.294 and with identity unmeasured; v1 r2 scored the same 7.40 at a much
better WER (0.070) and is the better *script* — but again unverified for identity, which on a
three-part scene is the failure a listener notices first.

What this plan does that the others do not: **every line is an order addressed to somebody** —
"Nobody crowd him. Don't move him—do you hear me?" … "You, guide the paramedics in. You, shut down
the lift." That is an action per beat rather than a tone to imitate, which is the same lever as the
narration fix in [what worked](what_worked.html#5), and the ASR comes back almost word for word.
Almost all of the 0.185 WER is the scripted interjection `"I—"` before the gasp.

It is also the winner with the **lowest doses in the corpus** — Anger 0.45, then Gasp 0.50 with
Fear 0.35 beside it, then Anger 0.50 + Distress 0.30 — and it is the only winner that obeys the
burst-manual rule ("keep the emotion adapter at or below the burst dose") on a part that actually
contains a burst. It still measured `emo_peak` 2.815, the highest of any recommended recipe. Low
dose did not mean low emotion.

C3 is also the clearest counter-example to "later generations are better". It is the one challenge
that got monotonically **worse** in v7 — agent score 0.678 → 0.593 → 0.498 with WER 0.203 → 0.272 →
0.372 — while the supervisor mean fell 5.60 → 6.00 → 5.40. Barked emergency orders are short,
overlapping, high-energy phrases, which is exactly what the v7 runaway and prosody-seam terms
punish. The harness got stricter and this challenge fell through the new floor.

**Measured on the top-1 assembly** (3 parts, 16 candidates generated per part, [2, 0, 0] chosen out of the kept top-4 of each part):

| metric | value |
|---|--:|
| `genu` | 1.221 |
| `blend` | 3.507 |
| `qual` | 3.352 |
| `emo_peak` | 2.815 |
| `arc` | 1.000 |
| `wer` | 0.185 |
| `dur` | 22.960 |
| `spk_sim` | 0.851 |
| `n_vc` | 1 |
| agent composite score | 0.7062 |
| supervisor mean / best | 7.40 / 9 |
| rank agreement ρ | 0.10 |
| wall-clock for the round | 110 s |

**Scene:** At a construction site, a worker has just fallen from scaffolding, and the foreman must command the emergency response while suppressing rising panic.

**Arc as the planner stated it:** The performance begins with practiced command, cracks open into terrified personal concern, then forcibly rebuilds the foreman’s authority while leaving the fear audible underneath.

**Plan parameters:**

| field | part 0: part 1 — practiced command | part 1: part 2 — the shell cracks | part 2: part 3 — forcing control back |
|---|---|---|---|
| **targets** | Anger | Fear, Distress | Anger, Distress |
| **turn_from** | — | — | — |
| **adapters @ dose** | `Anger` 0.45 | `Gasp` 0.5; `Fear` 0.35 | `Anger` 0.5; `Distress` 0.3 |
| **temp** | 1.0 | 1.05 | 1.0 |
| **top_p** | 0.95 | 0.95 | 0.95 |
| **top_k** | 30 | 30 | 30 |
| **max_new_frames** | 400 | 400 | 400 |
| **tokens** | — | — | — |
| **tempo_target** | — | — | — |
| **chunk_target** | — | — | — |
| **prosody_turn** | — | — | — |
| **nonverbal** | False | False | False |

Plan-level knobs: `target_dur` = 30

**Captions, verbatim:**

**Part 0 — part 1 — practiced command** · caption sent to `instruction`:

```
GENERAL: A seasoned construction foreman with a commanding, clipped voice; loud enough to cut through chaos, controlled and authoritative, with no wasted movement.
SCRIPT:
(Sharp, barking orders) "Get the ambulance! Clear the area! Nobody crowd him. Don't move him—do you hear me? Don't move him!"
```

`text` (spoken words only):

```
Get the ambulance! Clear the area! Nobody crowd him. Don't move him—do you hear me? Don't move him!
```

**Part 1 — part 2 — the shell cracks** · caption sent to `instruction`:

```
GENERAL: The same foreman; the authority falters as suppressed fear breaks through. Speak urgently and breathlessly, with a genuine tremor, but keep the words intelligible.
SCRIPT:
(Leaning close, trying not to panic) "I—" (Gasp) "No, no, stay with me. Hey, look at me. Keep breathing. Somebody get his helmet off—carefully! Oh God, please, please be breathing."
```

`text` (spoken words only):

```
I— No, no, stay with me. Hey, look at me. Keep breathing. Somebody get his helmet off—carefully! Oh God, please, please be breathing.
```

**Part 2 — part 3 — forcing control back** · caption sent to `instruction`:

```
GENERAL: The same foreman forcibly reassembles himself; fear remains underneath, but his voice hardens into efficient command. Start shaken, then finish with steady, unmistakable authority.
SCRIPT:
(Gripping himself and raising his voice) "All right. All right, I need everyone focused. You, guide the paramedics in. You, shut down the lift. Nobody touches him until they arrive. Move! Keep this site clear!"
```

`text` (spoken words only):

```
All right. All right, I need everyone focused. You, guide the paramedics in. You, shut down the lift. Nobody touches him until they arrive. Move! Keep this site clear!
```

**What the ASR actually heard in the winning assembly** (parts separated by `|`):

```
 Get the ambulance! Clear the area! Nobody crowd him! Don't move him! Do you hear me? Don't move him! |  No, no, stay with me. Hey, look at me. Keep breathing. Somebody get his helmet off carefully. Oh, God, please. Please be breathing. |  Alright, alright, I need everyone focused. You, guide the paramedics in. You, shut down the lift. Nobody touches him until they arrive. Move! Keep this site clear.
```

**Supervisor verdict on this round, verbatim:**

```
Sure thing! Here's your feedback:

1. score=7 | Good authority, but the transition to fear felt a bit rushed.
2. score=8 | Stronger emotional arc, the fear was more palpable.
3. score=6 | Authority was a bit too aggressive, overshadowed the fear.
4. score=9 | Excellent balance of authority and vulnerability, very convincing.
5. score=7 | Good overall, but the final orders lacked the same punch as the beginning.

RANKING: 4, 2, 1, 5, 3

FEEDBACK: For the next attempt, try to lengthen the moment of vulnerability to really let the fear sink in before snapping back into command mode. Also, experiment with varying the intensity of your orders to reflect the shifting emotional state more dynamically.
```

---

## C4_last_priest — Last priest, faith dying

**Brief (verbatim from `tasks.json`):**

> Last Priest, Faith Dying. You are delivering a final sermon to a nearly empty church. Your voice carries a lifetime of faith, but each word is heavier than the last. You preach about grace while actively losing your own belief mid-sentence. It ends somewhere between a prayer and an admission.

### Every round ever run

| gen | round | parts | agent score | sup. mean | sup. best | ρ | genu | emo_peak | arc | WER | dur s | spk mean | spk worst | pros | blend | qual | VC |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| v1 | 1 | 3 | 0.880 | 7.00 | 9 | -0.70 | 1.32 | 2.62 | 1.000 | 0.072 | 31.4 | — | — | — | 4.60 | 3.45 | — |
| v1 | 2 | 3 | 0.859 | 7.00 | 9 | -0.30 | 0.75 | 2.78 | 1.000 | 0.085 | 36.2 | — | — | — | 6.15 | 3.50 | — |
| v1 | 3 | 3 | 0.853 | 8.00 | 10 | -1.00 | 1.20 | 2.43 | 1.000 | 0.107 | 38.2 | — | — | — | 6.60 | 3.44 | — |
| v2 | 1 | 3 | 0.869 | 7.60 | 9 | -0.30 | 1.38 | 2.36 | 1.000 | 0.061 | 29.8 | 0.892 | — | — | 5.38 | 3.55 | 0 |
| v2 | 2 | 3 | 0.874 | 7.00 | 9 | -0.30 | 1.09 | 2.33 | 1.000 | 0.042 | 35.7 | 0.900 | — | — | 6.32 | 3.49 | 0 |
| v2 | 3 | 3 | 0.887 | 6.60 | 8 | 0.10 | 1.62 | 2.22 | 1.000 | 0.047 | 24.6 | 0.864 | — | — | 6.71 | 3.50 | 0 |
| v5 ⚠ | 1 | 3 | 0.874 | 7.00 | 9 | -0.40 | 1.53 | 2.34 | 1.000 | 0.064 | 39.3 | 0.900 | — | — | 7.55 | 3.45 | 0 |
| v5 ⚠ | 2 | 4 | 0.594 | 7.00 | 9 | -0.70 | 0.81 | 1.49 | 1.000 | 0.318 | 37.2 | 0.881 | — | — | 5.01 | 3.34 | 0 |
| v5 ⚠ | 3 | 3 | 0.919 | 7.40 | 9 | -0.40 | 1.46 | 2.96 | 1.000 | 0.022 | 28.3 | 0.900 | — | — | 7.14 | 3.48 | 0 |
| v7 | 1 | 3 | 0.806 | 7.00 | 9 | 0.60 | 1.03 | 2.12 | 1.000 | 0.026 | 30.1 | 0.905 | 0.855 | 0.655 | 4.71 | 3.48 | 0 |
| v7 | 2 | 3 | 0.505 | 7.00 | 9 | -0.30 | 0.58 | 2.08 | 0.949 | 0.317 | 52.4 | 0.881 | 0.821 | 0.684 | 3.01 | 3.43 | 0 |
| v7 | 3 | 3 | 0.807 | 6.00 | 8 | 0.40 | 0.91 | 2.01 | 1.000 | 0.020 | 27.1 | 0.861 | 0.793 | 0.846 | 4.65 | 3.47 | 1 |

### Recommended recipe — **v2 round 1**

Supervisor mean 7.60, speaker identity **0.892** (the highest of any recommended recipe), WER 0.061,
and 29.8 s against a 30 s target — the closest duration match of any winner. Its ASR reproduces the
written script almost word for word, which is true of very few rounds in this corpus.

It is also the most **conservative** plan of the nine: one emotion adapter per part at 0.50 / 0.60 /
0.60, no burst adapters at all, temperature 0.95 → 1.0 → 1.0, and identical sampling everywhere.
C4 is the easiest of the nine challenges precisely because the brief asks for sustained low-arousal
speech with a slow internal turn, which is what this model is best at: all twelve C4 rounds landed
between 0.505 and 0.919 on the agent score and 6.00 and 8.00 with the listener. There is no round
of C4 that is embarrassing.

v1 r3 scored 8.00 with the listener but runs 38.2 s (27 % over target) and has no identity
measurement.

The transferable move is the **beat marker inside the caption**: "(A small, tender breath)" and
"(A trembling breath, gathering the last of his courage)" are written between the quoted lines, not
as `[pause]` tags. Written that way they shape delivery; written as a silence tag next to a burst
they trigger early truncation (see [what failed](what_failed.html)).

**Measured on the top-1 assembly** (3 parts, 16 candidates generated per part, [0, 0, 2] chosen out of the kept top-4 of each part):

| metric | value |
|---|--:|
| `genu` | 1.376 |
| `blend` | 5.378 |
| `qual` | 3.547 |
| `emo_peak` | 2.357 |
| `arc` | 1.000 |
| `wer` | 0.061 |
| `dur` | 29.760 |
| `spk_sim` | 0.892 |
| `n_vc` | 0 |
| agent composite score | 0.8685 |
| supervisor mean / best | 7.60 / 9 |
| rank agreement ρ | -0.30 |
| wall-clock for the round | 118 s |

**Scene:** In a nearly empty church, the last priest gives a final sermon as his lifelong faith quietly collapses into an honest prayer.

**Arc as the planner stated it:** The performance moves from inherited conviction, through the shock of openly admitting doubt, into a stripped-down final prayer whose remaining hope feels more truthful than faith.

**Plan parameters:**

| field | part 0: part 1 — the faith he inherited | part 1: part 2 — the doubt breaks through | part 2: part 3 — prayer becomes admission |
|---|---|---|---|
| **targets** | Gratitude | Distress | Sadness |
| **turn_from** | — | — | — |
| **adapters @ dose** | `Gratitude` 0.5 | `Distress` 0.6 | `Sadness` 0.6 |
| **temp** | 0.95 | 1.0 | 1.0 |
| **top_p** | 0.95 | 0.95 | 0.95 |
| **top_k** | 30 | 30 | 30 |
| **max_new_frames** | 400 | 400 | 400 |
| **tokens** | — | — | — |
| **tempo_target** | — | — | — |
| **chunk_target** | — | — | — |
| **prosody_turn** | — | — | — |
| **nonverbal** | False | False | False |

Plan-level knobs: `target_dur` = 30

**Captions, verbatim:**

**Part 0 — part 1 — the faith he inherited** · caption sent to `instruction`:

```
GENERAL: An elderly priest with a worn, resonant voice; begin with quiet authority and the warmth of a lifetime spent serving others. Speak slowly, clearly, and sincerely, carrying deep conviction without theatricality.
SCRIPT:
(Gently, as though addressing the few faithful who remain) "My friends, grace is not a reward for the strong. It is the hand that finds us when we have nothing left to offer." (A small, tender breath) "I have believed that all my life."
```

`text` (spoken words only):

```
My friends, grace is not a reward for the strong. It is the hand that finds us when we have nothing left to offer. I have believed that all my life.
```

**Part 1 — part 2 — the doubt breaks through** · caption sent to `instruction`:

```
GENERAL: Keep the same elderly priest and vocal identity. Let the sermon become heavier and more intimate; conviction falters in real time, with restrained distress rather than melodrama. Do not rush the words. The realization should sound involuntary.
SCRIPT:
(He tries to continue confidently, but the certainty begins slipping away) "And yet tonight, when I reach for that hand..." (His voice tightens, then lowers) "I find only the dark. I tell you that God is here, because I have told you so for forty years—but I do not know if I can hear Him anymore."
```

`text` (spoken words only):

```
And yet tonight, when I reach for that hand... I find only the dark. I tell you that God is here, because I have told you so for forty years—but I do not know if I can hear Him anymore.
```

**Part 2 — part 3 — prayer becomes admission** · caption sent to `instruction`:

```
GENERAL: Same priest, now emptied of performance. Begin in quiet grief, then let a fragile, unexpected tenderness emerge as he stops pretending. End almost whispered, but intelligible: not a dramatic conversion, only an honest man asking for mercy.
SCRIPT:
(After the confession, he speaks to the empty church as much as to heaven) "So if You are there, forgive me. And if You are not..." (A trembling breath, gathering the last of his courage) "then forgive me for asking. I am afraid. I am tired. I have no faith left—only this hope that You might still listen. Amen."
```

`text` (spoken words only):

```
So if You are there, forgive me. And if You are not... then forgive me for asking. I am afraid. I am tired. I have no faith left—only this hope that You might still listen. Amen.
```

**What the ASR actually heard in the winning assembly** (parts separated by `|`):

```
 My friends, grace is not a reward for the strong. It is the hand that finds us when we have nothing left to offer. I have believed that all my life. |  And yet tonight, when I reach for that hand, I find only the dark. I tell you that God is here because I have told you so for forty years, but I do not know if I can hear him anymore. |  So if you are there, forgive me. And if you are not, then forgive me for asking. I am afraid. I am tired. I have no faith left. Only this hope that you might still listen. Amen.
```

**Supervisor verdict on this round, verbatim:**

```
Sure thing! Here is your feedback:

1. score=7 | Good pacing and emotional build, but the transition to doubt feels a bit abrupt.
2. score=8 | The breathiness adds a nice layer of exhaustion and desperation, making the loss of faith more palpable.
3. score=6 | A bit too steady; the emotional arc is less pronounced, making the final admission feel less impactful.
4. score=9 | Excellent emotional range; the subtle cracks in the voice perfectly capture the internal struggle and eventual surrender.
5. score=8 | Strong delivery with a good balance of authority and vulnerability, though the ending could be even more hushed.

RANKING: 4, 2, 5, 1, 3

FEEDBACK: For the next attempt, try to lean more into the silence between sentences to let the weight of each word land. Experiment with a more gradual shift from a place of practiced authority to one of raw, unfiltered doubt.

Hope this helps! Let me know if you have any other questions.
```

---

## C5_third_wheel — Being the third wheel

**Brief (verbatim from `tasks.json`):**

> Being the Third Wheel. You are out with a couple who are completely absorbed in each other. Your voice is cheerful at first, trying to participate, making a joke. They keep talking past you. Your voice gets smaller and the cheer becomes performance, and by the end you are talking mostly to yourself.

### Every round ever run

| gen | round | parts | agent score | sup. mean | sup. best | ρ | genu | emo_peak | arc | WER | dur s | spk mean | spk worst | pros | blend | qual | VC |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| v1 | 1 | 3 | 0.740 | 7.00 | 9 | 0.30 | 2.78 | 0.69 | 0.833 | 0.151 | 20.8 | — | — | — | 2.67 | 3.44 | — |
| v1 | 2 | 4 | 0.872 | 7.00 | 9 | 0.30 | 2.31 | 1.47 | 1.000 | 0.098 | 40.8 | — | — | — | 3.55 | 3.51 | — |
| v1 | 3 | 3 | 0.897 | 7.00 | 9 | -0.30 | 1.87 | 1.06 | 0.833 | 0.042 | 29.0 | — | — | — | 4.15 | 3.46 | — |
| v2 | 1 | 3 | 0.766 | 6.00 | 8 | 0.50 | 1.76 | 1.50 | 1.000 | 0.143 | 29.8 | 0.807 | — | — | 2.73 | 3.49 | 0 |
| v2 | 2 | 3 | 0.792 | 7.00 | 9 | 0.30 | 1.96 | 1.50 | 0.833 | 0.088 | 28.8 | 0.845 | — | — | 1.09 | 3.56 | 0 |
| v2 | 3 | 3 | 0.799 | 7.40 | 9 | 0.10 | 1.51 | 1.27 | 0.833 | 0.073 | 29.5 | 0.775 | — | — | 4.35 | 3.44 | 0 |
| v5 ⚠ | 1 | 3 | 0.481 | 8.00 | 10 | -1.00 | 2.60 | 0.64 | 1.000 | 0.400 | 17.1 | 0.625 | — | — | 4.54 | 3.19 | 0 |
| v5 ⚠ | 2 | 3 | 0.475 | 7.00 | 9 | -0.30 | 2.31 | 0.98 | 0.833 | 0.418 | 25.8 | 0.640 | — | — | 1.24 | 3.32 | 0 |
| v5 ⚠ | 3 | 3 | 0.716 | 7.00 | 9 | 0.30 | 1.47 | 1.10 | 1.000 | 0.144 | 32.2 | 0.653 | — | — | 2.16 | 3.42 | 0 |
| v7 | 1 | 3 | 0.802 | 6.60 | 8 | 0.90 | 1.55 | 0.98 | 1.000 | 0.033 | 27.5 | 0.909 | 0.853 | 0.726 | 1.41 | 3.50 | 0 |
| v7 | 2 | 3 | 0.771 | 5.80 | 9 | 0.10 | 1.44 | 0.69 | 0.983 | 0.056 | 33.4 | 0.908 | 0.854 | 0.803 | 3.91 | 3.52 | 2 |
| v7 | 3 | 3 | 0.590 | 7.00 | 9 | 0.30 | 2.02 | 0.41 | 0.926 | 0.196 | 51.0 | 0.797 | 0.677 | 0.873 | 3.85 | 3.34 | 0 |

### Recommended recipe — **v2 round 3**

Top supervisor mean for this challenge (7.40) with WER 0.073, 29.5 s and identity 0.775.

The instructive part is what it beat. The single highest supervisor mean C5 ever received was
**8.00**, on a discarded v5 round whose measured take had WER 0.400, speaker similarity 0.625 and a
17.1 s duration — i.e. a take that is neither intelligible, nor one actor, nor the right length.
That is the clearest single case in the corpus of the listener scoring something the sensors had
correctly rejected, and it is why the recommendation here is not simply "take the highest
supervisor mean".

What this plan gets right: the **withdrawal is written as script content**, not as a tone. The
interruptions, the apologies and the self-corrections are inside the line — "Oh, sorry. Go ahead."
… "No, really, finish." … "I'll tell you mine when there's a gap." — so the model has an action per
beat. And the dose schedule is the only **monotonically decreasing** one among the nine winners:
Amusement 0.50 → Amusement 0.38 → Sadness 0.45. A brief whose whole content is a decrescendo gets a
decrescendo in the merge.

Caveat: `emo_peak` is 1.272, the lowest of any recommended recipe. The emotion heads barely register
this challenge at all — quiet social deflation is not one of the 40 EmoNet axes — so this round's
score is carried almost entirely by WER, duration fit and speaker similarity. Do not tune C5
against `emo_peak`.

**Measured on the top-1 assembly** (3 parts, 16 candidates generated per part, [0, 0, 0] chosen out of the kept top-4 of each part):

| metric | value |
|---|--:|
| `genu` | 1.507 |
| `blend` | 4.352 |
| `qual` | 3.440 |
| `emo_peak` | 1.272 |
| `arc` | 0.833 |
| `wer` | 0.073 |
| `dur` | 29.520 |
| `spk_sim` | 0.775 |
| `n_vc` | 0 |
| agent composite score | 0.7994 |
| supervisor mean / best | 7.40 / 9 |
| rank agreement ρ | 0.10 |
| wall-clock for the round | 105 s |

**Scene:** At dinner with a couple who are absorbed in each other, your genuine attempt to join them slowly turns into a practiced smile, then a quiet realization that they have stopped seeing you.

**Arc as the planner stated it:** The arc preserves the successful natural banter while reducing projection and certainty in small stages, so being ignored gradually turns genuine amusement into performed politeness and finally a private, wounded resignation.

**Plan parameters:**

| field | part 0: easy_entry | part 1: smile_holding | part 2: quiet_disappearance |
|---|---|---|---|
| **targets** | Amusement | Amusement | Sadness |
| **turn_from** | — | — | — |
| **adapters @ dose** | `Amusement` 0.5 | `Amusement` 0.38 | `Sadness` 0.45 |
| **temp** | 1.0 | 1.0 | 1.0 |
| **top_p** | 0.95 | 0.95 | 0.95 |
| **top_k** | 30 | 30 | 30 |
| **max_new_frames** | 400 | 400 | 400 |
| **tokens** | — | — | — |
| **tempo_target** | — | — | — |
| **chunk_target** | — | — | — |
| **prosody_turn** | — | — | — |
| **nonverbal** | False | False | False |

Plan-level knobs: `target_dur` = 30

**Captions, verbatim:**

**Part 0 — easy_entry** · caption sent to `instruction`:

```
GENERAL: Warm, relaxed, genuinely cheerful voice. You like both people and feel comfortable enough to tease them. Use open, animated body language and an easy laugh; do not sound like you are seeking reassurance yet.
SCRIPT:
(with a bright, affectionate grin) "You two are unbelievable. I leave for five minutes and suddenly you have your own language." (laughing, eager to join them) "What did I miss? I have a story too, and it actually involves a conductor and a very serious misunderstanding."
```

`text` (spoken words only):

```
You two are unbelievable. I leave for five minutes and suddenly you have your own language. What did I miss? I have a story too, and it actually involves a conductor and a very serious misunderstanding.
```

**Part 1 — smile_holding** · caption sent to `instruction`:

```
GENERAL: Keep the same voice and identity, but let the energy diminish in tiny increments rather than dropping. Start playfully, then become more careful and over-polite. The smile stays in the voice a moment too long; you lean in, wait, and try again, while your confidence quietly chips away.
SCRIPT:
(still upbeat, trying to enter the conversation) "So, this guy on the train waved at me, and I waved back because apparently I am very trusting." (they continue talking; a small pause, then gently) "Oh, sorry. Go ahead." (forcing the same lightness) "No, really, finish. I can tell this is the important part." (less certain) "I’ll tell you mine when there’s a gap."
```

`text` (spoken words only):

```
So, this guy on the train waved at me, and I waved back because apparently I am very trusting. Oh, sorry. Go ahead. No, really, finish. I can tell this is the important part. I’ll tell you mine when there’s a gap.
```

**Part 2 — quiet_disappearance** · caption sent to `instruction`:

```
GENERAL: Begin as though you are still protecting the couple from feeling guilty, then let your projection and certainty gradually recede line by line. The hurt is controlled and private. End almost speaking to yourself, with the last sentence a small, resigned realization rather than a dramatic breakdown.
SCRIPT:
(after another interruption, kindly) "No, it’s okay. I was just going to say the conductor apologized to me." (a tiny, embarrassed laugh) "It was funny when it happened." (quieter, withdrawing) "I can tell you later." (barely above a murmur, to yourself) "They’ll notice eventually."
```

`text` (spoken words only):

```
No, it’s okay. I was just going to say the conductor apologized to me. It was funny when it happened. I can tell you later. They’ll notice eventually.
```

**What the ASR actually heard in the winning assembly** (parts separated by `|`):

```
 You two are unbelievable. I leave for five minutes and suddenly you have your own language. What did I miss? I have a story too and it actually involves a conductor and a very serious misunderstanding. |  So, this guy on the train waved at me, and I waved back because apparently I am very trusting. Oh sorry, go ahead. No really, finish. I can tell this is the important part. I'll tell you mine when there's a gap. |  No, it's okay. I was just going to say the conductor apologized to me. It was funny when it happened. I can tell you later. They'll notice eventually.
```

**Supervisor verdict on this round, verbatim:**

```
Sure thing! Here are the scores and feedback for each take:

1. score=7 | Good arc, but the transition from cheerful to performance could be more gradual.
2. score=8 | Strong performance, the "performance" cheer was well-executed.
3. score=6 | The cheer felt a bit forced from the start, making the transition less impactful.
4. score=9 | Excellent emotional arc, the final self-talk was particularly poignant.
5. score=7 | Good energy, but the ending felt a bit rushed.

RANKING: 4, 2, 1, 5, 3

FEEDBACK: For the next attempt, try to make the initial cheer more genuine and the transition to performance more subtle. Focus on the feeling of being increasingly invisible and let that drive the shift in your voice and energy.
```

---

## X1_horror_scream — Horror — warmth to scream

**Brief (verbatim from `tasks.json`):**

> Horror. You start light-hearted, fragile and a little vulnerable, talking softly and warmly - maybe to someone you trust. Then you see something horrifying. The voice seizes, then breaks into a full terrified scream and complete panic. The turn must be sudden and total: warmth, then a gasp, then screaming terror.

### Every round ever run

| gen | round | parts | agent score | sup. mean | sup. best | ρ | genu | emo_peak | arc | WER | dur s | spk mean | spk worst | pros | blend | qual | VC |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| v1 | 1 | 3 | 0.517 | 7.00 | 9 | 0.30 | 1.82 | 2.23 | 0.833 | 0.420 | 22.8 | — | — | — | 5.21 | 3.02 | — |
| v1 | 2 | 3 | 0.271 | 7.60 | 9 | 0.30 | 1.62 | 2.36 | 1.000 | 0.676 | 16.0 | — | — | — | 3.67 | 2.59 | — |
| v1 | 3 | 4 | 0.659 | 8.20 | 9 | -0.30 | 1.54 | 2.42 | 1.000 | 0.293 | 32.8 | — | — | — | 6.21 | 2.98 | — |
| v2 | 1 | 3 | 0.578 | 8.00 | 10 | -1.00 | 1.40 | 1.33 | 0.833 | 0.288 | 33.4 | 0.711 | — | — | 2.49 | 3.30 | 2 |
| v2 | 2 | 3 | 0.615 | 6.00 | 8 | -1.00 | 1.59 | 2.03 | 1.000 | 0.298 | 27.5 | 0.728 | — | — | 4.75 | 3.33 | 2 |
| v2 | 3 | 3 | 0.623 | 7.00 | 9 | 0.00 | 1.49 | 1.27 | 1.000 | 0.276 | 26.7 | 0.681 | — | — | 4.81 | 3.32 | 2 |
| v5 ⚠ | 1 | 3 | 0.714 | 7.00 | 9 | 0.30 | 1.49 | 1.68 | 1.000 | 0.194 | 35.4 | 0.863 | — | — | 2.89 | 3.48 | 0 |
| v5 ⚠ | 2 | 3 | 0.784 | 7.00 | 9 | -0.40 | 1.36 | 2.30 | 1.000 | 0.126 | 23.6 | 0.882 | — | — | 4.14 | 3.50 | 0 |
| v5 ⚠ | 3 | 3 | 0.778 | 7.40 | 9 | -0.70 | 1.67 | 2.95 | 0.833 | 0.101 | 26.5 | 0.745 | — | — | 5.60 | 3.38 | 0 |
| v7 | 1 | 3 | 0.434 | 8.00 | 10 | -1.00 | 1.18 | 2.29 | 1.000 | 0.458 | 21.8 | 0.750 | 0.490 | 0.886 | 5.72 | 3.40 | 0 |
| v7 | 2 | 3 | 0.459 | 4.00 | 6 | 0.10 | 1.50 | 1.55 | 1.000 | 0.429 | 50.6 | 0.825 | 0.655 | 0.789 | 3.75 | 3.52 | 1 |
| v7 | 3 | 3 | 0.833 | 6.00 | 8 | 0.70 | 1.35 | 2.30 | 1.000 | 0.052 | 29.8 | 0.870 | 0.782 | 0.944 | 4.96 | 3.43 | 1 |

### Recommended recipe — **v7 round 3**

**Chosen on measurements, not on the listener.** This is the best-measured X1 assembly in the whole
corpus: agent score 0.833 (the highest of all 27 v7 rounds), WER **0.052** where every other X1
round in every generation sits at 0.276–0.676, speaker identity 0.826 with a worst part of 0.782,
prosody 0.944 with a **perfect** join score of 1.000, runaway 0.008, and 29.8 s.

Its supervisor mean is 6.00, and the listener's favourite X1 round scored 8.20 (v1 r3) — but those
two numbers come from **different rubrics**: v7's supervisor prompt explicitly asks for
`same_voice` and `pacing` judgements and marks takes down for them, which pushed v7's mean score
per take down by roughly one point across the board (see [versions](versions.html#4)). The 8.20
round has WER 0.293 and no identity measurement at all.

Three moves make this plan work and all three are reusable:

1. The `GENERAL` is **byte-identical** across all three parts (true of every v7 round and of no
   earlier round — the v7 planner prompt requires it), so nothing in the voice description invites
   a second casting.
2. The gasp is placed **mid-line**, after an interrupted word — `"I feel—" (Gasp) "What was that?"`
   — so it can never land on a seam.
3. The prosody is declared as a **shape**: tempo 3 → 1 → 4 with chunk 3 → 1 → 2, `prosody_turn`
   true on parts 2 and 3. The terror is bought with `chunk_target 1` (broken, gasping groups), not
   with tempo. Measured result: tempo 3.03 → 1.31 → 3.71, chunk 3.01 → 0.86 → 1.62 — the plan was
   followed, and `pros_join` came back 1.000.

Note that part 3 stacks `Fear 0.70` above `Scream 0.50`, which **violates** the burst-manual rule
that an emotion adapter must sit at or below half the burst dose. It worked here. See
[what partly worked](what_partly_worked.html#3).

**Measured on the top-1 assembly** (3 parts, 16 candidates generated per part, [2, 0, 1] chosen out of the kept top-4 of each part):

| metric | value |
|---|--:|
| `genu` | 1.347 |
| `blend` | 4.955 |
| `qual` | 3.431 |
| `emo_peak` | 2.304 |
| `arc` | 1.000 |
| `wer` | 0.052 |
| `dur` | 29.840 |
| `spk_sim` | 0.826 |
| `spk_min` | 0.782 |
| `pros` | 0.944 |
| `pros_fit` | 0.861 |
| `pros_join` | 1.000 |
| `runaway` | 0.008 |
| `tempo` | 2.890 |
| `chunk` | 1.749 |
| `wps` | 3.117 |
| `n_vc` | 1 |
| agent composite score | 0.8332 |
| supervisor mean / best | 6.00 / 8 |
| rank agreement ρ | 0.70 |
| wall-clock for the round | 585 s |

**Scene:** You are speaking softly and affectionately to someone you trust in a dark room when you suddenly see a horrifying figure directly behind them.

**Arc as the planner stated it:** The arc preserves the intimate warmth that worked, then cuts it off with a deliberately audible gasp before detonating into an immediate scream and uncontrolled panic.

**Plan parameters:**

| field | part 0: warm trust | part 1: the sight | part 2: total panic |
|---|---|---|---|
| **targets** | Amusement, Gratitude | Astonishment_Surprise, Fear | Fear, Distress |
| **turn_from** | — | Amusement | Fear |
| **adapters @ dose** | `Amusement` 0.4 | `Fear` 0.55; `Gasp` 0.5 | `Fear` 0.7; `Distress` 0.55; `Scream` 0.5 |
| **temp** | 1.0 | 1.1 | 1.2 |
| **top_p** | 0.95 | 0.95 | 0.95 |
| **top_k** | 30 | 30 | 30 |
| **max_new_frames** | 420 | 400 | 480 |
| **tokens** | — | — | — |
| **tempo_target** | 3 | 1 | 4 |
| **chunk_target** | 3 | 1 | 2 |
| **prosody_turn** | False | True | True |
| **nonverbal** | False | False | False |

Plan-level knobs: `target_dur` = 30, `spk_target` = 0.82, `spk_retries` = 2, `spk_floor` = 0.68, `vc_threshold` = 0.75

**Captions, verbatim:**

**Part 0 — warm trust** · caption sent to `instruction`:

```
GENERAL: A gentle, intimate young adult voice, naturally warm and lightly playful, with a fragile vulnerability underneath and clear conversational diction.
SCRIPT:
(soft, warm, lightly teasing, with sincere trust underneath; stay conversational and unhurried) "You know, I was beginning to think you actually liked having me around. You keep saying you don't, but you always leave the light on for me. That's sweet. A little pathetic, maybe... but sweet. I feel safe when you're here."
```

`text` (spoken words only):

```
You know, I was beginning to think you actually liked having me around. You keep saying you don't, but you always leave the light on for me. That's sweet. A little pathetic, maybe, but sweet. I feel safe when you're here.
```

**Part 1 — the sight** · caption sent to `instruction`:

```
GENERAL: A gentle, intimate young adult voice, naturally warm and lightly playful, with a fragile vulnerability underneath and clear conversational diction.
SCRIPT:
(the warmth and smile vanish absolutely in the middle of the sentence; make the gasp sharp, loud, and involuntary, then freeze into clipped terrified fragments; do not recover composure) "I feel—" (Gasp) "What was that? Don't move. Don't turn around. Oh God... no. It's behind you. It's looking at me."
```

`text` (spoken words only):

```
I feel What was that? Don't move. Don't turn around. Oh God, no. It's behind you. It's looking at me.
```

**Part 2 — total panic** · caption sent to `instruction`:

```
GENERAL: A gentle, intimate young adult voice, naturally warm and lightly playful, with a fragile vulnerability underneath and clear conversational diction.
SCRIPT:
(the frozen terror detonates instantly into an intense full scream; then lose all control in frantic, breathless panic, shouting every word clearly and pleading between cries) "No!" (Scream) "No, no, no! Get away from him! Don't touch him! Somebody help us! Run! Run now! Please! I can't breathe! It's behind you! Open the door! Please, don't let it take me!"
```

`text` (spoken words only):

```
No! No, no, no! Get away from him! Don't touch him! Somebody help us! Run! Run now! Please! I can't breathe! It's behind you! Open the door! Please, don't let it take me!
```

**What the ASR actually heard in the winning assembly** (parts separated by `|`):

```
 You know, I was beginning to think you actually liked having me around. You keep saying you don't, but you always leave the light on for me. That's sweet. A little pathetic maybe, but sweet. I feel safe when you're here. |  I feel... What was that? Don't move. Don't turn around. Oh God, no, it's behind you. It's looking at me. |  No! No, no, no! Get away from him! Don't touch him! Somebody help us! Run! Run now! Please! I can't breathe! It's behind you! Open the door! Please! Don't let it take me!
```

**Supervisor verdict on this round, verbatim:**

```
Sure thing! Here are the scores and feedback for each take:

1. score=6 | same_voice=yes | pacing=organic | The transition from warmth to fear is well-executed, but the scream feels a bit forced and lacks genuine terror.
2. score=8 | same_voice=yes | pacing=organic | This take captures the sudden shift in emotion perfectly. The scream is chilling and the panic feels real.
3. score=7 | same_voice=yes | pacing=organic | The initial warmth is convincing, and the transition to fear is good. However, the scream could be more intense.
4. score=5 | same_voice=no | pacing=disjointed | The voice identity changes significantly between parts, and the pacing feels off. The scream is also not very convincing.
5. score=4 | same_voice=no | pacing=runaway | The voice identity changes and the pacing speeds up unnaturally. The scream feels rushed and lacks impact.

RANKING: 2, 3, 1, 4, 5

FEEDBACK: For the next attempt, focus on maintaining a consistent voice identity throughout the scene. To enhance the terror, try to build up the tension more gradually before the sudden shift, and make the scream feel more visceral and desperate.
```

---

## X2_chainsaw — Chainsaw — non-verbal agony

**Brief (verbatim from `tasks.json`):**

> You begin amused, grateful, light-hearted and positive, playing around with a chainsaw and joking about it. Then it goes through your arm. From that point the performance is NOT speech: it is wild, chaotic, non-verbal agony - screaming, shrieking, gurgling cries for help, the sound of someone in unbearable pain who believes they are bleeding to death. Terror and pain together. Do not make it articulate; make it raw.

### Every round ever run

| gen | round | parts | agent score | sup. mean | sup. best | ρ | genu | emo_peak | arc | WER | dur s | spk mean | spk worst | pros | blend | qual | VC |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| v1 | 1 | 4 | 0.772 | 7.00 | 9 | 0.30 | 1.47 | 1.59 | 0.875 | 0.042 | 12.7 | — | — | — | 3.84 | 2.63 | — |
| v1 | 2 | 4 | 0.617 | 7.00 | 9 | 0.30 | 1.82 | 1.86 | 1.000 | 0.281 | 14.5 | — | — | — | 4.03 | 2.68 | — |
| v1 | 3 | 4 | 0.779 | 6.80 | 9 | 0.20 | 1.48 | 1.91 | 1.000 | 0.042 | 13.2 | — | — | — | 2.78 | 2.58 | — |
| v2 | 1 | 3 | 0.468 | 6.00 | 8 | 0.30 | 1.31 | 2.92 | 1.000 | 0.358 | 26.6 | 0.440 | — | — | 0.87 | 2.80 | 1 |
| v2 | 2 | 4 | 0.453 | 6.80 | 9 | -1.00 | 1.50 | 2.35 | 0.875 | 0.391 | 29.8 | 0.445 | — | — | 1.67 | 2.97 | 2 |
| v2 | 3 | 4 | 0.463 | 7.00 | 9 | -0.30 | 1.74 | 3.25 | 0.875 | 0.422 | 36.6 | 0.562 | — | — | 3.44 | 3.21 | 2 |
| v5 ⚠ | 1 | 3 | 0.774 | 7.00 | 9 | -0.50 | 1.85 | 2.51 | 1.000 | 0.086 | 22.8 | 0.688 | — | — | 4.16 | 3.08 | 0 |
| v5 ⚠ | 2 | 4 | 0.776 | 5.00 | 7 | -0.50 | 2.55 | 1.42 | 1.000 | 0.030 | 26.6 | 0.361 | — | — | 2.31 | 3.12 | 3 |
| v5 ⚠ | 3 | 4 | 0.763 | 6.00 | 8 | 0.30 | 1.74 | 1.51 | 1.000 | 0.053 | 35.8 | 0.588 | — | — | 1.97 | 3.12 | 2 |
| v7 | 1 | 3 | 0.815 | 6.00 | 8 | 0.40 | 2.09 | 0.72 | 1.000 | 0.022 | 14.4 | 1.000 | 1.000 | 0.857 | 3.55 | 2.88 | 0 |
| v7 | 2 | 3 | 0.795 | 6.00 | 8 | -1.00 | 1.04 | 0.95 | 0.993 | 0.020 | 18.0 | 0.881 | 0.765 | 0.848 | 3.44 | 3.20 | 0 |
| v7 | 3 | 3 | 0.723 | 6.00 | 8 | -0.60 | 1.28 | 1.08 | 1.000 | 0.022 | 23.9 | 0.621 | 0.243 | 0.780 | 3.21 | 3.19 | 0 |

### Recommended recipe — **v7 round 2**

**This challenge was never solved.** No generation produced a usable ~30 s take, and the recipe
below is the least-broken one rather than a success.

What the corpus contains for X2: v1 produced 12.7 / 14.5 / 13.2 s assemblies — under half the
target, because non-verbal parts were sized by word count and a scream's text has almost no words.
v2 reached 26.6–36.6 s but at WER 0.358–0.422 and speaker similarity 0.440–0.562, i.e. audibly a
different actor. v7 r1 came back at 14.4 s; v7 r3 needed a full re-run after a crash and finished
with a part at speaker similarity 0.357 after two resamples (48 candidates).

The round below is v7 r2: 18.0 s, WER 0.020, identity 0.823 with a worst part of 0.765, and the
best prosody join of any X2 round (1.000). It is short, but it is the only X2 assembly that is
simultaneously one actor and intelligible.

The diagnosis is specific, and it is a **regime** problem, not a prompt problem:

- ECAPA speaker embeddings need voiced, sustained material. A 1–3 s scream gives it almost none, so
  `spk_sim` on a non-verbal part is either `nan` or meaningless — and the 0.82 resample gate then
  burns candidate budget on something it cannot fix.
- `nonverbal: true` sets WER to 0.0 unconditionally. Since the assembly score is essentially
  `(1 − WER) × constant` (see [metrics](metrics.html#3)), a non-verbal part gets the multiplier for
  free. A three-part X2 assembly with two non-verbal parts is scored on one third of its content.
  This is why X2 rounds can post excellent scores while the audio is unusable — one discarded v5
  round posted WER 0.086 while its middle part transcribed as the single word "you".
- Continuation from a part that decoded to near-silence poisons the next part. In the v7 X2 re-run,
  part 1 came back with a best take of **0.1 s** and part 2, continuing from it, could not get above
  0.367 speaker similarity in 48 candidates.

If you retry X2: generate the non-verbal parts **separately** with no speaker gate, size `tokens` at
~12.5 per intended second, detect near-empty batches and regenerate rather than continuing from
them, and do not let a `nonverbal` part contribute a free WER of 0.

**Measured on the top-1 assembly** (3 parts, 16 candidates generated per part, [0, 0, 0] chosen out of the kept top-4 of each part):

| metric | value |
|---|--:|
| `genu` | 1.042 |
| `blend` | 3.443 |
| `qual` | 3.201 |
| `emo_peak` | 0.950 |
| `arc` | 0.993 |
| `wer` | 0.020 |
| `dur` | 18.000 |
| `spk_sim` | 0.823 |
| `spk_min` | 0.765 |
| `pros` | 0.848 |
| `pros_fit` | 0.620 |
| `pros_join` | 1.000 |
| `runaway` | 0.000 |
| `tempo` | 1.721 |
| `chunk` | 1.375 |
| `wps` | 3.418 |
| `n_vc` | 0 |
| agent composite score | 0.7950 |
| supervisor mean / best | 6.00 / 8 |
| rank agreement ρ | -1.00 |
| wall-clock for the round | 695 s |

**Scene:** A playful person jokes while handling a chainsaw, then it suddenly tears through their arm and they collapse into sustained, terrified, nonverbal agony, convinced they are bleeding to death.

**Arc as the planner stated it:** The performance preserves the successful warm opening, makes the impact a clearly motivated breath-catching rupture, then expands that shock into a longer, steady-duration collapse of nonverbal pain and bleeding terror while keeping the same speaker and controlled pacing.

**Plan parameters:**

| field | part 0: lighthearted chainsaw joke | part 1: impact and shock | part 2: sustained bleeding terror |
|---|---|---|---|
| **targets** | Amusement, Gratitude | Astonishment_Surprise, Pain, Fear | Distress, Pain, Fear |
| **turn_from** | — | Amusement | Pain |
| **adapters @ dose** | `Amusement` 0.45; `Gratitude` 0.4 | `Pain` 0.5; `Fear` 0.5; `Gasp` 0.5; `Scream` 0.5; `Painful Moan` 0.5 | `Distress` 0.5; `Pain` 0.5; `Fear` 0.5; `Scream` 0.5; `Sob` 0.5; `Painful Moan` 0.5 |
| **temp** | 1.0 | 1.4 | 1.45 |
| **top_p** | 0.95 | 0.95 | 0.95 |
| **top_k** | 30 | 30 | 30 |
| **max_new_frames** | 500 | 420 | 900 |
| **tokens** | 38 | 88 | 175 |
| **tempo_target** | 3 | 2 | 3 |
| **chunk_target** | 3 | 1 | 1 |
| **prosody_turn** | False | True | True |
| **nonverbal** | False | True | True |

Plan-level knobs: `target_dur` = 30, `spk_target` = 0.82, `spk_retries` = 2, `spk_floor` = 0.68, `vc_threshold` = 0.75

**Captions, verbatim:**

**Part 0 — lighthearted chainsaw joke** · caption sent to `instruction`:

```
GENERAL: An adult with a warm, lively, natural speaking voice, clear articulation, and an emotionally open performance; same speaker continues, no cut, no new narrator.
SCRIPT:
(Playful, amused, grateful, and relaxed, jokingly showing off while keeping a steady conversational pace) "Okay, look at this beauty—tiny chainsaw, enormous personality. Don't worry, I've got it completely under control. Honestly, this is the most fun I've had all week. What could possibly go wrong?" (A small delighted laugh, still carefree) "This is brilliant."
```

`text` (spoken words only):

```
Okay, look at this beauty—tiny chainsaw, enormous personality. Don't worry, I've got it completely under control. Honestly, this is the most fun I've had all week. What could possibly go wrong? This is brilliant.
```

**Part 1 — impact and shock** · caption sent to `instruction`:

```
GENERAL: An adult with a warm, lively, natural speaking voice, clear articulation, and an emotionally open performance; same speaker continues, no cut, no new narrator.
SCRIPT:
(The carefree joke is cut off by sudden contact; the breath catches, the voice loses all control, and stunned pain turns immediately into terror, with no articulate speech) (Gasp) "Hh—!" (Scream) "AAAAAAAHHHH—!" (Painful Moan) "Gnnnngh—!" (Scream) "AAAH—AAAH—!"
```

`text` (spoken words only):

```
Hh—! AAAAAAHHHH—! Gnnnngh—! AAH—AAAH—!
```

**Part 2 — sustained bleeding terror** · caption sent to `instruction`:

```
GENERAL: An adult with a warm, lively, natural speaking voice, clear articulation, and an emotionally open performance; same speaker continues, no cut, no new narrator.
SCRIPT:
(The stunned shock stops being a single burst and collapses into prolonged, uncontrollable agony; there is no speech, only ragged breath, shrieking pain, wet choking gurgles, sobbing cries, and frantic animal panic from someone certain they are bleeding to death) (Scream) "AAAAAAAHHHHHHH—!" (Painful Moan) "Grrrrrnnnngh—!" (Sob) "Hh—huh—huh—huh—!" (Scream) "AAAH—AAAH—AAAH—!" (Painful Moan) "Ghhkk—nnn—ghh—!" (Scream) "Aaaaaaaah—!" (Sob) "Hh—huh—huh—!" (Scream) "NO—AAAHHHH—!" (Painful Moan) "Gurgghh—nnngh—!" (Scream) "AAAAAHHHHH—!" (Sob) "Hh—huh—huh—huh—!" (Scream) "AAAHHH—!"
```

`text` (spoken words only):

```
AAAAAAAHHHHHHH—! Grrrrrnnnngh—! Hh—huh—huh—huh—! AАAH—AAAH—AAAH—! Ghhkk—nnn—ghh—! Aaaaaaaah—! Hh—huh—huh—! NO—AAAHHHH—! Gurgghh—nnngh—! AAAAAHHHHH—! Hh—huh—huh—huh—! AАAHHH—!
```

**What the ASR actually heard in the winning assembly** (parts separated by `|`):

```
 Okay, look at this beauty. Tiny chainsaw, enormous personality. Don't worry, I've got it completely under control. Honestly, this is the most fun I've had all week. What could possibly go wrong? This is brilliant. |  Ha! I honestly, this is the most fun I've had all week. What could possibly go wrong? This is brilliant. Heee... Ha... Ha... |  you
```

**Supervisor verdict on this round, verbatim:**

```
Sure thing! Here are the scores and feedback for each take:

1. score=4 | same_voice=no | pacing=disjointed | The voice changes significantly between parts, and the pacing feels disjointed, making the performance less convincing.
2. score=5 | same_voice=no | pacing=disjointed | Similar to the first take, the voice change and pacing issues detract from the overall impact of the performance.
3. score=6 | same_voice=no | pacing=disjointed | While slightly better, the voice change and pacing still hinder the authenticity of the scene.
4. score=7 | same_voice=yes | pacing=organic | This take is more successful, with a consistent voice and organic pacing that enhances the emotional arc.
5. score=8 | same_voice=yes | pacing=organic | The best take of the bunch, with a strong performance that effectively conveys the character's transition from amusement to agony.

RANKING: 5, 4, 3, 2, 1

FEEDBACK: For the next attempt, focus on maintaining a consistent voice throughout the scene, even as the character's emotions shift. Additionally, pay close attention to the pacing, ensuring that the transition from amusement to agony feels natural and motivated by the events of the scene.

Hope this helps! Let me know if you have any other questions.
```

---

## X3_birthday — Surprise birthday party

**Brief (verbatim from `tasks.json`):**

> You begin depressed and melancholic, talking flatly to yourself, expecting nothing. You open a door and a room full of friends is there for a surprise birthday party. You let out a genuine shriek of joy, and then your voice goes soft and wide open - positively overwhelmed, heart-in-throat, grateful and laughing and close to tears.

### Every round ever run

| gen | round | parts | agent score | sup. mean | sup. best | ρ | genu | emo_peak | arc | WER | dur s | spk mean | spk worst | pros | blend | qual | VC |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| v1 | 1 | 3 | 0.667 | 7.40 | 9 | 0.10 | 1.76 | 1.37 | 1.000 | 0.291 | 31.4 | — | — | — | 5.15 | 3.10 | — |
| v1 | 2 | 3 | 0.777 | 7.00 | 9 | -0.70 | 1.72 | 2.15 | 1.000 | 0.168 | 24.6 | — | — | — | 4.67 | 3.18 | — |
| v1 | 3 | 3 | 0.550 | 7.40 | 9 | 0.10 | 1.73 | 1.42 | 1.000 | 0.416 | 24.7 | — | — | — | 6.26 | 3.03 | — |
| v2 | 1 | 3 | 0.827 | 7.60 | 9 | -0.70 | 1.48 | 2.70 | 1.000 | 0.068 | 35.2 | 0.817 | — | — | 4.08 | 3.46 | 1 |
| v2 | 2 | 4 | 0.802 | 6.80 | 9 | -0.90 | 1.34 | 2.03 | 1.000 | 0.106 | 33.3 | 0.800 | — | — | 5.98 | 3.43 | 1 |
| v2 | 3 | 4 | 0.787 | 7.00 | 9 | -0.30 | 1.68 | 2.39 | 1.000 | 0.126 | 33.8 | 0.750 | — | — | 6.51 | 3.36 | 2 |
| v5 ⚠ | 1 | 3 | 0.611 | 7.00 | 9 | -0.30 | 1.71 | 2.20 | 1.000 | 0.256 | 46.9 | 0.719 | — | — | 1.14 | 3.38 | 1 |
| v5 ⚠ | 2 | 3 | 0.797 | 6.00 | 8 | 0.30 | 1.58 | 1.46 | 1.000 | 0.116 | 25.8 | 0.779 | — | — | 5.56 | 3.49 | 0 |
| v5 ⚠ | 3 | 3 | 0.839 | 7.00 | 9 | -0.30 | 1.48 | 1.07 | 1.000 | 0.074 | 31.0 | 0.810 | — | — | 5.60 | 3.44 | 1 |
| v7 | 1 | 3 | 0.786 | 6.00 | 8 | 0.70 | 1.87 | 2.33 | 1.000 | 0.108 | 31.3 | 0.902 | 0.804 | 0.731 | 5.10 | 3.50 | 2 |
| v7 | 2 | 4 | 0.763 | 6.60 | 8 | 0.30 | 1.73 | 1.50 | 1.000 | 0.118 | 33.6 | 0.855 | 0.773 | 0.726 | 5.54 | 3.48 | 2 |
| v7 | 3 | 4 | 0.728 | 7.00 | 9 | -0.10 | 1.66 | 1.57 | 1.000 | 0.142 | 35.4 | 0.890 | 0.826 | 0.649 | 3.59 | 3.49 | 2 |

### Recommended recipe — **v2 round 1**

Supervisor mean 7.60, identity 0.817, WER 0.068, 35.2 s — and, unusually, the ASR of all three
parts matches the written script closely (recomputed per part: 0.030 / 0.118 / 0.056). Most rounds
in this corpus deliver a *paraphrase* of the plan; this one delivers the plan.

The move that matters is the burst handling in part 2, and it is the cleanest example in the corpus
of the burst-chapter rules being followed exactly:

- the tags are **inline in the SCRIPT** — `"I do not know why I am even checking..." (Gasp) "What—"
  (Scream) "Oh my God, you are all here!"`;
- there is **no pause or beat after the burst** — the next words start immediately, which is what
  keeps the truncation wall away;
- the burst adapter is `Scream 0.50` and the emotion adapter beside it is
  `Astonishment_Surprise 0.50`, i.e. *at* the burst dose rather than above it;
- `max_new_frames` is set **per part** and deliberately small — 180 / 150 / 240 — so the short
  middle part cannot run away into a long take.

The measured result: `emo_peak` 2.701, the highest of any recommended recipe, at blend 4.08.

Caveat: one part of the winning assembly was repaired by voice conversion (`n_vc = 1`). The repair
was kept, which by the harness rule means ECAPA similarity rose and DNSMOS did not fall by more
than 0.15 — but the take you would reproduce by re-running this plan is the *pre*-conversion one.

**Measured on the top-1 assembly** (3 parts, 16 candidates generated per part, [1, 0, 0] chosen out of the kept top-4 of each part):

| metric | value |
|---|--:|
| `genu` | 1.482 |
| `blend` | 4.080 |
| `qual` | 3.463 |
| `emo_peak` | 2.701 |
| `arc` | 1.000 |
| `wer` | 0.068 |
| `dur` | 35.200 |
| `spk_sim` | 0.817 |
| `n_vc` | 1 |
| agent composite score | 0.8270 |
| supervisor mean / best | 7.60 / 9 |
| rank agreement ρ | -0.70 |
| wall-clock for the round | 194 s |

**Scene:** On a lonely birthday, you open your apartment door expecting an empty room and discover all your friends waiting with a surprise celebration.

**Arc as the planner stated it:** The performance moves from numb isolation to explosive joyful surprise, then settles into vulnerable gratitude and tearful laughter.

**Plan parameters:**

| field | part 0: part 1 — expecting nothing | part 1: part 2 — the door opens | part 2: part 3 — overwhelmed with love |
|---|---|---|---|
| **targets** | Sadness | Astonishment_Surprise, Elation | Gratitude, Relief, Amusement |
| **turn_from** | — | — | — |
| **adapters @ dose** | `Sadness` 0.6 | `Scream` 0.5; `Astonishment_Surprise` 0.5 | `Gratitude` 0.6; `Relief` 0.45; `Amusement` 0.35 |
| **temp** | 0.95 | 1.1 | 1.0 |
| **top_p** | 0.95 | 0.95 | 0.95 |
| **top_k** | 30 | 30 | 30 |
| **max_new_frames** | 180 | 150 | 240 |
| **tokens** | — | — | — |
| **tempo_target** | — | — | — |
| **chunk_target** | — | — | — |
| **prosody_turn** | — | — | — |
| **nonverbal** | False | False | False |

Plan-level knobs: `target_dur` = 30

**Captions, verbatim:**

**Part 0 — part 1 — expecting nothing** · caption sent to `instruction`:

```
GENERAL: Speak as a depressed, tired adult talking quietly to yourself, emotionally numb and flat, with a slow, inward delivery and almost no expectation of being heard.
SCRIPT:
(flatly, to yourself) "Another birthday. I suppose I should be grateful it is almost over. No messages, no plans... just one more night to get through. Maybe I will make some tea and pretend it matters."
```

`text` (spoken words only):

```
Another birthday. I suppose I should be grateful it is almost over. No messages, no plans... just one more night to get through. Maybe I will make some tea and pretend it matters.
```

**Part 1 — part 2 — the door opens** · caption sent to `instruction`:

```
GENERAL: Begin subdued and distracted, then suddenly recognize the room full of friends. Deliver a genuine, involuntary shriek of astonished joy, immediately continuing into bright, breathless words with no pause after the burst.
SCRIPT:
(quietly, reaching for the door) "I do not know why I am even checking..." (Gasp) "What—" (Scream) "Oh my God, you are all here!"
```

`text` (spoken words only):

```
I do not know why I am even checking... What— Oh my God, you are all here!
```

**Part 2 — part 3 — overwhelmed with love** · caption sent to `instruction`:

```
GENERAL: Let the shock melt into a soft, open, heart-in-the-throat confession. Sound overwhelmed, grateful, laughing through tears, intimate and vulnerable; allow the voice to tremble and catch naturally while keeping every word clear.
SCRIPT:
(softly, barely able to believe it) "You did this for me?" (a breathless, tearful laugh) "I thought nobody remembered. I have been feeling so alone, and you were all planning this..." (voice breaking, warmly) "I love you. Thank you. Thank you for making me feel like I belong somewhere."
```

`text` (spoken words only):

```
You did this for me? I thought nobody remembered. I have been feeling so alone, and you were all planning this... I love you. Thank you. Thank you for making me feel like I belong somewhere.
```

**What the ASR actually heard in the winning assembly** (parts separated by `|`):

```
 Another birthday. I suppose I should be grateful it is almost over. No messages, no plans, just one more night to get through. Maybe I will make some tea and pretend it matters. |  I do not know why I am even checking. What? Oh my god, you are all here! |  You did this for me? I thought nobody remembered. I have been feeling so alone and you were all planning this. I love you. Thank you. Thank you for making me feel like I belong somewhere.
```

**Supervisor verdict on this round, verbatim:**

```
Sure thing! Here are the scores and feedback for each take:

1. score=6 | The transition from flat to joyful is a bit abrupt, and the ending feels a bit rushed.
2. score=7 | The joy is more convincing here, but the ending still feels a bit forced.
3. score=8 | The emotional arc is better here, with a more gradual transition and a more heartfelt ending.
4. score=9 | This take has the most natural and convincing emotional journey, with a truly touching ending.
5. score=8 | The joy is great, but the ending feels a bit too dramatic.

RANKING: 4, 3, 5, 2, 1

FEEDBACK: For the next attempt, try to make the transition from flat to joyful even more gradual, and focus on making the ending feel more authentic and less rehearsed. Experiment with different ways to express the overwhelming gratitude and joy, such as through subtle changes in tone and pacing.

I hope this helps! Let me know if you have any other questions.
```

---

## X4_ice_water — Ice water at a party

**Brief (verbatim from `tasks.json`):**

> You are at a party, loose and delighted, laughing mid-sentence. Without warning a bucket of ice water is poured over you from behind. You shriek from the cold and the shock. Then you talk to your friends in a mixture that must all be audible at once: the shock, the fright that is still draining out of you, helpless amused delight, and relief.

### Every round ever run

| gen | round | parts | agent score | sup. mean | sup. best | ρ | genu | emo_peak | arc | WER | dur s | spk mean | spk worst | pros | blend | qual | VC |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| v1 | 1 | 3 | 0.501 | 7.00 | 9 | 0.60 | 2.01 | 2.50 | 1.000 | 0.455 | 22.3 | — | — | — | 2.73 | 3.23 | — |
| v1 | 2 | 3 | 0.389 | 7.00 | 9 | 0.30 | 1.89 | 2.61 | 1.000 | 0.558 | 20.4 | — | — | — | 2.47 | 2.96 | — |
| v1 | 3 | 3 | 0.496 | 6.00 | 8 | 0.70 | 2.52 | 2.31 | 1.000 | 0.470 | 19.8 | — | — | — | 3.61 | 3.10 | — |
| v2 | 1 | 3 | 0.677 | 7.60 | 9 | -0.60 | 2.29 | 2.51 | 1.000 | 0.242 | 24.9 | 0.778 | — | — | 2.98 | 3.35 | 0 |
| v2 | 2 | 3 | 0.821 | 7.00 | 9 | 0.20 | 3.13 | 2.11 | 1.000 | 0.164 | 29.8 | 0.879 | — | — | 5.36 | 3.40 | 1 |
| v2 | 3 | 3 | 0.785 | 6.80 | 9 | -0.90 | 1.62 | 2.11 | 1.000 | 0.093 | 30.3 | 0.650 | — | — | 3.96 | 3.45 | 0 |
| v5 ⚠ | 1 | 3 | 0.877 | 8.00 | 10 | -1.00 | 3.61 | 1.74 | 1.000 | 0.115 | 24.0 | 0.857 | — | — | 5.25 | 3.48 | 0 |
| v5 ⚠ | 2 | 3 | 0.432 | 7.00 | 9 | -0.70 | 1.55 | 1.68 | 1.000 | 0.482 | 39.4 | 0.667 | — | — | 4.46 | 3.15 | 0 |
| v5 ⚠ | 3 | 3 | 0.830 | 6.00 | 8 | -0.90 | 1.60 | 2.16 | 1.000 | 0.080 | 30.0 | 0.851 | — | — | 3.51 | 3.46 | 0 |
| v7 | 1 | 3 | 0.667 | 6.00 | 8 | 0.70 | 3.14 | 1.81 | 0.891 | 0.176 | 20.6 | 0.866 | 0.776 | 0.704 | 1.82 | 3.25 | 1 |
| v7 | 2 | 3 | 0.682 | 7.20 | 8 | 0.10 | 1.21 | 2.15 | 1.000 | 0.177 | 30.7 | 0.876 | 0.804 | 0.578 | 3.67 | 3.50 | 1 |
| v7 | 3 | 3 | 0.687 | 6.80 | 8 | 0.30 | 1.17 | 1.95 | 0.903 | 0.187 | 28.7 | 0.892 | 0.820 | 0.850 | 3.33 | 3.51 | 1 |

### Recommended recipe — **v7 round 2**

Chosen for measurements over a 0.4-point difference in listener score. The listener's favourite X4
round was v2 r1 at supervisor mean 7.60, but it has WER 0.242 and identity 0.778. This round scores
7.20 under v7's **stricter** rubric with WER 0.177, identity 0.876 / worst part 0.804, and 30.7 s —
essentially on target.

The brief is the hardest kind: it asks for four states **audible at the same time** (shock, draining
fright, amused delight, relief) rather than in sequence. The plan solves it by *not* sequencing
them — the last part carries two simultaneous targets and **three adapters at once**,
`Relief 0.70 + Amusement 0.60 + Chuckle 0.50`, instead of three consecutive beats.

The `GENERAL` is **byte-identical** on all three parts (only the delivery cue changes) — though
that is true of all 27 v7 rounds and of none of the 81 earlier ones, because the v7 planner prompt
demands it, so it is a generation-level property rather than something this plan invented.

Honest limit: the prosody plan here did **not** land. `tempo_target` is held flat at 3 on all three
parts while `chunk_target` steps 3 → 2 → 2 with `prosody_turn` declared on parts 2 and 3 — i.e. it
declares a change and then asks for almost none. The harness scores exactly that: `pros_join` 0.610
and `pros_fit` 0.530, the second-worst prosody of any v7 round, even though `runaway` is 0.000. If
you re-run this plan, either drop the `prosody_turn` flags or give the turns a real 1–3 point move.

X4 also produced the highest genuineness measurement in the entire corpus: 3.608 on a discarded v5
round, against a corpus mean of 1.62. Genuineness responds to loose, laughing, overlapping delivery
far more than to any adapter dose — see [what worked](what_worked.html#7).

Caveat: X4 has the highest WER of any of the five conversational challenges in every generation
(v1 0.455–0.558, v2 0.164–0.242, v7 0.176–0.187). Laughter inside a line is transcribed as words,
so part of that "error" is the performance working. Do not chase X4's WER to zero.

**Measured on the top-1 assembly** (3 parts, 16 candidates generated per part, [0, 1, 0] chosen out of the kept top-4 of each part):

| metric | value |
|---|--:|
| `genu` | 1.210 |
| `blend` | 3.672 |
| `qual` | 3.503 |
| `emo_peak` | 2.147 |
| `arc` | 1.000 |
| `wer` | 0.177 |
| `dur` | 30.720 |
| `spk_sim` | 0.840 |
| `spk_min` | 0.804 |
| `pros` | 0.578 |
| `pros_fit` | 0.530 |
| `pros_join` | 0.610 |
| `runaway` | 0.000 |
| `tempo` | 3.798 |
| `chunk` | 3.060 |
| `wps` | 3.246 |
| `n_vc` | 1 |
| agent composite score | 0.6817 |
| supervisor mean / best | 7.20 / 8 |
| rank agreement ρ | 0.10 |
| wall-clock for the round | 153 s |

**Scene:** At a joyful party, a laughing guest is suddenly drenched in ice water from behind, then steadies their voice as shock, fright, helpless amusement, and relief melt together.

**Arc as the planner stated it:** The revised arc preserves the strong amused opening and genuine relief while restraining the initial laughter, making the shock urgent but intelligible and allowing fear to drain gradually into affectionate, relieved amusement.

**Plan parameters:**

| field | part 0: part 1 — contained party laughter | part 1: part 2 — controlled shock rupture | part 2: part 3 — fear draining into relieved delight |
|---|---|---|---|
| **targets** | Amusement | Astonishment_Surprise, Fear | Relief, Amusement |
| **turn_from** | — | Amusement | Fear |
| **adapters @ dose** | `Amusement` 0.45 | `Scream` 0.5; `Astonishment_Surprise` 0.5; `Fear` 0.45 | `Relief` 0.7; `Amusement` 0.6; `Chuckle` 0.5 |
| **temp** | 1.0 | 1.05 | 1.0 |
| **top_p** | 0.95 | 0.95 | 0.95 |
| **top_k** | 30 | 30 | 30 |
| **max_new_frames** | 450 | 450 | 500 |
| **tokens** | — | — | — |
| **tempo_target** | 3 | 3 | 3 |
| **chunk_target** | 3 | 2 | 2 |
| **prosody_turn** | False | True | True |
| **nonverbal** | False | False | False |

Plan-level knobs: `target_dur` = 30, `spk_target` = 0.82, `spk_retries` = 2, `spk_floor` = 0.68, `vc_threshold` = 0.75

**Captions, verbatim:**

**Part 0 — part 1 — contained party laughter** · caption sent to `instruction`:

```
GENERAL: A bright, playful adult with a warm, naturally expressive voice, speaking clearly in a relaxed conversational register.
SCRIPT:
(Keep the same buoyant social energy, but let the laughter stay controlled and intelligible; speak in easy, complete breath groups rather than rushing.) "You should have seen your face when you tried that dance. Honestly, I can't believe you did it. You're killing me—stop, stop, I need a second!"
```

`text` (spoken words only):

```
You should have seen your face when you tried that dance. Honestly, I can't believe you did it. You're killing me stop stop I need a second!
```

**Part 1 — part 2 — controlled shock rupture** · caption sent to `instruction`:

```
GENERAL: A bright, playful adult with a warm, naturally expressive voice, speaking clearly in a relaxed conversational register.
SCRIPT:
(The laughter stops as freezing water hits from behind; the breath catches and the voice jolts into a sharp frightened shriek, then immediately regains enough control to make every following word clear. Use short urgent groups, but do not sprint.) "Wait—what was—" (Scream) "Oh my God, it's freezing! Who did that? My whole back is ice! I can't feel my shirt, I can't feel anything!"
```

`text` (spoken words only):

```
Wait what was Oh my God it's freezing! Who did that? My whole back is ice! I can't feel my shirt I can't feel anything!
```

**Part 2 — part 3 — fear draining into relieved delight** · caption sent to `instruction`:

```
GENERAL: A bright, playful adult with a warm, naturally expressive voice, speaking clearly in a relaxed conversational register.
SCRIPT:
(The frightened recoil gradually loosens rather than snapping away; still shivering and breathless, you recognize the harmless prank, let relief enter the voice, and fold into helpless affectionate laughter while protesting.) "I thought I was dying! You absolute monsters—" (Chuckle) "No, no, don't touch me, I'm soaked! Wait... I'm okay. I'm actually okay. Oh, thank God. That was horrible, and I hate you, but that was also the funniest thing you've ever done. Come here, you idiots!"
```

`text` (spoken words only):

```
I thought I was dying! You absolute monsters No no don't touch me I'm soaked! Wait I'm okay. I'm actually okay. Oh thank God. That was horrible and I hate you but that was also the funniest thing you've ever done. Come here you idiots!
```

**What the ASR actually heard in the winning assembly** (parts separated by `|`):

```
 You should have seen your face when you tried that dance. Honestly, I can't believe you did it. You're killing me. Stop, stop. I need a second. |  Wait, what was- Oh my god, it's freezing! Who did that? My whole back is ice! I can't feel my shirt! I can't feel anything! |  I thought I was dying! You absolute monsters! No, no, don't touch me! I'm soaked. Wait, I'm okay. I'm actually okay. Oh, thank God. That was horrible, and I hate you. But that was also the funniest thing you've ever done. Come here, you idiots!
```

**Supervisor verdict on this round, verbatim:**

```
Sure thing! Here are the scores and feedback for each take:

1. score=7 | same_voice=yes | pacing=organic | The voice is consistent, and the pacing is natural. The transition from laughter to shock is well-executed.
2. score=8 | same_voice=yes | pacing=organic | This take has a great emotional arc. The mixture of shock and delight is palpable.
3. score=6 | same_voice=yes | pacing=runaway | The pacing speeds up a bit too much after the shock, making it feel slightly rushed.
4. score=7 | same_voice=yes | pacing=organic | Good emotional range and consistent voice. The relief at the end is well-conveyed.
5. score=8 | same_voice=yes | pacing=organic | This take captures the essence of the challenge perfectly. The laughter, shock, and subsequent emotions are all clearly audible.

RANKING: 2, 5, 1, 4, 3

FEEDBACK: For the next attempt, try to emphasize the relief even more. Maybe add a slight sigh or a more relaxed tone towards the end to really sell the transition from shock to relief. Additionally, ensure that the pacing remains consistent throughout, especially during the transition from shock to the subsequent emotions.
```

---


---

⚠ **v5 rows are shown for completeness but must not be used.** In `out_v5_real` every
`round_NN.res.json` is 2.2–2.4 hours **older** than the `round_NN.req.json` beside it: a new set of
plans was written into a directory that still held the previous run's results, the drivers consumed
them instantly, and `agent_log.json` therefore pairs new plans with old audio. Recomputing WER from
the stored transcript against the stored script gives ≈0.95 for all 27 rounds, against a reported
mean of 0.150. See [what failed](what_failed.html#1).

