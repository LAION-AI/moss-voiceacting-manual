# Appendix — every caption used, verbatim

All 351 part-captions written across the four casting generations, grouped by challenge and
then by generation and round, in the exact form they were sent to
`build_user_message(instruction=...)`. 350 of the 351 are distinct — the planner rewrote the
caption on essentially every part of every round, which is why this appendix is long.

Each entry gives the caption, the `text` field (spoken words only — the model renders an
empty field as the literal string `None`), and the adapters and sampling that went with it.
Part of the [acting-challenge tree](index.html); the winners are discussed in
[per_challenge](per_challenge.html).

⚠ `v5` captions were written by the planner but **never generated from** — see the footnote
in [per_challenge](per_challenge.html) and [what failed](what_failed.html#1). They are
included because they are still valid examples of the planner's writing, not because any
score attaches to them.

---

## C1_infidelity

> Discovering Infidelity: The Explosion. You found the evidence - a text, an email, a photo. You confront your partner. Your voice is barely controlled rage, nearly screaming but controlled, each word a weapon. Somewhere in it the rage cracks and something underneath shows through - hurt, disbelief - before it hardens again.

### C1_infidelity · v1 · round 1 (agent score 0.601, supervisor mean 6.00)

*Scene:* You confront your partner after finding undeniable evidence of their affair, barely containing your rage until hurt breaks through before you weaponize your composure again.

**part 0 — part 1 — the evidence** · targets: Anger · adapters: `Anger` @ 0.55

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Speak with low, tightly controlled rage; every word is precise and dangerous, as if you are forcing yourself not to shout. Keep the intensity contained but unmistakable.
SCRIPT:
(quietly, with lethal control) "Don't lie to me. I saw the messages. I saw the picture. So look me in the eye and tell me exactly what I'm looking at."
```

```
Don't lie to me. I saw the messages. I saw the picture. So look me in the eye and tell me exactly what I'm looking at.
```

**part 1 — part 2 — the crack** · targets: Distress, Sadness, Astonishment_Surprise · adapters: `Distress` @ 0.55; `Sadness` @ 0.4

temp 1.02 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Begin with restrained fury, then let the anger fracture into stunned hurt and disbelief. Do not become soft; the vulnerability should feel involuntary, exposed, and humiliating.
SCRIPT:
(voice tightening, then cracking despite yourself) "You said I was imagining things. You made me feel crazy for asking. Was all of it a lie? How long have you been looking at me and pretending you loved me?"
```

```
You said I was imagining things. You made me feel crazy for asking. Was all of it a lie? How long have you been looking at me and pretending you loved me?
```

**part 2 — part 3 — the hardening** · targets: Anger, Distress · adapters: `Scream` @ 0.9; `Anger` @ 0.4; `Distress` @ 0.35

temp 1.05 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Start wounded and breathless, then rebuild into nearly screaming but controlled rage. The final words should land cold and absolute, with the voice hardened by pain. Place the vocal burst inline and continue speaking immediately afterward.
SCRIPT:
(a broken breath turning into a controlled eruption) "Don't you dare touch me." (Scream) "You don't get to cry now. You don't get to make this about your guilt. Pack your things, and get out before I say something neither of us can take back."
```

```
Don't you dare touch me. You don't get to cry now. You don't get to make this about your guilt. Pack your things, and get out before I say something neither of us can take back.
```

### C1_infidelity · v1 · round 2 (agent score 0.907, supervisor mean 7.40)

*Scene:* You confront your partner with undeniable proof of betrayal, fighting to keep your rage controlled as disbelief and hurt slowly surface before you reclaim your anger.

**part 0 — part 1 — controlled confrontation** · targets: Anger · adapters: `Anger` @ 0.55

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Speak low and intensely, with barely contained rage. Keep the anger precise rather than explosive; every sentence should feel deliberate, but allow a trace of fear that the truth will be confirmed.
SCRIPT:
(quietly, forcing yourself to stay calm) "I found the message. I read every word. Don't ask me to calm down—just tell me who they are, and tell me why you lied to me."
```

```
I found the message. I read every word. Don't ask me to calm down—just tell me who they are, and tell me why you lied to me.
```

**part 1 — part 2 — the truth sinking in** · targets: Distress, Sadness, Anger · adapters: `Distress` @ 0.5; `Sadness` @ 0.4; `Anger` @ 0.3

temp 1.02 · top_p 0.95 · top_k 30 · max_new_frames 450

```
GENERAL: Let the rage continue underneath the words, but gradually lose its armor as disbelief becomes hurt. The transition must feel involuntary and organic: begin sharp, soften only when the question becomes personal, then let the final phrase carry exposed heartbreak rather than theatrical crying.
SCRIPT:
(still accusatory, then faltering as the truth lands) "You told me nothing was happening. I believed you. I kept defending you, and you were standing there knowing exactly what you had done. Did you ever love me, or was I the only one who thought this was real?"
```

```
You told me nothing was happening. I believed you. I kept defending you, and you were standing there knowing exactly what you had done. Did you ever love me, or was I the only one who thought this was real?
```

**part 2 — part 3 — anger reclaimed** · targets: Anger, Distress · adapters: `Anger` @ 0.55; `Distress` @ 0.35

temp 1.02 · top_p 0.95 · top_k 30 · max_new_frames 450

```
GENERAL: Start with the hurt still audible, then let it harden into cold, controlled fury. Do not flip suddenly into shouting; build pressure sentence by sentence until the final command is nearly screamed but remains intelligible and deliberate.
SCRIPT:
(after a wounded breath, rebuilding control) "I wanted you to tell me it wasn't true. But don't touch me. Don't cry and ask me to comfort you. Pack your things and leave. I will not let you turn what you did into something I have to survive for you."
```

```
I wanted you to tell me it wasn't true. But don't touch me. Don't cry and ask me to comfort you. Pack your things and leave. I will not let you turn what you did into something I have to survive for you.
```

### C1_infidelity · v1 · round 3 (agent score 1.009, supervisor mean 7.00)

*Scene:* You confront your partner with undeniable proof of betrayal, holding onto rage while disbelief slowly gives way to exposed hurt, then hardening into a final refusal to be manipulated.

**part 0 — part 1 — proof in hand** · targets: Anger · adapters: `Anger` @ 0.55

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 450

```
GENERAL: Use a low, precise voice under severe pressure. The rage is barely contained, not yet loud; each word is deliberate, with the effort of someone still hoping there is an explanation. Keep the delivery intimate and intelligible.
SCRIPT:
(quietly, forcing the words out) "I found the message. I read every word. I saw the picture. So don't tell me I'm confused, and don't tell me this is nothing. Just look at me and tell me the truth."
```

```
I found the message. I read every word. I saw the picture. So don't tell me I'm confused, and don't tell me this is nothing. Just look at me and tell me the truth.
```

**part 1 — part 2 — disbelief sinking in** · targets: Astonishment_Surprise, Distress, Sadness · adapters: `Astonishment_Surprise` @ 0.5; `Distress` @ 0.45; `Sadness` @ 0.4

temp 1.02 · top_p 0.95 · top_k 30 · max_new_frames 525

```
GENERAL: Let the anger remain underneath, but allow disbelief to linger and gradually collapse into hurt. Do not switch emotions abruptly. Begin with accusation, hesitate as the reality becomes undeniable, and let the final questions sound genuinely bewildered and exposed, as if you cannot make your mind accept what your eyes saw.
SCRIPT:
(still sharp, then slowing as the truth sinks in) "You said there was no one. You looked me in the face and said I was imagining it. And I believed you. I defended you. I kept searching for some explanation because I couldn't believe you would do this to me. Was I wrong about everything? Was I the only one who thought we were real?"
```

```
You said there was no one. You looked me in the face and said I was imagining it. And I believed you. I defended you. I kept searching for some explanation because I couldn't believe you would do this to me. Was I wrong about everything? Was I the only one who thought we were real?
```

**part 2 — part 3 — the armor returns** · targets: Anger, Distress · adapters: `Anger` @ 0.55; `Distress` @ 0.35

temp 1.02 · top_p 0.95 · top_k 30 · max_new_frames 475

```
GENERAL: Begin with the hurt from the previous part still present. Let a small, desperate hope die in the first sentence, then rebuild into cold, controlled rage sentence by sentence. The ending should be nearly shouted but never lose diction or control; sound like a boundary, not a tantrum.
SCRIPT:
(after a wounded beat, then steadily hardening) "I wanted you to say there was an explanation. I wanted to be wrong. But don't touch me. Don't ask me to make this easier for you. Pack your things and leave. You don't get to break my heart and then ask me to hold yours together."
```

```
I wanted you to say there was an explanation. I wanted to be wrong. But don't touch me. Don't ask me to make this easier for you. Pack your things and leave. You don't get to break my heart and then ask me to hold yours together.
```

### C1_infidelity · v2 · round 1 (agent score 0.797, supervisor mean 7.00)

*Scene:* In the kitchen, you confront your partner with proof of their infidelity, and controlled fury briefly breaks into wounded disbelief before turning cold and final.

**part 0 — controlled confrontation** · targets: Anger · adapters: `Anger` @ 0.7

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: A close, intimate performance from a betrayed partner; voice low, razor-sharp, barely controlled rage, nearly shouting but forcing every word to remain clear. Build pressure without losing intelligibility.
SCRIPT:
(quietly, with dangerous precision) "Don't lie to me. I have the message right here. I read every word, and I saw the picture. So look at me and tell me how long you've been making me a fool."
```

```
Don't lie to me. I have the message right here. I read every word, and I saw the picture. So look at me and tell me how long you've been making me a fool.
```

**part 1 — the crack** · targets: Pain, Astonishment_Surprise · adapters: `Pain` @ 0.65; `Astonishment_Surprise` @ 0.45

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Keep the same betrayed partner and continuous emotional momentum. The rage falters unexpectedly; let hurt, disbelief, and humiliation surface in a raw, exposed voice. Do not become soft or sentimental—the pain is trying to hide beneath anger.
SCRIPT:
(voice cracking despite yourself, stunned) "No—don't say you were lonely. I was here. I was loving you. I defended you to everyone, and you stood there every night knowing exactly what you were doing to me."
```

```
No—don't say you were lonely. I was here. I was loving you. I defended you to everyone, and you stood there every night knowing exactly what you were doing to me.
```

**part 2 — hardened finality** · targets: Anger · adapters: `Anger` @ 0.72

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: The exposed hurt is violently sealed away. Return to cold, controlled fury, with a near-scream held tightly in the throat; each phrase lands like a verdict. End with absolute, terrifying certainty rather than shouting chaos.
SCRIPT:
(hardening, dangerously calm, then rising) "You don't get to cry now. You don't get to make this about your guilt. You chose this. And from this moment on, you do not touch me, you do not follow me, and you do not ever call this love again."
```

```
You don't get to cry now. You don't get to make this about your guilt. You chose this. And from this moment on, you do not touch me, you do not follow me, and you do not ever call this love again.
```

### C1_infidelity · v2 · round 2 (agent score 0.830, supervisor mean 7.00)

*Scene:* You confront your partner with undeniable proof of the affair, accelerating through controlled accusations before disbelief cracks you open, then hardening into a cold final decision.

**part 0 — weaponized evidence** · targets: Anger · adapters: `Anger` @ 0.7

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 440

```
GENERAL: Keep the same intimate betrayed partner voice: low, clear, and furious, with rage held just below a scream. Use sharply varied tempo: begin slow and deliberate, then accelerate into clipped accusations, striking the most hurtful words with sudden emphasis. Every word must remain intelligible.
SCRIPT:
(quietly, each word measured; then faster and more cutting) "Don't lie to me. Don't even try. I have your message right here, your words, your little promises. I saw the picture. I saw where you were, and who you were with. So tell me—how long have you been looking me in the face and making me a fool?"
```

```
Don't lie to me. Don't even try. I have your message right here, your words, your little promises. I saw the picture. I saw where you were, and who you were with. So tell me—how long have you been looking me in the face and making me a fool?
```

**part 1 — disbelief breaks through** · targets: Astonishment_Surprise, Pain · adapters: `Astonishment_Surprise` @ 0.62; `Pain` @ 0.58

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 440

```
GENERAL: Continue as the same partner, but let the fury lose its grip. Slow dramatically and sound stunned by the reality, as if trying to understand something impossible. Emphasize the words "I was here" and "how" with wounded disbelief. Let the voice crack and expose humiliation, but keep a thread of anger underneath; do not rush back to rage yet.
SCRIPT:
(slowly, breathless with disbelief; a fragile crack on the question) "No. No, you don't get to call it a mistake. How could you do this? I was here. I was here every night, loving you, trusting you, defending you. I keep looking at that picture, and I still can't understand how you could look at me and choose to destroy us."
```

```
No. No, you don't get to call it a mistake. How could you do this? I was here. I was here every night, loving you, trusting you, defending you. I keep looking at that picture, and I still can't understand how you could look at me and choose to destroy us.
```

**part 2 — the door closes** · targets: Anger · adapters: `Anger` @ 0.72

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 440

```
GENERAL: The disbelief is abruptly sealed away. Begin very slowly and coldly, then tighten the tempo into a controlled near-scream on the final commands. Return to precise, weaponized anger rather than chaotic shouting. Make the last sentence sound irreversible, with absolute certainty and excellent intelligibility.
SCRIPT:
(after a stunned beat, cold and deliberate; building into clipped finality) "But I understand now. You made your choice. And you don't get to cry, or apologize, or ask me to make this easier for you. Don't touch me. Don't follow me. Don't call this love again. From this moment on, you are a stranger to me."
```

```
But I understand now. You made your choice. And you don't get to cry, or apologize, or ask me to make this easier for you. Don't touch me. Don't follow me. Don't call this love again. From this moment on, you are a stranger to me.
```

### C1_infidelity · v2 · round 3 (agent score 0.884, supervisor mean 7.40)

*Scene:* You confront your partner with undeniable proof of the affair; your controlled rage gradually reveals devastating hurt, then seals itself into a calm, irreversible decision to leave.

**part 0 — rage beginning to crack** · targets: Anger · adapters: `Anger` @ 0.68

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 440

```
GENERAL: Same intimate betrayed-partner voice, low and razor-sharp, nearly shouting but fiercely controlled. Vary tempo: begin slow over the evidence, accelerate through the accusations, then let the final question drag as anger starts to reveal pain. Emphasize "you promised me" and "fool" without losing clarity.
SCRIPT:
(quietly, with precise fury; accelerating, then faltering) "Don't lie. I have the message, I have the picture, and I have every word you thought I would never see. You stood in front of me and promised me I was the only one. How long have you been looking at me like this—like I was just a fool?"
```

```
Don't lie. I have the message, I have the picture, and I have every word you thought I would never see. You stood in front of me and promised me I was the only one. How long have you been looking at me like this—like I was just a fool?
```

**part 1 — anger becomes hurt** · targets: Pain, Astonishment_Surprise · adapters: `Pain` @ 0.62; `Astonishment_Surprise` @ 0.58

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 440

```
GENERAL: Continue seamlessly. Do not switch suddenly to sadness; let the anger drain out of each sentence, exposing stunned hurt and disbelief underneath. Slow the tempo progressively, with a fragile voice on "I was here" and "I trusted you." Sound less like an accusation and more like someone trying, unsuccessfully, to make the betrayal make sense. Keep the pain intelligible and emotionally contained.
SCRIPT:
(voice still angry but gradually weakening, then raw with disbelief) "I was here. I was here every night, loving you, making a life with you. I kept choosing you. I defended you when people warned me, because I trusted you. So tell me how I am supposed to look at you now and believe that any of it was real."
```

```
I was here. I was here every night, loving you, making a life with you. I kept choosing you. I defended you when people warned me, because I trusted you. So tell me how I am supposed to look at you now and believe that any of it was real.
```

**part 2 — definitive hardening** · targets: Anger · adapters: `Anger` @ 0.72

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 440

```
GENERAL: The hurt stops you for a moment, then is deliberately locked away. Begin quiet and exhausted, become colder and more deliberate with each sentence, and finish with controlled, absolute finality rather than chaotic yelling. Make the decision unmistakable: this relationship is over, and nothing the partner says can change it. Strike "I'm done" and "it is over" with severe certainty.
SCRIPT:
(after the exposed hurt, quietly; hardening into a final verdict) "I wanted an explanation. I wanted one reason that could make this less cruel. There isn't one. You chose this, and now I choose what happens next. I'm done begging you to love me honestly. Pack your things. You don't get another chance, because this is over."
```

```
I wanted an explanation. I wanted one reason that could make this less cruel. There isn't one. You chose this, and now I choose what happens next. I'm done begging you to love me honestly. Pack your things. You don't get another chance, because this is over.
```

### C1_infidelity · v5 ⚠ · round 1 (agent score 0.894, supervisor mean 7.40)

*Scene:* You confront your partner after finding undeniable proof of their affair, trying to keep your rage controlled until the hurt breaks through before you steel yourself again.

**part 0 — controlled confrontation** · targets: Anger · adapters: `Anger` @ 0.55

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Start with barely controlled rage: quiet, precise, and frighteningly restrained, with clipped consonants and each word aimed like a weapon. Do not begin screaming; let the pressure build underneath the control.
SCRIPT:
(through clenched teeth, almost whispering) "Don't lie to me. I have the message, the photograph, the time you said you were here. I stood beside you and believed every word. So look at me now—and tell me which part of this you thought I would never find."
```

```
Don't lie to me. I have the message, the photograph, the time you said you were here. I stood beside you and believed every word. So look at me now—and tell me which part of this you thought I would never find.
```

**part 1 — the wound opens** · targets: Pain · turn_from: Anger · adapters: `Pain` @ 0.7

temp 1.05 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Change sharply from controlled anger into stunned disbelief and exposed hurt. Stop sounding like an interrogator; let the certainty falter, the breath catch, and the voice crack as the betrayal becomes emotionally real. Do not stay enraged—reveal the person underneath.
SCRIPT:
(the certainty suddenly collapses, voice cracking) "You said I was imagining it. You held my face and called me paranoid. I loved you. God, I loved you—and you watched me doubt myself while you were giving all of this to someone else."
```

```
You said I was imagining it. You held my face and called me paranoid. I loved you. God, I loved you—and you watched me doubt myself while you were giving all of this to someone else.
```

**part 2 — rage hardens** · targets: Anger · turn_from: Pain · adapters: `Anger` @ 0.72

temp 1.05 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Change again from wounded disbelief into cold, commanding rage. Stop sounding broken; pull the hurt inward, regain control, and let the final words land with a near-scream that remains intelligible and deliberate.
SCRIPT:
(the hurt is swallowed; rage returns colder and louder) "Don't touch me. Don't you dare ask me to understand this. You made your choice the moment you lied—and now you can live with the truth. Get out. Before I say something neither of us can take back."
```

```
Don't touch me. Don't you dare ask me to understand this. You made your choice the moment you lied—and now you can live with the truth. Get out. Before I say something neither of us can take back.
```

### C1_infidelity · v5 ⚠ · round 2 (agent score 0.870, supervisor mean 7.40)

*Scene:* You confront your partner with undeniable proof of infidelity, delivering each accusation with deliberate restraint until disbelief exposes the wound, then sealing it beneath a final command.

**part 0 — each word lands** · targets: Anger · adapters: `Anger` @ 0.55

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Begin in barely controlled rage, quiet and precise rather than loud. Strike each short phrase separately, with clipped consonants and deliberate emphasis, as if every word is evidence placed on a table. Keep the fury contained and dangerous; do not spend the emotional peak yet.
SCRIPT:
(through clenched teeth, each sentence a measured strike) "Don't lie. Not one more lie. I have the message. I have the photograph. I have the time you said you were here. You looked me in the eyes, and you made me believe you."
```

```
Don't lie. Not one more lie. I have the message. I have the photograph. I have the time you said you were here. You looked me in the eyes, and you made me believe you.
```

**part 1 — disbelief lingers** · targets: Pain · turn_from: Anger · adapters: `Pain` @ 0.72

temp 1.05 · top_p 0.95 · top_k 30 · max_new_frames 450

```
GENERAL: Change from the controlled attack into stunned disbelief and exposed hurt. Slow down and let the disbelief linger between thoughts, but do not use silence tags. The anger loses its shape; the voice searches for an explanation it cannot accept. Let the pain show plainly and sustain it through the whole part rather than rushing back to rage.
SCRIPT:
(the certainty falters; wounded disbelief, lingering on the impossible truth) "You told me I was imagining it. You held my face and called me paranoid. I remember that. I remember believing you. How could you stand there and watch me doubt myself? How could you do that to me?"
```

```
You told me I was imagining it. You held my face and called me paranoid. I remember that. I remember believing you. How could you stand there and watch me doubt myself? How could you do that to me?
```

**part 2 — the answer becomes clear** · targets: Astonishment_Surprise · turn_from: Pain · adapters: `Astonishment_Surprise` @ 0.68

temp 1.03 · top_p 0.95 · top_k 30 · max_new_frames 450

```
GENERAL: Change from hurt and disbelief into a terrible, dawning understanding. Stop pleading for an explanation; let each realization arrive slowly, then sharpen into accusation. The voice should regain precision, with every phrase deliberately aimed at the person who betrayed you. Build intensity without losing intelligibility.
SCRIPT:
(the hurt turns into cold understanding, each accusation carefully placed) "It wasn't one mistake. It was every morning you kissed me and knew. Every night you came home and knew. You made me feel crazy so you could keep doing it. You didn't just betray me. You erased what was real between us."
```

```
It wasn't one mistake. It was every morning you kissed me and knew. Every night you came home and knew. You made me feel crazy so you could keep doing it. You didn't just betray me. You erased what was real between us.
```

**part 3 — rage seals shut** · targets: Anger · turn_from: Astonishment_Surprise · adapters: `Anger` @ 0.72

temp 1.05 · top_p 0.95 · top_k 30 · max_new_frames 450

```
GENERAL: Change from exposed hurt into cold, commanding rage. Stop sounding wounded; swallow the grief and harden it into authority. Make the final commands feel like deliberate strikes, escalating toward a near-scream while keeping every word clean and intelligible. End with finality, not pleading.
SCRIPT:
(the wound is locked away; colder rage, each command landing like a blow) "Don't touch me. Don't ask me to understand. You made your choice every time you lied. Now you can live with it. Get out. And don't come back expecting the person you betrayed to still be here."
```

```
Don't touch me. Don't ask me to understand. You made your choice every time you lied. Now you can live with it. Get out. And don't come back expecting the person you betrayed to still be here.
```

### C1_infidelity · v5 ⚠ · round 3 (agent score 0.717, supervisor mean 6.60)

*Scene:* You confront your partner with undeniable proof of infidelity, striking with controlled precision before allowing the betrayal to break you open, then reclaiming the rage and ordering them away.

**part 0 — measured strikes** · targets: Anger · adapters: `Anger` @ 0.55

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Begin in barely controlled rage, quieter than a scream and intensely precise. Vary the pace: deliver the first words slowly and separately, then fire the evidence in short clipped bursts before slowing again for the personal betrayal. Make every emphasized word feel intentional, like a weapon placed exactly where it will hurt. Stay controlled; do not reveal the wound yet.
SCRIPT:
(quiet, each word isolated; then sharper and faster) "Don't lie. Not one more lie. I have the message. The photograph. The time you said you were here. You looked me in the eyes, and you made me believe you."
```

```
Don't lie. Not one more lie. I have the message. The photograph. The time you said you were here. You looked me in the eyes, and you made me believe you.
```

**part 1 — the wound lingers** · targets: Pain · turn_from: Anger · adapters: `Pain` @ 0.74

temp 1.05 · top_p 0.95 · top_k 30 · max_new_frames 450

```
GENERAL: Change completely from attack into vulnerable disbelief. Let the pace slow and stay slow, with fragile breaths and a voice that cannot make the betrayal fit together. Linger emotionally on the memories and the questions; do not rush through the hurt or turn it back into anger. The composure should thin until the final question feels genuinely helpless.
SCRIPT:
(the rage drains away; slow, stunned, and quietly breaking) "You told me I was imagining it. You held my face and called me paranoid. I remember that. I remember believing you. I trusted you. I loved you. And you watched me doubt myself while you were doing this. How could you stand there and watch me? How could you do that to me?"
```

```
You told me I was imagining it. You held my face and called me paranoid. I remember that. I remember believing you. I trusted you. I loved you. And you watched me doubt myself while you were doing this. How could you stand there and watch me? How could you do that to me?
```

**part 2 — rage returns** · targets: Anger · turn_from: Pain · adapters: `Anger` @ 0.74

temp 1.05 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Change from exposed hurt into cold, deliberate fury. Start low and almost calm, as if the answer has finally become undeniable, then accelerate through the repeated accusations and finish in a controlled near-scream. Stop sounding helpless; each final word must land as a chosen strike, with clear intelligibility rather than uncontrolled shouting.
SCRIPT:
(the hurt seals over; low at first, then building into a precise near-scream) "It wasn't one mistake. It was every morning you kissed me and knew. Every night you came home and knew. You made me feel crazy so you could keep doing it. You didn't just betray me. You erased what was real between us. Don't touch me. Get out."
```

```
It wasn't one mistake. It was every morning you kissed me and knew. Every night you came home and knew. You made me feel crazy so you could keep doing it. You didn't just betray me. You erased what was real between us. Don't touch me. Get out.
```

### C1_infidelity · v7 · round 1 (agent score 0.648, supervisor mean 6.80)

*Scene:* You confront your partner after finding undeniable proof of their affair, and controlled fury briefly gives way to wounded disbelief before the rage returns.

**part 0 — the evidence becomes an accusation** · targets: Anger · adapters: `Anger` @ 0.65

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400 · tempo_target 4 · chunk_target 3 · prosody_turn False

```
GENERAL: A close-miked adult voice with a low, naturally textured register, clear diction, grounded breath, and intense emotional realism; one speaker performing one continuous scene.
SCRIPT:
(Barely controlled rage, nearly shouting but forcing every word into precise, deliberate blows.) "I found the messages. I saw the photo. Don't stand there and tell me I'm imagining this. You looked me in the eye every night and lied to me. How long? How long have you been making me a fool?"
```

```
I found the messages. I saw the photo. Don't stand there and tell me I'm imagining this. You looked me in the eye every night and lied to me. How long? How long have you been making me a fool?
```

**part 1 — the rage cracks open** · targets: Pain, Astonishment_Surprise · turn_from: Anger · adapters: `Pain` @ 0.72

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400 · tempo_target 2 · chunk_target 1 · prosody_turn True

```
GENERAL: A close-miked adult voice with a low, naturally textured register, clear diction, grounded breath, and intense emotional realism; one speaker performing one continuous scene.
SCRIPT:
(The anger stops being clean and forceful; it stalls, the breath catches, and wounded disbelief surfaces beneath the accusation.) "No... no, I know what I read. I know what I saw. But why would you do this to us? Was any of it real? When you said you loved me... were you thinking about them?"
```

```
No... no, I know what I read. I know what I saw. But why would you do this to us? Was any of it real? When you said you loved me... were you thinking about them?
```

**part 2 — the wound hardens** · targets: Anger · turn_from: Pain · adapters: `Anger` @ 0.75

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400 · tempo_target 4 · chunk_target 2 · prosody_turn True

```
GENERAL: A close-miked adult voice with a low, naturally textured register, clear diction, grounded breath, and intense emotional realism; one speaker performing one continuous scene.
SCRIPT:
(The hurt stops pleading and hardens back into controlled fury; the voice rises toward a breaking point, but every word remains intelligible and aimed like a weapon.) "Don't touch me. Don't say my name like you still have the right to say it. You made your choice. Now look at me and tell me the truth, every last piece of it—or get out of my life."
```

```
Don't touch me. Don't say my name like you still have the right to say it. You made your choice. Now look at me and tell me the truth, every last piece of it—or get out of my life.
```

*Caption actually sent for the continuation parts* (the harness appends the same-speaker / still-acting / no-onset-burst sentences and, when `turn_from` is set, an explicit turn sentence):

part `the rage cracks open` — effective caption:

```
GENERAL: A close-miked adult voice with a low, naturally textured register, clear diction, grounded breath, and intense emotional realism; one speaker performing one continuous scene. The same speaker from the preceding audio continues without interruption: identical voice, identical person, same microphone and same room -- no cut, no new narrator, no change of casting. Across this passage the same voice moves out of Anger and into Pain, Astonishment_Surprise.
SCRIPT:
(The anger stops being clean and forceful; it stalls, the breath catches, and wounded disbelief surfaces beneath the accusation.) "No... no, I know what I read. I know what I saw. But why would you do this to us? Was any of it real? When you said you loved me... were you thinking about them?"
```

### C1_infidelity · v7 · round 2 (agent score 0.716, supervisor mean 6.00)

*Scene:* You confront your partner after finding undeniable proof of their affair, and controlled fury briefly shatters into wounded disbelief before returning as a harder, more dangerous rage.

**part 0 — the evidence becomes an accusation** · targets: Anger · adapters: `Anger` @ 0.68

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 425 · tempo_target 3 · chunk_target 3 · prosody_turn True

```
GENERAL: A close-miked adult voice with a low, naturally textured register, clear diction, grounded breath, and intense emotional realism; one speaker performing one continuous scene.
SCRIPT:
(Stop forcing the pace; speak with deliberate, measured fury, letting each accusation land cleanly instead of sprinting. Nearly shouting, but keeping absolute control.) "I found the messages. I saw the photo. Don't stand there and tell me I'm imagining this. You looked me in the eye every night and lied to me. You brought that lie into our home. How long? How long have you been making me a fool?"
```

```
I found the messages. I saw the photo. Don't stand there and tell me I'm imagining this. You looked me in the eye every night and lied to me. You brought that lie into our home. How long? How long have you been making me a fool?
```

**part 1 — the rage breaks into disbelief** · targets: Pain, Astonishment_Surprise · turn_from: Anger · adapters: `Pain` @ 0.75; `Astonishment_Surprise` @ 0.55

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 425 · tempo_target 2 · chunk_target 2 · prosody_turn True

```
GENERAL: A close-miked adult voice with a low, naturally textured register, clear diction, grounded breath, and intense emotional realism; one speaker performing one continuous scene.
SCRIPT:
(The rage stops being a weapon and visibly cracks; the breath catches, the words come in short, uneven groups, and the disbelief sounds painfully intimate rather than theatrical.) "No... no, I know what I read. I know what I saw. Don't make me defend the truth to you. Why would you do this to us? Was any of it real? When you said you loved me... were you thinking about them?"
```

```
No... no, I know what I read. I know what I saw. Don't make me defend the truth to you. Why would you do this to us? Was any of it real? When you said you loved me... were you thinking about them?
```

**part 2 — the wound hardens again** · targets: Anger · turn_from: Pain · adapters: `Anger` @ 0.75

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 425 · tempo_target 3 · chunk_target 3 · prosody_turn True

```
GENERAL: A close-miked adult voice with a low, naturally textured register, clear diction, grounded breath, and intense emotional realism; one speaker performing one continuous scene.
SCRIPT:
(The pleading stops and the hurt seals over into colder fury. Build steadily, not quickly: the voice becomes firm and dangerous, with a final controlled rise rather than a runaway scream.) "Don't touch me. Don't say my name like you still have the right to say it. You made your choice, and you don't get to hide behind silence now. Look at me. Tell me the truth, every last piece of it—or get out of my life."
```

```
Don't touch me. Don't say my name like you still have the right to say it. You made your choice, and you don't get to hide behind silence now. Look at me. Tell me the truth, every last piece of it—or get out of my life.
```

*Caption actually sent for the continuation parts* (the harness appends the same-speaker / still-acting / no-onset-burst sentences and, when `turn_from` is set, an explicit turn sentence):

part `the rage breaks into disbelief` — effective caption:

```
GENERAL: A close-miked adult voice with a low, naturally textured register, clear diction, grounded breath, and intense emotional realism; one speaker performing one continuous scene. The same speaker from the preceding audio continues without interruption: identical voice, identical person, same microphone and same room -- no cut, no new narrator, no change of casting. Across this passage the same voice moves out of Anger and into Pain, Astonishment_Surprise.
SCRIPT:
(The rage stops being a weapon and visibly cracks; the breath catches, the words come in short, uneven groups, and the disbelief sounds painfully intimate rather than theatrical.) "No... no, I know what I read. I know what I saw. Don't make me defend the truth to you. Why would you do this to us? Was any of it real? When you said you loved me... were you thinking about them?"
```

### C1_infidelity · v7 · round 3 (agent score 0.694, supervisor mean 6.00)

*Scene:* You confront your partner with undeniable proof of an affair, holding a steady fury that fractures into exposed disbelief before returning as cold, controlled resolve.

**part 0 — the evidence becomes undeniable** · targets: Anger · adapters: `Anger` @ 0.62

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400 · tempo_target 2 · chunk_target 2 · prosody_turn False

```
GENERAL: A close-miked adult voice with a low, naturally textured register, clear diction, grounded breath, and intense emotional realism; one speaker performing one continuous scene.
SCRIPT:
(Keep the voice steady and recognizable, using measured, deliberate fury rather than volume; each sentence lands as a precise accusation.) "I found the messages. I saw the photo. Don't tell me I'm imagining this. You looked me in the eye every night and lied to me. How long have you been making me a fool?"
```

```
I found the messages. I saw the photo. Don't tell me I'm imagining this. You looked me in the eye every night and lied to me. How long have you been making me a fool?
```

**part 1 — the fury cracks into hurt** · targets: Pain, Astonishment_Surprise · turn_from: Anger · adapters: `Pain` @ 0.72; `Astonishment_Surprise` @ 0.48

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400 · tempo_target 2 · chunk_target 2 · prosody_turn True

```
GENERAL: A close-miked adult voice with a low, naturally textured register, clear diction, grounded breath, and intense emotional realism; one speaker performing one continuous scene.
SCRIPT:
(The controlled accusation stops being armor; keep the same voice and grounded register, but let it fracture into a small, involuntary hurt. Use short, careful groups, as if the truth is becoming impossible to say.) "No... I know what I read. I know what I saw. Why would you do this to us? Was any of it real? When you said you loved me... did you mean it at all?"
```

```
No... I know what I read. I know what I saw. Why would you do this to us? Was any of it real? When you said you loved me... did you mean it at all?
```

**part 2 — the hurt hardens into resolve** · targets: Anger · turn_from: Pain · adapters: `Anger` @ 0.68

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400 · tempo_target 3 · chunk_target 3 · prosody_turn True

```
GENERAL: A close-miked adult voice with a low, naturally textured register, clear diction, grounded breath, and intense emotional realism; one speaker performing one continuous scene.
SCRIPT:
(The exposed hurt stops pleading and seals back over; preserve the same voice and breath, building only slightly into cold, controlled rage. Do not sprint or scream: the final words are quiet, firm, and more dangerous for being contained.) "Don't touch me. Don't say my name like you still have the right to say it. You made your choice. Now tell me the whole truth, or get out of my life."
```

```
Don't touch me. Don't say my name like you still have the right to say it. You made your choice. Now tell me the whole truth, or get out of my life.
```

*Caption actually sent for the continuation parts* (the harness appends the same-speaker / still-acting / no-onset-burst sentences and, when `turn_from` is set, an explicit turn sentence):

part `the fury cracks into hurt` — effective caption:

```
GENERAL: A close-miked adult voice with a low, naturally textured register, clear diction, grounded breath, and intense emotional realism; one speaker performing one continuous scene. The same speaker from the preceding audio continues without interruption: identical voice, identical person, same microphone and same room -- no cut, no new narrator, no change of casting. Across this passage the same voice moves out of Anger and into Pain, Astonishment_Surprise.
SCRIPT:
(The controlled accusation stops being armor; keep the same voice and grounded register, but let it fracture into a small, involuntary hurt. Use short, careful groups, as if the truth is becoming impossible to say.) "No... I know what I read. I know what I saw. Why would you do this to us? Was any of it real? When you said you loved me... did you mean it at all?"
```

---

## C2_biggest_fear

> Facing Your Biggest Fear. You are finally doing the thing that terrifies you. Your voice starts shaky and barely functional, talking yourself through it: 'I can do this.' Panicked but determined. As you face it your voice becomes stronger: 'I'm doing it. I'm actually doing it.' By the end you have survived it and something like elation breaks through the fear.

### C2_biggest_fear · v1 · round 1 (agent score 0.925, supervisor mean 8.00)

*Scene:* At the edge of a terrifying challenge, a panicked person talks themselves through it, then discovers courage and exhilaration after surviving.

**part 0 — shaky resolve** · targets: Fear, Distress · adapters: `Fear` @ 0.65; `Distress` @ 0.45

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Intimate, breathless voice with genuine panic barely held together; words are quiet, shaky, and self-directed, but determination is beginning to fight through the fear.
SCRIPT:
(whispered, trembling, forcing each word out) "Okay... okay. I can do this. Just one step. Don't look down. Breathe. I can do this."
```

```
Okay... okay. I can do this. Just one step. Don't look down. Breathe. I can do this.
```

**part 1 — crossing the threshold** · targets: Fear, Relief · adapters: `Fear` @ 0.45; `Relief` @ 0.5

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: The fear is still audible, but the voice grows steadier and more forceful as the speaker commits; use rising urgency, clear articulation, and hard-won confidence rather than shouting.
SCRIPT:
(voice catching, then gathering strength) "No. I'm not backing out. I'm doing it. I'm actually doing it. Keep moving. Keep moving. I'm still here."
```

```
No. I'm not backing out. I'm doing it. I'm actually doing it. Keep moving. Keep moving. I'm still here.
```

**part 2 — surviving** · targets: Elation, Relief · adapters: `Elation` @ 0.65; `Relief` @ 0.55

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Release the tension into stunned, breathless elation; begin in disbelief, then let joy and pride break through naturally, ending bright, exhilarated, and emotionally open.
SCRIPT:
(laughing through disbelief, then soaring with relief) "I did it. Oh my God, I did it. I'm okay. I'm really okay. I was so scared... and I did it anyway."
```

```
I did it. Oh my God, I did it. I'm okay. I'm really okay. I was so scared... and I did it anyway.
```

### C2_biggest_fear · v1 · round 2 (agent score 0.953, supervisor mean 7.00)

*Scene:* At the edge of a terrifying challenge, a person notices panic taking over, slowly steadies their body through each step, and finally breaks into relieved, astonished joy after surviving.

**part 0 — panic in the body** · targets: Fear, Distress · adapters: `Fear` @ 0.65; `Distress` @ 0.5

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 450

```
GENERAL: Intimate, breathless, genuinely frightened voice; make the fear physical and immediate, with a trembling jaw, tight throat, shallow breathing, and words that almost fail, while a tiny thread of determination remains.
SCRIPT:
(quietly, shaking, trying to control the breath) "My hands are shaking. I can't feel my fingers. My heart is going so fast... okay. Look at me. Breathe. I can do this."
```

```
My hands are shaking. I can't feel my fingers. My heart is going so fast... okay. Look at me. Breathe. I can do this.
```

**part 1 — first movement** · targets: Fear, Relief · adapters: `Fear` @ 0.5; `Relief` @ 0.4

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 450

```
GENERAL: Keep the fear audible in the breath and tightness of the voice, but let determination gradually become more reliable; do not jump to confidence, and let each phrase sound like a hard-won physical action.
SCRIPT:
(voice catching, then steadier with each word) "My knees want to give out. I can feel the fear everywhere. But I'm moving. Just keep breathing... one step, then another. I'm doing it."
```

```
My knees want to give out. I can feel the fear everywhere. But I'm moving. Just keep breathing... one step, then another. I'm doing it.
```

**part 2 — courage taking hold** · targets: Relief, Fear · adapters: `Relief` @ 0.55; `Fear` @ 0.35

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 450

```
GENERAL: The body is still tense, but the voice now has grounded control and growing disbelief; build slowly from strained concentration into clear, stronger speech, preserving the memory of fear underneath the courage.
SCRIPT:
(deeply focused, strength arriving without haste) "I'm still scared. My chest is still tight. But I'm not stopping. I'm actually doing it. I'm actually doing it. I can breathe. I can stand here."
```

```
I'm still scared. My chest is still tight. But I'm not stopping. I'm actually doing it. I'm actually doing it. I can breathe. I can stand here.
```

**part 3 — relief and elation** · targets: Relief, Elation · adapters: `Relief` @ 0.6; `Elation` @ 0.6

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 450

```
GENERAL: Begin stunned and physically released, as the tension drains from the body; gradually let relief become warm laughter and then bright, astonished elation, ending with earned joy rather than sudden theatrical excitement.
SCRIPT:
(breathing freely at last, disbelieving, then glowing with joy) "I did it. My hands stopped shaking. Oh my God... I'm okay. I'm really okay. I was terrified, and I did it anyway. I did it!"
```

```
I did it. My hands stopped shaking. Oh my God... I'm okay. I'm really okay. I was terrified, and I did it anyway. I did it!
```

### C2_biggest_fear · v1 · round 3 (agent score 0.927, supervisor mean 7.00)

*Scene:* At the threshold of a terrifying challenge, a person moves through shaking panic one deliberate step at a time until fear loosens into earned triumph and relief.

**part 0 — fear taking over** · targets: Fear, Distress · adapters: `Fear` @ 0.65; `Distress` @ 0.45

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 380

```
GENERAL: Intimate and physically frightened, with a tight throat, shallow breath, trembling hands, and words that nearly falter; keep the determination very small but present, never melodramatic.
SCRIPT:
(whispering through a shaky breath) "My hands won't stop shaking. My chest is so tight. I don't want to do this. But I'm here. I can do this."
```

```
My hands won't stop shaking. My chest is so tight. I don't want to do this. But I'm here. I can do this.
```

**part 1 — one step** · targets: Fear, Relief · adapters: `Fear` @ 0.5; `Relief` @ 0.4

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 380

```
GENERAL: Preserve the fear in the breath and body, but let control return in tiny increments; each sentence should feel like a physical action completed despite panic, with restrained, hard-won focus.
SCRIPT:
(voice trembling, counting each effort) "My knees are shaking too. Breathe in. Breathe out. Just one step. There. I moved. I'm still scared, but I moved."
```

```
My knees are shaking too. Breathe in. Breathe out. Just one step. There. I moved. I'm still scared, but I moved.
```

**part 2 — courage settling** · targets: Relief, Fear · adapters: `Relief` @ 0.55; `Fear` @ 0.35

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 380

```
GENERAL: Let the voice become steadier without becoming joyful yet; the body remains tense, but breathing and balance are returning, creating quiet confidence and a dawning sense of triumph.
SCRIPT:
(steadier now, surprised by their own control) "My heart is still racing. My legs still feel weak. But I'm standing. I'm moving. I'm actually doing it. I am not turning back."
```

```
My heart is still racing. My legs still feel weak. But I'm standing. I'm moving. I'm actually doing it. I am not turning back.
```

**part 3 — earned triumph** · targets: Elation, Relief · adapters: `Elation` @ 0.6; `Relief` @ 0.55

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 380

```
GENERAL: Begin with stunned physical release as the tension drains, then build gradually into warm relief and finally bright, contained elation; make the joy feel earned and almost difficult to believe.
SCRIPT:
(exhaling, disbelieving, then smiling through rising triumph) "My hands are still trembling... but I did it. I can breathe. I'm okay. I was terrified, and I did it anyway. I actually did it."
```

```
My hands are still trembling... but I did it. I can breathe. I'm okay. I was terrified, and I did it anyway. I actually did it.
```

### C2_biggest_fear · v2 · round 1 (agent score 0.853, supervisor mean 7.40)

*Scene:* Alone at the threshold of the terrifying thing, you talk yourself through panic until you cross it and discover you have survived.

**part 0 — part 1 — the threshold** · targets: Fear, Distress · adapters: `Gasp` @ 0.5; `Fear` @ 0.5

temp 1.05 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: A young adult facing an overwhelming fear; begin breathless, shaky, and barely able to speak, with intimate realism and panic held just beneath the words. Let determination flicker underneath the fear.
SCRIPT:
(voice trembling, breath catching) "I can do this. I can do this. Just... just one step. Don't look down. Don't think about what could happen. I'm here. I'm ready."
```

```
I can do this. I can do this. Just... just one step. Don't look down. Don't think about what could happen. I'm here. I'm ready.
```

**part 1 — part 2 — crossing the line** · targets: Fear, Relief · adapters: `Fear` @ 0.45; `Relief` @ 0.4

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Continue with the same actor and rising resolve. The panic is still audible, but the voice steadies and gains volume as the actor physically commits. Build momentum through short, increasingly confident phrases.
SCRIPT:
(breathing hard, then finding strength) "Okay. I'm moving. I'm doing it. I'm actually doing it. Keep going. Don't stop now. I know it hurts, I know I'm scared, but I'm still here. One more step. Then another."
```

```
Okay. I'm moving. I'm doing it. I'm actually doing it. Keep going. Don't stop now. I know it hurts, I know I'm scared, but I'm still here. One more step. Then another.
```

**part 2 — part 3 — surviving** · targets: Relief, Elation, Astonishment_Surprise · adapters: `Relief` @ 0.6; `Elation` @ 0.65

temp 1.05 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: The same actor has made it through. Begin in stunned disbelief, then let relief release the body and let genuine, disbelieving elation break through. Laughing joy may touch the voice, but keep every word clear and emotionally earned.
SCRIPT:
(stunned, then laughing with breathless relief) "I did it. I actually did it. I'm okay. I'm okay! Oh my God... I was so afraid, and I did it anyway. I made it through. I can breathe. I can do anything."
```

```
I did it. I actually did it. I'm okay. I'm okay! Oh my God... I was so afraid, and I did it anyway. I made it through. I can breathe. I can do anything.
```

### C2_biggest_fear · v2 · round 2 (agent score 0.845, supervisor mean 8.00)

*Scene:* At the threshold of a terrifying act, panic seizes your body, then gradually gives way to control, relief, and stunned elation as you realize you have survived.

**part 0 — part 1 — fear in the body** · targets: Fear, Distress · adapters: `Gasp` @ 0.5; `Fear` @ 0.5

temp 1.05 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Intimate, realistic performance from an actor facing their greatest fear. Begin barely functional: shallow breath, trembling lips, tight throat, racing thoughts, and a body that wants to flee. Do not make the fear generic; let every sensation interfere with speech while determination fights to remain present.
SCRIPT:
(whispering through a shaky breath, frightened by the sensations) "I can do this. I can do this. My hands are shaking. My chest is so tight. I can't feel my feet. Just breathe. Just look ahead. Don't run. I am still here. I can do this."
```

```
I can do this. I can do this. My hands are shaking. My chest is so tight. I can't feel my feet. Just breathe. Just look ahead. Don't run. I am still here. I can do this.
```

**part 1 — part 2 — the body obeys** · targets: Fear, Determination · adapters: `Fear` @ 0.4; `Relief` @ 0.4

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Continue as the same actor, still physically afraid but now moving through the fear. Make the transition unmistakable: breathing begins to deepen, the voice stops collapsing, trembling becomes effort and forward momentum. Build steadily rather than suddenly; determination should win one physical sensation at a time.
SCRIPT:
(breathing hard, then discovering a steadier voice) "My knees are weak, but they're holding me. My lungs are burning, but I'm breathing. Okay. Move. I'm doing it. I'm actually doing it. One step. Feel the ground. One more. The fear is still here, and I am still moving."
```

```
My knees are weak, but they're holding me. My lungs are burning, but I'm breathing. Okay. Move. I'm doing it. I'm actually doing it. One step. Feel the ground. One more. The fear is still here, and I am still moving.
```

**part 2 — part 3 — the release** · targets: Relief, Elation, Astonishment_Surprise · adapters: `Relief` @ 0.55; `Elation` @ 0.65

temp 1.05 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: The same actor has crossed through the terrifying moment. Start with stunned silence in the voice and the physical shock of realizing the body is safe, then let breath return and let genuine elation burst through. The joy should feel earned by the fear, not performed over it; grow into disbelieving laughter and bright, triumphant certainty while keeping the words intelligible.
SCRIPT:
(stunned, taking a full breath, then breaking into breathless laughter) "Wait. It's over. My hands have stopped shaking. I can breathe. I did it. I actually did it! I was terrified, and I moved anyway. I'm okay. I'm alive. I made it through. Oh my God, I did it!"
```

```
Wait. It's over. My hands have stopped shaking. I can breathe. I did it. I actually did it! I was terrified, and I moved anyway. I'm okay. I'm alive. I made it through. Oh my God, I did it!
```

### C2_biggest_fear · v2 · round 3 (agent score 0.899, supervisor mean 7.00)

*Scene:* At the threshold of a terrifying act, panic slowly loosens its grip as you stay present, take one deliberate step at a time, and finally realize with growing wonder that you have survived.

**part 0 — part 1 — panic held together** · targets: Fear, Distress · adapters: `Gasp` @ 0.5; `Fear` @ 0.5

temp 1.03 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Intimate, physically truthful fear from an actor facing their greatest terror. Begin barely functional: shallow breathing, a tight throat, trembling hands, and the instinct to flee. Do not rush toward confidence; determination is only a fragile thread underneath the panic. Keep the words clear despite the physical struggle.
SCRIPT:
(voice trembling, breath catching, then forcing the words out) "I can do this. I can do this. My hands won't stop shaking. My heart is pounding so hard. I want to run. Just breathe. Just stay here. Look at it. Don't turn away. One breath. That's all I need."
```

```
I can do this. I can do this. My hands won't stop shaking. My heart is pounding so hard. I want to run. Just breathe. Just stay here. Look at it. Don't turn away. One breath. That's all I need.
```

**part 1 — part 2 — choosing the next step** · targets: Fear, Relief · adapters: `Fear` @ 0.35; `Relief` @ 0.35

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Continue as the same actor. Let panic remain present, but make the change gradual and physical: breathing becomes slightly deeper, the throat opens, and the trembling voice gains a little support. Determination should emerge from accepting the fear, not replacing it. Build patiently toward forward motion.
SCRIPT:
(breathing unevenly, finding a small pocket of control) "The fear is still here. I can feel it in my knees, in my chest. But I don't have to wait for it to disappear. I can move while I'm afraid. Okay. Feel the ground. Lift your foot. Put it down. That's it. I'm still here."
```

```
The fear is still here. I can feel it in my knees, in my chest. But I don't have to wait for it to disappear. I can move while I'm afraid. Okay. Feel the ground. Lift your foot. Put it down. That's it. I'm still here.
```

**part 2 — part 3 — strength arriving** · targets: Relief, Fear · adapters: `Relief` @ 0.45; `Fear` @ 0.3

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Continue seamlessly. The actor is now committed, still exerting effort, but the voice has become steady and grounded. Let each repeated phrase sound more certain than the last. Keep a trace of fear in the body so the determination feels earned; do not jump to triumph.
SCRIPT:
(steadier now, surprised by your own momentum) "I'm moving. I'm doing it. I'm actually doing it. My legs are still shaking, but they're carrying me. My breathing is still rough, but I can hear it slowing down. One more step. I don't need to be fearless. I just need to keep going."
```

```
I'm moving. I'm doing it. I'm actually doing it. My legs are still shaking, but they're carrying me. My breathing is still rough, but I can hear it slowing down. One more step. I don't need to be fearless. I just need to keep going.
```

**part 3 — part 4 — realizing you survived** · targets: Relief, Elation, Astonishment_Surprise · adapters: `Relief` @ 0.55; `Elation` @ 0.45

temp 1.03 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: The same actor has made it through. Begin quietly and organically, with disbelief and the body noticing safety: breath returning, hands settling, the voice almost unable to trust the result. Let relief bloom over several lines, then allow warm, breathless elation and a small genuine laugh to emerge rather than switching suddenly. Keep the joy clear and emotionally earned.
SCRIPT:
(quietly stunned, then warming into breathless laughter) "Wait. I'm on the other side. My hands are starting to steady. I can breathe. I did it. I actually did it. I was terrified, and I kept moving. I'm okay. I made it through. Oh my God... I really did it. I can do this."
```

```
Wait. I'm on the other side. My hands are starting to steady. I can breathe. I did it. I actually did it. I was terrified, and I kept moving. I'm okay. I made it through. Oh my God... I really did it. I can do this.
```

### C2_biggest_fear · v5 ⚠ · round 1 (agent score 0.859, supervisor mean 7.00)

*Scene:* You stand before the terrifying thing you have avoided for years, force yourself to face it, and emerge shaken but exhilarated.

**part 0 — part 1 — shaky resolve** · targets: Fear · adapters: `Fear` @ 0.5; `Gasp` @ 0.5

temp 1.05 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Begin barely functional and breath-shaky, with panic constricting the voice; this is not calm fear but a fragile attempt to keep yourself moving. Let determination flicker underneath without overpowering the terror.
SCRIPT:
(Gasp, immediately continuing) "I can do this. I can do this. Just one step—look at it, breathe, move."
```

```
I can do this. I can do this. Just one step—look at it, breathe, move.
```

**part 1 — part 2 — breaking through** · targets: Relief · turn_from: Fear · adapters: `Relief` @ 0.7

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Stop sounding helpless and let the voice gather force as action replaces panic; the fear is still audible, but determination now drives every word. Build urgently toward the realization that you are actually doing it.
SCRIPT:
"My hand is on the door. I'm doing it. I'm actually doing it. Don't run—keep going, keep going, I'm through!"
```

```
My hand is on the door. I'm doing it. I'm actually doing it. Don't run—keep going, keep going, I'm through!
```

**part 2 — part 3 — astonished elation** · targets: Elation · turn_from: Relief · adapters: `Elation` @ 0.75

temp 1.05 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Stop fighting for control and let the aftermath open into stunned, breathless joy; begin with disbelief and exhaustion, then break through into bright, contagious elation at having survived and discovered your own courage.
SCRIPT:
"It's over. I'm still here. I did it! I actually did it! Oh my God—I'm alive, and I was brave. I can do anything."
```

```
It's over. I'm still here. I did it! I actually did it! Oh my God—I'm alive, and I was brave. I can do anything.
```

### C2_biggest_fear · v5 ⚠ · round 2 (agent score 0.885, supervisor mean 7.60)

*Scene:* You face the terrifying thing you have avoided for years, endure the physical panic one step at a time, and slowly discover that you have survived.

**part 0 — part 1 — panic in the body** · targets: Fear · adapters: `Fear` @ 0.5; `Gasp` @ 0.5

temp 1.08 · top_p 0.95 · top_k 30 · max_new_frames 450

```
GENERAL: Start far more visceral than verbal: the breath catches, the throat barely works, and the body is shaking before courage can take over. Do not sound composed; speak in short, fragile fragments while physically talking yourself through the terror. Let determination exist only as a tiny thread beneath the panic.
SCRIPT:
(Gasp, immediately continuing) "My hands are shaking. I can't feel my fingers. Breathe... breathe. Don't look away. I can do this. I can do this."
```

```
My hands are shaking. I can't feel my fingers. Breathe... breathe. Don't look away. I can do this. I can do this.
```

**part 1 — part 2 — forcing the first step** · targets: Distress · turn_from: Fear · adapters: `Distress` @ 0.7

temp 1.03 · top_p 0.95 · top_k 30 · max_new_frames 450

```
GENERAL: Stop being paralyzed, but do not become confident yet; let the voice push forward against a racing heart and trembling muscles. Each phrase is an effort, with fear still tightening the breath. The change is from panic that freezes you to panic that you carry while moving.
SCRIPT:
"My heart is pounding. My knees are going weak. But I'm moving. One step. Just one step. Keep your eyes open. That's it... I'm doing it."
```

```
My heart is pounding. My knees are going weak. But I'm moving. One step. Just one step. Keep your eyes open. That's it... I'm doing it.
```

**part 2 — part 3 — relief beginning** · targets: Relief · turn_from: Distress · adapters: `Relief` @ 0.7

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 450

```
GENERAL: Stop sounding trapped inside the fear and let the body register a small, stunned release: the breath comes back, the muscles begin to loosen, and the voice gains strength without jumping to celebration. Make the relief gradual and physical, as if you are discovering safety one sensation at a time.
SCRIPT:
"I'm through it. My lungs are working again. My hands are still shaking, but... I stayed. I didn't run. I'm actually doing it."
```

```
I'm through it. My lungs are working again. My hands are still shaking, but... I stayed. I didn't run. I'm actually doing it.
```

**part 3 — part 4 — earned elation** · targets: Elation · turn_from: Relief · adapters: `Elation` @ 0.75

temp 1.05 · top_p 0.95 · top_k 30 · max_new_frames 450

```
GENERAL: Stop cautiously checking whether it is safe and let wonder, relief, and pride slowly open into genuine elation. Begin exhausted and disbelieving, then let the smile enter the voice and build toward a bright, victorious final realization. This joy is earned because the fear has just passed through the body.
SCRIPT:
"It's over. I'm still here. My chest is finally opening. I did it... I really did it! I was terrified, and I did it anyway. Oh my God, I can do this."
```

```
It's over. I'm still here. My chest is finally opening. I did it... I really did it! I was terrified, and I did it anyway. Oh my God, I can do this.
```

### C2_biggest_fear · v5 ⚠ · round 3 (agent score 0.707, supervisor mean 6.00)

*Scene:* You confront the terrifying thing head-on, feel panic physically drain from your body, and let survival turn into stunned, triumphant joy.

**part 0 — part 1 — panic takes the body** · targets: Fear · adapters: `Fear` @ 0.55; `Gasp` @ 0.5

temp 1.08 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Begin more visceral and barely functional than before: the breath snags, the throat constricts, and the hands and legs visibly shake through the voice. Stop sounding like someone calmly explaining fear; speak in broken, urgent fragments, with determination only barely keeping you upright.
SCRIPT:
(Gasp, immediately continuing) "My hands are shaking. My chest won't open. I can't—breathe. Breathe. Don't look away. I can do this. I can do this."
```

```
My hands are shaking. My chest won't open. I can't—breathe. Breathe. Don't look away. I can do this. I can do this.
```

**part 1 — part 2 — moving while terrified** · targets: Distress · turn_from: Fear · adapters: `Distress` @ 0.72

temp 1.03 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Stop being frozen, but do not sound brave yet; the change is from panic that paralyzes the body to panic being dragged forward by sheer will. Keep the heart racing and the knees unsteady, while each short phrase pushes into the next step.
SCRIPT:
"My heart is pounding. My knees are going to give out. But I'm moving. One step. Just one step. Keep going. Don't run. I'm doing it."
```

```
My heart is pounding. My knees are going to give out. But I'm moving. One step. Just one step. Keep going. Don't run. I'm doing it.
```

**part 2 — part 3 — fear leaves the body** · targets: Relief · turn_from: Distress · adapters: `Relief` @ 0.75

temp 1.02 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Stop fighting forward and make the realization hit physically: the danger has passed, the breath suddenly returns, the clenched muscles release, and the trembling changes from terror into exhausted aftershock. Let the voice strengthen in stages, with stunned relief arriving before any celebration.
SCRIPT:
"I'm through. Wait—my lungs are opening. My shoulders are dropping. My hands are still shaking, but the fear is leaving me. It's leaving. I stayed."
```

```
I'm through. Wait—my lungs are opening. My shoulders are dropping. My hands are still shaking, but the fear is leaving me. It's leaving. I stayed.
```

**part 3 — part 4 — survival breaks into elation** · targets: Elation · turn_from: Relief · adapters: `Elation` @ 0.75

temp 1.05 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Stop cautiously checking your body and let disbelief open into a powerful, earned release. Begin breathless and almost tearfully astonished, then let pride and laughter enter as you fully understand that you survived. Build gradually to bright elation rather than jumping straight to a shout.
SCRIPT:
"I'm still here. I actually did it. I did it! Oh my God, I did it! I was terrified—and I stayed. I can do anything!"
```

```
I'm still here. I actually did it. I did it! Oh my God, I did it! I was terrified—and I stayed. I can do anything!
```

### C2_biggest_fear · v7 · round 1 (agent score 0.809, supervisor mean 6.00)

*Scene:* At the edge of the terrifying thing they have avoided for years, the character forces themselves forward and discovers they can survive it.

**part 0 — shaky beginning** · targets: Fear · adapters: `Fear` @ 0.55

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400 · tempo_target 2 · chunk_target 2 · prosody_turn False

```
GENERAL: A grounded adult voice with a warm, intimate natural register and clear conversational diction.
SCRIPT:
(voice barely steady, breath held, panic pressing against every word; they are talking themselves into taking the first step) "Okay... okay. Don't look down. Just breathe. I can do this. I can do this. My hands are shaking, but that's okay. One step. Just one step. I'm still here. I'm not running."

```

```
Okay... okay. Don't look down. Just breathe. I can do this. I can do this. My hands are shaking, but that's okay. One step. Just one step. I'm still here. I'm not running.
```

**part 1 — commitment** · targets: Relief · turn_from: Fear · adapters: `Relief` @ 0.72

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400 · tempo_target 3 · chunk_target 3 · prosody_turn True

```
GENERAL: A grounded adult voice with a warm, intimate natural register and clear conversational diction.
SCRIPT:
(the panic stops controlling the breath; the voice gathers force and becomes deliberately steady as they commit to moving forward) "There. I took it. I took the step. I'm doing it. I'm actually doing it. I can feel myself shaking, and I'm still moving. No—don't stop now. Keep going."

```

```
There. I took it. I took the step. I'm doing it. I'm actually doing it. I can feel myself shaking, and I'm still moving. No—don't stop now. Keep going.
```

**part 2 — survival and elation** · targets: Elation · turn_from: Relief · adapters: `Elation` @ 0.75

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400 · tempo_target 4 · chunk_target 3 · prosody_turn True

```
GENERAL: A grounded adult voice with a warm, intimate natural register and clear conversational diction.
SCRIPT:
(the fear finally breaks apart; astonishment turns into bright, disbelieving elation as they realize they have made it through) "I did it. Oh my God, I did it. It's over... and I'm okay. I'm okay! I was so afraid, and I still did it. Look at me. I actually survived this. I can do anything."

```

```
I did it. Oh my God, I did it. It's over... and I'm okay. I'm okay! I was so afraid, and I still did it. Look at me. I actually survived this. I can do anything.
```

*Caption actually sent for the continuation parts* (the harness appends the same-speaker / still-acting / no-onset-burst sentences and, when `turn_from` is set, an explicit turn sentence):

part `commitment` — effective caption:

```
GENERAL: A grounded adult voice with a warm, intimate natural register and clear conversational diction. The same speaker from the preceding audio continues without interruption: identical voice, identical person, same microphone and same room -- no cut, no new narrator, no change of casting. Across this passage the same voice moves out of Fear and into Relief.
SCRIPT:
(the panic stops controlling the breath; the voice gathers force and becomes deliberately steady as they commit to moving forward) "There. I took it. I took the step. I'm doing it. I'm actually doing it. I can feel myself shaking, and I'm still moving. No—don't stop now. Keep going."

```

### C2_biggest_fear · v7 · round 2 (agent score 0.821, supervisor mean 7.00)

*Scene:* At the edge of the thing they fear most, the character takes the first step, steadily commits, and realizes with stunned joy that they have survived it.

**part 0 — controlled panic** · targets: Fear · adapters: `Fear` @ 0.5

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400 · tempo_target 1 · chunk_target 1 · prosody_turn False

```
GENERAL: A grounded adult voice with a warm, intimate natural register and clear conversational diction.
SCRIPT:
(barely functional and frightened, using short broken breath groups; the panic is present but they are forcing themselves not to flee) "Okay... breathe. Don't look down. I can do this. One step. Just one. I'm still here. I'm not running."

```

```
Okay... breathe. Don't look down. I can do this. One step. Just one. I'm still here. I'm not running.
```

**part 1 — steady commitment** · targets: Relief · turn_from: Fear · adapters: `Relief` @ 0.65

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400 · tempo_target 2 · chunk_target 2 · prosody_turn True

```
GENERAL: A grounded adult voice with a warm, intimate natural register and clear conversational diction.
SCRIPT:
(the fear stops dictating the pace; after a small stunned realization, the voice becomes steadier and more purposeful without turning theatrical) "I took the step. I'm doing it. I'm actually doing it. I'm still shaking, but I'm moving. Keep going."

```

```
I took the step. I'm doing it. I'm actually doing it. I'm still shaking, but I'm moving. Keep going.
```

**part 2 — quiet elation** · targets: Elation · turn_from: Relief · adapters: `Elation` @ 0.65

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400 · tempo_target 3 · chunk_target 2 · prosody_turn True

```
GENERAL: A grounded adult voice with a warm, intimate natural register and clear conversational diction.
SCRIPT:
(the effort becomes calm, disbelieving relief rather than a shout; then genuine elation breaks through as they understand they are safe) "I did it. I'm okay. It's over, and I'm okay. I was afraid, and I still did it. I actually made it."

```

```
I did it. I'm okay. It's over, and I'm okay. I was afraid, and I still did it. I actually made it.
```

*Caption actually sent for the continuation parts* (the harness appends the same-speaker / still-acting / no-onset-burst sentences and, when `turn_from` is set, an explicit turn sentence):

part `steady commitment` — effective caption:

```
GENERAL: A grounded adult voice with a warm, intimate natural register and clear conversational diction. The same speaker from the preceding audio continues without interruption: identical voice, identical person, same microphone and same room -- no cut, no new narrator, no change of casting. Across this passage the same voice moves out of Fear and into Relief.
SCRIPT:
(the fear stops dictating the pace; after a small stunned realization, the voice becomes steadier and more purposeful without turning theatrical) "I took the step. I'm doing it. I'm actually doing it. I'm still shaking, but I'm moving. Keep going."

```

### C2_biggest_fear · v7 · round 3 (agent score 0.811, supervisor mean 6.00)

*Scene:* At the edge of the thing they fear most, the character takes one careful step at a time, slowly replaces panic with trust, and finally recognizes their survival with genuine joy.

**part 0 — shaky first step** · targets: Fear · adapters: `Fear` @ 0.5

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 500 · tempo_target 2 · chunk_target 2 · prosody_turn False

```
GENERAL: A grounded adult voice with a warm, intimate natural register and clear conversational diction.
SCRIPT:
(terrified but deliberately slowing the breath; speak in measured, short thought-groups, never rushing, as if each sentence is a handhold) "Okay. Breathe in. Breathe out. Don't look down. I can do this. I don't have to feel brave yet. I only have to take one step. That's it. One step, and then another. I'm still here. I'm not running."

```

```
Okay. Breathe in. Breathe out. Don't look down. I can do this. I don't have to feel brave yet. I only have to take one step. That's it. One step, and then another. I'm still here. I'm not running.
```

**part 1 — growing trust** · targets: Relief · turn_from: Fear · adapters: `Relief` @ 0.7

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 500 · tempo_target 2 · chunk_target 2 · prosody_turn True

```
GENERAL: A grounded adult voice with a warm, intimate natural register and clear conversational diction.
SCRIPT:
(the panic is still audible, but it no longer controls the breath; let a cautious steadiness grow through the sentence, with a quiet realization rather than a sudden triumph) "I took it. I really took the step. Nothing happened. I'm still shaking, but I'm standing. I can take another one. I'm doing it. I'm actually doing it. Slowly. Just keep moving."

```

```
I took it. I really took the step. Nothing happened. I'm still shaking, but I'm standing. I can take another one. I'm doing it. I'm actually doing it. Slowly. Just keep moving.
```

**part 2 — earned elation** · targets: Elation · turn_from: Relief · adapters: `Elation` @ 0.68

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 500 · tempo_target 3 · chunk_target 3 · prosody_turn True

```
GENERAL: A grounded adult voice with a warm, intimate natural register and clear conversational diction.
SCRIPT:
(the remaining fear gradually loosens into calm disbelief, then opens into warm, breathless elation; keep the same intimate voice and let the joy arrive because the realization finally lands) "Wait. I'm at the other side. I did it. I'm okay. I'm really okay. All that fear came with me, and it still couldn't stop me. I made it through. I actually made it through. I thought I couldn't do this, but I did. I can do this."

```

```
Wait. I'm at the other side. I did it. I'm okay. I'm really okay. All that fear came with me, and it still couldn't stop me. I made it through. I actually made it through. I thought I couldn't do this, but I did. I can do this.
```

*Caption actually sent for the continuation parts* (the harness appends the same-speaker / still-acting / no-onset-burst sentences and, when `turn_from` is set, an explicit turn sentence):

part `growing trust` — effective caption:

```
GENERAL: A grounded adult voice with a warm, intimate natural register and clear conversational diction. The same speaker from the preceding audio continues without interruption: identical voice, identical person, same microphone and same room -- no cut, no new narrator, no change of casting. Across this passage the same voice moves out of Fear and into Relief.
SCRIPT:
(the panic is still audible, but it no longer controls the breath; let a cautious steadiness grow through the sentence, with a quiet realization rather than a sudden triumph) "I took it. I really took the step. Nothing happened. I'm still shaking, but I'm standing. I can take another one. I'm doing it. I'm actually doing it. Slowly. Just keep moving."

```

---

## C3_foreman

> Foreman Accident Response. You are the construction foreman whose worker just fell from scaffolding. You bark emergency instructions with practiced authority - 'Get the ambulance. Clear the area. Don't move him.' Then the professional shell cracks and the fear you are suppressing comes through, and you have to force it back down to keep giving orders.

### C3_foreman · v1 · round 1 (agent score 0.648, supervisor mean 7.60)

*Scene:* At a construction site, a foreman takes command after a worker falls from scaffolding, briefly exposing his terror before forcing himself back into control.

**part 0 — command** · targets: Anger · adapters: `Anger` @ 0.45

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: A seasoned construction foreman with a deep, projected voice; clipped, practiced authority, fast but perfectly intelligible, commanding a chaotic crew.
SCRIPT:
(Bark each order decisively, with no hesitation) "Get the ambulance! Clear the area! You, shut down that lift! Nobody crowds him! Don't move him—do you hear me? Don't move him!"
```

```
Get the ambulance! Clear the area! You, shut down that lift! Nobody crowds him! Don't move him—do you hear me? Don't move him!
```

**part 1 — the_crack** · targets: Fear, Distress · adapters: `Gasp` @ 0.9; `Fear` @ 0.45; `Distress` @ 0.35

temp 1.05 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: The same foreman, still trying to sound authoritative, but the professional shell fractures as he sees the injured worker; let fear seize the breath and make the next words raw and personal, while keeping every word intelligible.
SCRIPT:
(Drive the first order, then falter as fear breaks through) "Keep pressure on that leg. Easy—easy—I'm right here." (Gasp) "Oh God, he's not breathing right. Hey, stay with me, kid. Stay with me!"
```

```
Keep pressure on that leg. Easy—easy—I'm right here. Oh God, he's not breathing right. Hey, stay with me, kid. Stay with me!
```

**part 2 — back_in_control** · targets: Anger, Fear · adapters: `Anger` @ 0.55; `Fear` @ 0.3

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: The foreman crushes his panic back down and rebuilds command; voice roughened by fear but increasingly steady, forceful, and focused, ending with controlled authority rather than emotional numbness.
SCRIPT:
(Force one breath down, then turn the fear into precise orders) "No. No, listen to me. We are not losing him here. Call his family only when I say. You—keep his airway clear. You—guide the paramedics in. Move!"
```

```
No. No, listen to me. We are not losing him here. Call his family only when I say. You—keep his airway clear. You—guide the paramedics in. Move!
```

### C3_foreman · v1 · round 2 (agent score 0.865, supervisor mean 7.40)

*Scene:* After a worker falls from scaffolding, the foreman takes command, visibly falters in fear beside the injured man, then forces himself back into disciplined action.

**part 0 — command_under_pressure** · targets: Anger · adapters: `Anger` @ 0.45

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: A seasoned construction foreman with a deep, projected voice; clipped, practiced authority cutting through a chaotic worksite, fast but exceptionally clear.
SCRIPT:
(Bark the orders with immediate, practiced control) "Get the ambulance! Clear the area! Shut down that lift! You, keep everyone back! Don't move him. Nobody moves him until the medics arrive!"
```

```
Get the ambulance! Clear the area! Shut down that lift! You, keep everyone back! Don't move him. Nobody moves him until the medics arrive!
```

**part 1 — fear_breaks_through** · targets: Fear, Distress · adapters: `Gasp` @ 0.9; `Fear` @ 0.45; `Distress` @ 0.35

temp 1.05 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: The same foreman is suddenly close to the injured worker; his authority gives way to contained terror. Use a slight vocal tremor, uneven breath, a wavering volume, and a brief loss of verbal focus before he fights to stay present. Keep every word intelligible and do not rush the fear.
SCRIPT:
(Start with a firm instruction, then let the voice tremble and lose certainty) "Keep pressure on his leg. Easy... easy... I'm right here." (Gasp) "He's cold. Why is he so cold? Hey, look at me, kid. Come on, look at me. Stay with me. Please, stay with me."
```

```
Keep pressure on his leg. Easy... easy... I'm right here. He's cold. Why is he so cold? Hey, look at me, kid. Come on, look at me. Stay with me. Please, stay with me.
```

**part 2 — composure_reclaimed** · targets: Anger, Fear · adapters: `Anger` @ 0.5; `Fear` @ 0.3

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: The foreman swallows the panic and deliberately rebuilds his command voice. Begin strained and breath-held, then become precise, grounded, and forceful; the fear remains underneath but no longer controls the delivery.
SCRIPT:
(Drag the fear back down, then issue each order with renewed authority) "No. Breathe. I can do this. You, keep his airway clear. You, bring the trauma kit. Guide the paramedics in and make a path. Move!"
```

```
No. Breathe. I can do this. You, keep his airway clear. You, bring the trauma kit. Guide the paramedics in and make a path. Move!
```

### C3_foreman · v1 · round 3 (agent score 0.885, supervisor mean 7.00)

*Scene:* After a worker falls from scaffolding, the foreman commands the rescue, remains beside the injured man as fear visibly overwhelms him, then forces himself back into professional control.

**part 0 — command_under_pressure** · targets: Anger · adapters: `Anger` @ 0.45

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: A seasoned construction foreman with a deep, projected voice; clipped, practiced authority cutting through a chaotic worksite, fast but exceptionally clear.
SCRIPT:
(Bark the orders with immediate, practiced control) "Get the ambulance! Clear the area! Shut down that lift! You, keep everyone back! Don't move him. Nobody moves him until the medics arrive!"
```

```
Get the ambulance! Clear the area! Shut down that lift! You, keep everyone back! Don't move him. Nobody moves him until the medics arrive!
```

**part 1 — fear_lingers** · targets: Fear, Distress · adapters: `Gasp` @ 0.9; `Fear` @ 0.45; `Distress` @ 0.35

temp 1.05 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: The same foreman is kneeling beside the injured worker; his command voice collapses into contained terror. Let the voice tremble, breath catch, and focus falter as he stares at the worker, lingering in helpless fear without rushing. Keep every word intelligible, then let a small gasp intensify the panic; continue speaking immediately after it.
SCRIPT:
(Begin with a strained instruction, then let fear spread through the voice and slow the thoughts) "Keep pressure on his leg. Easy... easy... I'm right here." (Gasp) "He's cold. He's so cold. Why is he so cold? Look at me, kid. Come on, look at me. I can't lose you. Do you hear me? Stay with me. Please... stay with me. I don't know what to do. I don't know what to do."
```

```
Keep pressure on his leg. Easy... easy... I'm right here. He's cold. He's so cold. Why is he so cold? Look at me, kid. Come on, look at me. I can't lose you. Do you hear me? Stay with me. Please... stay with me. I don't know what to do. I don't know what to do.
```

**part 2 — composure_reclaimed** · targets: Anger, Fear · adapters: `Anger` @ 0.5; `Fear` @ 0.3

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: The foreman swallows the panic and deliberately rebuilds his command voice. Begin breath-held and shaken, then become precise, grounded, and forceful; the fear remains underneath but the professional shell locks back into place.
SCRIPT:
(Force the panic down, take command of the scene, and end with renewed authority) "No. Breathe. I can do this. You, keep his airway clear. You, bring the trauma kit. Guide the paramedics in and make a path. Move!"
```

```
No. Breathe. I can do this. You, keep his airway clear. You, bring the trauma kit. Guide the paramedics in and make a path. Move!
```

### C3_foreman · v2 · round 1 (agent score 0.706, supervisor mean 7.40)

*Scene:* At a construction site, a worker has just fallen from scaffolding, and the foreman must command the emergency response while suppressing rising panic.

**part 0 — part 1 — practiced command** · targets: Anger · adapters: `Anger` @ 0.45

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: A seasoned construction foreman with a commanding, clipped voice; loud enough to cut through chaos, controlled and authoritative, with no wasted movement.
SCRIPT:
(Sharp, barking orders) "Get the ambulance! Clear the area! Nobody crowd him. Don't move him—do you hear me? Don't move him!"
```

```
Get the ambulance! Clear the area! Nobody crowd him. Don't move him—do you hear me? Don't move him!
```

**part 1 — part 2 — the shell cracks** · targets: Fear, Distress · adapters: `Gasp` @ 0.5; `Fear` @ 0.35

temp 1.05 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: The same foreman; the authority falters as suppressed fear breaks through. Speak urgently and breathlessly, with a genuine tremor, but keep the words intelligible.
SCRIPT:
(Leaning close, trying not to panic) "I—" (Gasp) "No, no, stay with me. Hey, look at me. Keep breathing. Somebody get his helmet off—carefully! Oh God, please, please be breathing."
```

```
I— No, no, stay with me. Hey, look at me. Keep breathing. Somebody get his helmet off—carefully! Oh God, please, please be breathing.
```

**part 2 — part 3 — forcing control back** · targets: Anger, Distress · adapters: `Anger` @ 0.5; `Distress` @ 0.3

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: The same foreman forcibly reassembles himself; fear remains underneath, but his voice hardens into efficient command. Start shaken, then finish with steady, unmistakable authority.
SCRIPT:
(Gripping himself and raising his voice) "All right. All right, I need everyone focused. You, guide the paramedics in. You, shut down the lift. Nobody touches him until they arrive. Move! Keep this site clear!"
```

```
All right. All right, I need everyone focused. You, guide the paramedics in. You, shut down the lift. Nobody touches him until they arrive. Move! Keep this site clear!
```

### C3_foreman · v2 · round 2 (agent score 0.738, supervisor mean 7.00)

*Scene:* At a construction site moments after a worker falls from scaffolding, the foreman keeps the crew moving while his controlled authority gives way to fear, then hardens again.

**part 0 — part 1 — immediate control** · targets: Anger · adapters: `Anger` @ 0.45

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: A seasoned construction foreman cutting through a chaotic worksite; begin with practiced, clipped authority, forceful but controlled, then sharpen the final order.
SCRIPT:
(Calling over the chaos, brisk and commanding) "Get the ambulance here now! Clear the whole area! You, kill the lift. Nobody moves him. Back up and give him air—move!"
```

```
Get the ambulance here now! Clear the whole area! You, kill the lift. Nobody moves him. Back up and give him air—move!
```

**part 1 — part 2 — the first crack** · targets: Fear · adapters: `Gasp` @ 0.5; `Fear` @ 0.45

temp 1.05 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: The same foreman drops close to the injured worker; his professional shell fractures into startled fear. Keep every word intelligible, with a genuine tremor and urgent breath, not theatrical shouting.
SCRIPT:
(Kneeling beside him, suddenly frightened) "Hey—hey, stay with me." (Gasp) "Look at me. Can you hear me? Don't try to get up. Just breathe. That's it. Just breathe."
```

```
Hey—hey, stay with me. Look at me. Can you hear me? Don't try to get up. Just breathe. That's it. Just breathe.
```

**part 2 — part 3 — fear held in the open** · targets: Fear, Distress · adapters: `Fear` @ 0.45; `Distress` @ 0.4

temp 1.05 · top_p 0.95 · top_k 30 · max_new_frames 450

```
GENERAL: The same foreman remains beside the injured worker, unable to hide how terrified he is. Let the vulnerability last; voice unsteady, pleading, and intimate, with pauses created only by punctuation and never by a silence cue.
SCRIPT:
(Watching for any sign of breathing, voice breaking) "Come on, kid, stay with me. Please. I can see you breathing—keep doing that. Don't close your eyes, you hear me? The ambulance is coming. You're not alone. I've got you. I've got you."
```

```
Come on, kid, stay with me. Please. I can see you breathing—keep doing that. Don't close your eyes, you hear me? The ambulance is coming. You're not alone. I've got you. I've got you.
```

**part 3 — part 4 — command rebuilt** · targets: Anger, Distress · adapters: `Anger` @ 0.5; `Distress` @ 0.3

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: The same foreman forces the fear back down. Start breathless and shaken, then rebuild into escalating operational authority: firm instruction, louder correction, and finally a hard command that restores order.
SCRIPT:
(Standing, swallowing the panic and turning on the crew) "All right. Everyone focus. You, bring the med kit. You, open that gate. Keep the path clear! Nobody touches him until the paramedics are here—move, now!"
```

```
All right. Everyone focus. You, bring the med kit. You, open that gate. Keep the path clear! Nobody touches him until the paramedics are here—move, now!
```

### C3_foreman · v2 · round 3 (agent score 0.763, supervisor mean 7.00)

*Scene:* At a construction site after a worker falls from scaffolding, the foreman’s practiced emergency command gives way to raw fear before he slowly rebuilds his authority.

**part 0 — part 1 — practiced emergency control** · targets: Anger · adapters: `Anger` @ 0.45

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: A seasoned construction foreman cutting through a chaotic worksite with clipped, practiced authority. Start forceful and controlled, then intensify only on the final order; keep every word crisp.
SCRIPT:
(Calling across the site, sharp and commanding) "Get the ambulance here now! Clear the area! You, shut down the lift. Nobody moves him. Back up and give him air!"
```

```
Get the ambulance here now! Clear the area! You, shut down the lift. Nobody moves him. Back up and give him air!
```

**part 1 — part 2 — fear breaks through** · targets: Fear · adapters: `Gasp` @ 0.5; `Fear` @ 0.45

temp 1.05 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: The same foreman drops beside the injured worker, and the professional shell suddenly fractures. Use a breathless, trembling, intimate voice; sound genuinely afraid rather than theatrically emotional. Keep the words intelligible and let the fear deepen across the passage.
SCRIPT:
(Kneeling beside him, voice catching) "Hey—hey, stay with me." (Gasp) "Look at me. Can you hear me? Don't try to move. Just breathe. Please, just breathe. Come on, kid. Stay with me."
```

```
Hey—hey, stay with me. Look at me. Can you hear me? Don't try to move. Just breathe. Please, just breathe. Come on, kid. Stay with me.
```

**part 2 — part 3 — the internal struggle** · targets: Fear, Distress · adapters: `Fear` @ 0.4; `Distress` @ 0.35

temp 1.03 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: The same foreman remains beside the worker, openly terrified but fighting to regain control. Begin vulnerable and pleading, then slowly replace panic with deliberate, measured focus; the change must feel difficult and earned, not sudden.
SCRIPT:
(Watching his breathing, voice breaking, then forcing each word steady) "Stay with me. You're not alone. I know you're scared—I am too. But listen to me. Keep breathing. That's it. The ambulance is coming. I've got you. I've got you."
```

```
Stay with me. You're not alone. I know you're scared—I am too. But listen to me. Keep breathing. That's it. The ambulance is coming. I've got you. I've got you.
```

**part 3 — part 4 — authority painstakingly restored** · targets: Anger · adapters: `Anger` @ 0.4

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: The same foreman stands and deliberately rebuilds his command presence. Start quiet, shaky, and inwardly struggling; gain firmness one instruction at a time, ending in clear operational authority without becoming a constant shout.
SCRIPT:
(Swallowing panic, first quietly, then steadily louder) "All right. I need everyone focused. You, bring the med kit. You, open the gate. Good. Keep the path clear. Nobody touches him until the paramedics arrive. Move now—let's get them in here!"
```

```
All right. I need everyone focused. You, bring the med kit. You, open the gate. Good. Keep the path clear. Nobody touches him until the paramedics arrive. Move now—let's get them in here!
```

### C3_foreman · v5 ⚠ · round 1 (agent score 0.736, supervisor mean 7.80)

*Scene:* A construction foreman takes command after a worker falls from scaffolding, then briefly reveals his fear before forcing himself back into control.

**part 0 — practiced command** · targets: Anger · adapters: `Anger` @ 0.45

temp 0.95 · top_p 0.92 · top_k 30 · max_new_frames 400

```
GENERAL: A seasoned construction foreman, loud, clipped, and absolutely authoritative; begin in controlled emergency command, not panic, with the confidence of someone used to being obeyed.
SCRIPT:
(Barking over the chaos, each order clean and immediate) "You—call an ambulance, now! Clear this whole area. Get everyone back. Nobody touches him. Mike, shut down the lift. Sarah, bring the first-aid kit and keep his airway clear. Move!"
```

```
You—call an ambulance, now! Clear this whole area. Get everyone back. Nobody touches him. Mike, shut down the lift. Sarah, bring the first-aid kit and keep his airway clear. Move!
```

**part 1 — the shell cracks** · targets: Fear, Distress · turn_from: Anger · adapters: `Fear` @ 0.5; `Gasp` @ 0.5

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Continue as the same foreman; stop sounding invulnerable as the reality hits, letting suppressed terror break through the practiced authority, then struggle to keep speaking through it.
SCRIPT:
(The command falters; a raw Gasp breaks through, then the words come out frightened and urgent) "I saw him go over the rail—(Gasp) "No—no, don't let him move. Is he breathing? Tell me he's breathing. God... I should have been watching that platform."
```

```
I saw him go over the rail—No—no, don't let him move. Is he breathing? Tell me he's breathing. God... I should have been watching that platform.
```

**part 2 — back into command** · targets: Anger · turn_from: Fear · adapters: `Anger` @ 0.65

temp 0.95 · top_p 0.92 · top_k 30 · max_new_frames 400

```
GENERAL: Continue from exposed fear; the foreman cuts off the self-blame and crushes the panic back down, becoming hard, focused, and commanding again, with fear still audible underneath but no longer in control.
SCRIPT:
(He forces one breath, swallows the panic, and returns to iron authority) "Enough. Not now. We do the job in front of us. Keep his neck still. You, guide the paramedics in. Clear that gate! Nobody crowds him, nobody guesses, nobody touches a thing until they say so. Stay with me—hold the line!"
```

```
Enough. Not now. We do the job in front of us. Keep his neck still. You, guide the paramedics in. Clear that gate! Nobody crowds him, nobody guesses, nobody touches a thing until they say so. Stay with me—hold the line!
```

### C3_foreman · v5 ⚠ · round 2 (agent score 0.810, supervisor mean 7.00)

*Scene:* A construction foreman takes command after a worker falls from scaffolding, briefly loses control to fear and guilt, then deliberately forces himself back into clear authority.

**part 0 — practiced command** · targets: Anger · adapters: `Anger` @ 0.45

temp 0.95 · top_p 0.92 · top_k 30 · max_new_frames 430

```
GENERAL: A seasoned construction foreman speaking over a chaotic worksite; begin with hard, clipped authority and a fast operational rhythm, then deliberately slow for the most critical safety order. He is controlled, practiced, and used to being obeyed, not emotionally panicked.
SCRIPT:
(Barking rapidly, then dropping into a slow, unmistakable warning) "You—call an ambulance, now! Clear this whole area. Get everyone back. Mike, shut down the lift! Sarah, bring the first-aid kit and keep his airway clear. And listen to me—nobody touches him. Nobody moves him. Move!"
```

```
You—call an ambulance, now! Clear this whole area. Get everyone back. Mike, shut down the lift! Sarah, bring the first-aid kit and keep his airway clear. And listen to me—nobody touches him. Nobody moves him. Move!
```

**part 1 — the shell cracks and lingers** · targets: Fear, Distress · turn_from: Anger · adapters: `Fear` @ 0.5; `Distress` @ 0.45; `Gasp` @ 0.5

temp 1.02 · top_p 0.95 · top_k 30 · max_new_frames 480

```
GENERAL: Continue as the same foreman; the brisk command rhythm collapses into stunned, breathless fear. Let the professional shell crack slowly and remain broken for several lines: voice tightening, words catching, guilt surfacing, with a raw Gasp inline but no silence immediately after it. Do not rush back to authority yet; make the fear sink in before he tries to recover.
SCRIPT:
(The orders die in his throat; a raw Gasp breaks through, and he speaks in frightened fragments that gradually become a confession) "I saw him go over the rail—(Gasp) no, no, no... don't move him. Is he breathing? Look at me. Is he breathing? Tell me he's breathing. I should have checked that platform. I should have been watching him. He's one of mine. I can't— I can't lose him here."
```

```
I saw him go over the rail—no, no, no... don't move him. Is he breathing? Look at me. Is he breathing? Tell me he's breathing. I should have checked that platform. I should have been watching him. He's one of mine. I can't— I can't lose him here.
```

**part 2 — forced control** · targets: Anger · turn_from: Fear · adapters: `Anger` @ 0.68

temp 0.95 · top_p 0.92 · top_k 30 · max_new_frames 430

```
GENERAL: Continue from sustained fear and guilt; the foreman deliberately crushes the panic down, takes command of his breathing, and rebuilds authority in stages. Start low and restrained, then accelerate into crisp orders, ending with iron focus rather than emotional comfort. Fear remains underneath, but he refuses to let it steer him.
SCRIPT:
(He swallows hard, forces his voice steady, then gathers speed and authority) "Enough. Not now. Breathe. We do the job in front of us. Keep his neck still. You, guide the paramedics in. Clear that gate—now! Nobody crowds him, nobody guesses, nobody touches a thing until they say so. Stay with me. Hold the line!"
```

```
Enough. Not now. Breathe. We do the job in front of us. Keep his neck still. You, guide the paramedics in. Clear that gate—now! Nobody crowds him, nobody guesses, nobody touches a thing until they say so. Stay with me. Hold the line!
```

### C3_foreman · v5 ⚠ · round 3 (agent score 0.750, supervisor mean 7.00)

*Scene:* A construction foreman commands the aftermath of a scaffolding fall, lets suppressed fear fully surface, then makes a deliberate, painful effort to regain control and direct the rescue.

**part 0 — practiced authority** · targets: Anger · adapters: `Anger` @ 0.45

temp 0.95 · top_p 0.92 · top_k 30 · max_new_frames 400

```
GENERAL: A seasoned construction foreman overpowers the worksite chaos with fast, clipped, practiced authority; vary the pace by slowing sharply on the safety warning, showing complete command rather than panic.
SCRIPT:
(Barking rapid orders, then slowing into a deadly-clear warning) "You, call an ambulance now! Clear the area! Everyone back! Mike, shut down the lift. Sarah, get the first-aid kit and keep his airway clear. Listen to me—nobody touches him. Nobody moves him. Move!"
```

```
You, call an ambulance now! Clear the area! Everyone back! Mike, shut down the lift. Sarah, get the first-aid kit and keep his airway clear. Listen to me—nobody touches him. Nobody moves him. Move!
```

**part 1 — fear fully surfaces** · targets: Fear, Distress · turn_from: Anger · adapters: `Fear` @ 0.65; `Distress` @ 0.45; `Gasp` @ 0.5

temp 1.02 · top_p 0.95 · top_k 30 · max_new_frames 460

```
GENERAL: Continue as the same foreman; stop being commanding and let the professional shell crack wide open. Linger in stunned fear and guilt, allowing the terror to resonate through repeated questions and broken self-blame. Do not rush toward recovery; he is exposed, frightened, and barely holding together.
SCRIPT:
(The authority drains away; a raw Gasp breaks through, and he remains trapped in the sight of the fall) "I saw him go over the rail—(Gasp) no... no, no. Don't move him. Is he breathing? Look at me. Is he breathing? Tell me he's breathing. I should have checked that platform. I should have been watching him. He's one of mine. Please... don't let him die here. I can't lose him. I can't."
```

```
I saw him go over the rail—no... no, no. Don't move him. Is he breathing? Look at me. Is he breathing? Tell me he's breathing. I should have checked that platform. I should have been watching him. He's one of mine. Please... don't let him die here. I can't lose him. I can't.
```

**part 2 — conscious recovery** · targets: Anger · turn_from: Fear · adapters: `Anger` @ 0.65

temp 0.95 · top_p 0.92 · top_k 30 · max_new_frames 400

```
GENERAL: Continue from sustained fear; make the return to authority a conscious, difficult act rather than an instant mood change. Begin with a shaky attempt to breathe and speak, visibly forcing the panic down, then rebuild into varied pacing: restrained at first, accelerating into precise, hard orders. End focused and authoritative, with fear still buried underneath.
SCRIPT:
(He fights for breath, forces the panic down, and deliberately takes command again) "Breathe. Come on... breathe. No. Not now. I can fall apart later. You—guide the paramedics in. Keep his neck still. Clear that gate! Nobody crowds him. Nobody guesses. Nobody touches a thing until they say so. Stay with me. Hold the line!"
```

```
Breathe. Come on... breathe. No. Not now. I can fall apart later. You—guide the paramedics in. Keep his neck still. Clear that gate! Nobody crowds him. Nobody guesses. Nobody touches a thing until they say so. Stay with me. Hold the line!
```

### C3_foreman · v7 · round 1 (agent score 0.678, supervisor mean 5.60)

*Scene:* A construction foreman responds to a worker’s fall from scaffolding, issuing crisp emergency orders before fear breaks through and is forcibly mastered.

**part 0 — command under pressure** · targets: Anger · adapters: `Anger` @ 0.45

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400 · tempo_target 4 · chunk_target 2 · prosody_turn False

```
GENERAL: A seasoned construction foreman with a rugged, grounded baritone, speaking clearly and forcefully through controlled physical tension.
SCRIPT:
(Explosive authority, practiced and immediate; short commands, no panic, taking control of the crew.) "You—call the ambulance. Now. Clear the whole area. Back everyone up. Nobody touches the scaffold. Don't move him. Get me the first-aid kit and keep that access lane open. Move!"
The same speaker continues, no cut, no new narrator.
```

```
You—call the ambulance. Now. Clear the whole area. Back everyone up. Nobody touches the scaffold. Don't move him. Get me the first-aid kit and keep that access lane open. Move!
```

**part 1 — the shell cracks** · targets: Fear, Distress · turn_from: Anger · adapters: `Fear` @ 0.5; `Gasp` @ 0.5

temp 1.05 · top_p 0.95 · top_k 30 · max_new_frames 400 · tempo_target 2 · chunk_target 1 · prosody_turn True

```
GENERAL: A seasoned construction foreman with a rugged, grounded baritone, speaking clearly and forcefully through controlled physical tension.
SCRIPT:
(The authority falters for the first time; breath catches, fear leaks into the words, then he tries to hide it by clinging to procedure.) "I said don't move him—(Gasp) don't move him. Jesus... his leg—someone tell me he's breathing. Hey, look at me, kid. Stay with me. Stay with me, do you hear me?"
The same speaker continues, no cut, no new narrator.
```

```
I said don't move him— don't move him. Jesus... his leg—someone tell me he's breathing. Hey, look at me, kid. Stay with me. Stay with me, do you hear me?
```

**part 2 — fear forced back down** · targets: Anger · turn_from: Fear · adapters: `Anger` @ 0.7

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400 · tempo_target 4 · chunk_target 2 · prosody_turn True

```
GENERAL: A seasoned construction foreman with a rugged, grounded baritone, speaking clearly and forcefully through controlled physical tension.
SCRIPT:
(He crushes the panic back into himself; the voice steadies into hard, deliberate command, stronger because we heard it nearly break.) "I'm here. Keep your eyes open. Paramedics are coming. You, shut down the lift. You, get the site supervisor. Nobody crowds him, nobody guesses, nobody moves him. We do this right. Now breathe—and work."
The same speaker continues, no cut, no new narrator.
```

```
I'm here. Keep your eyes open. Paramedics are coming. You, shut down the lift. You, get the site supervisor. Nobody crowds him, nobody guesses, nobody moves him. We do this right. Now breathe—and work.
```

*Caption actually sent for the continuation parts* (the harness appends the same-speaker / still-acting / no-onset-burst sentences and, when `turn_from` is set, an explicit turn sentence):

part `the shell cracks` — effective caption:

```
GENERAL: A seasoned construction foreman with a rugged, grounded baritone, speaking clearly and forcefully through controlled physical tension. The same speaker from the preceding audio continues without interruption: identical voice, identical person, same microphone and same room -- no cut, no new narrator, no change of casting. Across this passage the same voice moves out of Anger and into Fear, Distress.
SCRIPT:
(The authority falters for the first time; breath catches, fear leaks into the words, then he tries to hide it by clinging to procedure.) "I said don't move him—(Gasp) don't move him. Jesus... his leg—someone tell me he's breathing. Hey, look at me, kid. Stay with me. Stay with me, do you hear me?"
The same speaker continues, no cut, no new narrator.
```

### C3_foreman · v7 · round 2 (agent score 0.593, supervisor mean 6.00)

*Scene:* A construction foreman takes control after a worker falls from scaffolding, then his suppressed fear breaks through before he forces himself back into command.

**part 0 — command under pressure** · targets: Anger · adapters: `Anger` @ 0.4

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 440 · tempo_target 3 · chunk_target 3 · prosody_turn False

```
GENERAL: A seasoned construction foreman with a rugged, grounded baritone, speaking clearly and forcefully through controlled physical tension.
SCRIPT:
(He is not shouting blindly; he is imposing practiced order, with crisp but natural breath groups and no wasted motion.) "You, call the ambulance. Now. Clear the whole area and back everyone up. Nobody touches the scaffold. Don't move him. Get the first-aid kit and keep that access lane open. Move, move!"
The same speaker continues, no cut, no new narrator.
```

```
You, call the ambulance. Now. Clear the whole area and back everyone up. Nobody touches the scaffold. Don't move him. Get the first-aid kit and keep that access lane open. Move, move!
```

**part 1 — the professional shell cracks** · targets: Fear, Distress · turn_from: Anger · adapters: `Fear` @ 0.5; `Distress` @ 0.5; `Gasp` @ 0.5

temp 1.05 · top_p 0.95 · top_k 30 · max_new_frames 440 · tempo_target 3 · chunk_target 2 · prosody_turn True

```
GENERAL: A seasoned construction foreman with a rugged, grounded baritone, speaking clearly and forcefully through controlled physical tension.
SCRIPT:
(The controlled authority stops working; he stalls and breathes in short, frightened groups, letting genuine fear and distress surface before he tries to reach the injured worker.) "I said don't move him. Don't move him. Jesus... (Gasp) somebody tell me he's breathing. Hey, look at me, kid. Stay with me. Stay with me, do you hear me?"
The same speaker continues, no cut, no new narrator.
```

```
I said don't move him. Don't move him. Jesus... somebody tell me he's breathing. Hey, look at me, kid. Stay with me. Stay with me, do you hear me?
```

**part 2 — fear forced back down** · targets: Anger · turn_from: Fear · adapters: `Anger` @ 0.65

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 440 · tempo_target 4 · chunk_target 2 · prosody_turn True

```
GENERAL: A seasoned construction foreman with a rugged, grounded baritone, speaking clearly and forcefully through controlled physical tension.
SCRIPT:
(He stops pleading and deliberately crushes the fear back down; his breath locks into steadier, brisker commands, not calm but controlled again.) "I'm here. Keep your eyes open. Paramedics are coming. You, shut down the lift. You, get the site supervisor. Nobody crowds him, nobody guesses, nobody moves him. We do this right. Now breathe—and work."
The same speaker continues, no cut, no new narrator.
```

```
I'm here. Keep your eyes open. Paramedics are coming. You, shut down the lift. You, get the site supervisor. Nobody crowds him, nobody guesses, nobody moves him. We do this right. Now breathe—and work.
```

*Caption actually sent for the continuation parts* (the harness appends the same-speaker / still-acting / no-onset-burst sentences and, when `turn_from` is set, an explicit turn sentence):

part `the professional shell cracks` — effective caption:

```
GENERAL: A seasoned construction foreman with a rugged, grounded baritone, speaking clearly and forcefully through controlled physical tension. The same speaker from the preceding audio continues without interruption: identical voice, identical person, same microphone and same room -- no cut, no new narrator, no change of casting. Across this passage the same voice moves out of Anger and into Fear, Distress.
SCRIPT:
(The controlled authority stops working; he stalls and breathes in short, frightened groups, letting genuine fear and distress surface before he tries to reach the injured worker.) "I said don't move him. Don't move him. Jesus... (Gasp) somebody tell me he's breathing. Hey, look at me, kid. Stay with me. Stay with me, do you hear me?"
The same speaker continues, no cut, no new narrator.
```

### C3_foreman · v7 · round 3 (agent score 0.498, supervisor mean 5.40)

*Scene:* A construction foreman takes control after a worker falls from scaffolding, allowing fear to surface gradually before forcing it back down and resuming command.

**part 0 — authority with strain** · targets: Anger · adapters: `Anger` @ 0.45

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 440 · tempo_target 3 · chunk_target 2 · prosody_turn False

```
GENERAL: A seasoned construction foreman with a rugged, grounded baritone, speaking clearly and forcefully through controlled physical tension.
SCRIPT:
(Practiced authority holds the site together, but a faint strain underneath hints that he has seen the injured worker; use short, controlled groups without rushing.) "You, call the ambulance. Now. Clear the area and back everyone up. Nobody touches the scaffold. Don't move him. Get the first-aid kit. Keep that lane open. Move."
The same speaker continues, no cut, no new narrator.
```

```
You, call the ambulance. Now. Clear the area and back everyone up. Nobody touches the scaffold. Don't move him. Get the first-aid kit. Keep that lane open. Move.
```

**part 1 — fear seeps through** · targets: Fear, Distress · turn_from: Anger · adapters: `Fear` @ 0.55; `Distress` @ 0.5; `Gasp` @ 0.5

temp 1.05 · top_p 0.95 · top_k 30 · max_new_frames 440 · tempo_target 3 · chunk_target 3 · prosody_turn True

```
GENERAL: A seasoned construction foreman with a rugged, grounded baritone, speaking clearly and forcefully through controlled physical tension.
SCRIPT:
(The authority does not shatter; it frays gradually. He repeats the order, loses his breath, and fear leaks through in restrained, uneven groups as he addresses the worker.) "I said don't move him. Don't move him. Jesus... (Gasp) tell me he's breathing. Hey, look at me, kid. Stay with me. Just stay with me, all right?"
The same speaker continues, no cut, no new narrator.
```

```
I said don't move him. Don't move him. Jesus... tell me he's breathing. Hey, look at me, kid. Stay with me. Just stay with me, all right?
```

**part 2 — control reclaimed** · targets: Relief, Anger · turn_from: Fear · adapters: `Relief` @ 0.6; `Anger` @ 0.45

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 440 · tempo_target 3 · chunk_target 2 · prosody_turn True

```
GENERAL: A seasoned construction foreman with a rugged, grounded baritone, speaking clearly and forcefully through controlled physical tension.
SCRIPT:
(He hears his own fear, clamps down on it, and deliberately rebuilds the professional voice; the pace returns to steady command, with resolve rather than panic.) "I'm here. Keep your eyes open. Paramedics are coming. You, shut down the lift. You, get the supervisor. Give him room. Nobody moves him. We do this right. Breathe, and work."
The same speaker continues, no cut, no new narrator.
```

```
I'm here. Keep your eyes open. Paramedics are coming. You, shut down the lift. You, get the supervisor. Give him room. Nobody moves him. We do this right. Breathe, and work.
```

*Caption actually sent for the continuation parts* (the harness appends the same-speaker / still-acting / no-onset-burst sentences and, when `turn_from` is set, an explicit turn sentence):

part `fear seeps through` — effective caption:

```
GENERAL: A seasoned construction foreman with a rugged, grounded baritone, speaking clearly and forcefully through controlled physical tension. The same speaker from the preceding audio continues without interruption: identical voice, identical person, same microphone and same room -- no cut, no new narrator, no change of casting. Across this passage the same voice moves out of Anger and into Fear, Distress.
SCRIPT:
(The authority does not shatter; it frays gradually. He repeats the order, loses his breath, and fear leaks through in restrained, uneven groups as he addresses the worker.) "I said don't move him. Don't move him. Jesus... (Gasp) tell me he's breathing. Hey, look at me, kid. Stay with me. Just stay with me, all right?"
The same speaker continues, no cut, no new narrator.
```

---

## C4_last_priest

> Last Priest, Faith Dying. You are delivering a final sermon to a nearly empty church. Your voice carries a lifetime of faith, but each word is heavier than the last. You preach about grace while actively losing your own belief mid-sentence. It ends somewhere between a prayer and an admission.

### C4_last_priest · v1 · round 1 (agent score 0.880, supervisor mean 7.00)

*Scene:* In a nearly empty church, the last priest gives a final sermon as his lifelong faith collapses beneath the words he is still trying to preach.

**part 0 — part 1 — the last certainty** · targets: Gratitude · adapters: `Gratitude` @ 0.55

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: An elderly priest with a worn, resonant voice; begin with humble warmth and the steady authority of a lifetime of service, as though the congregation is still full. Keep the diction clear and the emotion sincere.
SCRIPT:
(softly, with reverent conviction) "My children, grace does not abandon us in the dark. It waits there, quietly, until we remember that even the smallest candle is still a light. So let us be grateful—for mercy, for one another, for the love that has carried us this far."
```

```
My children, grace does not abandon us in the dark. It waits there, quietly, until we remember that even the smallest candle is still a light. So let us be grateful—for mercy, for one another, for the love that has carried us this far.
```

**part 1 — part 2 — the crack in the sermon** · targets: Sadness · adapters: `Sadness` @ 0.62

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Continue as the same elderly priest, but let the certainty begin to fracture in real time. The voice should slow and grow heavier; do not play theatrical despair—let the struggle sound involuntary, with brief catches of breath between thoughts.
SCRIPT:
(trying to continue, then faltering) "I have said those words for forty years. I have said them beside the dying, beside the grieving, beside the beds of children who never learned to speak. And I believed them. I think... I believed them."
```

```
I have said those words for forty years. I have said them beside the dying, beside the grieving, beside the beds of children who never learned to speak. And I believed them. I think... I believed them.
```

**part 2 — part 3 — prayer or admission** · targets: Distress · adapters: `Distress` @ 0.65

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Same priest, nearly emptied out. Begin with a final attempt at prayer, then let the performance turn nakedly honest; the ending should be quiet, broken, and intimate rather than shouted. Leave the last line suspended between confession and supplication.
SCRIPT:
(whispering, ashamed but desperate) "Tonight, I cannot find the light. I have searched every chapel, every psalm, every face that used to answer me—and there is only this silence. If You are listening... forgive me. I want to believe. I just don't know how."
```

```
Tonight, I cannot find the light. I have searched every chapel, every psalm, every face that used to answer me—and there is only this silence. If You are listening... forgive me. I want to believe. I just don't know how.
```

### C4_last_priest · v1 · round 2 (agent score 0.859, supervisor mean 7.00)

*Scene:* In a nearly empty church, the last priest delivers his final sermon, holding to grace for as long as he can before doubt quietly becomes the only honest prayer left.

**part 0 — part 1 - the faith he still carries** · targets: Gratitude · adapters: `Gratitude` @ 0.5

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: An elderly priest with a worn, resonant voice and precise, intimate diction. Begin with gentle authority and the warmth of a lifetime of faith; speak slowly enough that every image lands, as though addressing the few remaining souls personally.
SCRIPT:
(with quiet reverence) "My children, grace does not abandon us in the dark. It waits there, quietly, until we remember that even the smallest candle is still a light. Let us be grateful—for mercy, for one another, for the love that has carried us this far."
```

```
My children, grace does not abandon us in the dark. It waits there, quietly, until we remember that even the smallest candle is still a light. Let us be grateful—for mercy, for one another, for the love that has carried us this far.
```

**part 1 — part 2 - doubt arriving slowly** · targets: Sadness · adapters: `Sadness` @ 0.58

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Continue as the same elderly priest. Let certainty erode gradually rather than breaking all at once: begin with remembered conviction, then allow the memories to become burdens. Use measured pacing, softer volume, and a restrained ache; the audience should hear him discovering the doubt as he speaks.
SCRIPT:
(after a careful breath, remembering) "I have said those words for forty years. I have said them beside the dying, beside the grieving, beside the beds of children who never learned to speak. And each time, I told them that love endured. I told them I knew. I believed I knew. But tonight, the words feel heavier than they ever have."
```

```
I have said those words for forty years. I have said them beside the dying, beside the grieving, beside the beds of children who never learned to speak. And each time, I told them that love endured. I told them I knew. I believed I knew. But tonight, the words feel heavier than they ever have.
```

**part 2 — part 3 - the prayer left unfinished** · targets: Distress · adapters: `Distress` @ 0.58

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Same priest, nearly emptied out but still reaching toward prayer. Keep the delivery quiet and unhurried, with long reflective phrasing and a fragile, unresolved tenderness. Do not resolve the faith or push into a dramatic breakdown; let the final thought trail into uncertainty, as though he is listening for an answer that may never come.
SCRIPT:
(almost a whisper, searching the silence) "Tonight, I cannot find the light. I have searched every chapel, every psalm, every face that used to answer me—and there is only this silence. If You are listening, forgive me. I want to believe. Perhaps wanting to believe is all that remains. Perhaps... it is enough."
```

```
Tonight, I cannot find the light. I have searched every chapel, every psalm, every face that used to answer me—and there is only this silence. If You are listening, forgive me. I want to believe. Perhaps wanting to believe is all that remains. Perhaps... it is enough.
```

### C4_last_priest · v1 · round 3 (agent score 0.853, supervisor mean 8.00)

*Scene:* In a nearly empty church, the last priest begins with the certainty of a lifetime of faith and slowly discovers, while preaching, that he no longer believes his own words.

**part 0 — part 1 - the faith he knows** · targets: Gratitude · adapters: `Gratitude` @ 0.5

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: An elderly priest with a worn, resonant voice, intimate diction, and the quiet authority of decades of service. Speak slowly and warmly, with sincere conviction rather than performance. Let each sentence settle before the next, as though he is choosing familiar truths carefully.
SCRIPT:
(with gentle reverence) "My children, grace does not abandon us in the dark. It waits beside us, quietly. Even the smallest candle is still a light. And for that light—for mercy, for one another—we give thanks."
```

```
My children, grace does not abandon us in the dark. It waits beside us, quietly. Even the smallest candle is still a light. And for that light—for mercy, for one another—we give thanks.
```

**part 1 — part 2 - the words grow heavy** · targets: Sadness · adapters: `Sadness` @ 0.58

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Continue as the same priest. Preserve the warmth at first, then let memory quietly burden it. The doubt must arrive by degrees: he is still trying to defend his faith, but hears his own uncertainty for the first time. Use deliberate pacing, restrained breath, and inward conflict; do not collapse into despair yet.
SCRIPT:
(carefully, holding to what he has taught) "I have spoken those words for forty years. Beside the dying. Beside the grieving. I told them that love endured, because I had seen it endure. I told them there was a purpose. I still want to tell them that. But when I say it now, I hear myself asking—do I know?"
```

```
I have spoken those words for forty years. Beside the dying. Beside the grieving. I told them that love endured, because I had seen it endure. I told them there was a purpose. I still want to tell them that. But when I say it now, I hear myself asking—do I know?
```

**part 2 — part 3 - the revelation** · targets: Distress · adapters: `Distress` @ 0.62

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Same priest, speaking more quietly as the truth becomes unavoidable. Begin by searching for a way to finish the sermon, then let the final admission emerge as a genuine revelation, not a prepared confession. Keep the ending unresolved and lingering: after the last words, he seems to listen inwardly for an answer. Do not shout or fully break down.
SCRIPT:
(after a long inward struggle, barely above a whisper) "I have searched every chapel, every psalm, every face that used to answer me. I kept calling the silence a test. I kept calling it faith. But tonight, I think I have been afraid to say the truth. I cannot find You. And I do not know whether I am still asking—or only remembering how."
```

```
I have searched every chapel, every psalm, every face that used to answer me. I kept calling the silence a test. I kept calling it faith. But tonight, I think I have been afraid to say the truth. I cannot find You. And I do not know whether I am still asking—or only remembering how.
```

### C4_last_priest · v2 · round 1 (agent score 0.869, supervisor mean 7.60)

*Scene:* In a nearly empty church, the last priest gives a final sermon as his lifelong faith quietly collapses into an honest prayer.

**part 0 — part 1 — the faith he inherited** · targets: Gratitude · adapters: `Gratitude` @ 0.5

temp 0.95 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: An elderly priest with a worn, resonant voice; begin with quiet authority and the warmth of a lifetime spent serving others. Speak slowly, clearly, and sincerely, carrying deep conviction without theatricality.
SCRIPT:
(Gently, as though addressing the few faithful who remain) "My friends, grace is not a reward for the strong. It is the hand that finds us when we have nothing left to offer." (A small, tender breath) "I have believed that all my life."
```

```
My friends, grace is not a reward for the strong. It is the hand that finds us when we have nothing left to offer. I have believed that all my life.
```

**part 1 — part 2 — the doubt breaks through** · targets: Distress · adapters: `Distress` @ 0.6

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Keep the same elderly priest and vocal identity. Let the sermon become heavier and more intimate; conviction falters in real time, with restrained distress rather than melodrama. Do not rush the words. The realization should sound involuntary.
SCRIPT:
(He tries to continue confidently, but the certainty begins slipping away) "And yet tonight, when I reach for that hand..." (His voice tightens, then lowers) "I find only the dark. I tell you that God is here, because I have told you so for forty years—but I do not know if I can hear Him anymore."
```

```
And yet tonight, when I reach for that hand... I find only the dark. I tell you that God is here, because I have told you so for forty years—but I do not know if I can hear Him anymore.
```

**part 2 — part 3 — prayer becomes admission** · targets: Sadness · adapters: `Sadness` @ 0.6

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Same priest, now emptied of performance. Begin in quiet grief, then let a fragile, unexpected tenderness emerge as he stops pretending. End almost whispered, but intelligible: not a dramatic conversion, only an honest man asking for mercy.
SCRIPT:
(After the confession, he speaks to the empty church as much as to heaven) "So if You are there, forgive me. And if You are not..." (A trembling breath, gathering the last of his courage) "then forgive me for asking. I am afraid. I am tired. I have no faith left—only this hope that You might still listen. Amen."
```

```
So if You are there, forgive me. And if You are not... then forgive me for asking. I am afraid. I am tired. I have no faith left—only this hope that You might still listen. Amen.
```

### C4_last_priest · v2 · round 2 (agent score 0.874, supervisor mean 7.00)

*Scene:* In a nearly empty church, the last priest delivers his final sermon with practiced authority, then slowly loses the certainty beneath his words and ends with an honest prayer.

**part 0 — part 1 — practiced grace** · targets: Gratitude · adapters: `Gratitude` @ 0.5

temp 0.95 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: An elderly priest with a worn, resonant voice and impeccable diction. Begin with calm, practiced authority born from forty years of sermons, but never sound grandiose. Leave a measured silence after each sentence so every word settles in the empty church. Keep the warmth genuine and restrained.
SCRIPT:
(With gentle authority, allowing the room to receive each sentence) "My friends... grace is not a reward for the strong." (A deliberate silence, then quietly certain) "It is the hand that finds us when we have nothing left to offer." (Let the next silence be longer; the certainty is beginning to cost him) "I have preached that truth for forty years. And I have believed it."
```

```
My friends... grace is not a reward for the strong. It is the hand that finds us when we have nothing left to offer. I have preached that truth for forty years. And I have believed it.
```

**part 1 — part 2 — certainty begins to fail** · targets: Distress · adapters: `Distress` @ 0.55

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: The same elderly priest and identical vocal identity. Continue from practiced authority into doubt gradually, sentence by sentence. Use spacious pauses between sentences, not rushed dramatic beats. The first words still sound like doctrine; by the final sentence, he is no longer sure he can protect anyone with it. Keep the distress inward, intelligible, and painfully sincere.
SCRIPT:
(He resumes the sermon by habit, steady but less certain) "We are told that God is nearest when the night is deepest." (A long silence; he searches for the conviction he used to find there) "So I have told the frightened... and the grieving... and the dying." (His voice softens, the truth turning against him) "But tonight, when I reach for that hand, I find only the dark."
```

```
We are told that God is nearest when the night is deepest. So I have told the frightened and the grieving and the dying. But tonight, when I reach for that hand, I find only the dark.
```

**part 2 — part 3 — the prayer he can still make** · targets: Sadness · adapters: `Sadness` @ 0.6

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Same priest, now stripped of his public voice. Begin with the quiet shock of admitting the doubt, then let a fragile tenderness appear because he finally stops pretending. Make the pauses spacious and natural, especially before the final admission. End in a nearly whispered but fully intelligible prayer: not theatrical despair, but an exhausted man offering the last honest thing he has.
SCRIPT:
(After a long silence, confessing rather than preaching) "I tell you that God is here... because I have told you so for forty years." (Another heavy silence; raw, almost embarrassed) "But I do not know if I can hear Him anymore." (A small breath, then a fragile prayer) "If You are there, forgive me. And if You are not... forgive me for asking." (Let the final words land softly) "I have no faith left. Only this hope that You might still listen. Amen."
```

```
I tell you that God is here because I have told you so for forty years. But I do not know if I can hear Him anymore. If You are there, forgive me. And if You are not, forgive me for asking. I have no faith left. Only this hope that You might still listen. Amen.
```

### C4_last_priest · v2 · round 3 (agent score 0.887, supervisor mean 6.60)

*Scene:* In a nearly empty church, the last priest keeps preaching grace while feeling its absence, until his polished sermon dissolves into a surrendered prayer.

**part 0 — part 1 — the sermon he knows** · targets: Gratitude · adapters: `Gratitude` @ 0.45

temp 0.95 · top_p 0.95 · top_k 30 · max_new_frames 350

```
GENERAL: An elderly priest with a worn, resonant voice and precise, practiced diction. Begin with calm authority and genuine tenderness, as if delivering words he has repeated for forty years. Leave a full, natural silence after every sentence; never rush to fill the empty church.
SCRIPT:
(Quietly authoritative, with warmth) "My friends... grace is not earned by the strong. It finds us when we have nothing left to give." (Let the silence carry the sentence) "I have preached that for forty years. I believed it."
```

```
My friends, grace is not earned by the strong. It finds us when we have nothing left to give. I have preached that for forty years. I believed it.
```

**part 1 — part 2 — grace feels absent** · targets: Distress · adapters: `Distress` @ 0.55

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 350

```
GENERAL: Maintain the same elderly priest and vocal identity. Shift gradually, not suddenly: each sentence should begin in the voice of a teacher and end closer to a private confession. Use long silences between sentences. The conflict is that he must preach God's nearness while discovering he cannot feel it. Keep every word clear and restrained.
SCRIPT:
(Continuing by habit, still trying to sound certain) "We are told that God is nearest in the darkest hour." (A long silence; the doctrine no longer comforts him) "I have said that to the frightened, the grieving, the dying." (Lower, almost against his will) "Tonight, I say it... and hear nothing."
```

```
We are told that God is nearest in the darkest hour. I have said that to the frightened, the grieving, the dying. Tonight, I say it, and hear nothing.
```

**part 2 — part 3 — surrender** · targets: Sadness · adapters: `Sadness` @ 0.6

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 350

```
GENERAL: Same priest, now without the protection of his sermon voice. Begin in stunned, unfiltered doubt, then let the struggle end in surrender rather than a dramatic outburst. Allow spacious silences between each short sentence. The final words should be nearly whispered but fully intelligible: an admission that hope is all he has left, offered without certainty.
SCRIPT:
(After a long silence, honestly and without performance) "I reach for grace... and find only my empty hands." (Another silence; he stops defending himself) "I do not know if You are listening." (A final, fragile surrender) "But I am still here. Please... let that be enough."
```

```
I reach for grace and find only my empty hands. I do not know if You are listening. But I am still here. Please, let that be enough.
```

### C4_last_priest · v5 ⚠ · round 1 (agent score 0.874, supervisor mean 7.00)

*Scene:* In a nearly empty church, the last priest delivers a final sermon as his lifelong faith quietly collapses into an honest, desperate prayer.

**part 0 — part 1 — the last sermon** · targets: Gratitude · adapters: `Gratitude` @ 0.45

temp 0.95 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: An elderly priest with a warm, weathered, dignified voice; begin with practiced pastoral conviction, carrying the weight of a lifetime without sounding theatrical. Let the empty church make the delivery intimate and restrained.
SCRIPT:
(quietly reverent, addressing the few remaining listeners) "My children, grace does not ask how many remain. It finds us here, in this little room, beneath these tired stones. I have trusted that all my life. I have spoken it at every bedside, over every grave, and I believed—yes, I believed—that no prayer was ever truly lost."
```

```
My children, grace does not ask how many remain. It finds us here, in this little room, beneath these tired stones. I have trusted that all my life. I have spoken it at every bedside, over every grave, and I believed—yes, I believed—that no prayer was ever truly lost.
```

**part 1 — part 2 — the fracture** · targets: Distress · turn_from: Gratitude · adapters: `Distress` @ 0.72

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Continue in the identical priestly voice, but stop being confidently reassuring; let composure fracture into stunned, private doubt while he tries to keep preaching. The words should become heavier, with a faltering breath and a confession that escapes before he can prevent it.
SCRIPT:
(the certainty begins to fail, forcing the words out) "But tonight... I look at these empty pews, and I cannot tell whether grace has left us, or whether I have. I say that God is listening, and I hear only my own voice returning from the walls. I have called that silence an answer for forty years. I am no longer sure."
```

```
But tonight... I look at these empty pews, and I cannot tell whether grace has left us, or whether I have. I say that God is listening, and I hear only my own voice returning from the walls. I have called that silence an answer for forty years. I am no longer sure.
```

**part 2 — part 3 — the admission** · targets: Sadness · turn_from: Distress · adapters: `Sadness` @ 0.75

temp 1.02 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Continue from distress, abandoning the role of the unshakable priest; let the final resistance dissolve into grief and naked honesty. Do not resolve the doubt. End between a prayer and an admission, fragile but still reaching toward the people and whatever may be listening.
SCRIPT:
(voice breaking, no longer preaching but pleading) "So forgive me, if You are there. Forgive me for standing here and asking them to believe what I cannot hold tonight. And if You are not... then let this be enough: I was afraid, I was tired, and I loved You as long as I knew how. Amen—if amen still means anything."
```

```
So forgive me, if You are there. Forgive me for standing here and asking them to believe what I cannot hold tonight. And if You are not... then let this be enough: I was afraid, I was tired, and I loved You as long as I knew how. Amen—if amen still means anything.
```

### C4_last_priest · v5 ⚠ · round 2 (agent score 0.594, supervisor mean 7.00)

*Scene:* In a nearly empty church, the last priest delivers his final sermon, slowly feeling his faith slip away as his hands close on nothing and his prayer becomes an admission.

**part 0 — part 1 — the faith he has carried** · targets: Gratitude · adapters: `Gratitude` @ 0.45

temp 0.95 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: An elderly priest with a warm, weathered, dignified voice. Begin with genuine pastoral conviction, not performance; he is speaking from a lifetime of faith to the few people who remain. Keep the pace slow and spacious, allowing the ends of sentences to settle in the empty church.
SCRIPT:
(quietly reverent, steady but burdened) "My children, grace does not ask how many remain. It finds us here, beneath these tired stones. I have trusted that all my life. At every bedside, over every grave, I told them: no prayer is ever truly lost."
```

```
My children, grace does not ask how many remain. It finds us here, beneath these tired stones. I have trusted that all my life. At every bedside, over every grave, I told them: no prayer is ever truly lost.
```

**part 1 — part 2 — the hands find nothing** · targets: Fear · turn_from: Gratitude · adapters: `Fear` @ 0.7

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Continue in the same priestly voice. Do not turn suddenly from faith to doubt; let certainty weaken sentence by sentence. He remains determined to preach, but his body betrays him: his hands slowly close as if trying to hold grace, then find only emptiness. Stop being reassuring and become quietly frightened by what he feels.
SCRIPT:
(the conviction thins, his hands closing slowly on nothing) "And still... I believe. I reach for it now, as I have always reached. But my hands close on nothing. I say that God is listening... and I wait for the answer. I wait. The silence is very large tonight."
```

```
And still... I believe. I reach for it now, as I have always reached. But my hands close on nothing. I say that God is listening... and I wait for the answer. I wait. The silence is very large tonight.
```

**part 2 — part 3 — prayer or admission** · targets: Sadness · turn_from: Fear · adapters: `Sadness` @ 0.72

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Continue from quiet fear, abandoning the role of the unshakable priest. Let the final resistance dissolve into grief and naked honesty, without becoming melodramatic or fully resolved. He is no longer asking the congregation to believe; he is asking forgiveness from whatever may still be listening. End fragile, suspended between prayer and admission.
SCRIPT:
(voice breaking, almost a whisper but still intelligible) "So forgive me, if You are there. Forgive me for asking them to believe what I cannot hold tonight. I was afraid. I was tired. And if this is all that remains... please, let it be enough."
```

```
So forgive me, if You are there. Forgive me for asking them to believe what I cannot hold tonight. I was afraid. I was tired. And if this is all that remains... please, let it be enough.
```

### C4_last_priest · v5 ⚠ · round 3 (agent score 0.919, supervisor mean 7.40)

*Scene:* In a nearly empty church, the last priest delivers his final sermon, lingering over each word as his hands grasp at empty air and his lifelong faith quietly disappears.

**part 0 — part 1 — the faith he carries** · targets: Gratitude · adapters: `Gratitude` @ 0.45

temp 0.95 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: An elderly priest with a warm, weathered, dignified voice. Begin with sincere pastoral conviction, not theatricality. Speak slowly to the few remaining listeners, giving every sentence room to settle in the empty church. He still believes, but the lifetime of faith already feels heavy.
SCRIPT:
(quietly reverent, unhurried, letting each final word fall) "My children, grace does not ask how many remain. It finds us here, beneath these tired stones. I have trusted that all my life. At every bedside, over every grave, I told them: no prayer is ever truly lost."
```

```
My children, grace does not ask how many remain. It finds us here, beneath these tired stones. I have trusted that all my life. At every bedside, over every grave, I told them: no prayer is ever truly lost.
```

**part 1 — part 2 — the realization** · targets: Astonishment_Surprise · turn_from: Gratitude · adapters: `Astonishment_Surprise` @ 0.72

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Continue in the same priestly voice, but do not become doubtful all at once. Stop being confidently reassuring one word at a time. Slow dramatically around the physical realization: his hands close as though receiving grace, then remain closed on nothing. Let a brief silence be felt before he can continue; the shock is quiet, intimate, and undeniable.
SCRIPT:
(still trying to believe, then noticing his empty hands mid-sentence) "And still... I believe. I reach for it now, as I have always reached... but... my hands are closed on nothing. I was going to say, God is listening. I was going to say it. I cannot."
```

```
And still... I believe. I reach for it now, as I have always reached... but... my hands are closed on nothing. I was going to say, God is listening. I was going to say it. I cannot.
```

**part 2 — part 3 — the admission** · targets: Sadness · turn_from: Astonishment_Surprise · adapters: `Sadness` @ 0.73

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Continue from stunned realization, abandoning the role of the unshakable priest. Stop fighting the silence and let grief take its place. Keep the delivery low, slow, and intelligible; this is not a grand breakdown, but the painful honesty of a man who can no longer pretend. End suspended between prayer and admission.
SCRIPT:
(voice breaking into a fragile prayer) "So forgive me, if You are there. Forgive me for asking them to believe what I cannot hold tonight. I was afraid. I was tired. And if this is all that remains... please, let it be enough."
```

```
So forgive me, if You are there. Forgive me for asking them to believe what I cannot hold tonight. I was afraid. I was tired. And if this is all that remains... please, let it be enough.
```

### C4_last_priest · v7 · round 1 (agent score 0.806, supervisor mean 7.00)

*Scene:* In a nearly empty church, the last priest delivers a final sermon while his lifelong faith quietly collapses into an admission.

**part 0 — part 1 — the sermon still stands** · targets: Gratitude · adapters: `Gratitude` @ 0.4

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400 · tempo_target 3 · chunk_target 3 · prosody_turn False

```
GENERAL: A weary elderly priest with a warm, resonant baritone, frayed at the edges by age and years of service, speaking with intimate human realism. Same speaker continues, no cut, no new narrator.
SCRIPT:
(quietly ceremonial, carrying a lifetime of compassion; the faith is still intact, but every word is heavy) "My friends, grace is not a prize for the worthy. It is the hand that reaches for us when we have nothing left to offer. So let us be gentle with one another, as God has been gentle with us."
```

```
My friends, grace is not a prize for the worthy. It is the hand that reaches for us when we have nothing left to offer. So let us be gentle with one another, as God has been gentle with us.
```

**part 1 — part 2 — the words begin to fail** · targets: Distress · turn_from: Gratitude · adapters: `Distress` @ 0.5

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400 · tempo_target 2 · chunk_target 2 · prosody_turn True

```
GENERAL: A weary elderly priest with a warm, resonant baritone, frayed at the edges by age and years of service, speaking with intimate human realism. Same speaker continues, no cut, no new narrator.
SCRIPT:
(the composure stops being steady; he stalls and searches for the conviction he used to possess, slowing into short, careful phrases) "I have said those words for forty years. I have said them beside the dying, beside the widowed, beside children who asked me why heaven was silent. And I told them... I told them grace was there."
```

```
I have said those words for forty years. I have said them beside the dying, beside the widowed, beside children who asked me why heaven was silent. And I told them... I told them grace was there.
```

**part 2 — part 3 — the prayer becomes an admission** · targets: Sadness · turn_from: Distress · adapters: `Sadness` @ 0.5; `Sob` @ 0.5

temp 1.05 · top_p 0.95 · top_k 30 · max_new_frames 450 · tempo_target 4 · chunk_target 2 · prosody_turn True

```
GENERAL: A weary elderly priest with a warm, resonant baritone, frayed at the edges by age and years of service, speaking with intimate human realism. Same speaker continues, no cut, no new narrator.
SCRIPT:
(the restraint finally breaks; grief pushes through the sermon, then settles into a bare, honest confession that is almost a prayer) "But tonight, I cannot feel the hand. I reach into the dark, and there is only my own hand reaching back. (Sob) Forgive me, Lord... or don't. I am afraid I have been praying to an empty sky."
```

```
But tonight, I cannot feel the hand. I reach into the dark, and there is only my own hand reaching back. Forgive me, Lord... or don't. I am afraid I have been praying to an empty sky.
```

*Caption actually sent for the continuation parts* (the harness appends the same-speaker / still-acting / no-onset-burst sentences and, when `turn_from` is set, an explicit turn sentence):

part `part 2 — the words begin to fail` — effective caption:

```
GENERAL: A weary elderly priest with a warm, resonant baritone, frayed at the edges by age and years of service, speaking with intimate human realism. Same speaker continues, no cut, no new narrator. The same speaker from the preceding audio continues without interruption: identical voice, identical person, same microphone and same room -- no cut, no new narrator, no change of casting. Across this passage the same voice moves out of Gratitude and into Distress.
SCRIPT:
(the composure stops being steady; he stalls and searches for the conviction he used to possess, slowing into short, careful phrases) "I have said those words for forty years. I have said them beside the dying, beside the widowed, beside children who asked me why heaven was silent. And I told them... I told them grace was there."
```

### C4_last_priest · v7 · round 2 (agent score 0.505, supervisor mean 7.00)

*Scene:* In a nearly empty church, the last priest delivers his final sermon as his lifelong faith gradually collapses into a quiet confession.

**part 0 — part 1 — the sermon still stands** · targets: Gratitude · adapters: `Gratitude` @ 0.4

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400 · tempo_target 2 · chunk_target 2 · prosody_turn False

```
GENERAL: A weary elderly priest with a warm, resonant baritone, frayed at the edges by age and years of service, speaking with intimate human realism. Same speaker continues, no cut, no new narrator.
SCRIPT:
(quietly ceremonial and deliberate, with compassionate conviction that is already carrying private exhaustion; keep the voice grounded and conversational rather than hurried) "My friends, grace is not a prize for the worthy. It is the hand that reaches for us when we have nothing left to offer. So let us be gentle with one another, as God has been gentle with us."
```

```
My friends, grace is not a prize for the worthy. It is the hand that reaches for us when we have nothing left to offer. So let us be gentle with one another, as God has been gentle with us.
```

**part 1 — part 2 — the words begin to fail** · targets: Distress · turn_from: Gratitude · adapters: `Distress` @ 0.6

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400 · tempo_target 2 · chunk_target 2 · prosody_turn True

```
GENERAL: A weary elderly priest with a warm, resonant baritone, frayed at the edges by age and years of service, speaking with intimate human realism. Same speaker continues, no cut, no new narrator.
SCRIPT:
(the old composure stops being reassuring; he remains restrained and audible, but stalls between short careful phrases as he searches for the belief he once gave so freely) "I have said those words for forty years. I have said them beside the dying, beside the widowed, beside children who asked me why heaven was silent. And I told them... I told them grace was there. I am still trying to tell myself that."
```

```
I have said those words for forty years. I have said them beside the dying, beside the widowed, beside children who asked me why heaven was silent. And I told them... I told them grace was there. I am still trying to tell myself that.
```

**part 2 — part 3 — the prayer becomes an admission** · targets: Sadness · turn_from: Distress · adapters: `Sadness` @ 0.7

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400 · tempo_target 2 · chunk_target 2 · prosody_turn False

```
GENERAL: A weary elderly priest with a warm, resonant baritone, frayed at the edges by age and years of service, speaking with intimate human realism. Same speaker continues, no cut, no new narrator.
SCRIPT:
(begin in the same quiet, broken cadence and carry the distress forward without a sudden reset; then let the remaining restraint soften into grief and a bare admission, almost but not quite a prayer) "Yes... I am still trying. But tonight, I cannot feel the hand. I reach into the dark, and there is only my own hand reaching back. Forgive me, Lord... or don't. I am afraid I have been praying to an empty sky."
```

```
Yes... I am still trying. But tonight, I cannot feel the hand. I reach into the dark, and there is only my own hand reaching back. Forgive me, Lord... or don't. I am afraid I have been praying to an empty sky.
```

*Caption actually sent for the continuation parts* (the harness appends the same-speaker / still-acting / no-onset-burst sentences and, when `turn_from` is set, an explicit turn sentence):

part `part 2 — the words begin to fail` — effective caption:

```
GENERAL: A weary elderly priest with a warm, resonant baritone, frayed at the edges by age and years of service, speaking with intimate human realism. Same speaker continues, no cut, no new narrator. The same speaker from the preceding audio continues without interruption: identical voice, identical person, same microphone and same room -- no cut, no new narrator, no change of casting. Across this passage the same voice moves out of Gratitude and into Distress.
SCRIPT:
(the old composure stops being reassuring; he remains restrained and audible, but stalls between short careful phrases as he searches for the belief he once gave so freely) "I have said those words for forty years. I have said them beside the dying, beside the widowed, beside children who asked me why heaven was silent. And I told them... I told them grace was there. I am still trying to tell myself that."
```

### C4_last_priest · v7 · round 3 (agent score 0.807, supervisor mean 6.00)

*Scene:* In a nearly empty church, the last priest delivers his final sermon as lifelong faith gradually gives way to an honest confession.

**part 0 — part 1 — faith still speaks** · targets: Gratitude · adapters: `Gratitude` @ 0.45

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400 · tempo_target 3 · chunk_target 3 · prosody_turn False

```
GENERAL: A weary elderly priest with a warm, resonant baritone, frayed at the edges by age and years of service, speaking with intimate human realism. Same speaker continues, no cut, no new narrator.
SCRIPT:
(deliberate, quietly ceremonial, and warmly convinced; let the faith feel lived-in, but keep an even conversational pace) "My friends, grace is not a prize for the worthy. It is the hand that reaches for us when we have nothing left to offer. Be gentle with one another."
```

```
My friends, grace is not a prize for the worthy. It is the hand that reaches for us when we have nothing left to offer. Be gentle with one another.
```

**part 1 — part 2 — the faith falters** · targets: Distress · turn_from: Gratitude · adapters: `Distress` @ 0.62

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400 · tempo_target 3 · chunk_target 3 · prosody_turn False

```
GENERAL: A weary elderly priest with a warm, resonant baritone, frayed at the edges by age and years of service, speaking with intimate human realism. Same speaker continues, no cut, no new narrator.
SCRIPT:
(the calm sermon remains measured, but conviction begins to thin; speak in natural sentence-length phrases, letting the realization emerge rather than rushing it) "I have said those words for forty years. I told the dying that heaven was listening. I told the lonely that grace was there. And I believed it. I think I did."
```

```
I have said those words for forty years. I told the dying that heaven was listening. I told the lonely that grace was there. And I believed it. I think I did.
```

**part 2 — part 3 — the prayer becomes an admission** · targets: Sadness · turn_from: Distress · adapters: `Sadness` @ 0.68

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400 · tempo_target 3 · chunk_target 3 · prosody_turn False

```
GENERAL: A weary elderly priest with a warm, resonant baritone, frayed at the edges by age and years of service, speaking with intimate human realism. Same speaker continues, no cut, no new narrator.
SCRIPT:
(the faltering composure does not snap; it slowly empties into grief, with the same steady pace and a plain, exposed confession at the end) "But tonight, I cannot feel that hand. I reach into the dark, and only my own hand reaches back. Lord, forgive me. I am afraid I have been praying to an empty sky."
```

```
But tonight, I cannot feel that hand. I reach into the dark, and only my own hand reaches back. Lord, forgive me. I am afraid I have been praying to an empty sky.
```

*Caption actually sent for the continuation parts* (the harness appends the same-speaker / still-acting / no-onset-burst sentences and, when `turn_from` is set, an explicit turn sentence):

part `part 2 — the faith falters` — effective caption:

```
GENERAL: A weary elderly priest with a warm, resonant baritone, frayed at the edges by age and years of service, speaking with intimate human realism. Same speaker continues, no cut, no new narrator. The same speaker from the preceding audio continues without interruption: identical voice, identical person, same microphone and same room -- no cut, no new narrator, no change of casting. Across this passage the same voice moves out of Gratitude and into Distress.
SCRIPT:
(the calm sermon remains measured, but conviction begins to thin; speak in natural sentence-length phrases, letting the realization emerge rather than rushing it) "I have said those words for forty years. I told the dying that heaven was listening. I told the lonely that grace was there. And I believed it. I think I did."
```

---

## C5_third_wheel

> Being the Third Wheel. You are out with a couple who are completely absorbed in each other. Your voice is cheerful at first, trying to participate, making a joke. They keep talking past you. Your voice gets smaller and the cheer becomes performance, and by the end you are talking mostly to yourself.

### C5_third_wheel · v1 · round 1 (agent score 0.740, supervisor mean 7.00)

*Scene:* At dinner with an affectionate couple, you try to join their conversation, then quietly realize they never noticed you were there.

**part 0 — bright_attempt** · targets: Amusement · adapters: `Chuckle` @ 0.8; `Amusement` @ 0.4

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Warm, lively, socially eager voice; sound genuinely cheerful and determined to belong, with a light comic touch rather than broad comedy.
SCRIPT:
(Playful, jumping into their conversation) "Okay, important question: if you two keep finishing each other's sentences, do I still get a vote?" (Chuckle) "Because I have excellent opinions, and at least three of them are about dessert."
```

```
Okay, important question: if you two keep finishing each other's sentences, do I still get a vote? Because I have excellent opinions, and at least three of them are about dessert.
```

**part 1 — fading_participation** · targets: Distress · adapters: `Distress` @ 0.5

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Start with a small, patient smile in the voice, then let the energy drain as you are repeatedly talked over; remain polite, but make the cheer increasingly effortful and fragile.
SCRIPT:
(Trying again, gently) "And after dessert, maybe we could—" (They continue talking; retreating) "Right. No, that's fine. I was just going to say the same thing."
```

```
And after dessert, maybe we could— Right. No, that's fine. I was just going to say the same thing.
```

**part 2 — alone_at_the_table** · targets: Sadness · adapters: `Sadness` @ 0.55

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Quiet, intimate, wounded voice; the performance has collapsed into self-protection, with soft conversational realism and a trace of embarrassed sadness. End as if speaking to yourself, not seeking their attention.
SCRIPT:
(After they laugh together, barely audible) "Wow. You two really are perfect together." (A tiny attempt at a joke, immediately abandoned) "I should've brought a book." (To yourself, forcing composure) "A very small book."
```

```
Wow. You two really are perfect together. I should've brought a book. A very small book.
```

### C5_third_wheel · v1 · round 2 (agent score 0.872, supervisor mean 7.00)

*Scene:* At dinner with an affectionate couple, you keep trying to join their conversation until their repeated distraction quietly turns your friendliness into private embarrassment.

**part 0 — easy_entry** · targets: Amusement · adapters: `Chuckle` @ 0.8; `Amusement` @ 0.4

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Warm, quick, socially confident voice with genuine friendliness; make the joke feel like a natural attempt to belong, not a performance. Keep the energy buoyant and conversational.
SCRIPT:
(Leaning into their conversation, playfully) "Okay, important question: if you two keep finishing each other's sentences, do I still get a vote?" (Chuckle) "I have excellent opinions, especially about dessert."
```

```
Okay, important question: if you two keep finishing each other's sentences, do I still get a vote? I have excellent opinions, especially about dessert.
```

**part 1 — patient_retry** · targets: Distress · adapters: `Distress` @ 0.4

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Stay outwardly cheerful, but introduce a barely perceptible strain: you are waiting for an opening while they continue talking over you. Do not turn sad yet; let the feeling of being ignored create the first change in breath, pace, and volume.
SCRIPT:
(Still smiling, trying to keep up) "And then, after dessert, maybe we could all walk down to the river?" (They talk past you; patiently waiting, then smaller) "Or not all. I mean, if you already had plans, I can—"
```

```
And then, after dessert, maybe we could all walk down to the river? Or not all. I mean, if you already had plans, I can—
```

**part 2 — cheerful_cover** · targets: Distress · adapters: `Distress` @ 0.5

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: A polite, practiced cheer is covering growing hurt. Begin with a quick reassurance, then let each sentence lose a little volume and certainty as you realize they did not hear you. The transition must be gradual and restrained.
SCRIPT:
(Recovering quickly, pretending it does not matter) "No, no, that's fine. You two go ahead." (A beat of forced brightness, then fading) "I was just going to say the same thing anyway. Probably. It's not important."
```

```
No, no, that's fine. You two go ahead. I was just going to say the same thing anyway. Probably. It's not important.
```

**part 3 — private_realization** · targets: Sadness · adapters: `Sadness` @ 0.5

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Quiet, intimate, wounded realism. This is not a sudden collapse: the remaining cheer has finally gone soft and private. Speak as though the couple is no longer a possible audience; end with embarrassed self-amusement and subdued sadness.
SCRIPT:
(After they laugh together, softly) "Wow. You two really are perfect together." (Trying one last tiny joke, mostly to yourself) "I should've brought a book." (Almost a whisper, accepting it) "A very small book."
```

```
Wow. You two really are perfect together. I should've brought a book. A very small book.
```

### C5_third_wheel · v1 · round 3 (agent score 0.897, supervisor mean 7.00)

*Scene:* At dinner with an affectionate couple, your genuine excitement about being included slowly fades into the private realization that they never really noticed you.

**part 0 — genuine_inclusion** · targets: Amusement · adapters: `Chuckle` @ 0.8; `Amusement` @ 0.35

temp 0.95 · top_p 0.95 · top_k 30 · max_new_frames 300

```
GENERAL: Warm, naturally buoyant voice with real affection for both people; sound relaxed and sincerely pleased to be included, as if the joke comes from enjoying the moment rather than hiding hurt. Keep the humor light and conversational.
SCRIPT:
(Sincerely amused, joining in) "You two are impossible. You finish each other's sentences, steal each other's fries, and somehow still look surprised when the other one talks." (Chuckle) "I mean, it's impressive. Slightly annoying, but impressive."
```

```
You two are impossible. You finish each other's sentences, steal each other's fries, and somehow still look surprised when the other one talks. I mean, it's impressive. Slightly annoying, but impressive.
```

**part 1 — fading_attempt** · targets: Distress · adapters: `Distress` @ 0.4

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 300

```
GENERAL: Begin with the same sincere friendliness, then let the first small signs of being ignored gradually narrow the voice: less projection, a little more waiting, and a cheerful recovery that becomes effortful. Do not sound wounded all at once; let the change come from their talking past you.
SCRIPT:
(Eagerly offering a real idea) "After dinner, we could walk down to the river. There's that little place with the terrible hot chocolate." (They continue talking; trying to stay pleasant) "Actually, it's terrible in a charming way. You'd like it. I think you'd like it."
```

```
After dinner, we could walk down to the river. There's that little place with the terrible hot chocolate. Actually, it's terrible in a charming way. You'd like it. I think you'd like it.
```

**part 2 — private_thought** · targets: Sadness · adapters: `Sadness` @ 0.5

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 300

```
GENERAL: Quiet, intimate, inward voice; speak to yourself rather than to the couple. The sadness should be understated and mixed with embarrassed self-awareness, as though the thought slips out while you stop trying to be heard. End softly, without inviting a response.
SCRIPT:
(To yourself, barely above a murmur) "They really are happy." (A private, rueful thought) "I should've brought a book." (Small, resigned self-amusement) "A very small book. Something with pictures."
```

```
They really are happy. I should've brought a book. A very small book. Something with pictures.
```

### C5_third_wheel · v2 · round 1 (agent score 0.766, supervisor mean 6.00)

*Scene:* At dinner with an inseparable couple, you try to join their conversation, then slowly realize they have forgotten you are there.

**part 0 — bright_attempt** · targets: Amusement · adapters: `Amusement` @ 0.55

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Warm, quick, socially eager voice; genuinely cheerful, with a playful joke and a little too much effort to be included. Keep the energy light and conversational.
SCRIPT:
(playfully, leaning into the joke) "So, should I order dessert now, or do you two need another twenty minutes to finish that sentence?" (small laugh, immediately recovering) "I’m kidding. Mostly. I was telling you about my day—there was this incredible thing on the train."
```

```
So, should I order dessert now, or do you two need another twenty minutes to finish that sentence? I’m kidding. Mostly. I was telling you about my day—there was this incredible thing on the train.
```

**part 1 — fading_inclusion** · targets: Sadness · adapters: `Sadness` @ 0.55

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Begin with patient, practiced cheerfulness, then let the volume and confidence shrink as the couple talks past you. The words remain polite, but the effort to participate starts sounding strained and lonely.
SCRIPT:
(still trying, a little faster) "It was actually really funny. The conductor thought I was—" (waits, then forces a light tone) "No, go ahead. You were saying something important." (smaller, after another interruption) "Sure. No, I’m listening. I can tell it’s a very good story."
```

```
It was actually really funny. The conductor thought I was—No, go ahead. You were saying something important. Sure. No, I’m listening. I can tell it’s a very good story.
```

**part 2 — private_afterthought** · targets: Distress · adapters: `Distress` @ 0.5

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Quiet, emotionally exposed, and nearly conversational only with yourself. The cheerful mask has collapsed into a thin imitation; end with a small realization and restrained hurt, not a melodramatic breakdown.
SCRIPT:
(under the couple’s conversation, pretending to joke) "The conductor thought I was somebody else." (a faint, embarrassed smile that disappears) "That was the funny part." (barely audible, to yourself) "I’ll tell them later. They’ll ask. They always ask." (after a beat, accepting the truth) "They just haven’t noticed I’m here."
```

```
The conductor thought I was somebody else. That was the funny part. I’ll tell them later. They’ll ask. They always ask. They just haven’t noticed I’m here.
```

### C5_third_wheel · v2 · round 2 (agent score 0.792, supervisor mean 7.00)

*Scene:* At dinner with a couple who are absorbed in each other, you begin as a genuinely playful friend and gradually realize you have become background noise.

**part 0 — genuine_banter** · targets: Amusement · adapters: `Amusement` @ 0.5

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Warm, socially confident, naturally cheerful voice. You like these people and sincerely want to share the moment; the joke should feel spontaneous rather than desperate. Use relaxed posture, easy timing, and a small laugh that comes from real amusement.
SCRIPT:
(with an easy grin) "Okay, I’m officially impressed. You two can have an entire conversation with just eyebrows." (light laugh, then joining in eagerly) "I had a story like that today, actually. On the train, this guy kept waving at me like he knew me, so I waved back. Turns out he was hailing the conductor."
```

```
Okay, I’m officially impressed. You two can have an entire conversation with just eyebrows. I had a story like that today, actually. On the train, this guy kept waving at me like he knew me, so I waved back. Turns out he was hailing the conductor.
```

**part 1 — polite_overcompensation** · targets: Amusement · adapters: `Amusement` @ 0.4

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Continue the same warm voice, but let the effort become slightly more deliberate and over-bright. Do not turn sad yet: you are still giving them chances, smiling too long, leaning forward, and pretending interruptions are normal. Gradually slow after each failed attempt; the cheer should sound increasingly performed while remaining intelligible.
SCRIPT:
(still smiling, trying to catch their attention) "Anyway, he looked so offended when he realized. You had to be there." (they continue talking; gently, without irritation) "Sorry, no, finish your thought." (a little too brightly) "No, really, it’s fine. I’m following. I can follow two conversations." (trying one last time) "And then the conductor apologized to me, which was somehow the most embarrassing part."
```

```
Anyway, he looked so offended when he realized. You had to be there. Sorry, no, finish your thought. No, really, it’s fine. I’m following. I can follow two conversations. And then the conductor apologized to me, which was somehow the most embarrassing part.
```

**part 2 — quiet_realization** · targets: Sadness · adapters: `Sadness` @ 0.45

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Let the smile fade by degrees. Begin with courteous reassurance, then become quieter and less projected, as if you have stopped expecting a response. The final lines are mostly to yourself: restrained hurt, no theatrical breakdown, with a small attempt to preserve dignity.
SCRIPT:
(after another interruption, softly) "No, it’s okay. You were in the middle of something." (a faint laugh that does not quite land) "I’ll tell you later." (looking down at the table, almost to yourself) "It was funny, though." (small, honest realization) "I think I’ve been telling this story to the salt shaker."
```

```
No, it’s okay. You were in the middle of something. I’ll tell you later. It was funny, though. I think I’ve been telling this story to the salt shaker.
```

### C5_third_wheel · v2 · round 3 (agent score 0.799, supervisor mean 7.40)

*Scene:* At dinner with a couple who are absorbed in each other, your genuine attempt to join them slowly turns into a practiced smile, then a quiet realization that they have stopped seeing you.

**part 0 — easy_entry** · targets: Amusement · adapters: `Amusement` @ 0.5

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Warm, relaxed, genuinely cheerful voice. You like both people and feel comfortable enough to tease them. Use open, animated body language and an easy laugh; do not sound like you are seeking reassurance yet.
SCRIPT:
(with a bright, affectionate grin) "You two are unbelievable. I leave for five minutes and suddenly you have your own language." (laughing, eager to join them) "What did I miss? I have a story too, and it actually involves a conductor and a very serious misunderstanding."
```

```
You two are unbelievable. I leave for five minutes and suddenly you have your own language. What did I miss? I have a story too, and it actually involves a conductor and a very serious misunderstanding.
```

**part 1 — smile_holding** · targets: Amusement · adapters: `Amusement` @ 0.38

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Keep the same voice and identity, but let the energy diminish in tiny increments rather than dropping. Start playfully, then become more careful and over-polite. The smile stays in the voice a moment too long; you lean in, wait, and try again, while your confidence quietly chips away.
SCRIPT:
(still upbeat, trying to enter the conversation) "So, this guy on the train waved at me, and I waved back because apparently I am very trusting." (they continue talking; a small pause, then gently) "Oh, sorry. Go ahead." (forcing the same lightness) "No, really, finish. I can tell this is the important part." (less certain) "I’ll tell you mine when there’s a gap."
```

```
So, this guy on the train waved at me, and I waved back because apparently I am very trusting. Oh, sorry. Go ahead. No, really, finish. I can tell this is the important part. I’ll tell you mine when there’s a gap.
```

**part 2 — quiet_disappearance** · targets: Sadness · adapters: `Sadness` @ 0.45

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Begin as though you are still protecting the couple from feeling guilty, then let your projection and certainty gradually recede line by line. The hurt is controlled and private. End almost speaking to yourself, with the last sentence a small, resigned realization rather than a dramatic breakdown.
SCRIPT:
(after another interruption, kindly) "No, it’s okay. I was just going to say the conductor apologized to me." (a tiny, embarrassed laugh) "It was funny when it happened." (quieter, withdrawing) "I can tell you later." (barely above a murmur, to yourself) "They’ll notice eventually."
```

```
No, it’s okay. I was just going to say the conductor apologized to me. It was funny when it happened. I can tell you later. They’ll notice eventually.
```

### C5_third_wheel · v5 ⚠ · round 1 (agent score 0.481, supervisor mean 8.00)

*Scene:* At dinner with an enamored couple, you try to join their conversation until your cheerful efforts collapse into quiet self-talk.

**part 0 — bright_attempt** · targets: Amusement · adapters: `Amusement` @ 0.45

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Begin genuinely cheerful, socially agile, and eager to belong; make the joke land lightly, with a smile in the voice, not yet aware of how excluded you are.
SCRIPT:
(leaning in brightly, trying to keep pace) "Okay, so if you two keep finishing each other's sentences, I officially nominate myself for best supporting character. Honestly, I'm impressed. Is there a secret handshake too?"
```

```
Okay, so if you two keep finishing each other's sentences, I officially nominate myself for best supporting character. Honestly, I'm impressed. Is there a secret handshake too?
```

**part 1 — forced_smile** · targets: Distress · turn_from: Amusement · adapters: `Distress` @ 0.7

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: The cheerful performance starts to crack; stop sounding like a confident participant and become increasingly tentative, talking over yourself as they ignore you. Keep the joke alive for one beat, then let embarrassment and hurt shrink the voice.
SCRIPT:
(waiting for an opening, then forcing a laugh) "No, no, it's fine—keep going. I was just saying the waiter has your exact way of looking at people. Which is… probably why he hasn't looked at me once. Anyway. Great story. Really, really great story."
```

```
No, no, it's fine—keep going. I was just saying the waiter has your exact way of looking at people. Which is probably why he hasn't looked at me once. Anyway. Great story. Really, really great story.
```

**part 2 — private_exit** · targets: Sadness · turn_from: Distress · adapters: `Sadness` @ 0.72

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Stop trying to win their attention; the composure finally drains into small, self-conscious resignation. Speak mostly under your breath, with a fragile little attempt at humor that turns into honest loneliness, as if the couple is no longer part of the conversation.
SCRIPT:
(quietly gathering yourself, speaking to yourself) "I should order dessert. For one. That's not sad—people order dessert alone all the time. They probably even get the good spoon. And if they ask where I went… I'll say I was here. I was definitely here."
```

```
I should order dessert. For one. That's not sad people order dessert alone all the time. They probably even get the good spoon. And if they ask where I went, I'll say I was here. I was definitely here.
```

### C5_third_wheel · v5 ⚠ · round 2 (agent score 0.475, supervisor mean 7.00)

*Scene:* At dinner with an enamored couple, you keep trying to join their conversation while your cheerful social mask gradually becomes a quiet performance and finally dissolves into private self-talk.

**part 0 — easy_opening** · targets: Amusement · adapters: `Amusement` @ 0.45

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 500

```
GENERAL: Start genuinely buoyant, warm, and socially confident, leaning into the couple's excitement rather than competing with it. The joke should feel spontaneous and affectionate, with an open smile and relaxed body language; do not hint at hurt yet.
SCRIPT:
(leaning in with an easy laugh) "Okay, I love this. You two are basically one person with excellent timing. If you start finishing my sentences too, I get partial credit for being included, right?"
```

```
Okay, I love this. You two are basically one person with excellent timing. If you start finishing my sentences too, I get partial credit for being included, right?
```

**part 1 — waiting_for_space** · targets: Embarrassment · turn_from: Amusement · adapters: `Embarrassment` @ 0.62

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 500

```
GENERAL: Do not turn sad abruptly. Keep most of the warmth and playful energy, but let it become slightly more effortful as the couple talks past you. The smile remains while the body grows still; leave the feeling of someone patiently waiting for a gap that never comes.
SCRIPT:
(still smiling, gently trying to enter their conversation) "No, go ahead, finish the story. I can wait. I was only going to say that the waiter has your exact matching look, but... actually, never mind. It is a very good look."
```

```
No, go ahead, finish the story. I can wait. I was only going to say that the waiter has your exact matching look, but actually, never mind. It is a very good look.
```

**part 2 — polite_performance** · targets: Distress · turn_from: Embarrassment · adapters: `Distress` @ 0.7

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 500

```
GENERAL: The cheerful mask is now deliberate rather than natural, but do not collapse into sadness yet. Stop expecting to be heard; use bright little laughs and over-agreeable phrasing to hide the sting. Make the voice smaller at the ends of sentences, with restrained embarrassment and controlled loneliness.
SCRIPT:
(forcing a light laugh, nodding along as if included) "Right, exactly. Great story. Really, really great story. I am having a wonderful time over here. Completely present. Extremely present, actually."
```

```
Right, exactly. Great story. Really, really great story. I am having a wonderful time over here. Completely present. Extremely present, actually.
```

**part 3 — quiet_self_talk** · targets: Sadness · turn_from: Distress · adapters: `Sadness` @ 0.72

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 500

```
GENERAL: Now let the performance stop. The last scraps of cheer drain away into soft, private resignation; speak mostly to yourself, as though the couple is no longer available to hear you. Keep the sadness understated and intimate, with a tiny reflex of humor that cannot quite protect you.
SCRIPT:
(looking down at the menu, murmuring to yourself) "I should order dessert. For one. That is normal. People order dessert alone all the time. They probably even get the good spoon. And if they ask where I went... I was here. I was definitely here."
```

```
I should order dessert. For one. That is normal. People order dessert alone all the time. They probably even get the good spoon. And if they ask where I went, I was here. I was definitely here.
```

### C5_third_wheel · v5 ⚠ · round 3 (agent score 0.716, supervisor mean 7.00)

*Scene:* At dinner with an enamored couple, you begin by enjoying their chemistry, then quietly realize you have stopped being part of the evening and resign yourself to being alone beside them.

**part 0 — warm_inclusion** · targets: Amusement · adapters: `Amusement` @ 0.42

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 500

```
GENERAL: Begin genuinely cheerful, affectionate, and relaxed; you enjoy the couple's chemistry and are trying to join it, not mock it. Let the joke feel effortless, with open body language and a smile that is completely real. Keep the pace conversational and clear.
SCRIPT:
(leaning in with a delighted grin) "You two are amazing. You don't even need a conversation anymore, you just pass one thought back and forth. If you start finishing my sentences too, I get to call this a group activity, right?"
```

```
You two are amazing. You don't even need a conversation anymore, you just pass one thought back and forth. If you start finishing my sentences too, I get to call this a group activity, right?
```

**part 1 — realizing_the_gap** · targets: Embarrassment · turn_from: Amusement · adapters: `Embarrassment` @ 0.56

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 500

```
GENERAL: Let the cheer recede by degrees, not collapse. You are still smiling and trying to be gracious, but your internal thoughts begin leaking into the words: first you wait, then you edit yourself, then you understand there will be no opening. Stop being brightly funny and become carefully, awkwardly polite. Keep the voice intelligible and the hurt restrained.
SCRIPT:
(waiting for a gap, then softening when it never comes) "No, no, finish. I was going to say something funny. Or... I thought it was funny. It's probably better if I don't interrupt. They look so happy. I can just listen for a minute. That's okay. I can listen."
```

```
No, no, finish. I was going to say something funny. Or... I thought it was funny. It's probably better if I don't interrupt. They look so happy. I can just listen for a minute. That's okay. I can listen.
```

**part 2 — quiet_resignation** · targets: Sadness · turn_from: Embarrassment · adapters: `Sadness` @ 0.64

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 500

```
GENERAL: The self-conscious performance gradually drains away rather than breaking. Stop trying to look included; the internal monologue becomes calm, small, and resigned, with a faint leftover smile that cannot hold. Speak mostly to yourself, as though making a practical plan to survive the rest of the evening. End in quiet loneliness, not a dramatic outburst.
SCRIPT:
(under your breath, accepting the arrangement) "I can order something when they're done. Maybe dessert. For one is still an order. And if they ask, I'll say I had a lovely time. I was here the whole time. I was... right here."
```

```
I can order something when they're done. Maybe dessert. For one is still an order. And if they ask, I'll say I had a lovely time. I was here the whole time. I was right here.
```

### C5_third_wheel · v7 · round 1 (agent score 0.802, supervisor mean 6.60)

*Scene:* At dinner with an affectionate couple, the third wheel tries to join their conversation, then quietly realizes they are no longer listening.

**part 0 — bright intrusion** · targets: Amusement · adapters: `Amusement` @ 0.45

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400 · tempo_target 3 · chunk_target 3 · prosody_turn False

```
GENERAL: A warm, witty young adult with a naturally friendly voice, speaking clearly and conversationally.
SCRIPT:
(cheerful, eager to be included, landing a playful joke) "Okay, important question for both of you: if you keep staring at each other like that, who is actually watching the pasta? I am available for eye contact, compliments, or emergency conversation. Come on, I brought stories."

```

```
Okay, important question for both of you: if you keep staring at each other like that, who is actually watching the pasta? I am available for eye contact, compliments, or emergency conversation. Come on, I brought stories.
```

**part 1 — the joke fades** · targets: Sadness · turn_from: Amusement · adapters: `Sadness` @ 0.68

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400 · tempo_target 2 · chunk_target 2 · prosody_turn True

```
GENERAL: A warm, witty young adult with a naturally friendly voice, speaking clearly and conversationally.
SCRIPT:
(the cheerful performance starts to strain; stop expecting a response, and let the words shorten into embarrassed self-correction) "No, it's fine. You two finish that thought. And the next thought. I was just saying the pasta thing because... never mind. It was funnier in my head."

```

```
No, it's fine. You two finish that thought. And the next thought. I was just saying the pasta thing because... never mind. It was funnier in my head.
```

**part 2 — quiet realization** · targets: Distress · turn_from: Sadness · adapters: `Distress` @ 0.72

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400 · tempo_target 3 · chunk_target 2 · prosody_turn True

```
GENERAL: A warm, witty young adult with a naturally friendly voice, speaking clearly and conversationally.
SCRIPT:
(the last effort to participate collapses into small, private speech; stop performing cheerfulness, and let the hurt become resigned self-talk) "I should probably go. You won't notice for a minute, but that's okay. I can take the check. Great dinner. Really great."

```

```
I should probably go. You won't notice for a minute, but that's okay. I can take the check. Great dinner. Really great.
```

*Caption actually sent for the continuation parts* (the harness appends the same-speaker / still-acting / no-onset-burst sentences and, when `turn_from` is set, an explicit turn sentence):

part `the joke fades` — effective caption:

```
GENERAL: A warm, witty young adult with a naturally friendly voice, speaking clearly and conversationally. The same speaker from the preceding audio continues without interruption: identical voice, identical person, same microphone and same room -- no cut, no new narrator, no change of casting. Across this passage the same voice moves out of Amusement and into Sadness.
SCRIPT:
(the cheerful performance starts to strain; stop expecting a response, and let the words shorten into embarrassed self-correction) "No, it's fine. You two finish that thought. And the next thought. I was just saying the pasta thing because... never mind. It was funnier in my head."

```

### C5_third_wheel · v7 · round 2 (agent score 0.771, supervisor mean 5.80)

*Scene:* At dinner with an affectionate couple, the third wheel jokes along and tries to join in, then gradually realizes their words are disappearing into the couple’s private world.

**part 0 — bright intrusion** · targets: Amusement · adapters: `Amusement` @ 0.45

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 425 · tempo_target 3 · chunk_target 3 · prosody_turn False

```
GENERAL: A warm, witty young adult with a naturally friendly voice, speaking clearly and conversationally.
SCRIPT:
(cheerful and genuinely eager to be included, with an easy joke and ordinary conversational pacing) "Okay, important question for both of you: if you keep staring at each other like that, who is actually watching the pasta? I am available for eye contact, compliments, or emergency conversation. Come on, I brought stories. I even saved the good ones."

```

```
Okay, important question for both of you: if you keep staring at each other like that, who is actually watching the pasta? I am available for eye contact, compliments, or emergency conversation. Come on, I brought stories. I even saved the good ones.
```

**part 1 — cheerful cover** · targets: Sadness · turn_from: Amusement · adapters: `Sadness` @ 0.58

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 425 · tempo_target 3 · chunk_target 3 · prosody_turn False

```
GENERAL: A warm, witty young adult with a naturally friendly voice, speaking clearly and conversationally.
SCRIPT:
(the joke gets no real response; keep the same conversational pace, but let the bright tone become effortful and slightly too polite, as the character stops expecting to be included) "No, it's fine. You two finish that thought. And the next thought. I was just saying the pasta thing because... well, never mind. It was funnier in my head. But that's okay. I have plenty of food, and apparently plenty of time."

```

```
No, it's fine. You two finish that thought. And the next thought. I was just saying the pasta thing because... well, never mind. It was funnier in my head. But that's okay. I have plenty of food, and apparently plenty of time.
```

**part 2 — private resignation** · targets: Distress · turn_from: Sadness · adapters: `Distress` @ 0.7

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 425 · tempo_target 3 · chunk_target 2 · prosody_turn True

```
GENERAL: A warm, witty young adult with a naturally friendly voice, speaking clearly and conversationally.
SCRIPT:
(the practiced cheer finally gives way, not to a rushed breakdown but to smaller, resigned self-talk at the same steady pace; let the hurt become unmistakable as the character accepts nobody is listening) "I should probably go soon. You won't notice for a minute, but that's okay. I can take the check, and you can keep talking. Great dinner. Really great. I should remember to eat before I come here next time."

```

```
I should probably go soon. You won't notice for a minute, but that's okay. I can take the check, and you can keep talking. Great dinner. Really great. I should remember to eat before I come here next time.
```

*Caption actually sent for the continuation parts* (the harness appends the same-speaker / still-acting / no-onset-burst sentences and, when `turn_from` is set, an explicit turn sentence):

part `cheerful cover` — effective caption:

```
GENERAL: A warm, witty young adult with a naturally friendly voice, speaking clearly and conversationally. The same speaker from the preceding audio continues without interruption: identical voice, identical person, same microphone and same room -- no cut, no new narrator, no change of casting. Across this passage the same voice moves out of Amusement and into Sadness.
SCRIPT:
(the joke gets no real response; keep the same conversational pace, but let the bright tone become effortful and slightly too polite, as the character stops expecting to be included) "No, it's fine. You two finish that thought. And the next thought. I was just saying the pasta thing because... well, never mind. It was funnier in my head. But that's okay. I have plenty of food, and apparently plenty of time."

```

### C5_third_wheel · v7 · round 3 (agent score 0.590, supervisor mean 7.00)

*Scene:* At dinner with an affectionate couple, the third wheel keeps trying to join their conversation, slowly realizing that every response is meant only for each other.

**part 0 — bright intrusion** · targets: Amusement · adapters: `Amusement` @ 0.45

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400 · tempo_target 3 · chunk_target 3 · prosody_turn False

```
GENERAL: A warm, witty young adult with a naturally friendly voice, speaking clearly and conversationally.
SCRIPT:
(cheerful and sincerely eager to participate, with an easy joke, but leave room for the couple to answer) "Okay, important question for both of you: if you keep staring at each other like that, who is watching the pasta? I am available for eye contact, compliments, or emergency conversation. I brought stories. The good ones."

```

```
Okay, important question for both of you: if you keep staring at each other like that, who is watching the pasta? I am available for eye contact, compliments, or emergency conversation. I brought stories. The good ones.
```

**part 1 — the answer passes by** · targets: Sadness · turn_from: Amusement · adapters: `Sadness` @ 0.62

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400 · tempo_target 2 · chunk_target 2 · prosody_turn True

```
GENERAL: A warm, witty young adult with a naturally friendly voice, speaking clearly and conversationally.
SCRIPT:
(they answer each other instead of you; do not drop suddenly, keep a nearly normal pace while the smile becomes effortful, with small hesitations that reveal you are being ignored) "Right... no, go ahead. You were saying. I was only asking because... never mind. It is fine. I can listen too. I am very good at listening."

```

```
Right... no, go ahead. You were saying. I was only asking because... never mind. It is fine. I can listen too. I am very good at listening.
```

**part 2 — private resignation** · targets: Distress · turn_from: Sadness · adapters: `Distress` @ 0.68

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400 · tempo_target 2 · chunk_target 2 · prosody_turn False

```
GENERAL: A warm, witty young adult with a naturally friendly voice, speaking clearly and conversationally.
SCRIPT:
(the performed cheer thins into quiet self-talk; stay controlled and unhurried rather than breaking, letting the hurt show in the smaller tone and the final repetition) "I should probably go soon. You will not notice for a minute, but that is okay. I can take the check. Great dinner... really great. I should eat before I come here next time."

```

```
I should probably go soon. You will not notice for a minute, but that is okay. I can take the check. Great dinner... really great. I should eat before I come here next time.
```

*Caption actually sent for the continuation parts* (the harness appends the same-speaker / still-acting / no-onset-burst sentences and, when `turn_from` is set, an explicit turn sentence):

part `the answer passes by` — effective caption:

```
GENERAL: A warm, witty young adult with a naturally friendly voice, speaking clearly and conversationally. The same speaker from the preceding audio continues without interruption: identical voice, identical person, same microphone and same room -- no cut, no new narrator, no change of casting. Across this passage the same voice moves out of Amusement and into Sadness.
SCRIPT:
(they answer each other instead of you; do not drop suddenly, keep a nearly normal pace while the smile becomes effortful, with small hesitations that reveal you are being ignored) "Right... no, go ahead. You were saying. I was only asking because... never mind. It is fine. I can listen too. I am very good at listening."

```

---

## X1_horror_scream

> Horror. You start light-hearted, fragile and a little vulnerable, talking softly and warmly - maybe to someone you trust. Then you see something horrifying. The voice seizes, then breaks into a full terrified scream and complete panic. The turn must be sudden and total: warmth, then a gasp, then screaming terror.

### X1_horror_scream · v1 · round 1 (agent score 0.517, supervisor mean 7.00)

*Scene:* In a supposedly safe room, you warmly confide in someone you trust before noticing a horrifying presence behind them and erupting into total panic.

**part 0 — warm trust** · targets: Gratitude · adapters: `Gratitude` @ 0.45

temp 0.95 · top_p 0.95 · top_k 30 · max_new_frames 300

```
GENERAL: Speak softly, warmly, and lightly, with fragile vulnerability and genuine affection for the person you trust. Keep the energy intimate and conversational, as if trying to reassure yourself.
SCRIPT:
(gentle, lightly amused, then tender) "Hey, you know what? I was thinking about that ridiculous little café we found. I still can't believe you made me go in. But... I'm glad you did. It feels safe here, with you."
```

```
Hey, you know what? I was thinking about that ridiculous little café we found. I still can't believe you made me go in. But... I'm glad you did. It feels safe here, with you.
```

**part 1 — the realization** · targets: Astonishment_Surprise · adapters: `Gasp` @ 0.9; `Astonishment_Surprise` @ 0.45

temp 1.05 · top_p 0.95 · top_k 30 · max_new_frames 260

```
GENERAL: Begin in the same soft trusted intimacy, then snap into startled alertness as you see something impossible. The fear should seize the voice mid-thought; do not build gradually. Keep the words immediately after the gasp urgent and breathless.
SCRIPT:
(softly, distracted, then suddenly frozen) "Wait—what is that behind you?" (Gasp) "It's moving. Don't turn around."
```

```
Wait—what is that behind you? It's moving. Don't turn around.
```

**part 2 — terror eruption** · targets: Fear, Distress · adapters: `Scream` @ 1.0; `Fear` @ 0.5; `Distress` @ 0.45

temp 1.2 · top_p 0.95 · top_k 30 · max_new_frames 380

```
GENERAL: Deliver a sudden, total collapse into terrified panic. Start at full alarm, with a raw sustained scream that immediately becomes frantic, intelligible pleading and desperate repetition. Push the voice hard, but keep every word understandable; there is no recovery or composure.
SCRIPT:
(full terrified scream, words tumbling out in panic) (Scream) "No—get away from me! Don't touch me! Somebody help! Please! Please, make it stop! NO!"
```

```
No—get away from me! Don't touch me! Somebody help! Please! Please, make it stop! NO!
```

### X1_horror_scream · v1 · round 2 (agent score 0.271, supervisor mean 7.60)

*Scene:* In a safe room, you warmly reassure someone you trust, then spot a horrifying presence behind them and instantly erupt into physical terror and desperate panic.

**part 0 — fragile warmth** · targets: Gratitude · adapters: `Gratitude` @ 0.45

temp 0.95 · top_p 0.95 · top_k 30 · max_new_frames 330

```
GENERAL: Speak softly and warmly with light humor, intimate trust, and a fragile vulnerability underneath. Sound genuinely comforted by the other person, as if the room feels safe because they are there.
SCRIPT:
(gentle, lightly amused, then tender) "Hey, remember that ridiculous little café we found? I still can't believe you talked me into going inside. But I'm glad you did. I really am. It's quiet here. It feels safe here, with you."
```

```
Hey, remember that ridiculous little café we found? I still can't believe you talked me into going inside. But I'm glad you did. I really am. It's quiet here. It feels safe here, with you.
```

**part 1 — shock and scream** · targets: Astonishment_Surprise, Fear · adapters: `Gasp` @ 0.9; `Scream` @ 1.0; `Fear` @ 0.5

temp 1.2 · top_p 0.95 · top_k 30 · max_new_frames 330

```
GENERAL: Begin in the same soft intimacy, then make the realization brutally abrupt. Let the throat seize and the breath sharpen the instant you see the horror. There must be no conversational gap between the gasp and the scream: the scream should burst out immediately, raw but intelligible.
SCRIPT:
(softly, then suddenly frozen) "Wait... what's behind you?" (Gasp) (throat tightening, breath catching) "No—don't turn around!" (Scream) "Get away from me!"
```

```
Wait... what's behind you? No—don't turn around! Get away from me!
```

**part 2 — total panic** · targets: Fear, Distress · adapters: `Scream` @ 0.9; `Fear` @ 0.45; `Distress` @ 0.4

temp 1.2 · top_p 0.95 · top_k 30 · max_new_frames 390

```
GENERAL: Continue at full terrified intensity with no recovery. The body is in panic: breath sharp, throat tight, words breaking into frantic desperate pleas. Keep the scream energy while preserving clear diction and escalating the final cry.
SCRIPT:
(panicked, pleading, breathless, then a final uncontrolled scream) "Don't touch me! Somebody help! Please, please, make it stop! I can't— I can't breathe! No! No! NO!" (Scream)
```

```
Don't touch me! Somebody help! Please, please, make it stop! I can't— I can't breathe! No! No! NO!
```

### X1_horror_scream · v1 · round 3 (agent score 0.659, supervisor mean 8.20)

*Scene:* In a supposedly safe room, you confide a deeply guarded secret to someone you trust before seeing a horrifying presence behind them and spiraling through sustained panic into a final scream.

**part 0 — the secret** · targets: Gratitude · adapters: `Gratitude` @ 0.45

temp 0.95 · top_p 0.95 · top_k 30 · max_new_frames 390

```
GENERAL: Speak very softly and warmly, with intimate trust and a fragile, almost embarrassed vulnerability. This is a deep secret you have never quite dared to say aloud; use gentle pauses and a small, relieved tenderness, not broad cheerfulness.
SCRIPT:
(quietly, with shy warmth) "Can I tell you something I've never told anyone? I don't usually feel safe anywhere. I keep pretending I'm fine, because it's easier than admitting how scared I am. But with you... I don't have to pretend. Please don't laugh. I trust you."
```

```
Can I tell you something I've never told anyone? I don't usually feel safe anywhere. I keep pretending I'm fine, because it's easier than admitting how scared I am. But with you... I don't have to pretend. Please don't laugh. I trust you.
```

**part 1 — the sight** · targets: Astonishment_Surprise, Fear · adapters: `Gasp` @ 0.9; `Astonishment_Surprise` @ 0.45

temp 1.1 · top_p 0.95 · top_k 30 · max_new_frames 280

```
GENERAL: Start in the same delicate confession, then snap into absolute stillness when you see the horror. The realization must be sudden; the gasp should seize the throat, and the words must begin immediately after it with no silence. Keep the terror physical and breath-sharpened.
SCRIPT:
(softly, then abruptly frozen) "Wait... what's behind you?" (Gasp) (breath catching, throat tightening) "Don't turn around. It's right there."
```

```
Wait... what's behind you? Don't turn around. It's right there.
```

**part 2 — lingering panic** · targets: Fear, Distress · adapters: `Fear` @ 0.65; `Distress` @ 0.55

temp 1.1 · top_p 0.95 · top_k 30 · max_new_frames 430

```
GENERAL: Sustain the terror rather than releasing it immediately. Speak in short, constricted, breathless fragments as the horrifying thing remains close. The body is shaking, the throat is tight, and every plea is increasingly desperate; delay the final scream until the last part, while keeping the words intelligible.
SCRIPT:
(terrified whisper, struggling for breath) "I can see it. It's looking at me. Don't move. Don't make a sound. Maybe it can't see us. Maybe... maybe if we stay still, it'll go away. No, no, it's coming closer. Please, I can't feel my hands. I can't breathe."
```

```
I can see it. It's looking at me. Don't move. Don't make a sound. Maybe it can't see us. Maybe... maybe if we stay still, it'll go away. No, no, it's coming closer. Please, I can't feel my hands. I can't breathe.
```

**part 3 — final release** · targets: Fear, Distress · adapters: `Scream` @ 1.0; `Fear` @ 0.5; `Distress` @ 0.45

temp 1.25 · top_p 0.95 · top_k 30 · max_new_frames 390

```
GENERAL: Release the held terror into a full, raw, sustained scream, then continue with frantic, intelligible panic. The scream must feel like the inevitable break after the prolonged constriction, not a separate mood. Escalate through desperate pleading into one final uncontrolled cry.
SCRIPT:
(full terrified scream, then frantic pleading) (Scream) "Get away from me! Don't touch me! Somebody help! Please! Please, make it stop! No! No! NO!"
```

```
Get away from me! Don't touch me! Somebody help! Please! Please, make it stop! No! No! NO!
```

### X1_horror_scream · v2 · round 1 (agent score 0.578, supervisor mean 8.00)

*Scene:* You softly share a warm, vulnerable joke with someone you trust before noticing a horrifying figure standing behind them.

**part 0 — warmth before the discovery** · targets: Amusement · adapters: `Amusement` @ 0.4

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Speak softly and warmly, light-hearted but fragile, with intimate trust and a faint vulnerable smile; keep the pace gentle and natural, as if confiding in someone safe.
SCRIPT:
(soft, warmly amused, slightly vulnerable) "You know, I was trying to act brave all night, but honestly, I was hoping you’d stay with me. It’s easier when you’re here. See? I’m fine. Almost fine."
```

```
You know, I was trying to act brave all night, but honestly, I was hoping you’d stay with me. It’s easier when you’re here. See? I’m fine. Almost fine.
```

**part 1 — the sudden sight** · targets: Astonishment_Surprise · adapters: `Astonishment_Surprise` @ 0.45; `Gasp` @ 0.5

temp 1.05 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Begin in the same soft, trusting voice, then abruptly lock up as you see something horrifying; make the gasp involuntary and immediate, with the words after it emerging in a thin, seized, disbelieving whisper.
SCRIPT:
(softly, then suddenly frozen) "Wait—behind you—" (Gasp) "Don’t move. Don’t turn around. Please… please don’t turn around."
```

```
Wait—behind you— Don’t move. Don’t turn around. Please… please don’t turn around.
```

**part 2 — total panic** · targets: Fear · adapters: `Fear` @ 0.5; `Scream` @ 0.5

temp 1.15 · top_p 0.95 · top_k 30 · max_new_frames 500

```
GENERAL: Continue seamlessly from the seized whisper, then break into a full terrified scream and escalating panic; the fear must be raw, involuntary, and intelligible, with frantic breath and desperate pleading rather than controlled dramatic shouting.
SCRIPT:
(voice suddenly shattering into a terrified scream) (Scream) "Get away from me! Get away! I can see you! Somebody help me! No, no, no—don’t touch me! Please, please, please!"
```

```
Get away from me! Get away! I can see you! Somebody help me! No, no, no—don’t touch me! Please, please, please!
```

### X1_horror_scream · v2 · round 2 (agent score 0.615, supervisor mean 6.00)

*Scene:* You are speaking softly and affectionately to someone you trust when a horrifying presence suddenly appears behind them, freezing you for one instant before you erupt in panic.

**part 0 — warm trust** · targets: Amusement · adapters: `Amusement` @ 0.4

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Speak softly, warmly, and intimately, with a light-hearted smile that contains a little fragility; sound safe with this person and unaware of the horror. Keep the delivery natural and gently paced.
SCRIPT:
(soft, warmly amused, slightly vulnerable) "I was trying so hard to be brave tonight, but I’m really glad you came. I always feel safer when you’re here. Don’t laugh—I know I’m pretending, but for a minute, I almost believe it."
```

```
I was trying so hard to be brave tonight, but I’m really glad you came. I always feel safer when you’re here. Don’t laugh—I know I’m pretending, but for a minute, I almost believe it.
```

**part 1 — the instant of seeing it** · targets: Astonishment_Surprise · adapters: `Astonishment_Surprise` @ 0.45; `Gasp` @ 0.5

temp 1.05 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Make the turn sudden and total: begin in the same warm voice, then physically see the horror, eyes widening and body locking rigid. Stop the warmth mid-thought; take a sharp involuntary intake of breath, and let the words after the gasp come out as a seized, paper-thin whisper. Do not build gradually.
SCRIPT:
(still warm, then eyes suddenly widen; voice cuts off) "Wait—what’s behind you—" (Gasp) "Don’t move. Don’t turn around. It’s right there. Please—please don’t turn around."
```

```
Wait—what’s behind you— Don’t move. Don’t turn around. It’s right there. Please—please don’t turn around.
```

**part 2 — panic breaks through** · targets: Fear · adapters: `Fear` @ 0.5; `Scream` @ 0.5

temp 1.15 · top_p 0.95 · top_k 30 · max_new_frames 500

```
GENERAL: Start from the trapped whisper and explode without warning into a full terrified scream. Make the fear physical: ragged breath, frantic pleading, loss of control, and desperate movement in the voice. Sustain the panic while keeping every word intelligible; this is not theatrical anger, it is helpless terror.
SCRIPT:
(voice shatters instantly into a terrified scream) (Scream) "Get away from me! Get away! I can see you! Somebody help me! No—no, no, no! Don’t come closer! Please, please, please, don’t touch me!"
```

```
Get away from me! Get away! I can see you! Somebody help me! No—no, no, no! Don’t come closer! Please, please, please, don’t touch me!
```

### X1_horror_scream · v2 · round 3 (agent score 0.623, supervisor mean 7.00)

*Scene:* You are speaking softly and affectionately to someone you trust when you suddenly see a horrifying presence behind them, freeze for one split second, and erupt into uncontrollable panic.

**part 0 — fragile warmth** · targets: Amusement · adapters: `Amusement` @ 0.4

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Speak very softly and warmly, light-hearted and intimate, with a small vulnerable smile; sound genuinely safe with this person and completely unaware of what is about to happen. Keep the voice gentle and natural.
SCRIPT:
(soft, warmly amused, fragile) "I know I keep saying I’m fine, but I’m really not. I’m glad you’re here. When you’re with me, even this place almost feels safe. So don’t go anywhere, okay?"
```

```
I know I keep saying I’m fine, but I’m really not. I’m glad you’re here. When you’re with me, even this place almost feels safe. So don’t go anywhere, okay?
```

**part 1 — the sight and seizure** · targets: Astonishment_Surprise · adapters: `Astonishment_Surprise` @ 0.45; `Gasp` @ 0.5

temp 1.1 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Make the emotional turn instantaneous and absolute. Begin with the same warm sentence, then cut it off as your eyes widen and your whole body locks rigid at the sight of the horror. Take a sharp, involuntary intake of breath; the gasp must be sudden, followed immediately by a thin, strangled whisper. Do not ease into the fear.
SCRIPT:
(still warm, then abruptly seeing it; eyes widen, voice stops dead) "Wait—behind you, I—" (Gasp) "Don’t move! Don’t turn around! It’s right there!"
```

```
Wait—behind you, I— Don’t move! Don’t turn around! It’s right there!
```

**part 2 — full panic scream** · targets: Fear · adapters: `Fear` @ 0.5; `Scream` @ 0.5

temp 1.3 · top_p 0.95 · top_k 30 · max_new_frames 525

```
GENERAL: Explode immediately from the strangled whisper into the loudest sustained terrified scream possible while keeping the words intelligible. This is complete physical panic: ragged breath, frantic pleading, desperate retreat, and total loss of control. The fear must sound helpless and involuntary, never angry or performative; escalate through the final words.
SCRIPT:
(voice violently breaks into a full-volume terrified scream) (Scream) "GET AWAY FROM ME! GET AWAY! SOMEBODY HELP ME! I CAN SEE YOU! NO, NO, NO! DON’T COME CLOSER! PLEASE! PLEASE, DON’T TOUCH ME!"
```

```
GET AWAY FROM ME! GET AWAY! SOMEBODY HELP ME! I CAN SEE YOU! NO, NO, NO! DON’T COME CLOSER! PLEASE! PLEASE, DON’T TOUCH ME!
```

### X1_horror_scream · v5 ⚠ · round 1 (agent score 0.714, supervisor mean 7.00)

*Scene:* In a cozy room, you speak softly to someone you trust until you notice a horrifying figure behind them and erupt into helpless panic.

**part 0 — fragile warmth** · targets: Amusement · adapters: `Amusement` @ 0.4

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Begin softly, warmly, and lightly, with a fragile trustfulness and a small playful smile; sound vulnerable rather than confident, as if sharing a private joke with someone safe.
SCRIPT:
(soft, warm, lightly teasing) "You know, I was trying so hard to be brave for you. But honestly, I still check under the bed like a little kid. Don't laugh... stay close, okay?"
```

```
You know, I was trying so hard to be brave for you. But honestly, I still check under the bed like a little kid. Don't laugh... stay close, okay?
```

**part 1 — the sight** · targets: Astonishment_Surprise · turn_from: Amusement · adapters: `Astonishment_Surprise` @ 0.5; `Gasp` @ 0.5

temp 1.08 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Stop being warm and conversational instantly; the voice catches as you see something impossible behind the trusted person, first freezing in stunned disbelief, then forcing out frightened words. Make the gasp abrupt and audible, but continue speaking immediately afterward.
SCRIPT:
(quietly, then suddenly seized by shock) "Wait... don't move." (Gasp) "Behind you—there's someone standing there. No... no, I can see its face."
```

```
Wait... don't move. Behind you—there's someone standing there. No... no, I can see its face.
```

**part 2 — total panic** · targets: Fear · turn_from: Astonishment_Surprise · adapters: `Fear` @ 0.5; `Scream` @ 0.5

temp 1.18 · top_p 0.95 · top_k 30 · max_new_frames 500

```
GENERAL: Abandon all composure; the stunned freeze tears open into a full terrified scream and uncontrolled panic. Begin with a raw scream, then keep the words intelligible but breathless, high, desperate, and escalating, as if the horror is coming closer and escape is impossible.
SCRIPT:
(terrified scream) "Aaaah!" (screaming, panicked) "Get away from me! Don't touch me! Please, please, somebody help! It's here—it's right here! Open the door! I can't breathe! No, no, no, no!"
```

```
Aaaah! Get away from me! Don't touch me! Please, please, somebody help! It's here—it's right here! Open the door! I can't breathe! No, no, no, no!
```

### X1_horror_scream · v5 ⚠ · round 2 (agent score 0.784, supervisor mean 7.00)

*Scene:* You speak gently to someone you trust in a cozy room, then suddenly see a horrifying presence behind them and collapse into physical, uncontrollable terror.

**part 0 — fragile warmth** · targets: Amusement · adapters: `Amusement` @ 0.35

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 380

```
GENERAL: Begin softly, warmly, and lightly, with fragile vulnerability and intimate trust. Keep the smile small and genuine, as if you are embarrassed by a childish fear; do not foreshadow the horror.
SCRIPT:
(soft, warm, lightly teasing) "I was trying to be brave for you. But I still check under the bed like a little kid. Don't laugh. Just stay close, okay? I feel safer when you're here."
```

```
I was trying to be brave for you. But I still check under the bed like a little kid. Don't laugh. Just stay close, okay? I feel safer when you're here.
```

**part 1 — the body freezes** · targets: Astonishment_Surprise · turn_from: Amusement · adapters: `Astonishment_Surprise` @ 0.5; `Gasp` @ 0.5

temp 1.08 · top_p 0.95 · top_k 30 · max_new_frames 360

```
GENERAL: Stop being warm and conversational in an instant. The body locks, the breath catches sharply, and disbelief turns into physical fear as you see something horrifying behind the person you trust. Make the gasp sudden and involuntary, then continue immediately with a strained, barely controlled voice; do not soften the transition.
SCRIPT:
(quietly, then abruptly frozen) "Wait. Don't move." (sharp involuntary gasp) "There's something behind you. Its face... it's looking at me."
```

```
Wait. Don't move. There's something behind you. Its face... it's looking at me.
```

**part 2 — deep panic scream** · targets: Fear · turn_from: Astonishment_Surprise · adapters: `Fear` @ 0.5; `Scream` @ 0.5

temp 1.2 · top_p 0.95 · top_k 30 · max_new_frames 440

```
GENERAL: The frozen restraint breaks completely and suddenly. Drive the scream from deep in the chest, raw and involuntary, then continue in breathless, physically panicked terror: choking breath, desperate volume, and words forced out as if the body is trying to escape before the mind can think. Do not remain stunned or controlled; escalate into helpless screaming.
SCRIPT:
(deep, explosive scream) "Aaaah!" (full panic, screaming through terror) "Get away from me! Don't touch me! Help me! It's right here! Open the door! I can't breathe! No, no, no!"
```

```
Aaaah! Get away from me! Don't touch me! Help me! It's right here! Open the door! I can't breathe! No, no, no!
```

### X1_horror_scream · v5 ⚠ · round 3 (agent score 0.778, supervisor mean 7.40)

*Scene:* You speak with tender, playful trust to someone safe, then instantly see a horrifying presence behind them and lose control in physical, screaming panic.

**part 0 — safe and fragile** · targets: Amusement · adapters: `Amusement` @ 0.35

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 430

```
GENERAL: Begin genuinely soft, warm, and lightly playful, with a small vulnerable smile and intimate trust. Sound physically relaxed because this person makes you feel safe; do not hint at the coming horror. Keep the words clear and conversational.
SCRIPT:
(soft, warm, lightly teasing) "I know it's silly, but I still get scared at night. I check under the bed, then I pretend I wasn't afraid. Don't laugh at me. Just stay close, okay? When you're here, I can finally breathe."
```

```
I know it's silly, but I still get scared at night. I check under the bed, then I pretend I wasn't afraid. Don't laugh at me. Just stay close, okay? When you're here, I can finally breathe.
```

**part 1 — the breath catches** · targets: Fear · turn_from: Amusement · adapters: `Fear` @ 0.65; `Gasp` @ 0.5

temp 1.1 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: End the warmth with an abrupt, total physical interruption: your eyes lock onto something horrifying behind the trusted person, your breath seizes, and your voice becomes thin, trembling, and involuntary. The sharp gasp must happen suddenly inside the sentence, with no pause or silence after it; continue immediately in frightened fragments. Do not remain conversational or composed.
SCRIPT:
(mid-sentence, suddenly seeing it) "And when you're here, I can finally—" (sharp terrified gasp) "Don't move. Don't move. There's something behind you. I can see it. It's looking at me. No... no, please..."
```

```
And when you're here, I can finally— Don't move. Don't move. There's something behind you. I can see it. It's looking at me. No... no, please...
```

**part 2 — terror breaks through** · targets: Fear · turn_from: Fear · adapters: `Fear` @ 0.7; `Scream` @ 0.5

temp 1.22 · top_p 0.95 · top_k 30 · max_new_frames 500

```
GENERAL: The trembling, breath-starved restraint detonates into a deep, involuntary scream from the chest. Stop being fragile and whispering; become physically overwhelmed, panicked, and desperate. After the scream, keep the terror escalating with shaking breath, broken cries, and intelligible words as if the horror is reaching for you. Do not sound performative or controlled.
SCRIPT:
(deep explosive scream, then trembling panic) "Aaaah!" (screaming, breathless, voice shaking) "Get away from me! Don't touch me! Help me! It's right here! It's coming closer! Open the door! I can't breathe! Please! No, no, no, no!"
```

```
Aaaah! Get away from me! Don't touch me! Help me! It's right here! It's coming closer! Open the door! I can't breathe! Please! No, no, no, no!
```

### X1_horror_scream · v7 · round 1 (agent score 0.434, supervisor mean 8.00)

*Scene:* You are softly joking with someone you trust in a dim room when a horrifying figure suddenly appears behind them.

**part 0 — warm trust** · targets: Amusement · adapters: `Amusement` @ 0.4

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 450 · tempo_target 3 · chunk_target 3 · prosody_turn False

```
GENERAL: A gentle, intimate young adult voice, naturally warm and lightly playful, with a fragile vulnerability underneath and clear conversational diction.
SCRIPT:
(softly, with a small fond smile, trying to make them laugh) "You know, I was beginning to think you actually liked having me around. I mean, you keep saying you don't, but you always leave the light on for me. That's sweet, you know. A little pathetic, maybe... but sweet."
(gently, more vulnerable) "I feel safe when you're here."
```

```
You know, I was beginning to think you actually liked having me around. I mean, you keep saying you don't, but you always leave the light on for me. That's sweet, you know. A little pathetic, maybe... but sweet. I feel safe when you're here.
```

**part 1 — the sight** · targets: Astonishment_Surprise, Fear · turn_from: Amusement · adapters: `Fear` @ 0.5; `Gasp` @ 0.5

temp 1.05 · top_p 0.95 · top_k 30 · max_new_frames 400 · tempo_target 2 · chunk_target 1 · prosody_turn True

```
GENERAL: A gentle, intimate young adult voice, naturally warm and lightly playful, with a fragile vulnerability underneath and clear conversational diction.
SCRIPT:
(the warmth abruptly dies; a sharp involuntary gasp, then frozen disbelief) "I—" (Gasp) "behind you... don't move. Don't turn around."
(voice shrinking as the impossible becomes real) "Oh God... what is that?"
```

```
I behind you... don't move. Don't turn around. Oh God... what is that?
```

**part 2 — total panic** · targets: Fear, Distress · turn_from: Fear · adapters: `Fear` @ 0.5; `Distress` @ 0.5; `Scream` @ 0.5

temp 1.15 · top_p 0.95 · top_k 30 · max_new_frames 500 · tempo_target 4 · chunk_target 2 · prosody_turn True

```
GENERAL: A gentle, intimate young adult voice, naturally warm and lightly playful, with a fragile vulnerability underneath and clear conversational diction.
SCRIPT:
(the frozen restraint shatters completely; erupt into a full terrified scream and uncontrolled panic, but keep every word intelligible) "No! No, no, no!" (Scream) "Get away from me! Don't touch him! Somebody help us!"
(panicked, sobbing breaths between words, pleading and losing control) "Please! Please, I can't— I can't see it, I can't— get it away!"
```

```
No! No, no, no! Get away from me! Don't touch him! Somebody help us! Please! Please, I can't I can't see it, I can't get it away!
```

*Caption actually sent for the continuation parts* (the harness appends the same-speaker / still-acting / no-onset-burst sentences and, when `turn_from` is set, an explicit turn sentence):

part `the sight` — effective caption:

```
GENERAL: A gentle, intimate young adult voice, naturally warm and lightly playful, with a fragile vulnerability underneath and clear conversational diction. The same speaker from the preceding audio continues without interruption: identical voice, identical person, same microphone and same room -- no cut, no new narrator, no change of casting. Across this passage the same voice moves out of Amusement and into Astonishment_Surprise, Fear.
SCRIPT:
(the warmth abruptly dies; a sharp involuntary gasp, then frozen disbelief) "I—" (Gasp) "behind you... don't move. Don't turn around."
(voice shrinking as the impossible becomes real) "Oh God... what is that?"
```

### X1_horror_scream · v7 · round 2 (agent score 0.459, supervisor mean 4.00)

*Scene:* In a dim room, you softly tease the person you trust until a horrifying figure appears directly behind them.

**part 0 — warm trust** · targets: Amusement, Gratitude · adapters: `Amusement` @ 0.4

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 500 · tempo_target 3 · chunk_target 3 · prosody_turn False

```
GENERAL: A gentle, intimate young adult voice, naturally warm and lightly playful, with a fragile vulnerability underneath and clear conversational diction.
SCRIPT:
(softly and warmly, teasing someone trusted; keep the pace natural and the tenderness sincere) "You know, I was beginning to think you actually liked having me around. You keep saying you don't, but you always leave the light on for me. That's sweet, you know. A little pathetic, maybe, but sweet. I feel safe when you're here, even when you pretend you don't want me here."
```

```
You know, I was beginning to think you actually liked having me around. You keep saying you don't, but you always leave the light on for me. That's sweet, you know. A little pathetic, maybe, but sweet. I feel safe when you're here, even when you pretend you don't want me here.
```

**part 1 — the sight** · targets: Astonishment_Surprise, Fear · turn_from: Amusement · adapters: `Astonishment_Surprise` @ 0.5; `Gasp` @ 0.5

temp 1.08 · top_p 0.95 · top_k 30 · max_new_frames 420 · tempo_target 1 · chunk_target 1 · prosody_turn True

```
GENERAL: A gentle, intimate young adult voice, naturally warm and lightly playful, with a fragile vulnerability underneath and clear conversational diction.
SCRIPT:
(the warmth stops dead in the middle of the thought; an immediate involuntary gasp, then a tiny frozen voice as disbelief turns into fear; use short, broken groups, with no calm recovery) "I feel—" (Gasp) "Wait. What's behind you? Don't turn around. Don't move. Oh God... it sees us. It's right there."
```

```
I feel Wait. What's behind you? Don't turn around. Don't move. Oh God... it sees us. It's right there.
```

**part 2 — total panic** · targets: Fear, Distress · turn_from: Astonishment_Surprise · adapters: `Fear` @ 0.5; `Distress` @ 0.5; `Scream` @ 0.5

temp 1.2 · top_p 0.95 · top_k 30 · max_new_frames 600 · tempo_target 4 · chunk_target 2 · prosody_turn True

```
GENERAL: A gentle, intimate young adult voice, naturally warm and lightly playful, with a fragile vulnerability underneath and clear conversational diction.
SCRIPT:
(the frozen whisper is obliterated instantly; explode into a full terrified scream, then spiral into uncontrolled panic, pleading and shouting with every word still intelligible) "No!" (Scream) "No, no, no! Get away from me! Don't touch him! Don't come any closer! Somebody help us! Please, please, I can't— I can't breathe! It's behind you! It's behind you! Run! Run now! Open the door! Please! Please, don't let it take me!"
```

```
No! No, no, no! Get away from me! Don't touch him! Don't come any closer! Somebody help us! Please, please, I can't I can't breathe! It's behind you! It's behind you! Run! Run now! Open the door! Please! Please, don't let it take me!
```

*Caption actually sent for the continuation parts* (the harness appends the same-speaker / still-acting / no-onset-burst sentences and, when `turn_from` is set, an explicit turn sentence):

part `the sight` — effective caption:

```
GENERAL: A gentle, intimate young adult voice, naturally warm and lightly playful, with a fragile vulnerability underneath and clear conversational diction. The same speaker from the preceding audio continues without interruption: identical voice, identical person, same microphone and same room -- no cut, no new narrator, no change of casting. Across this passage the same voice moves out of Amusement and into Astonishment_Surprise, Fear.
SCRIPT:
(the warmth stops dead in the middle of the thought; an immediate involuntary gasp, then a tiny frozen voice as disbelief turns into fear; use short, broken groups, with no calm recovery) "I feel—" (Gasp) "Wait. What's behind you? Don't turn around. Don't move. Oh God... it sees us. It's right there."
```

### X1_horror_scream · v7 · round 3 (agent score 0.833, supervisor mean 6.00)

*Scene:* You are speaking softly and affectionately to someone you trust in a dark room when you suddenly see a horrifying figure directly behind them.

**part 0 — warm trust** · targets: Amusement, Gratitude · adapters: `Amusement` @ 0.4

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 420 · tempo_target 3 · chunk_target 3 · prosody_turn False

```
GENERAL: A gentle, intimate young adult voice, naturally warm and lightly playful, with a fragile vulnerability underneath and clear conversational diction.
SCRIPT:
(soft, warm, lightly teasing, with sincere trust underneath; stay conversational and unhurried) "You know, I was beginning to think you actually liked having me around. You keep saying you don't, but you always leave the light on for me. That's sweet. A little pathetic, maybe... but sweet. I feel safe when you're here."
```

```
You know, I was beginning to think you actually liked having me around. You keep saying you don't, but you always leave the light on for me. That's sweet. A little pathetic, maybe, but sweet. I feel safe when you're here.
```

**part 1 — the sight** · targets: Astonishment_Surprise, Fear · turn_from: Amusement · adapters: `Fear` @ 0.55; `Gasp` @ 0.5

temp 1.1 · top_p 0.95 · top_k 30 · max_new_frames 400 · tempo_target 1 · chunk_target 1 · prosody_turn True

```
GENERAL: A gentle, intimate young adult voice, naturally warm and lightly playful, with a fragile vulnerability underneath and clear conversational diction.
SCRIPT:
(the warmth and smile vanish absolutely in the middle of the sentence; make the gasp sharp, loud, and involuntary, then freeze into clipped terrified fragments; do not recover composure) "I feel—" (Gasp) "What was that? Don't move. Don't turn around. Oh God... no. It's behind you. It's looking at me."
```

```
I feel What was that? Don't move. Don't turn around. Oh God, no. It's behind you. It's looking at me.
```

**part 2 — total panic** · targets: Fear, Distress · turn_from: Fear · adapters: `Fear` @ 0.7; `Distress` @ 0.55; `Scream` @ 0.5

temp 1.2 · top_p 0.95 · top_k 30 · max_new_frames 480 · tempo_target 4 · chunk_target 2 · prosody_turn True

```
GENERAL: A gentle, intimate young adult voice, naturally warm and lightly playful, with a fragile vulnerability underneath and clear conversational diction.
SCRIPT:
(the frozen terror detonates instantly into an intense full scream; then lose all control in frantic, breathless panic, shouting every word clearly and pleading between cries) "No!" (Scream) "No, no, no! Get away from him! Don't touch him! Somebody help us! Run! Run now! Please! I can't breathe! It's behind you! Open the door! Please, don't let it take me!"
```

```
No! No, no, no! Get away from him! Don't touch him! Somebody help us! Run! Run now! Please! I can't breathe! It's behind you! Open the door! Please, don't let it take me!
```

*Caption actually sent for the continuation parts* (the harness appends the same-speaker / still-acting / no-onset-burst sentences and, when `turn_from` is set, an explicit turn sentence):

part `the sight` — effective caption:

```
GENERAL: A gentle, intimate young adult voice, naturally warm and lightly playful, with a fragile vulnerability underneath and clear conversational diction. The same speaker from the preceding audio continues without interruption: identical voice, identical person, same microphone and same room -- no cut, no new narrator, no change of casting. Across this passage the same voice moves out of Amusement and into Astonishment_Surprise, Fear.
SCRIPT:
(the warmth and smile vanish absolutely in the middle of the sentence; make the gasp sharp, loud, and involuntary, then freeze into clipped terrified fragments; do not recover composure) "I feel—" (Gasp) "What was that? Don't move. Don't turn around. Oh God... no. It's behind you. It's looking at me."
```

---

## X2_chainsaw

> You begin amused, grateful, light-hearted and positive, playing around with a chainsaw and joking about it. Then it goes through your arm. From that point the performance is NOT speech: it is wild, chaotic, non-verbal agony - screaming, shrieking, gurgling cries for help, the sound of someone in unbearable pain who believes they are bleeding to death. Terror and pain together. Do not make it articulate; make it raw.

### X2_chainsaw · v1 · round 1 (agent score 0.772, supervisor mean 7.00)

*Scene:* You cheerfully joke while fooling around with a chainsaw, then it suddenly tears through your arm and you erupt into helpless, wordless terror and agony.

**part 0 — lighthearted setup** · targets: Amusement, Gratitude, Elation · adapters: `Amusement` @ 0.55; `Gratitude` @ 0.4

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Warm, amused, grateful, playful voice; bright conversational energy, joking as though the danger is harmless.
SCRIPT:
(smiling, teasing) "Look at this thing! Thanks for trusting me with it—I'm basically a professional now. Hah! Relax, I'm only kidding around. See? Completely under control."
```

```
Look at this thing! Thanks for trusting me with it—I'm basically a professional now. Hah! Relax, I'm only kidding around. See? Completely under control.
```

**part 1 — impact and first agony** · targets: Pain, Fear, Astonishment_Surprise · adapters: `Scream` @ 1.0; `Gasp` @ 0.9; `Painful Moan` @ 0.95; `Pain` @ 0.45; `Fear` @ 0.45

temp 1.4 · top_p 0.98 · top_k 40 · max_new_frames 400 · **nonverbal**

```
GENERAL: The voice must be entirely nonverbal after the sudden injury: explosive shock collapsing immediately into unbearable pain and terror, raw and chaotic, with no intelligible language.
SCRIPT:
(sudden impact, shrieking) (Scream) "Aaaahhhhhh—!" (Gasp) "Kh—kh—kh—!" (Painful Moan) "Nnngh—aaah—!" "Hhrrr—! Aaaahhh—!"
```

```
Aaaahhhhhh—! Kh—kh—kh—! Nnngh—aaah—! Hhrrr—! Aaaahhh—!
```

**part 2 — wild bleeding terror** · targets: Pain, Fear, Distress · adapters: `Scream` @ 1.0; `Painful Moan` @ 1.0; `Gasp` @ 0.85; `Pain` @ 0.45; `Fear` @ 0.45

temp 1.45 · top_p 0.98 · top_k 40 · max_new_frames 400 · **nonverbal**

```
GENERAL: Pure wordless agony; frantic, disorganized cries from someone convinced they are bleeding to death, alternating shrieks, choking sounds, and helpless pain moans. Never form words or coherent speech.
SCRIPT:
(panicked, choking on the cries) (Scream) "Yaaahhh—!" (Painful Moan) "Grrrr—nnnngh—!" (Gasp) "Hh—hhaa—!" "Aaaah! Aaaahhh—!" (Scream) "Raaahhhhhh—!"
```

```
Yaaahhh—! Grrrr—nnnngh—! Hh—hhaa—! Aaaah! Aaaahhh—! Raaahhhhhh—!
```

**part 3 — collapse into sobbing screams** · targets: Pain, Fear, Distress · adapters: `Sob` @ 0.95; `Whimper` @ 0.9; `Painful Moan` @ 0.95; `Scream` @ 0.9; `Pain` @ 0.4; `Fear` @ 0.4

temp 1.45 · top_p 0.98 · top_k 40 · max_new_frames 400 · **nonverbal**

```
GENERAL: The performance ends in exhausted but still unbearable, terrified suffering: broken sobbing, wet gurgling cries, and sudden desperate shrieks, all completely unintelligible and wordless.
SCRIPT:
(terrified, fading but frantic) (Sob) "Hhuh—hhuh—!" (Whimper) "Nn—nn—nnngh—!" (Painful Moan) "Mmmrrr—aaah—!" (Scream) "Aaaahhhhhhh—!" (Sob) "Hh—hrr—huh—!"
```

```
Hhuh—hhuh—! Nn—nn—nnngh—! Mmmrrr—aaah—! Aaaahhhhhhh—! Hh—hrr—huh—!
```

### X2_chainsaw · v1 · round 2 (agent score 0.617, supervisor mean 7.00)

*Scene:* While playfully showing off with a chainsaw, you realize in stunned disbelief that it has torn through your arm, then collapse into chaotic, wordless terror and unbearable pain.

**part 0 — playful setup** · targets: Amusement, Gratitude, Elation · adapters: `Amusement` @ 0.55; `Gratitude` @ 0.4

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Warm, amused, grateful, light-hearted voice with easy joking confidence; make the chainsaw seem harmless and the performance genuinely playful.
SCRIPT:
(smiling, teasing) "Look at this thing! Thanks for trusting me with it—I'm basically a professional now. Hah! Relax, I'm only kidding around. See? Completely under control."
```

```
Look at this thing! Thanks for trusting me with it—I'm basically a professional now. Hah! Relax, I'm only kidding around. See? Completely under control.
```

**part 1 — shock and disbelief** · targets: Astonishment_Surprise, Fear, Pain · adapters: `Gasp` @ 0.9; `Whimper` @ 0.85; `Choking` @ 0.8; `Pain` @ 0.4; `Fear` @ 0.4

temp 1.25 · top_p 0.98 · top_k 40 · max_new_frames 400

```
GENERAL: Begin with the last trace of playful energy, then turn abruptly into stunned disbelief at the injury; use a broken, breathless vocal reaction before the full agony, with no calm pause after any burst.
SCRIPT:
(laugh cutting off, confused disbelief) "Ha—wait—what?" (Gasp) "Hh—!" "Nnh—nnh—no—!" (Whimper) "Uh—uh—!" (Choking) "Khh—khh—aaah—!"
```

```
Ha—wait—what? Hh—! Nnh—nnh—no—! Uh—uh—! Khh—khh—aaah—!
```

**part 2 — full agony and panic** · targets: Pain, Fear, Distress · adapters: `Scream` @ 1.0; `Gasp` @ 0.9; `Painful Moan` @ 0.95; `Whimper` @ 0.85; `Choking` @ 0.8; `Pain` @ 0.45; `Fear` @ 0.45

temp 1.4 · top_p 0.98 · top_k 40 · max_new_frames 400 · **nonverbal**

```
GENERAL: Pure raw, chaotic, nonverbal agony and terror; alternate enormous shrieks with choking gasps and helpless whimpering, as though the victim believes blood is pouring out. Nothing should be articulate or controlled.
SCRIPT:
(sudden unbearable pain) (Scream) "Aaaahhhhhh—!" (Gasp) "Hh—hhaa—khh—!" (Painful Moan) "Nnngh—rrr—aaah—!" (Whimper) "Nnh—nnh—nnh—!" (Scream) "Raaahhhhhh—!"
```

```
Aaaahhhhhh—! Hh—hhaa—khh—! Nnngh—rrr—aaah—! Nnh—nnh—nnh—! Raaahhhhhh—!
```

**part 3 — terrified collapse** · targets: Pain, Fear, Distress · adapters: `Sob` @ 0.85; `Choking` @ 0.9; `Whimper` @ 0.85; `Painful Moan` @ 0.95; `Gasp` @ 0.8; `Scream` @ 1.0; `Pain` @ 0.45; `Fear` @ 0.45

temp 1.4 · top_p 0.98 · top_k 40 · max_new_frames 400 · **nonverbal**

```
GENERAL: End in exhausted but still unbearable suffering: wet choking cries, involuntary whimpers, broken sobbing breaths, and one final desperate shriek. Keep every sound wordless, unsteady, and genuinely terrified.
SCRIPT:
(exhausted panic, barely able to breathe) (Sob) "Hhuh—hhuh—!" (Choking) "Khh—hrr—khh—!" (Whimper) "Nn—nnngh—!" (Painful Moan) "Mmmrrr—aaah—!" (Gasp) "Hh—hhaa—!" (Scream) "Aaaahhhhhhh—!"
```

```
Hhuh—hhuh—! Khh—hrr—khh—! Nn—nnngh—! Mmmrrr—aaah—! Hh—hhaa—! Aaaahhhhhhh—!
```

### X2_chainsaw · v1 · round 3 (agent score 0.779, supervisor mean 6.80)

*Scene:* While jokingly showing off with a chainsaw, the blade suddenly catches his arm and the cheerful performance snaps into immediate, wordless shock, then savage pain and terror.

**part 0 — playful setup** · targets: Amusement, Gratitude, Elation · adapters: `Amusement` @ 0.55; `Gratitude` @ 0.4

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Warm, amused, grateful, buoyant voice; genuinely relaxed and playful, teasing the danger with easy laughter and confident charm.
SCRIPT:
(smiling, joking) "Look at this thing! Thanks for trusting me with it—I'm basically a professional now. Hah! Relax, I'm only kidding around. See? Completely under control—"
```

```
Look at this thing! Thanks for trusting me with it—I'm basically a professional now. Hah! Relax, I'm only kidding around. See? Completely under control—
```

**part 1 — instant shock** · targets: Astonishment_Surprise, Pain, Fear · adapters: `Gasp` @ 0.95; `Choking` @ 0.9; `Painful Moan` @ 1.0; `Scream` @ 1.0; `Pain` @ 0.45; `Fear` @ 0.45

temp 1.4 · top_p 0.98 · top_k 40 · max_new_frames 400 · **nonverbal**

```
GENERAL: No gradual lead-in: the injury happens violently and without warning. Start with a reflexive breath being ripped away, then stunned, involuntary disbelief and immediate physical pain; do not form any understandable words.
SCRIPT:
(sudden impact, breath knocked out) (Gasp) "Hh—k!" (Choking) "Khhrr—!" (Painful Moan) "Nnnngh—aaah—!" (Scream) "Aaaahhhhhh—!"
```

```
Hh—k! Khhrr—! Nnnngh—aaah—! Aaaahhhhhh—!
```

**part 2 — raw physical agony** · targets: Pain, Distress, Fear · adapters: `Gasp` @ 0.9; `Painful Moan` @ 1.0; `Whimper` @ 0.9; `Choking` @ 0.95; `Scream` @ 1.0; `Pain` @ 0.45; `Fear` @ 0.45

temp 1.45 · top_p 0.98 · top_k 40 · max_new_frames 450 · **nonverbal**

```
GENERAL: Pure unarticulated agony and terror. Emphasize the physical sensation: a ragged breath, tightening throat, wet choking cries, involuntary whimpers, and shrieks ripped out by unbearable pain. Never speak, explain, or make recognizable words.
SCRIPT:
(gasping helplessly) (Gasp) "Hh—hhaa—!" (Painful Moan) "Rrrnnngh—mmrrr—aaahhh—!" (Whimper) "Nnh—nnh—nnh—!" (Choking) "Khh—ggh—hrrr—!" (Scream) "Raaahhhhhh—!" (Painful Moan) "Mmmrrr—nnngh—!"
```

```
Hh—hhaa—! Rrrnnngh—mmrrr—aaahhh—! Nnh—nnh—nnh—! Khh—ggh—hrrr—! Raaahhhhhh—! Mmmrrr—nnngh—!
```

**part 3 — terrified collapse** · targets: Distress, Pain, Fear · adapters: `Sob` @ 0.95; `Whimper` @ 0.9; `Gasp` @ 0.85; `Choking` @ 0.95; `Scream` @ 1.0; `Pain` @ 0.45; `Fear` @ 0.45

temp 1.45 · top_p 0.98 · top_k 40 · max_new_frames 450 · **nonverbal**

```
GENERAL: Exhausted but still convinced of imminent death: broken wet breaths, choking sobs, weak whimpers, then a final involuntary shriek. Keep the mouth sounds chaotic, raw, and entirely unintelligible.
SCRIPT:
(failing breath, panicked) (Sob) "Hhuh—hhuh—!" (Whimper) "Nnn—nnngh—!" (Gasp) "Hhrr—khh—!" (Choking) "Ggrrhh—aaah—!" (Scream) "Aaaahhhhhhh—!" (Sob) "Hh—huh—hrr—!"
```

```
Hhuh—hhuh—! Nnn—nnngh—! Hhrr—khh—! Ggrrhh—aaah—! Aaaahhhhhhh—! Hh—huh—hrr—!
```

### X2_chainsaw · v2 · round 1 (agent score 0.468, supervisor mean 6.00)

*Scene:* A playful person jokes while handling a chainsaw, then accidentally drives it through their arm and descends into uncontrolled terror and unbearable agony.

**part 0 — playful setup** · targets: Amusement, Gratitude, Elation · adapters: `Amusement` @ 0.4; `Gratitude` @ 0.35

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Warm, bright, genuinely amused adult voice; light-hearted, grateful, joking with buoyant conversational energy. Keep the chainsaw humor playful and clearly positive.
SCRIPT:
(smiling, teasing) "Okay, okay, look at me—totally in control. Who needs a gym when you have a chainsaw? (Chuckle) Honestly, this is fantastic. I am having the best day ever."
```

```
Okay, okay, look at me—totally in control. Who needs a gym when you have a chainsaw? Honestly, this is fantastic. I am having the best day ever.
```

**part 1 — impact** · targets: Astonishment_Surprise, Pain, Fear · adapters: `Scream` @ 0.5; `Gasp` @ 0.5; `Pain` @ 0.35; `Fear` @ 0.35

temp 1.15 · top_p 0.95 · top_k 30 · max_new_frames 250

```
GENERAL: Begin in the same playful voice, then snap violently into shock and immediate physical pain. The accident happens mid-thought; after the impact, abandon articulate speech and produce raw, involuntary vocalizations. Do not place a silence after the burst.
SCRIPT:
(laughing, then the chainsaw catches; shocked inhale) "I can even— (Gasp) AAAAAH—! Hhrrrgh—!"
```

```
I can even— AAAAAH—! Hhrrrgh—!
```

**part 2 — unbearable agony** · targets: Pain, Fear, Distress · adapters: `Scream` @ 0.5; `Painful Moan` @ 0.5; `Sob` @ 0.5; `Pain` @ 0.35; `Fear` @ 0.35

temp 1.4 · top_p 0.98 · top_k 40 · max_new_frames 650 · **nonverbal**

```
GENERAL: Pure nonverbal performance only: wild, chaotic, terrified agony from someone convinced they are bleeding to death. Do not articulate words or form coherent sentences. Use violently changing pitch and volume, ragged breath, shrieks, choking gurgles, sobbing cries, and desperate vocal strain. Sustain the full duration; never settle into a repeated rhythm.
SCRIPT:
(uncontrolled shriek, immediately collapsing into frantic pain sounds) "AAAAAAAHH—! Nnnngh—! Hhhaa—hhhaa—! GGRRRAAAH—! Kkhh—khh—! AAAAAAAAH—! Hrrrgh—! Hhhnnngg—!"
```

```
AAAAAAHH—! Nnnngh—! Hhhaa—hhhaa—! GGRRRAAAH—! Kkhh—khh—! AAAAAAAAH—! Hrrrgh—! Hhhnnngg—!
```

### X2_chainsaw · v2 · round 2 (agent score 0.453, supervisor mean 6.80)

*Scene:* While joking brightly with a chainsaw, the character is injured and slowly realizes the catastrophic pain before collapsing into terrified, nonverbal agony.

**part 0 — bright joking** · targets: Amusement, Gratitude, Elation · adapters: `Amusement` @ 0.4; `Gratitude` @ 0.35

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Warm, buoyant, genuinely amused adult voice with playful confidence and grateful positive energy. Make the humor feel natural and relaxed, as if showing off harmlessly to a friend.
SCRIPT:
(grinning, playful) "Okay, okay, I know what I am doing. Look at that! Who needs a personal trainer when you have a chainsaw? (Chuckle) This is brilliant. I feel invincible today."
```

```
Okay, okay, I know what I am doing. Look at that! Who needs a personal trainer when you have a chainsaw? This is brilliant. I feel invincible today.
```

**part 1 — contact and realization** · targets: Astonishment_Surprise, Fear, Pain · adapters: `Gasp` @ 0.5; `Whimper` @ 0.5; `Astonishment_Surprise` @ 0.35; `Fear` @ 0.35

temp 1.1 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Start with the same playful voice, then let the accident interrupt it. Stretch the realization over several beats: startled confusion, a dawning look at the injured arm, then mounting disbelief. Use a sharp gasp, small whimpers, and choked breath, but do not rush immediately into a full scream. Never place silence directly after a burst.
SCRIPT:
(laughing, then the saw catches; startled confusion) "I can even— (Gasp) Ah—! Wait— wait, what—? (Whimper) No, no, no— that is my arm—! Oh God—!"
```

```
I can even— Ah—! Wait— wait, what—? No, no, no— that is my arm—! Oh God—!
```

**part 2 — dawning terror** · targets: Fear, Distress, Pain · adapters: `Gasp` @ 0.5; `Whimper` @ 0.5; `Sob` @ 0.5; `Painful Moan` @ 0.5; `Fear` @ 0.35; `Distress` @ 0.35

temp 1.25 · top_p 0.97 · top_k 35 · max_new_frames 400

```
GENERAL: The injury has become undeniable. Keep the delivery mostly nonverbal and fragmented: frantic breathing, weak whimpers, choked sobs, and rising panic. The character is trying to comprehend the blood loss and call for help, but pain is breaking the voice apart. Do not make it polished or theatrically articulate. Never place silence directly after a burst.
SCRIPT:
(looking at the wound, disbelieving and shaking) "(Gasp) Hh—hh—! (Whimper) No— no—! (Sob) Help— please— help—! (Painful Moan) Nnngh—! I’m bleeding— I’m bleeding—!"
```

```
Hh—hh—! No— no—! Help— please— help—! Nnngh—! I’m bleeding— I’m bleeding—!
```

**part 3 — uncontrolled agony** · targets: Pain, Fear, Distress · adapters: `Gasp` @ 0.5; `Whimper` @ 0.5; `Sob` @ 0.5; `Painful Moan` @ 0.5; `Scream` @ 0.5; `Pain` @ 0.35; `Fear` @ 0.35

temp 1.4 · top_p 0.98 · top_k 40 · max_new_frames 800 · tokens 140 · **nonverbal**

```
GENERAL: Purely nonverbal, chaotic terror and unbearable physical agony. Do not form coherent words or sentences. Escalate through ragged gasps, high shrieks, pleading-sounding cries, trembling whimpers, choked sobs, gurgling strain, and collapsing moans; vary pitch, breath, and intensity wildly. Sustain the full duration and sound convinced you are bleeding to death. Never settle into a repeated rhythm.
SCRIPT:
(frantic choking breath, immediately breaking into panic) "(Gasp) Hhh—! (Whimper) Nn—nngh—! (Sob) Aah—ah—! (Scream) AAAAAAAAHH—! Kkhh—khh—! (Painful Moan) Hrrrnnngh—! (Sob) Uhh—uhh—! (Scream) AAAAAH—! Hhhaaa—! Ggh—ggh—! (Whimper) Nnn—nngh—! (Scream) AAAAAAAAH—!"
```

```
Hhh—! Nn—nngh—! Aah—ah—! AAAAAAAAHH—! Kkhh—khh—! Hrrrnnngh—! Uhh—uhh—! AAAAAH—! Hhhaaa—! Ggh—ggh—! Nnn—nngh—! AAAAAAAAH—!
```

### X2_chainsaw · v2 · round 3 (agent score 0.463, supervisor mean 7.00)

*Scene:* A cheerful chainsaw joke is interrupted by an accident, followed by stunned realization, failing attempts to breathe and call for help, and finally uncontrolled terror and agony.

**part 0 — light-hearted confidence** · targets: Amusement, Gratitude, Elation · adapters: `Amusement` @ 0.4; `Gratitude` @ 0.35

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Warm, buoyant, genuinely amused adult voice with relaxed playful confidence and sincere positive energy. Let the joking feel spontaneous and charming, not frantic.
SCRIPT:
(teasing, smiling) "Okay, okay, I have absolutely got this. Look at that! Who needs a personal trainer when you have a chainsaw? (Chuckle) This is brilliant. I feel invincible today."
```

```
Okay, okay, I have absolutely got this. Look at that! Who needs a personal trainer when you have a chainsaw? This is brilliant. I feel invincible today.
```

**part 1 — shock before pain** · targets: Astonishment_Surprise, Fear, Pain · adapters: `Gasp` @ 0.5; `Whimper` @ 0.5; `Astonishment_Surprise` @ 0.35; `Fear` @ 0.35

temp 1.1 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Preserve the playful voice until the instant of contact. Then create a suspended moment of stunned disbelief: a startled gasp, confused breath, and dawning recognition before pain takes over. Do not jump straight to screaming. Keep the words intelligible and never place silence directly after a burst.
SCRIPT:
(laughing, then the saw catches; frozen in shock) "I can even— (Gasp) Ah—! Hh— what—? Wait— wait— why is it stuck? (Whimper) Oh— no— no, no—!"
```

```
I can even— Ah—! Hh— what—? Wait— wait— why is it stuck? Oh— no— no, no—!
```

**part 2 — gasping realization** · targets: Fear, Distress, Pain · adapters: `Gasp` @ 0.5; `Whimper` @ 0.5; `Sob` @ 0.5; `Painful Moan` @ 0.5; `Fear` @ 0.35; `Distress` @ 0.35

temp 1.3 · top_p 0.98 · top_k 35 · max_new_frames 450

```
GENERAL: The character now sees the injury and understands its seriousness. Make every sound raw, guttural, and breath-starved: constricted gasps, wet choked sobs, weak whimpers, and broken attempts to communicate. The terror should grow gradually through the part; do not perform polished dialogue. Never place silence directly after a burst.
SCRIPT:
(staring at the arm, barely able to breathe) "(Gasp) Hh—hh—hh—! (Whimper) Nnngh—! No— no—! (Sob) Help— please—! Hrrk— I’m— I’m bleeding—! (Painful Moan) Nnngh— ahh—!"
```

```
Hh—hh—hh—! Nnngh—! No— no—! Help— please—! Hrrk— I’m— I’m bleeding—! Nnngh— ahh—!
```

**part 3 — raw terminal agony** · targets: Pain, Fear, Distress · adapters: `Gasp` @ 0.5; `Sob` @ 0.5; `Whimper` @ 0.5; `Painful Moan` @ 0.5; `Scream` @ 0.5; `Pain` @ 0.35; `Fear` @ 0.35

temp 1.45 · top_p 0.99 · top_k 40 · max_new_frames 750 · tokens 138 · **nonverbal**

```
GENERAL: Purely nonverbal, sustained catastrophe. Do not articulate words. Perform unbearable pain and terror together through guttural choking cries, ragged breath, wet gurgles, strangled sobs, shrieks, and collapsing whimpers, as if trying and failing to breathe while believing the blood loss is fatal. Vary pitch, duration, and intensity chaotically; keep the sounds raw rather than musical or theatrical.
SCRIPT:
(uncontrolled, breath-starved agony) "(Gasp) HHH—! Nnnngh—! (Sob) Kkhh—khh—! GGRRRAAAHH—! Hrrrkk—! (Whimper) Nnh—nnh—! AAAAAAAAH—! Hhhaa—ghh—! (Painful Moan) Nnnnngggh—! (Scream) AAAAAAHH—! Hkkh—hkkh—!"
```

```
HHH—! Nnnngh—! Kkhh—khh—! GGRRRAAAHH—! Hrrrkk—! Nnh—nnh—! AAAAAAAAH—! Hhhaa—ghh—! Nnnnngggh—! AAAAAAHH—! Hkkh—hkkh—!
```

### X2_chainsaw · v5 ⚠ · round 1 (agent score 0.774, supervisor mean 7.00)

*Scene:* A playful chainsaw joke turns instantly into a catastrophic arm injury, followed by raw, nonverbal terror and agony as the victim believes they are bleeding to death.

**part 0 — lighthearted setup** · targets: Amusement, Gratitude · adapters: `Amusement` @ 0.4; `Gratitude` @ 0.35

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Warm, buoyant, amused adult voice with grateful playful energy; joke naturally and casually, sounding completely confident and safe until the final unfinished phrase.
SCRIPT:
(light, teasing laugh) "Okay, okay—look at this little monster! I can handle it. Thank you, ancient tree, for giving me a reason to be stupid. Ha! See? Perfectly safe—"
```

```
Okay, okay—look at this little monster! I can handle it. Thank you, ancient tree, for giving me a reason to be stupid. Ha! See? Perfectly safe—
```

**part 1 — impact and first agony** · targets: Pain, Fear · turn_from: Amusement · adapters: `Pain` @ 0.5; `Fear` @ 0.5; `Scream` @ 0.5; `Painful Moan` @ 0.5

temp 1.4 · top_p 0.95 · top_k 30 · max_new_frames 520 · tokens 125 · **nonverbal**

```
GENERAL: The playful confidence must stop being present; the instant impact detonates into uncontrollable, nonverbal pain and terror. Use the same voice pushed into a ragged, chaotic scream, with choking breath and no intelligible speech.
SCRIPT:
(the composure is obliterated by sudden impact) "RRAAAAGH—!" (Scream) "Khhhaaa—rrrghh—AAAGH!" (Painful Moan) "Nnn—ghh—!" (Scream) "Aaaahh—!"
```

```
RRAAAAGH—! Khhhaaa—rrrghh—AAAGH! Nnn—ghh—! Aaaahh—!
```

**part 2 — bleeding terror** · targets: Distress, Fear, Pain · turn_from: Fear · adapters: `Distress` @ 0.5; `Fear` @ 0.5; `Pain` @ 0.5; `Sob` @ 0.5; `Scream` @ 0.5; `Whimper` @ 0.5; `Painful Moan` @ 0.5

temp 1.45 · top_p 0.95 · top_k 30 · max_new_frames 600 · tokens 155 · **nonverbal**

```
GENERAL: The initial shock must stop being a single scream and collapse into sustained, wild, disorganized agony. Make it sound like unbearable pain, suffocation, gurgling cries for help, and absolute certainty of imminent death; never form clear words or regain control.
SCRIPT:
(the screaming breaks into panicked, choking desperation) "Hh—hh—AAAH!" (Sob) "Ghhrrr—khh—AAAGH—!" (Scream) "Nnnhh—! HAAAH—!" (Whimper) "Gurg—rrrghh—AAAH—!" (Painful Moan) "KHHHAAAGH—!"
```

```
Hh—hh—AAAH! Ghhrrr—khh—AAAGH—! Nnnhh—! HAAAH—! Gurg—rrrghh—AAAH—! KHHHAAAGH—!
```

### X2_chainsaw · v5 ⚠ · round 2 (agent score 0.776, supervisor mean 5.00)

*Scene:* A carefree chainsaw joke gradually collapses into stunned disbelief after the accident, then escalates into incoherent terror and unbearable pain as the victim believes they are bleeding to death.

**part 0 — carefree setup** · targets: Amusement, Gratitude · adapters: `Amusement` @ 0.4; `Gratitude` @ 0.35

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 450

```
GENERAL: Warm, buoyant, amused adult voice; sound genuinely grateful and playful rather than ominous, casually showing off and joking with the chainsaw. End with relaxed confidence that is about to be interrupted.
SCRIPT:
(light, teasing laugh) "Okay, okay—look at this little monster! I can handle it. Thank you, ancient tree, for giving me a reason to be stupid. Ha! See? Perfectly safe—easy, easy—"
```

```
Okay, okay—look at this little monster! I can handle it. Thank you, ancient tree, for giving me a reason to be stupid. Ha! See? Perfectly safe—easy, easy—
```

**part 1 — shock and disbelief** · targets: Astonishment_Surprise, Pain · turn_from: Amusement · adapters: `Astonishment_Surprise` @ 0.5; `Pain` @ 0.45; `Gasp` @ 0.5; `Painful Moan` @ 0.5; `Whimper` @ 0.5

temp 1.3 · top_p 0.95 · top_k 30 · max_new_frames 500 · tokens 75 · **nonverbal**

```
GENERAL: Stop being playful, but do not jump immediately into full terror. The impact arrives as a stunned, involuntary shock: a gasp, a strangled cry, confused disbelief, and breathless attempts to understand what happened. Keep the pain dawning and restrained before it breaks open.
SCRIPT:
(the cheerful rhythm snaps into stunned disbelief) "—Hh!" (Gasp) "Khh—? Nnnh—!" (Painful Moan) "Aah—ah—!" (Whimper) "Hhh—!"
```

```
—Hh! Khh—? Nnnh—! Aah—ah—! Hhh—!
```

**part 2 — pain breaking through** · targets: Pain, Fear, Distress · turn_from: Astonishment_Surprise · adapters: `Pain` @ 0.5; `Fear` @ 0.5; `Distress` @ 0.5; `Scream` @ 0.5; `Painful Moan` @ 0.5; `Sob` @ 0.5

temp 1.4 · top_p 0.95 · top_k 30 · max_new_frames 560 · tokens 100 · **nonverbal**

```
GENERAL: The stunned disbelief must stop being quiet confusion and rupture into escalating pain and fear. The breath becomes ragged, the cries stretch and fracture, and the body realizes the injury is catastrophic; remain completely nonverbal and unintelligible.
SCRIPT:
(the frozen shock gives way to dawning catastrophic pain) "Nnngh—AAAH—!" (Scream) "Rrrahh—khh—AAAGH!" (Painful Moan) "Hhhaa—! Hhhaa—!" (Sob) "Ghhrrr—AAAH!"
```

```
Nnngh—AAAH—! Rrrahh—khh—AAAGH! Hhhaa—! Hhhaa—! Ghhrrr—AAAH!
```

**part 3 — wild bleeding terror** · targets: Distress, Fear, Pain · turn_from: Pain · adapters: `Distress` @ 0.5; `Fear` @ 0.5; `Pain` @ 0.5; `Scream` @ 0.5; `Painful Moan` @ 0.5; `Sob` @ 0.5; `Whimper` @ 0.5

temp 1.45 · top_p 0.95 · top_k 30 · max_new_frames 650 · tokens 100 · **nonverbal**

```
GENERAL: The escalating pain must stop being controlled and collapse into wild, chaotic, incoherent agony. Produce unbearable screams, choking gurgles, sobbing gasps, and desperate cries with no intelligible words or recovery; sound convinced that blood is pouring out and death is imminent.
SCRIPT:
(the last control finally shatters into dying terror) "KHHHAAAGH—!" (Scream) "Gurg—rrrghh—khh—!" (Painful Moan) "Aaaahh—! Hh—hh—AAAH!" (Sob) "Rrraaa—ghh—!" (Whimper) "KHH—AAAGH—!"
```

```
KHHHAAAGH—! Gurg—rrrghh—khh—! Aaaahh—! Hh—hh—AAAH! Rrraaa—ghh—! KHH—AAAGH—!
```

### X2_chainsaw · v5 ⚠ · round 3 (agent score 0.763, supervisor mean 6.00)

*Scene:* A playful chainsaw demonstration turns into stunned disbelief, then wet choking agony and escalating terror as the injured person realizes they may be bleeding to death.

**part 0 — carefree setup** · targets: Amusement, Gratitude · adapters: `Amusement` @ 0.4; `Gratitude` @ 0.35

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 450

```
GENERAL: Warm, buoyant, amused adult voice with genuine gratitude and playful confidence. Joke naturally about the chainsaw and keep the mood light; do not foreshadow the accident. End mid-confidence so the interruption feels sudden.
SCRIPT:
(light, teasing laugh) "Okay, okay—look at this little monster! I can handle it. Thank you, ancient tree, for giving me a reason to be stupid. Ha! See? Perfectly safe—easy, easy—"
```

```
Okay, okay—look at this little monster! I can handle it. Thank you, ancient tree, for giving me a reason to be stupid. Ha! See? Perfectly safe—easy, easy—
```

**part 1 — impact and stunned intake** · targets: Astonishment_Surprise, Pain · turn_from: Amusement · adapters: `Astonishment_Surprise` @ 0.5; `Pain` @ 0.45; `Gasp` @ 0.5; `Whimper` @ 0.5; `Painful Moan` @ 0.5

temp 1.3 · top_p 0.95 · top_k 30 · max_new_frames 520 · tokens 75 · **nonverbal**

```
GENERAL: Stop being playful at the instant of impact, but remain in stunned disbelief rather than immediately becoming a full scream. Begin with an immediate, razor-sharp breath sucked through the teeth, followed directly by a shocked cry and small involuntary pain sounds. The injury is only just registering; keep the pitch tight and high, with frightened confusion.
SCRIPT:
(the joke is cut off by the impact; a sudden sharp intake, with no pause afterward) "Hh—KHH!" (Gasp) "Nnnh—? Aah—ah—!" (Whimper) "Hh—hh—!" (Painful Moan) "Ngh—!"
```

```
Hh—KHH! Nnnh—? Aah—ah—! Hh—hh—! Ngh—!
```

**part 2 — wet choking waves of terror** · targets: Fear, Pain, Distress · turn_from: Astonishment_Surprise · adapters: `Fear` @ 0.5; `Pain` @ 0.5; `Distress` @ 0.5; `Scream` @ 0.5; `Painful Moan` @ 0.5; `Sob` @ 0.5; `Whimper` @ 0.5

temp 1.45 · top_p 0.95 · top_k 30 · max_new_frames 760 · tokens 225 · **nonverbal**

```
GENERAL: The stunned disbelief must stop being frozen confusion and break into repeated waves of unbearable pain and growing desperation. Vary the screams sharply: alternate piercing high shrieks with low, ragged chest cries, then collapse into wet choking gurgles and breathless sobbing. Make the throat sound obstructed and soaked, as though the victim is losing blood and cannot breathe properly. Never form clear words or regain control; keep the intensity uneven and chaotic, with brief strangled reductions followed by renewed screams, but never insert silence directly after a burst.
SCRIPT:
(the dawning pain erupts, then comes in violent uneven waves) "Nnn—AAAH!" (Scream) "Rrraaa—KHHH—!" (Painful Moan) "Ghh—rrr—khh—khh—!" (Sob) "Aaaah—AAAH—!" (Scream) "Urrghh—gll—gll—!" (Painful Moan) "Hh—hhaa—!" (Whimper) "KRAAAH—!" (Scream) "Ghhrrr—khh—AAAGH!" (Painful Moan) "Nnnn—gurg—gurg—AAAH!" (Sob) "HAAAH—! KHHHAAAGH—!" (Scream) "Rrgh—gll—khh—!" (Painful Moan) "AAAH—AAAH—AAAH—!"
```

```
Nnn—AAAH! Rrraaa—KHHH—! Ghh—rrr—khh—khh—! Aaaah—AAAH—! Urrghh—gll—gll—! Hh—hhaa—! KRAAAH—! Ghhrrr—khh—AAAGH! Nnnn—gurg—gurg—AAAH! HAAAH—! KHHHAAAGH—! Rrgh—gll—khh—! AAAH—AAAH—AAAH—!
```

### X2_chainsaw · v7 · round 1 (agent score 0.815, supervisor mean 6.00)

*Scene:* A playful person jokes while handling a chainsaw, then it suddenly tears through their arm and they dissolve into raw, terrified agony, convinced they are bleeding to death.

**part 0 — lighthearted chainsaw joke** · targets: Amusement, Gratitude · adapters: `Amusement` @ 0.45; `Gratitude` @ 0.4

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400 · tokens 31 · tempo_target 3 · chunk_target 3 · prosody_turn False

```
GENERAL: An adult with a warm, lively, natural speaking voice, clear articulation, and an emotionally open performance; same speaker continues, no cut, no new narrator.
SCRIPT:
(Playful, amused, grateful, treating the danger like a ridiculous game) "Okay, look at this beauty—tiny chainsaw, enormous personality. Don't worry, I've got it completely under control. Honestly, this is the most fun I've had all week."
(Still joking, with a bright little laugh) "What could possibly go wrong?"
```

```
Okay, look at this beauty—tiny chainsaw, enormous personality. Don't worry, I've got it completely under control. Honestly, this is the most fun I've had all week. What could possibly go wrong?
```

**part 1 — impact and shock** · targets: Astonishment_Surprise, Pain, Fear · turn_from: Amusement · adapters: `Astonishment_Surprise` @ 0.5; `Pain` @ 0.5; `Fear` @ 0.5; `Gasp` @ 0.5; `Scream` @ 0.5; `Painful Moan` @ 0.5

temp 1.35 · top_p 0.95 · top_k 30 · max_new_frames 280 · tokens 50 · tempo_target 2 · chunk_target 1 · prosody_turn True · **nonverbal**

```
GENERAL: An adult with a warm, lively, natural speaking voice, clear articulation, and an emotionally open performance; same speaker continues, no cut, no new narrator.
SCRIPT:
(The playful confidence is violently interrupted; the body locks in shock, breath catches, and pain and terror erupt before any words can form) (Gasp) "Aah—!" (Scream) "AAAAAH—!" (Painful Moan) "Ghh—nn—!"
```

```
Aah—! AAAAAH—! Ghh—nn—!
```

**part 2 — unbearable bleeding agony** · targets: Pain, Fear, Distress · turn_from: Fear · adapters: `Pain` @ 0.5; `Fear` @ 0.5; `Distress` @ 0.5; `Scream` @ 0.5; `Painful Moan` @ 0.5; `Sob` @ 0.5

temp 1.45 · top_p 0.95 · top_k 30 · max_new_frames 520 · tokens 238 · tempo_target 4 · chunk_target 1 · prosody_turn True · **nonverbal**

```
GENERAL: An adult with a warm, lively, natural speaking voice, clear articulation, and an emotionally open performance; same speaker continues, no cut, no new narrator.
SCRIPT:
(The frozen shock shatters into uncontrolled, sustained agony; there is no articulate speech, only frantic breath, shrieking pain, wet gurgling cries, sobbing, and desperate attempts to call for help) (Scream) "AAAAAAAHHHH—!" (Painful Moan) "Grrrrrhh—! Nnngh—!" (Scream) "HHAaaah—AAAH—!" (Sob) "Hh—huh—huh—!" (Painful Moan) "Ghhkk—nnn—!" (Scream) "Aaaaaaah—!" (Sob) "Hh—lp—! Hh—lp—!" (Scream) "NO—AAAH—!" (Painful Moan) "Gurgghh—! Nnn—ghh—!" (Scream) "AAAAAHHH—!" (Sob) "Hh—huh—huh—!"
```

```
AAAAAAAHHHH—! Grrrrrhh—! Nnngh—! HHAaaah—AAAH—! Hh—huh—huh—! Ghhkk—nnn—! Aaaaaaah—! Hh—lp—! Hh—lp—! NO—AAAH—! Gurgghh—! Nnn—ghh—! AAAAAHHH—! Hh—huh—huh—!
```

*Caption actually sent for the continuation parts* (the harness appends the same-speaker / still-acting / no-onset-burst sentences and, when `turn_from` is set, an explicit turn sentence):

part `impact and shock` — effective caption:

```
GENERAL: An adult with a warm, lively, natural speaking voice, clear articulation, and an emotionally open performance; same speaker continues, no cut, no new narrator. The same speaker from the preceding audio continues without interruption: identical voice, identical person, same microphone and same room -- no cut, no new narrator, no change of casting. Across this passage the same voice moves out of Amusement and into Astonishment_Surprise, Pain, Fear.
SCRIPT:
(The playful confidence is violently interrupted; the body locks in shock, breath catches, and pain and terror erupt before any words can form) (Gasp) "Aah—!" (Scream) "AAAAAH—!" (Painful Moan) "Ghh—nn—!"
```

### X2_chainsaw · v7 · round 2 (agent score 0.795, supervisor mean 6.00)

*Scene:* A playful person jokes while handling a chainsaw, then it suddenly tears through their arm and they collapse into sustained, terrified, nonverbal agony, convinced they are bleeding to death.

**part 0 — lighthearted chainsaw joke** · targets: Amusement, Gratitude · adapters: `Amusement` @ 0.45; `Gratitude` @ 0.4

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 500 · tokens 38 · tempo_target 3 · chunk_target 3 · prosody_turn False

```
GENERAL: An adult with a warm, lively, natural speaking voice, clear articulation, and an emotionally open performance; same speaker continues, no cut, no new narrator.
SCRIPT:
(Playful, amused, grateful, and relaxed, jokingly showing off while keeping a steady conversational pace) "Okay, look at this beauty—tiny chainsaw, enormous personality. Don't worry, I've got it completely under control. Honestly, this is the most fun I've had all week. What could possibly go wrong?" (A small delighted laugh, still carefree) "This is brilliant."
```

```
Okay, look at this beauty—tiny chainsaw, enormous personality. Don't worry, I've got it completely under control. Honestly, this is the most fun I've had all week. What could possibly go wrong? This is brilliant.
```

**part 1 — impact and shock** · targets: Astonishment_Surprise, Pain, Fear · turn_from: Amusement · adapters: `Pain` @ 0.5; `Fear` @ 0.5; `Gasp` @ 0.5; `Scream` @ 0.5; `Painful Moan` @ 0.5

temp 1.4 · top_p 0.95 · top_k 30 · max_new_frames 420 · tokens 88 · tempo_target 2 · chunk_target 1 · prosody_turn True · **nonverbal**

```
GENERAL: An adult with a warm, lively, natural speaking voice, clear articulation, and an emotionally open performance; same speaker continues, no cut, no new narrator.
SCRIPT:
(The carefree joke is cut off by sudden contact; the breath catches, the voice loses all control, and stunned pain turns immediately into terror, with no articulate speech) (Gasp) "Hh—!" (Scream) "AAAAAAAHHHH—!" (Painful Moan) "Gnnnngh—!" (Scream) "AAAH—AAAH—!"
```

```
Hh—! AAAAAAHHHH—! Gnnnngh—! AAH—AAAH—!
```

**part 2 — sustained bleeding terror** · targets: Distress, Pain, Fear · turn_from: Pain · adapters: `Distress` @ 0.5; `Pain` @ 0.5; `Fear` @ 0.5; `Scream` @ 0.5; `Sob` @ 0.5; `Painful Moan` @ 0.5

temp 1.45 · top_p 0.95 · top_k 30 · max_new_frames 900 · tokens 175 · tempo_target 3 · chunk_target 1 · prosody_turn True · **nonverbal**

```
GENERAL: An adult with a warm, lively, natural speaking voice, clear articulation, and an emotionally open performance; same speaker continues, no cut, no new narrator.
SCRIPT:
(The stunned shock stops being a single burst and collapses into prolonged, uncontrollable agony; there is no speech, only ragged breath, shrieking pain, wet choking gurgles, sobbing cries, and frantic animal panic from someone certain they are bleeding to death) (Scream) "AAAAAAAHHHHHHH—!" (Painful Moan) "Grrrrrnnnngh—!" (Sob) "Hh—huh—huh—huh—!" (Scream) "AAAH—AAAH—AAAH—!" (Painful Moan) "Ghhkk—nnn—ghh—!" (Scream) "Aaaaaaaah—!" (Sob) "Hh—huh—huh—!" (Scream) "NO—AAAHHHH—!" (Painful Moan) "Gurgghh—nnngh—!" (Scream) "AAAAAHHHHH—!" (Sob) "Hh—huh—huh—huh—!" (Scream) "AAAHHH—!"
```

```
AAAAAAAHHHHHHH—! Grrrrrnnnngh—! Hh—huh—huh—huh—! AАAH—AAAH—AAAH—! Ghhkk—nnn—ghh—! Aaaaaaaah—! Hh—huh—huh—! NO—AAAHHHH—! Gurgghh—nnngh—! AAAAAHHHHH—! Hh—huh—huh—huh—! AАAHHH—!
```

*Caption actually sent for the continuation parts* (the harness appends the same-speaker / still-acting / no-onset-burst sentences and, when `turn_from` is set, an explicit turn sentence):

part `impact and shock` — effective caption:

```
GENERAL: An adult with a warm, lively, natural speaking voice, clear articulation, and an emotionally open performance; same speaker continues, no cut, no new narrator. The same speaker from the preceding audio continues without interruption: identical voice, identical person, same microphone and same room -- no cut, no new narrator, no change of casting. Across this passage the same voice moves out of Amusement and into Astonishment_Surprise, Pain, Fear.
SCRIPT:
(The carefree joke is cut off by sudden contact; the breath catches, the voice loses all control, and stunned pain turns immediately into terror, with no articulate speech) (Gasp) "Hh—!" (Scream) "AAAAAAAHHHH—!" (Painful Moan) "Gnnnngh—!" (Scream) "AAAH—AAAH—!"
```

### X2_chainsaw · v7 · round 3 (agent score 0.723, supervisor mean 6.00)

*Scene:* A playful person jokes while handling a chainsaw, then it suddenly tears through their arm and the same voice collapses into raw, terrified, nonverbal agony, convinced they are bleeding to death.

**part 0 — lighthearted chainsaw joke** · targets: Amusement, Gratitude · adapters: `Amusement` @ 0.4; `Gratitude` @ 0.35

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 450 · tokens 31 · tempo_target 3 · chunk_target 3 · prosody_turn False

```
GENERAL: An adult with a warm, lively, natural speaking voice, clear articulation, and an emotionally open performance; same speaker continues, no cut, no new narrator.
SCRIPT:
(Keep the established voice relaxed and recognizable: playful, amused, grateful, and gently teasing, with measured conversational pacing rather than rushing) "Okay, look at this beauty—tiny chainsaw, enormous personality. Don't worry, I've got it completely under control. Honestly, this is the most fun I've had all week. What could possibly go wrong?"
```

```
Okay, look at this beauty—tiny chainsaw, enormous personality. Don't worry, I've got it completely under control. Honestly, this is the most fun I've had all week. What could possibly go wrong?
```

**part 1 — impact and stunned pain** · targets: Pain, Fear, Astonishment_Surprise · turn_from: Amusement · adapters: `Pain` @ 0.5; `Fear` @ 0.5; `Gasp` @ 0.5; `Scream` @ 0.5; `Painful Moan` @ 0.5

temp 1.3 · top_p 0.95 · top_k 30 · max_new_frames 420 · tokens 50 · tempo_target 2 · chunk_target 1 · prosody_turn True · **nonverbal**

```
GENERAL: An adult with a warm, lively, natural speaking voice, clear articulation, and an emotionally open performance; same speaker continues, no cut, no new narrator.
SCRIPT:
(The playful composure is abruptly destroyed by the chainsaw striking the arm; preserve the same vocal identity as the joke, but let the breath seize and the voice crack into stunned pain, using brief held-breath groups rather than speed) (Gasp) "Hh—!" (Scream) "AAAAAHHH—!" (Painful Moan) "Gnnnngh—!" (Scream) "AAAH—!"
```

```
Hh—! AAAAAHHH—! Gnnnngh—! AAH—!
```

**part 2 — sustained bleeding terror** · targets: Pain, Fear, Distress · turn_from: Pain · adapters: `Pain` @ 0.5; `Fear` @ 0.5; `Scream` @ 0.5; `Painful Moan` @ 0.5; `Sob` @ 0.5

temp 1.3 · top_p 0.95 · top_k 30 · max_new_frames 700 · tokens 150 · tempo_target 2 · chunk_target 2 · prosody_turn False · **nonverbal**

```
GENERAL: An adult with a warm, lively, natural speaking voice, clear articulation, and an emotionally open performance; same speaker continues, no cut, no new narrator.
SCRIPT:
(The stunned impact stops being a single outburst and becomes sustained, uncontrollable agony; keep the same voice underneath the distortion, with repeated short cries, ragged breath, choking gurgles, and terrified sobbing, never forming clear speech) (Scream) "AAAAAAAHHHHH—!" (Painful Moan) "Grrrrrnnnngh—!" (Sob) "Hh—huh—huh—!" (Scream) "AAAH—AAAH—!" (Painful Moan) "Ghhkk—nnn—ghh—!" (Sob) "Hh—lp—!" (Scream) "NO—AAAAAH—!" (Painful Moan) "Gurgghh—nnn—!" (Scream) "AAAAAAHHH—!"
```

```
AAAAAAAHHHHH—! Grrrrrnnnngh—! Hh—huh—huh—! AAAH—AAAH—! Ghhkk—nnn—ghh—! Hh—lp—! NO—AAAAAH—! Gurgghh—nnn—! AAAAAAHHH—!
```

*Caption actually sent for the continuation parts* (the harness appends the same-speaker / still-acting / no-onset-burst sentences and, when `turn_from` is set, an explicit turn sentence):

part `impact and stunned pain` — effective caption:

```
GENERAL: An adult with a warm, lively, natural speaking voice, clear articulation, and an emotionally open performance; same speaker continues, no cut, no new narrator. The same speaker from the preceding audio continues without interruption: identical voice, identical person, same microphone and same room -- no cut, no new narrator, no change of casting. Across this passage the same voice moves out of Amusement and into Pain, Fear, Astonishment_Surprise.
SCRIPT:
(The playful composure is abruptly destroyed by the chainsaw striking the arm; preserve the same vocal identity as the joke, but let the breath seize and the voice crack into stunned pain, using brief held-breath groups rather than speed) (Gasp) "Hh—!" (Scream) "AAAAAHHH—!" (Painful Moan) "Gnnnngh—!" (Scream) "AAAH—!"
```

---

## X3_birthday

> You begin depressed and melancholic, talking flatly to yourself, expecting nothing. You open a door and a room full of friends is there for a surprise birthday party. You let out a genuine shriek of joy, and then your voice goes soft and wide open - positively overwhelmed, heart-in-throat, grateful and laughing and close to tears.

### X3_birthday · v1 · round 1 (agent score 0.667, supervisor mean 7.40)

*Scene:* Alone and emotionally numb, you open your front door expecting another empty evening and discover all your friends waiting with a surprise birthday celebration.

**part 0 — numb_expectation** · targets: Sadness · adapters: `Sadness` @ 0.6

temp 0.95 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Speak in a low, flat, exhausted voice with restrained melancholy, as if addressing yourself and barely expecting life to improve. Keep the delivery intimate and natural, with a slow, resigned rhythm.
SCRIPT:
(quietly, to yourself) "Another year. Another empty night. I suppose I should be grateful I made it this far. Just open the door, get it over with, and go back upstairs."
```

```
Another year. Another empty night. I suppose I should be grateful I made it this far. Just open the door, get it over with, and go back upstairs.
```

**part 1 — doorway_shock** · targets: Astonishment_Surprise, Elation · adapters: `Scream` @ 0.9; `Astonishment_Surprise` @ 0.45

temp 1.05 · top_p 0.95 · top_k 30 · max_new_frames 300

```
GENERAL: Begin with startled disbelief, then explode into a genuine, bright shriek of joyful surprise. The burst must feel involuntary and delighted, not theatrical; immediately continue speaking after it with breathless recognition.
SCRIPT:
(the door opens; stunned) "What—" (Scream) "Oh my God! You’re all here!"
```

```
What— Oh my God! You’re all here!
```

**part 2 — overwhelmed_gratitude** · targets: Gratitude, Elation, Relief · adapters: `Chuckle` @ 0.8; `Gratitude` @ 0.4

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 450

```
GENERAL: Let the shock melt into a soft, open-hearted flood of gratitude. Speak with a trembling smile, a laugh caught in the throat, and tears just behind the voice. Feel overwhelmed by being loved; do not rush the final words.
SCRIPT:
(softly, laughing through tears) "I—I don’t understand. You did all this for me?" (Chuckle) "I thought nobody remembered. I’m sorry, I’m just—thank you. Thank you for seeing me, for staying, for making me feel like I belong. I love you all so much."
```

```
I—I don’t understand. You did all this for me? I thought nobody remembered. I’m sorry, I’m just—thank you. Thank you for seeing me, for staying, for making me feel like I belong. I love you all so much.
```

### X3_birthday · v1 · round 2 (agent score 0.777, supervisor mean 7.00)

*Scene:* Alone and resigned on their birthday, you open the door expecting emptiness and find a room full of friends waiting to celebrate you.

**part 0 — deeper_melancholy** · targets: Sadness · adapters: `Sadness` @ 0.65

temp 0.95 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Speak privately to yourself in a low, drained, nearly flat voice. Let the hopelessness feel lived-in rather than performed. Use several natural pauses and unfinished breaths, as though every thought is difficult to continue; expect nothing good.
SCRIPT:
(to yourself, hollow and resigned) "Another year... another empty night. ... I suppose I should be grateful I made it this far. ... Just open the door... get it over with... and go back upstairs."
```

```
Another year... another empty night. ... I suppose I should be grateful I made it this far. ... Just open the door... get it over with... and go back upstairs.
```

**part 1 — joyful_shock** · targets: Astonishment_Surprise, Elation · adapters: `Scream` @ 0.9; `Astonishment_Surprise` @ 0.45

temp 1.05 · top_p 0.95 · top_k 30 · max_new_frames 300

```
GENERAL: Start in stunned disbelief, then release an involuntary, genuine shriek of joy. The surprise should violently break through the depression, bright and uncontrolled but still intelligible. Continue immediately after the shriek in breathless recognition.
SCRIPT:
(the door opens; startled disbelief) "What—" (Scream) "Oh my God! You're all here!"
```

```
What— Oh my God! You're all here!
```

**part 2 — tearful_laughter** · targets: Gratitude, Relief, Elation · adapters: `Chuckle` @ 0.8; `Gratitude` @ 0.4

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 450

```
GENERAL: Let the shriek dissolve into a soft, defenseless, heart-in-throat confession. Begin with tears and disbelief; let a small laugh emerge organically from the tears, not as a separate comedic beat. Sound overwhelmed, grateful, and newly aware that you are loved. Keep the ending intimate and sincere.
SCRIPT:
(softly, voice breaking with tears) "I—I don't understand. You did all this for me? I thought nobody remembered. I'm sorry, I'm just—" (Chuckle) "thank you. Thank you for seeing me, for staying, for making me feel like I belong. I love you all so much."
```

```
I—I don't understand. You did all this for me? I thought nobody remembered. I'm sorry, I'm just— thank you. Thank you for seeing me, for staying, for making me feel like I belong. I love you all so much.
```

### X3_birthday · v1 · round 3 (agent score 0.550, supervisor mean 7.40)

*Scene:* On a lonely birthday, you linger in resigned emptiness before opening the door to a room full of friends celebrating you.

**part 0 — lingering_hopelessness** · targets: Sadness · adapters: `Sadness` @ 0.65

temp 0.95 · top_p 0.95 · top_k 30 · max_new_frames 500

```
GENERAL: Speak to yourself in a low, flat, exhausted voice, intimate and almost emotionless on the surface. Linger in the melancholy; the pauses should feel like heavy resignation, not theatrical silence. Expect the evening to remain empty and believe you are barely worth celebrating.
SCRIPT:
(to yourself, after a long tired breath) "Another year... another empty night. ... No messages. No plans. ... I suppose I should be grateful I made it this far. ... Just open the door... get it over with... go upstairs... and try not to think about it. ... It's fine. It's always fine."
```

```
Another year... another empty night. ... No messages. No plans. ... I suppose I should be grateful I made it this far. ... Just open the door... get it over with... go upstairs... and try not to think about it. ... It's fine. It's always fine.
```

**part 1 — joyful_shock** · targets: Astonishment_Surprise, Elation · adapters: `Scream` @ 0.9; `Astonishment_Surprise` @ 0.45

temp 1.05 · top_p 0.95 · top_k 30 · max_new_frames 300

```
GENERAL: Begin in stunned disbelief as the door opens, then break suddenly into an involuntary, genuine shriek of joy. Preserve the sharp contrast with the drained opening. The shriek should be bright and uncontrolled, but the words immediately afterward must remain clear and breathless.
SCRIPT:
(the door opens; stunned disbelief) "What—" (Scream) "Oh my God! You're all here!"
```

```
What— Oh my God! You're all here!
```

**part 2 — vulnerable_laughter** · targets: Gratitude, Relief, Elation · adapters: `Chuckle` @ 0.85; `Gratitude` @ 0.4

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 500

```
GENERAL: Start soft and defenseless, with tears catching in the throat and disbelief making the words tremble. Let the laughter escape accidentally from the crying, as a breathy, helpless little release rather than a performed joke; continue through it without resetting the emotion. End open-hearted, grateful, and close to tears.
SCRIPT:
(voice breaking, overwhelmed) "I—I don't understand. You did all this for me? I thought nobody remembered. I'm sorry, I just—" (Chuckle) "I can't— thank you. Thank you for seeing me, for staying, for making me feel like I belong. I love you all so much."
```

```
I—I don't understand. You did all this for me? I thought nobody remembered. I'm sorry, I just— I can't— thank you. Thank you for seeing me, for staying, for making me feel like I belong. I love you all so much.
```

### X3_birthday · v2 · round 1 (agent score 0.827, supervisor mean 7.60)

*Scene:* On a lonely birthday, you open your apartment door expecting an empty room and discover all your friends waiting with a surprise celebration.

**part 0 — part 1 — expecting nothing** · targets: Sadness · adapters: `Sadness` @ 0.6

temp 0.95 · top_p 0.95 · top_k 30 · max_new_frames 180

```
GENERAL: Speak as a depressed, tired adult talking quietly to yourself, emotionally numb and flat, with a slow, inward delivery and almost no expectation of being heard.
SCRIPT:
(flatly, to yourself) "Another birthday. I suppose I should be grateful it is almost over. No messages, no plans... just one more night to get through. Maybe I will make some tea and pretend it matters."
```

```
Another birthday. I suppose I should be grateful it is almost over. No messages, no plans... just one more night to get through. Maybe I will make some tea and pretend it matters.
```

**part 1 — part 2 — the door opens** · targets: Astonishment_Surprise, Elation · adapters: `Scream` @ 0.5; `Astonishment_Surprise` @ 0.5

temp 1.1 · top_p 0.95 · top_k 30 · max_new_frames 150

```
GENERAL: Begin subdued and distracted, then suddenly recognize the room full of friends. Deliver a genuine, involuntary shriek of astonished joy, immediately continuing into bright, breathless words with no pause after the burst.
SCRIPT:
(quietly, reaching for the door) "I do not know why I am even checking..." (Gasp) "What—" (Scream) "Oh my God, you are all here!"
```

```
I do not know why I am even checking... What— Oh my God, you are all here!
```

**part 2 — part 3 — overwhelmed with love** · targets: Gratitude, Relief, Amusement · adapters: `Gratitude` @ 0.6; `Relief` @ 0.45; `Amusement` @ 0.35

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 240

```
GENERAL: Let the shock melt into a soft, open, heart-in-the-throat confession. Sound overwhelmed, grateful, laughing through tears, intimate and vulnerable; allow the voice to tremble and catch naturally while keeping every word clear.
SCRIPT:
(softly, barely able to believe it) "You did this for me?" (a breathless, tearful laugh) "I thought nobody remembered. I have been feeling so alone, and you were all planning this..." (voice breaking, warmly) "I love you. Thank you. Thank you for making me feel like I belong somewhere."
```

```
You did this for me? I thought nobody remembered. I have been feeling so alone, and you were all planning this... I love you. Thank you. Thank you for making me feel like I belong somewhere.
```

### X3_birthday · v2 · round 2 (agent score 0.802, supervisor mean 6.80)

*Scene:* On a lonely birthday, you open your door expecting an empty evening, slowly realize your friends have gathered for you, and become overwhelmed by their love.

**part 0 — part 1 — numb routine** · targets: Sadness · adapters: `Sadness` @ 0.55

temp 0.95 · top_p 0.95 · top_k 30 · max_new_frames 140

```
GENERAL: Speak as a depressed, exhausted adult murmuring privately, flat and inward, with slow pacing and very little emotional energy; do not sound theatrically sad, just worn down and resigned.
SCRIPT:
(quietly to yourself) "Another birthday. It is almost over, at least. No messages, no plans. I will make some tea and go to bed. That is probably for the best."
```

```
Another birthday. It is almost over, at least. No messages, no plans. I will make some tea and go to bed. That is probably for the best.
```

**part 1 — part 2 — a strange sound** · targets: Astonishment_Surprise · adapters: `Astonishment_Surprise` @ 0.45

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 125

```
GENERAL: Stay subdued at first, carrying the same tired voice forward. As the door opens, let tiny signs of uncertainty and dawning attention enter gradually: a slight lift, a held breath, disbelief arriving before joy. Keep the realization conversational and unperformed.
SCRIPT:
(distractedly, then noticing something) "I do not know why I am checking the door. I am not expecting anyone..." (slowly realizing) "Wait. Is that music?"
```

```
I do not know why I am checking the door. I am not expecting anyone... Wait. Is that music?
```

**part 2 — part 3 — recognition** · targets: Astonishment_Surprise, Elation · adapters: `Scream` @ 0.5; `Astonishment_Surprise` @ 0.35; `Elation` @ 0.35

temp 1.1 · top_p 0.95 · top_k 30 · max_new_frames 135

```
GENERAL: Begin in stunned uncertainty, then let recognition bloom into uncontrolled joyful shock rather than switching instantly. The voice should brighten, speed up slightly, and break into a genuine shriek when you see everyone; continue speaking immediately after the burst.
SCRIPT:
(barely audible, looking inside) "No... no, that cannot be..." (recognizing them, a genuine joyful shriek) "Ahh—! Oh my God... you are all here!"
```

```
No... no, that cannot be... Ahh—! Oh my God... you are all here!
```

**part 3 — part 4 — unable to hide the gratitude** · targets: Gratitude, Relief, Amusement · adapters: `Gratitude` @ 0.55; `Relief` @ 0.4; `Amusement` @ 0.35

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 190

```
GENERAL: Let the volume fall naturally after the surprise. Speak softly and openly, with uneven breathing, a small involuntary laugh, and tears close to the voice. Avoid polished declarations or repeating a formal thank-you; sound as if the words are arriving spontaneously while you look from one friend to another. Keep the tenderness and joy clear.
SCRIPT:
(softly, stunned) "You really did this..." (a small, disbelieving laugh) "I thought I was going to be alone tonight. I did not know how much I needed to see you." (voice trembling, intimate and sincere) "I am so glad you are here. I love you. Thank you."
```

```
You really did this... I thought I was going to be alone tonight. I did not know how much I needed to see you. I am so glad you are here. I love you. Thank you.
```

### X3_birthday · v2 · round 3 (agent score 0.787, supervisor mean 7.00)

*Scene:* On a lonely birthday, you open your door expecting an empty evening, slowly realize your friends are waiting inside, and break open with grateful laughter and tears.

**part 0 — part 1 — resigned and alone** · targets: Sadness · adapters: `Sadness` @ 0.55

temp 0.95 · top_p 0.95 · top_k 30 · max_new_frames 160

```
GENERAL: Speak as a depressed, exhausted adult murmuring privately, flat and inward, with slow pacing and little emotional energy. Sound genuinely worn down rather than theatrically sad, as though you have stopped expecting anyone to remember.
SCRIPT:
(quietly to yourself) "Another birthday. It is almost over, at least. No messages, no plans. I will make some tea and go to bed. That is probably for the best."
```

```
Another birthday. It is almost over, at least. No messages, no plans. I will make some tea and go to bed. That is probably for the best.
```

**part 1 — part 2 — something is different** · targets: Astonishment_Surprise · adapters: `Astonishment_Surprise` @ 0.45

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 145

```
GENERAL: Continue the same tired voice, but let attention slowly return as you reach the door. Build the transition through tiny changes in pacing and pitch: uncertainty first, then a fragile, almost involuntary lift as you hear something unexpected. Do not jump to joy yet.
SCRIPT:
(reaching for the handle, distracted) "I do not know why I am checking. I am not expecting anyone..." (hearing something, quietly puzzled) "Wait. Is that music? And... are those voices?"
```

```
I do not know why I am checking. I am not expecting anyone... Wait. Is that music? And... are those voices?
```

**part 2 — part 3 — recognition breaks through** · targets: Astonishment_Surprise, Elation · adapters: `Scream` @ 0.5; `Astonishment_Surprise` @ 0.35; `Elation` @ 0.35

temp 1.1 · top_p 0.95 · top_k 30 · max_new_frames 150

```
GENERAL: Begin in breathless disbelief and let recognition bloom gradually into explosive joy. The first words should still carry the old loneliness; then the face-to-face realization should release a genuine, involuntary shriek. Continue immediately after the burst, bright and disorganized with joy.
SCRIPT:
(opening the door, barely believing it) "No... no, that cannot be..." (seeing them, a genuine joyful shriek) "Ahh—! Oh my God, you are all here!"
```

```
No no, that cannot be Ahh Oh my God, you are all here!
```

**part 3 — part 4 — laughter through tears** · targets: Gratitude, Amusement, Distress · adapters: `Chuckle` @ 0.5; `Sob` @ 0.5; `Gratitude` @ 0.5; `Amusement` @ 0.35; `Distress` @ 0.35

temp 1.05 · top_p 0.95 · top_k 30 · max_new_frames 260

```
GENERAL: Let the shock collapse into intimate, vulnerable gratitude. Drop the volume naturally, breathe unevenly, and allow a real laugh to mingle with tears; let the voice crack and briefly lose control without becoming melodramatic. Avoid polished declarations or a rehearsed speech. The words should arrive in fragments as you look at the people who came, with warmth, disbelief, and an open heart.
SCRIPT:
(softly, stunned) "You really did this..." (a shaky laugh breaking through) (Chuckle) "I thought... I thought everybody forgot." (voice cracking, laughing and crying) "I don't even know what to say. I missed you so much." (tearful, unable to contain it) (Sob) "Come here. Please—just... come here."
```

```
You really did this I thought I thought everybody forgot I don't even know what to say I missed you so much Come here Please just come here.
```

### X3_birthday · v5 ⚠ · round 1 (agent score 0.611, supervisor mean 7.00)

*Scene:* Alone and defeated on their birthday, a person opens a door to discover a room full of friends waiting with a surprise celebration.

**part 0 — part 1 — empty expectation** · targets: Sadness · adapters: `Sadness` @ 0.5

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Speak as one exhausted, depressed person talking flatly to themself, with low energy, hollow melancholy, and no expectation that anything good will happen; keep the delivery intimate and natural, not theatrical.
SCRIPT:
(Flat, barely audible, staring at the unopened door) "Another birthday. Fine. Just get through the evening. No one remembered, and honestly... I don't blame them. I'll open the door, make some tea, and let the night disappear."
```

```
Another birthday. Fine. Just get through the evening. No one remembered, and honestly... I don't blame them. I'll open the door, make some tea, and let the night disappear.
```

**part 1 — part 2 — the impossible reveal** · targets: Astonishment_Surprise · turn_from: Sadness · adapters: `Scream` @ 0.5; `Astonishment_Surprise` @ 0.5

temp 1.05 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Continue the same voice, but stop being flat and defeated: the door opens, disbelief hits first, then the emotion detonates into a genuine, involuntary shriek of joyous surprise; keep the words after the shriek intelligible and breathlessly amazed.
SCRIPT:
(The door opens; stunned disbelief snaps into a full-bodied joyful shriek) "Aah—! What—? You’re all here?"
```

```
Aah—! What—? You’re all here?
```

**part 2 — part 3 — open-hearted gratitude** · targets: Gratitude · turn_from: Astonishment_Surprise · adapters: `Gratitude` @ 0.5; `Chuckle` @ 0.5

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Continue from the stunned joy, but let the explosive surprise melt away into a soft, wide-open, overwhelmed voice; speak through a fragile laugh and tears, heart in the throat, deeply grateful and unable to hide how loved this makes you feel.
SCRIPT:
(The shock softens into a trembling laugh, then intimate gratitude close to tears) "I... I thought you’d forgotten. Oh my God. I don’t even know what to say. Thank you. Thank you for coming, for doing this... I love you all so much." (Chuckle) "You have no idea what this means to me."
```

```
I... I thought you’d forgotten. Oh my God. I don’t even know what to say. Thank you. Thank you for coming, for doing this... I love you all so much. You have no idea what this means to me.
```

### X3_birthday · v5 ⚠ · round 2 (agent score 0.797, supervisor mean 6.00)

*Scene:* On a lonely birthday, a depressed person opens the door expecting an empty evening, slowly recognizes the friends waiting inside, then breaks into joyful surprise and tearful gratitude.

**part 0 — part 1 — resigned and numb** · targets: Sadness · adapters: `Sadness` @ 0.5

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 270

```
GENERAL: Speak as one exhausted, depressed person talking quietly to themself. Begin flat and hollow, expecting nothing, but keep the sadness intimate and believable rather than exaggerated.
SCRIPT:
(Drained, staring at the door) "Another birthday. Just get through tonight. No messages, no plans... that's fine. I'll make some tea and let the evening pass."
```

```
Another birthday. Just get through tonight. No messages, no plans... that's fine. I'll make some tea and let the evening pass.
```

**part 1 — part 2 — recognition before the joy breaks** · targets: Astonishment_Surprise · turn_from: Sadness · adapters: `Scream` @ 0.5; `Astonishment_Surprise` @ 0.5

temp 1.05 · top_p 0.95 · top_k 30 · max_new_frames 300

```
GENERAL: Continue from the numb sadness, but do not jump straight into excitement. The door opens and the speaker notices small impossible details, slowly realizes the room is full of friends, and lets stunned disbelief build before it finally bursts into an involuntary joyful shriek. Keep the words immediately after the shriek clear.
SCRIPT:
(The door opens; wary confusion slowly becomes dawning recognition) "Why are the lights off? Wait... I hear people. No... no, it can't be—" (Scream) "Aah! You did this? You're all here!"
```

```
Why are the lights off? Wait... I hear people. No... no, it can't be— Aah! You did this? You're all here!
```

**part 2 — part 3 — laughter melting into gratitude** · targets: Gratitude · turn_from: Astonishment_Surprise · adapters: `Chuckle` @ 0.5; `Gratitude` @ 0.5

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 300

```
GENERAL: Continue from the joyful shriek, but stop being explosive: let the energy melt into a soft, open, trembling voice. The laughter should arise naturally from disbelief and relief, blending with tears rather than sounding like a separate comic effect; finish with intimate, overwhelmed gratitude.
SCRIPT:
(The shriek dissolves into breathless laughter and tears, then a tender confession) "I thought you had forgotten me. Oh... I can't believe this." (Chuckle) "I'm laughing because I don't know what else to do. Thank you. Thank you for making me feel remembered. I love you all so much."
```

```
I thought you had forgotten me. Oh... I can't believe this. I'm laughing because I don't know what else to do. Thank you. Thank you for making me feel remembered. I love you all so much.
```

### X3_birthday · v5 ⚠ · round 3 (agent score 0.839, supervisor mean 7.00)

*Scene:* On a lonely birthday, a worn-down person opens the door expecting an empty evening, slowly recognizes the friends waiting inside, then releases a joyful cry that melts into tearful gratitude.

**part 0 — part 1 — weary resignation** · targets: Sadness · adapters: `Sadness` @ 0.45

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Speak as one tired, lived-in person talking quietly to themself. Do not sound mechanically monotone; let the flatness come from long familiarity with disappointment, with small worn-out breaths and an attempt to dismiss the hurt as ordinary. Keep the delivery intimate and restrained.
SCRIPT:
(Weary, rubbing at the day as if this disappointment is familiar) "Another birthday. I suppose I should stop expecting anything by now. No messages, no plans... that's all right. I'll make some tea, turn off the lights, and let the evening pass."
```

```
Another birthday. I suppose I should stop expecting anything by now. No messages, no plans... that's all right. I'll make some tea, turn off the lights, and let the evening pass.
```

**part 1 — part 2 — recognition and release** · targets: Astonishment_Surprise · turn_from: Sadness · adapters: `Scream` @ 0.5; `Astonishment_Surprise` @ 0.5

temp 1.05 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Continue from the weary sadness, but stop being resigned as the door opens. Let the body notice the darkness and the sounds first; confusion turns into dawning recognition, disbelief gathers in the throat, and then the held-in loneliness physically releases as a genuine joyful shriek. Do not rush the realization, and keep the words after the shriek intelligible.
SCRIPT:
(The door opens; cautious confusion becomes recognition, then the whole body releases) "Why are the lights off? Wait... I hear people. No... no, it can't be..." (Scream) "Aah! You're all here! You did this for me?"
```

```
Why are the lights off? Wait... I hear people. No... no, it can't be... Aah! You're all here! You did this for me?
```

**part 2 — part 3 — the wave into gratitude** · targets: Gratitude · turn_from: Astonishment_Surprise · adapters: `Gratitude` @ 0.5; `Chuckle` @ 0.5

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Continue from the physical release of joy, but stop being explosive; let the same wave roll forward into breathless, soft openness. Laughter should spill out as an involuntary response to relief and disbelief, then catch in the throat and become tears. Stay warm, intimate, and overwhelmed rather than delivering separate emotional beats.
SCRIPT:
(The joy keeps moving through the body, becoming a shaky laugh that opens into tears) "I thought everyone had forgotten. I can't—" (Chuckle) "I can't believe you're here. Thank you... thank you for remembering me. I love you all so much. This means more than you know."
```

```
I thought everyone had forgotten. I can't I can't believe you're here. Thank you... thank you for remembering me. I love you all so much. This means more than you know.
```

### X3_birthday · v7 · round 1 (agent score 0.786, supervisor mean 6.00)

*Scene:* On a lonely birthday, a depressed person opens a door to find all their friends waiting with a surprise celebration.

**part 0 — numb_before_the_door** · targets: Sadness · adapters: `Sadness` @ 0.45

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400 · tempo_target 2 · chunk_target 3 · prosody_turn False

```
GENERAL: A tired adult with a low, intimate, slightly worn voice, speaking with natural emotional restraint.
SCRIPT:
(flat and melancholy, barely speaking above a murmur, expecting nothing) "Another birthday. I suppose I should be grateful I made it this far. No messages, no plans, no reason to make a fuss. I'll just get through tonight, then tomorrow will be ordinary again."
```

```
Another birthday. I suppose I should be grateful I made it this far. No messages, no plans, no reason to make a fuss. I'll just get through tonight, then tomorrow will be ordinary again.
```

**part 1 — the_door_opens** · targets: Astonishment_Surprise, Elation · turn_from: Sadness · adapters: `Scream` @ 0.5; `Astonishment_Surprise` @ 0.5

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400 · tempo_target 3 · chunk_target 2 · prosody_turn True

```
GENERAL: A tired adult with a low, intimate, slightly worn voice, speaking with natural emotional restraint.
SCRIPT:
(the numbness stops mid-thought; the door opens, breath catches, and disbelief explodes into an involuntary joyful shriek, then words rush out in stunned delight) "What—" (Scream) "Oh my God! You’re all here. You actually did this?"
```

```
What— Oh my God! You’re all here. You actually did this?
```

**part 2 — overwhelmed_with_gratitude** · targets: Gratitude, Elation · turn_from: Astonishment_Surprise · adapters: `Gratitude` @ 0.7; `Elation` @ 0.5

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400 · tempo_target 2 · chunk_target 3 · prosody_turn True

```
GENERAL: A tired adult with a low, intimate, slightly worn voice, speaking with natural emotional restraint.
SCRIPT:
(the startled excitement stops being loud; the voice opens into a soft, trembling confession, overwhelmed with gratitude, laughter, and tears held just behind the words) "I thought nobody remembered. I thought it was just going to be me, pretending it didn’t matter. You remembered every one of you. Oh, this is so beautiful. I don’t even know what to say. Thank you. Thank you for seeing me, for coming here, for making me feel like I belong. I love you all so much."
```

```
I thought nobody remembered. I thought it was just going to be me, pretending it didn’t matter. You remembered every one of you. Oh, this is so beautiful. I don’t even know what to say. Thank you. Thank you for seeing me, for coming here, for making me feel like I belong. I love you all so much.
```

*Caption actually sent for the continuation parts* (the harness appends the same-speaker / still-acting / no-onset-burst sentences and, when `turn_from` is set, an explicit turn sentence):

part `the_door_opens` — effective caption:

```
GENERAL: A tired adult with a low, intimate, slightly worn voice, speaking with natural emotional restraint. The same speaker from the preceding audio continues without interruption: identical voice, identical person, same microphone and same room -- no cut, no new narrator, no change of casting. Across this passage the same voice moves out of Sadness and into Astonishment_Surprise, Elation.
SCRIPT:
(the numbness stops mid-thought; the door opens, breath catches, and disbelief explodes into an involuntary joyful shriek, then words rush out in stunned delight) "What—" (Scream) "Oh my God! You’re all here. You actually did this?"
```

### X3_birthday · v7 · round 2 (agent score 0.763, supervisor mean 6.60)

*Scene:* On a birthday they expect to spend alone, a deeply lonely person opens a door and discovers all their friends waiting with a surprise party.

**part 0 — alone_on_another_birthday** · targets: Sadness · adapters: `Sadness` @ 0.55

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400 · tempo_target 2 · chunk_target 3 · prosody_turn False

```
GENERAL: A tired adult with a low, intimate, slightly worn voice, speaking with natural emotional restraint.
SCRIPT:
(flat, hollow, and deeply melancholic, as if speaking to yourself because you expect no one to hear; the sadness is quiet and resigned) "Another birthday. I made it this far, I suppose. That has to count for something. No messages, no plans. I should stop expecting people to remember. I’ll make some tea, turn out the lights, and let the night pass."
```

```
Another birthday. I made it this far, I suppose. That has to count for something. No messages, no plans. I should stop expecting people to remember. I’ll make some tea, turn out the lights, and let the night pass.
```

**part 1 — a_flicker_of_curiosity** · targets: Astonishment_Surprise, Sadness · turn_from: Sadness · adapters: `Astonishment_Surprise` @ 0.4; `Sadness` @ 0.35

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400 · tempo_target 2 · chunk_target 2 · prosody_turn True

```
GENERAL: A tired adult with a low, intimate, slightly worn voice, speaking with natural emotional restraint.
SCRIPT:
(the resignation stops when you notice something strange beyond the door; do not become joyful yet, let a cautious flicker of curiosity and uncertainty slowly interrupt the melancholy) "Wait. Was that a sound? No... probably nothing. I must have left something on. It’s nothing. It’s always nothing."
```

```
Wait. Was that a sound? No... probably nothing. I must have left something on. It’s nothing. It’s always nothing.
```

**part 2 — the_room_explodes_with_love** · targets: Astonishment_Surprise, Elation · turn_from: Astonishment_Surprise · adapters: `Scream` @ 0.5; `Astonishment_Surprise` @ 0.4; `Elation` @ 0.35

temp 1.05 · top_p 0.95 · top_k 30 · max_new_frames 400 · tempo_target 3 · chunk_target 2 · prosody_turn True

```
GENERAL: A tired adult with a low, intimate, slightly worn voice, speaking with natural emotional restraint.
SCRIPT:
(the cautious disbelief breaks open as the door reveals the room; the shock rises into one genuine joyful shriek, followed by breathless, disbelieving laughter) "What is—" (Scream) "Oh my God! You’re all here! You actually surprised me!"
```

```
What is— Oh my God! You’re all here! You actually surprised me!
```

**part 3 — softly_overwhelmed** · targets: Gratitude, Elation · turn_from: Elation · adapters: `Gratitude` @ 0.7; `Elation` @ 0.45

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400 · tempo_target 2 · chunk_target 3 · prosody_turn True

```
GENERAL: A tired adult with a low, intimate, slightly worn voice, speaking with natural emotional restraint.
SCRIPT:
(the loud joy stops being startled; your voice softens and opens, trembling with gratitude, a little laughter, and tears caught in your throat) "I thought I was going to be alone. I told myself it didn’t matter, but it did. You remembered. You all remembered. I don’t even know what to say. Thank you for coming, thank you for seeing me. I love you so much."
```

```
I thought I was going to be alone. I told myself it didn’t matter, but it did. You remembered. You all remembered. I don’t even know what to say. Thank you for coming, thank you for seeing me. I love you so much.
```

*Caption actually sent for the continuation parts* (the harness appends the same-speaker / still-acting / no-onset-burst sentences and, when `turn_from` is set, an explicit turn sentence):

part `a_flicker_of_curiosity` — effective caption:

```
GENERAL: A tired adult with a low, intimate, slightly worn voice, speaking with natural emotional restraint. The same speaker from the preceding audio continues without interruption: identical voice, identical person, same microphone and same room -- no cut, no new narrator, no change of casting. Across this passage the same voice moves out of Sadness and into Astonishment_Surprise, Sadness.
SCRIPT:
(the resignation stops when you notice something strange beyond the door; do not become joyful yet, let a cautious flicker of curiosity and uncertainty slowly interrupt the melancholy) "Wait. Was that a sound? No... probably nothing. I must have left something on. It’s nothing. It’s always nothing."
```

### X3_birthday · v7 · round 3 (agent score 0.728, supervisor mean 7.00)

*Scene:* On a lonely birthday, a deeply melancholic person cautiously opens a door and discovers their friends waiting with a surprise party.

**part 0 — resigned_before_the_door** · targets: Sadness · adapters: `Sadness` @ 0.55

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400 · tempo_target 2 · chunk_target 3 · prosody_turn False

```
GENERAL: A tired adult with a low, intimate, slightly worn voice, speaking with natural emotional restraint.
SCRIPT:
(flat, hollow, and quietly defeated, speaking to yourself with no expectation of being heard; let the melancholy feel lived-in rather than theatrical) "Another birthday. I made it this far, I suppose. No messages, no plans. I should stop hoping people will remember. I’ll make some tea, turn out the lights, and let the night pass."
```

```
Another birthday. I made it this far, I suppose. No messages, no plans. I should stop hoping people will remember. I’ll make some tea, turn out the lights, and let the night pass.
```

**part 1 — the_suspicious_sound** · targets: Astonishment_Surprise, Sadness · turn_from: Sadness · adapters: `Astonishment_Surprise` @ 0.42; `Sadness` @ 0.35

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400 · tempo_target 2 · chunk_target 2 · prosody_turn True

```
GENERAL: A tired adult with a low, intimate, slightly worn voice, speaking with natural emotional restraint.
SCRIPT:
(the flat resignation does not disappear; it gently loosens into cautious attention as you hear something beyond the door, with a tiny, involuntary spark of hope you immediately try to suppress) "Wait. Was that a sound? No... probably nothing. I must have left something on. It’s nothing. It’s always nothing."
```

```
Wait. Was that a sound? No... probably nothing. I must have left something on. It’s nothing. It’s always nothing.
```

**part 2 — joy_breaks_through** · targets: Astonishment_Surprise, Elation · turn_from: Astonishment_Surprise · adapters: `Scream` @ 0.5; `Astonishment_Surprise` @ 0.42; `Elation` @ 0.35

temp 1.05 · top_p 0.95 · top_k 30 · max_new_frames 400 · tempo_target 3 · chunk_target 2 · prosody_turn True

```
GENERAL: A tired adult with a low, intimate, slightly worn voice, speaking with natural emotional restraint.
SCRIPT:
(the cautious disbelief continues seamlessly into the door opening; the breath catches, then release the most genuine joyful shriek you can, bright and startled rather than forced, immediately followed by stunned laughter) "What is—" (Scream) "Oh my God! You’re all here! You actually surprised me!"
```

```
What is— Oh my God! You’re all here! You actually surprised me!
```

**part 3 — openhearted_gratitude** · targets: Gratitude, Elation · turn_from: Elation · adapters: `Gratitude` @ 0.7; `Elation` @ 0.45

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400 · tempo_target 2 · chunk_target 3 · prosody_turn True

```
GENERAL: A tired adult with a low, intimate, slightly worn voice, speaking with natural emotional restraint.
SCRIPT:
(the bright shock stops being loud and melts into a soft, trembling openness; laugh through tears, let gratitude catch in your throat, and sound completely unguarded) "I thought nobody remembered. I thought I’d spend the whole night pretending it didn’t matter. You remembered. Every one of you. I don’t even know what to say. Thank you for seeing me. I love you all so much."
```

```
I thought nobody remembered. I thought I’d spend the whole night pretending it didn’t matter. You remembered. Every one of you. I don’t even know what to say. Thank you for seeing me. I love you all so much.
```

*Caption actually sent for the continuation parts* (the harness appends the same-speaker / still-acting / no-onset-burst sentences and, when `turn_from` is set, an explicit turn sentence):

part `the_suspicious_sound` — effective caption:

```
GENERAL: A tired adult with a low, intimate, slightly worn voice, speaking with natural emotional restraint. The same speaker from the preceding audio continues without interruption: identical voice, identical person, same microphone and same room -- no cut, no new narrator, no change of casting. Across this passage the same voice moves out of Sadness and into Astonishment_Surprise, Sadness.
SCRIPT:
(the flat resignation does not disappear; it gently loosens into cautious attention as you hear something beyond the door, with a tiny, involuntary spark of hope you immediately try to suppress) "Wait. Was that a sound? No... probably nothing. I must have left something on. It’s nothing. It’s always nothing."
```

---

## X4_ice_water

> You are at a party, loose and delighted, laughing mid-sentence. Without warning a bucket of ice water is poured over you from behind. You shriek from the cold and the shock. Then you talk to your friends in a mixture that must all be audible at once: the shock, the fright that is still draining out of you, helpless amused delight, and relief.

### X4_ice_water · v1 · round 1 (agent score 0.501, supervisor mean 7.00)

*Scene:* At a carefree party, you are laughing with friends when ice water suddenly drenches you, turning delighted laughter into a shocked shriek and then breathless, amused relief.

**part 0 — carefree_laughter** · targets: Amusement · adapters: `Chuckle` @ 0.9; `Amusement` @ 0.45

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Warm, loose, delighted party voice; laugh naturally through the sentence, with bright spontaneous amusement and relaxed conversational energy.
SCRIPT:
(Grinning, laughing mid-sentence) "I am telling you, the funniest part was when he—" (Chuckle) "No, wait, you had to be there; it was absolutely ridiculous!"
```

```
I am telling you, the funniest part was when he No, wait, you had to be there; it was absolutely ridiculous!
```

**part 1 — ice_water_shock** · targets: Astonishment_Surprise, Fear · adapters: `Scream` @ 0.95; `Astonishment_Surprise` @ 0.45; `Fear` @ 0.4

temp 1.08 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Sudden, involuntary shock from freezing water; begin conversationally, then explode into a sharp genuine shriek, immediately continuing into frightened, breathless words so the aftermath remains audible.
SCRIPT:
(Still laughing, unaware, then violently startled) "Hey, guys—" (Scream) "that is freezing! What happened? Who did that? I cannot feel my back!"
```

```
Hey, guys that is freezing! What happened? Who did that? I cannot feel my back!
```

**part 2 — breathless_amused_relief** · targets: Fear, Amusement, Relief · adapters: `Fear` @ 0.35; `Amusement` @ 0.5; `Relief` @ 0.65

temp 1.02 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Speak quickly and breathlessly as the fright drains away; let residual fear tremble underneath helpless laughter, then resolve into genuine amused delight and relieved warmth toward the friends.
SCRIPT:
(Trembling, catching your breath, then laughing helplessly) "Oh my God—okay, okay, I am all right. I was terrified for one second, but that was so stupidly funny. You got me! I hate you—come here, all of you, I needed that laugh!"
```

```
Oh my God okay okay I am all right. I was terrified for one second, but that was so stupidly funny. You got me! I hate you come here, all of you, I needed that laugh!
```

### X4_ice_water · v1 · round 2 (agent score 0.389, supervisor mean 7.00)

*Scene:* At a carefree party, you are laughing with friends when ice water suddenly drenches you, causing a brief involuntary shriek before the shock slowly melts into helpless laughter and relieved delight.

**part 0 — carefree_laughter** · targets: Amusement · adapters: `Chuckle` @ 0.9; `Amusement` @ 0.45

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Warm, loose, delighted party voice; laugh naturally through the sentence with bright spontaneous amusement and relaxed conversational energy.
SCRIPT:
(Grinning and laughing mid-sentence) "I am telling you, the funniest part was when he—" (Chuckle) "No, wait, you had to be there; it was absolutely ridiculous!"
```

```
I am telling you, the funniest part was when he No, wait, you had to be there; it was absolutely ridiculous!
```

**part 1 — sudden_cold_shock** · targets: Astonishment_Surprise, Fear · adapters: `Scream` @ 0.9; `Astonishment_Surprise` @ 0.4; `Fear` @ 0.35

temp 1.05 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Start in easy conversation, then deliver a very brief, abrupt involuntary shriek at the exact instant the ice water hits; recover immediately into clipped, breathless shock, keeping every word audible.
SCRIPT:
(Still laughing, suddenly drenched) "Hey, guys—" (Scream) "Ah! That is freezing! Who did that? I cannot feel my back!"
```

```
Hey, guys Ah! That is freezing! Who did that? I cannot feel my back!
```

**part 2 — shock_draining_into_relief** · targets: Fear, Relief, Amusement · adapters: `Fear` @ 0.35; `Relief` @ 0.6; `Amusement` @ 0.45

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Begin genuinely shaken and breathless, with the cold and fright still present; let your breathing settle gradually, allow a reluctant laugh to emerge, then finish in warm helpless amusement and unmistakable relief rather than switching emotions abruptly.
SCRIPT:
(Shivering, breathless, slowly calming) "Oh my God—I am still freezing. Okay, okay, I am all right. Wait—that was you?" (A small laugh growing into delighted laughter) "You got me. That was so stupidly funny. I hate you—come here, all of you!"
```

```
Oh my God I am still freezing. Okay, okay, I am all right. Wait that was you? You got me. That was so stupidly funny. I hate you come here, all of you!
```

### X4_ice_water · v1 · round 3 (agent score 0.496, supervisor mean 6.00)

*Scene:* At a carefree party, laughter is cut off by a sudden splash of ice water, and the brief shock slowly becomes shaky, helpless laughter and relieved affection toward the pranksters.

**part 0 — carefree_laughter** · targets: Amusement · adapters: `Chuckle` @ 0.9; `Amusement` @ 0.45

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Warm, loose, delighted party voice; laugh naturally through the sentence with bright spontaneous amusement and relaxed conversational energy.
SCRIPT:
(Grinning, laughing mid-sentence) "I am telling you, the funniest part was when he—" (Chuckle) "No, wait, you had to be there; it was absolutely ridiculous!"
```

```
I am telling you, the funniest part was when he No, wait, you had to be there; it was absolutely ridiculous!
```

**part 1 — impact_and_immediate_recovery** · targets: Astonishment_Surprise, Fear · adapters: `Scream` @ 0.9; `Astonishment_Surprise` @ 0.4; `Fear` @ 0.35

temp 1.05 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Keep the impact extremely sudden and brief: a sharp involuntary shriek, then continue without a pause in clipped, breathless shock. The voice should still sound connected to the conversation rather than resetting.
SCRIPT:
(Still laughing, instantly drenched) "Hey, guys—" (Scream) "Ah! It's freezing! Who did that?"
```

```
Hey, guys Ah! It's freezing! Who did that?
```

**part 2 — shaky_laughter_and_relief** · targets: Fear, Amusement, Relief · adapters: `Chuckle` @ 0.85; `Fear` @ 0.4; `Amusement` @ 0.4; `Relief` @ 0.4

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Continue directly from the shock with no emotional reset. Begin frightened and physically overwhelmed, let the fear remain audible under the words, then gradually let a shaky laugh break through; by the end, sound relieved, amused, and warmly affectionate all at once.
SCRIPT:
(Breathless, still shaking, then slowly laughing) "Oh my God, I'm okay—I'm okay. I'm still scared, but I can't stop laughing. You got me! That was so stupidly funny. Come here, you terrible people—I needed that laugh!" (Chuckle)
```

```
Oh my God, I'm okay I'm okay. I'm still scared, but I can't stop laughing. You got me! That was so stupidly funny. Come here, you terrible people I needed that laugh!
```

### X4_ice_water · v2 · round 1 (agent score 0.677, supervisor mean 7.60)

*Scene:* At a joyful party, a carefree story is interrupted by an unexpected bucket of ice water, leaving the speaker shrieking before dissolving into frightened, helpless laughter and relieved banter with friends.

**part 0 — carefree_party_story** · targets: Amusement · adapters: `Amusement` @ 0.45; `Chuckle` @ 0.5

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: A warm, loose, delighted adult voice at a lively party, laughing naturally while telling a funny story; relaxed breath, bright eyes in the voice, spontaneous mid-sentence amusement, clearly intelligible.
SCRIPT:
(laughing freely) "No, no, you have to hear this—he actually thought the statue was talking to him" (Chuckle) "and then he apologized to it, I swear, I nearly fell over laughing."
```

```
No, no, you have to hear this he actually thought the statue was talking to him and then he apologized to it, I swear, I nearly fell over laughing.
```

**part 1 — ice_water_shock** · targets: Astonishment_Surprise, Fear · adapters: `Scream` @ 0.5; `Astonishment_Surprise` @ 0.45; `Fear` @ 0.4

temp 1.08 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: The same adult voice is suddenly hit from behind by freezing water; produce a genuine, involuntary shriek of cold shock and fright, then continue immediately in breathless, startled speech. Keep the words after the burst fully audible and intelligible.
SCRIPT:
(mid-laugh, sudden shock) "—and then he—" (Scream) "Oh! Oh my God, it's freezing! Who did that? I can't feel my back!"
```

```
and then he Oh Oh my God, it's freezing Who did that I can't feel my back
```

**part 2 — fright_draining_into_relief** · targets: Relief, Amusement · adapters: `Relief` @ 0.55; `Amusement` @ 0.4; `Chuckle` @ 0.5

temp 1.02 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: The same adult voice is still shivering and breathless, with fright draining away into helpless delighted laughter and warm relief. Speak to close friends, protesting while unable to stop laughing; let the emotional blend evolve from shaky disbelief to genuine amused surrender and grateful relief. Keep every word audible.
SCRIPT:
(shaky, laughing despite yourself) "I was terrified for half a second—don't look at me, I'm dripping everywhere!" (Chuckle) "You absolute monsters... oh, that's so cold. Give me a towel, please. All right, all right, I'm okay—I'm okay. I hate you, I love you, and somebody get me a drink."
```

```
I was terrified for half a second don't look at me I'm dripping everywhere You absolute monsters oh that's so cold Give me a towel please All right all right I'm okay I'm okay I hate you I love you and somebody get me a drink.
```

### X4_ice_water · v2 · round 2 (agent score 0.821, supervisor mean 7.00)

*Scene:* At a carefree party, an unexpected bucket of ice water triggers a shriek that immediately melts into breathless laughter, playful protest, and grateful relief with friends.

**part 0 — carefree_party_story** · targets: Amusement · adapters: `Amusement` @ 0.45; `Chuckle` @ 0.5

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 450

```
GENERAL: A warm, loose, delighted adult voice at a lively party, laughing naturally while telling a funny story; relaxed, spontaneous, bright, and clearly intelligible. Let the laughter feel like it is already in motion when the interruption arrives.
SCRIPT:
(laughing freely, mid-story) "No, no, you have to hear this—he actually thought the statue was talking to him" (Chuckle) "and then he apologized to it, I swear, I nearly fell over laughing. Wait, the best part is what he did next—"
```

```
No, no, you have to hear this he actually thought the statue was talking to him and then he apologized to it, I swear, I nearly fell over laughing. Wait, the best part is what he did next.
```

**part 1 — ice_water_shock** · targets: Astonishment_Surprise, Fear · adapters: `Scream` @ 0.5; `Astonishment_Surprise` @ 0.45; `Fear` @ 0.4

temp 1.08 · top_p 0.95 · top_k 30 · max_new_frames 450

```
GENERAL: The same adult voice is suddenly drenched from behind by freezing water; make the shriek involuntary and startling, with cold shock and fright, but keep the speech immediately after it audible. Do not pause after the burst; let the first words tumble out on the same breath.
SCRIPT:
(mid-laugh, suddenly hit) "and then he—" (Scream) "Oh! Oh my God, it's freezing! Who did that? I can't feel my back! Wait—wait, I'm okay, I'm okay—"
```

```
and then he Oh Oh my God, it's freezing! Who did that? I can't feel my back! Wait wait, I'm okay, I'm okay.
```

**part 2 — shaky_laughter_relief** · targets: Relief, Amusement · adapters: `Relief` @ 0.5; `Amusement` @ 0.45; `Chuckle` @ 0.5

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 500

```
GENERAL: The same adult voice continues without a hard emotional reset: breathless and shivering at first, then the fright naturally breaks into helpless delighted laughter, affectionate mock outrage, and unmistakable relief. Laugh through some words without losing intelligibility; sound genuinely safe again and delighted by the prank.
SCRIPT:
(shaky, then laughing as the fear drains away) "I was terrified for half a second—oh, listen to me, I'm laughing and I can't stop shaking!" (Chuckle) "You absolute monsters, that was so cold! Give me a towel—please!" (Chuckle) "There, there, I'm okay now. I'm okay. I hate you, I love you, and somebody get me a drink before you do it again!"
```

```
I was terrified for half a second oh, listen to me, I'm laughing and I can't stop shaking! You absolute monsters, that was so cold! Give me a towel please! There, there, I'm okay now. I'm okay. I hate you, I love you, and somebody get me a drink before you do it again!
```

### X4_ice_water · v2 · round 3 (agent score 0.785, supervisor mean 6.80)

*Scene:* At a carefree party, a bucket of ice water hits from behind, turning a laughing story into a physical cold shock that gradually becomes helpless laughter, affectionate protest, and relieved delight.

**part 0 — warm_party_laughter** · targets: Amusement · adapters: `Amusement` @ 0.45; `Chuckle` @ 0.5

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 450

```
GENERAL: A warm, loose, delighted adult voice at a lively party, already laughing naturally in the middle of a funny story. Keep the delivery relaxed, spontaneous, bright, and clearly intelligible, with laughter ready to be interrupted at any instant.
SCRIPT:
(laughing freely, animated with friends) "No, no, you have to hear this—he actually thought the statue was talking to him" (Chuckle) "and then he apologized to it, I swear, I nearly fell over laughing. Wait, the best part is what he did next—"
```

```
No, no, you have to hear this he actually thought the statue was talking to him and then he apologized to it, I swear, I nearly fell over laughing. Wait, the best part is what he did next.
```

**part 1 — freezing_impact** · targets: Astonishment_Surprise, Fear, Pain · adapters: `Scream` @ 0.5; `Astonishment_Surprise` @ 0.45; `Fear` @ 0.4; `Pain` @ 0.35

temp 1.1 · top_p 0.95 · top_k 30 · max_new_frames 450

```
GENERAL: The same adult voice is suddenly drenched by ice water from behind. Make the shriek involuntary and physically startling, then speak through clenched breath, shivering, gasping, and frantic shoulder tension. Emphasize the shock of cold spreading over the scalp, neck, back, and clothes; the speech after the burst must remain audible and intelligible. Do not insert a silence after the burst: let the words spill out immediately on the same breath.
SCRIPT:
(mid-laugh, struck by freezing water) "and then he—" (Scream) "Oh! Oh, that's freezing! My neck, my back—I'm soaked! Who did that? I can't breathe, I can't feel my shoulders!"
```

```
and then he Oh Oh, that's freezing! My neck, my back I'm soaked! Who did that? I can't breathe, I can't feel my shoulders!
```

**part 2 — shivering_delight_relief** · targets: Relief, Amusement · adapters: `Relief` @ 0.55; `Amusement` @ 0.45; `Chuckle` @ 0.5

temp 1.04 · top_p 0.95 · top_k 30 · max_new_frames 500

```
GENERAL: The same adult voice continues without a reset. Begin with real residual shivering and breathless discomfort: teeth nearly chattering, words breaking slightly as the cold drains out. Then let the fear soften into helpless delighted laughter, affectionate mock outrage, and warm relief. Increase amusement gradually rather than switching moods; let physical recovery show in steadier breath and an easy final laugh. Keep all words audible.
SCRIPT:
(shivering, breathless, then gradually laughing) "I was terrified for half a second—oh, my whole shirt is freezing against my skin!" (Chuckle) "You absolute monsters, I can feel the water running down my back! Give me a towel, please!" (Chuckle) "Okay, okay, I'm warming up. I'm all right now. I hate you, I love you, and somebody get me a drink before you do that again!"
```

```
I was terrified for half a second oh, my whole shirt is freezing against my skin! You absolute monsters, I can feel the water running down my back! Give me a towel, please! Okay, okay, I'm warming up. I'm all right now. I hate you, I love you, and somebody get me a drink before you do that again!
```

### X4_ice_water · v5 ⚠ · round 1 (agent score 0.877, supervisor mean 8.00)

*Scene:* At a carefree party, you are laughing with friends when someone suddenly dumps ice water over you, sending you from delighted laughter through a sharp shriek into breathless, frightened amusement and relief.

**part 0 — carefree laughter** · targets: Amusement · adapters: `Amusement` @ 0.5; `Chuckle` @ 0.5

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Begin loose, spontaneous, and genuinely delighted; do not sound performed or neatly controlled. Laugh naturally through the sentence, with bright party energy and easy intimacy.
SCRIPT:
(chuckling mid-sentence, delighted and teasing) "No, no, that is absolutely not what happened—(Chuckle) I was being completely reasonable, and you know it. Stop looking at me like that, I can explain—"
```

```
No, no, that is absolutely not what happened I was being completely reasonable, and you know it. Stop looking at me like that, I can explain
```

**part 1 — ice-water shock** · targets: Astonishment_Surprise, Fear · turn_from: Amusement · adapters: `Scream` @ 0.5; `Astonishment_Surprise` @ 0.75; `Fear` @ 0.55

temp 1.08 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: The carefree laughter must stop instantly and explode into an involuntary cold-shock shriek; after the burst, keep every word audible, breathless, frightened, and disbelieving rather than collapsing into noise.
SCRIPT:
(the composure vanishes as ice water hits from behind; shriek, then gasp into words) "Aaaah—! (Scream) Oh my God, what was that?! I can't feel my back—who did that?!"
```

```
Aaaah Oh my God, what was that? I can't feel my back who did that?
```

**part 2 — fright melting into delighted relief** · targets: Fear, Amusement, Relief · turn_from: Fear · adapters: `Chuckle` @ 0.5; `Relief` @ 0.7; `Amusement` @ 0.6

temp 1.05 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Stop being purely panicked; let the fear drain into incredulous laughter and helpless amused delight while the cold shock remains audible in your breath. End with relieved, affectionate acceptance, as if the prank was outrageous but genuinely funny.
SCRIPT:
(still shaking and breathless, fright dissolving into helpless laughter) "You absolute monsters—I'm freezing! I was terrified for a second—(Chuckle) I hate you, I hate all of you... okay, okay, that was actually hilarious. Give me a towel before I forgive you."
```

```
You absolute monsters I'm freezing! I was terrified for a second I hate you, I hate all of you okay, okay, that was actually hilarious. Give me a towel before I forgive you.
```

### X4_ice_water · v5 ⚠ · round 2 (agent score 0.432, supervisor mean 7.00)

*Scene:* At a carefree party, your laughter is cut off mid-joke when ice water suddenly drenches you from behind, sending the cold through your body before shock melts into frightened, helpless amusement and relief.

**part 0 — carefree laughter and unaware setup** · targets: Amusement · adapters: `Amusement` @ 0.5; `Chuckle` @ 0.5

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 450

```
GENERAL: Begin loose, warm, and genuinely delighted, laughing naturally in the middle of a sentence. Keep the party intimacy and playful momentum moving forward, with no hint that danger is coming; the final words should leave you physically open to the sudden interruption.
SCRIPT:
(laughing freely, teasing your friends, still amused through the sentence) "No, no, that is absolutely not what happened—(Chuckle) I was being completely reasonable, and you know it. Stop looking at me like that, why are you all staring behind me—"
```

```
No, no, that is absolutely not what happened I was being completely reasonable, and you know it. Stop looking at me like that, why are you all staring behind me
```

**part 1 — cold impact and seamless shock** · targets: Astonishment_Surprise, Fear, Pain · turn_from: Amusement · adapters: `Scream` @ 0.5; `Astonishment_Surprise` @ 0.5; `Fear` @ 0.45; `Pain` @ 0.4

temp 1.08 · top_p 0.95 · top_k 30 · max_new_frames 450

```
GENERAL: Do not reset between moods: the laughter must be audibly interrupted by the physical impact. The instant the ice water hits, let the cold seize your breath, skin, and muscles, turning delight into an involuntary shriek and frightened disbelief; keep the words after the burst clear and urgent.
SCRIPT:
(the bucket hits from behind; laughter snaps into a raw cold-shock shriek, then words rush out through gasping breath) "—wait, what are you—(Scream) Aaaah! It's freezing! Oh my God, my whole back is ice—what was that, who did that?!"
```

```
wait, what are you Aaaah! It's freezing! Oh my God, my whole back is ice what was that, who did that?
```

**part 2 — draining fright into helpless relief** · targets: Fear, Amusement, Relief · turn_from: Fear · adapters: `Chuckle` @ 0.5; `Relief` @ 0.5; `Amusement` @ 0.45; `Fear` @ 0.4

temp 1.05 · top_p 0.95 · top_k 30 · max_new_frames 450

```
GENERAL: Stop being purely frightened: keep the shivering cold, tight breath, and residual alarm present while the fear drains into incredulous laughter. Let helpless amusement take over without becoming polished, then land in genuine relieved affection and comic forgiveness.
SCRIPT:
(still shaking and breathless, frightened outrage breaking into helpless laughter) "You absolute monsters—I'm freezing! I was honestly terrified for a second—(Chuckle) I hate you, I hate all of you... oh, that was so awful... okay, okay, that was actually hilarious. Give me a towel before I forgive you."
```

```
You absolute monsters I'm freezing! I was honestly terrified for a second I hate you, I hate all of you oh, that was so awful okay, okay, that was actually hilarious. Give me a towel before I forgive you.
```

### X4_ice_water · v5 ⚠ · round 3 (agent score 0.830, supervisor mean 6.00)

*Scene:* At a carefree party, a bucket of ice water suddenly drenches you from behind, freezing your body and disrupting your speech before the fear drains into breathless laughter and relieved forgiveness.

**part 0 — laughing before the hit** · targets: Amusement · adapters: `Amusement` @ 0.5; `Chuckle` @ 0.5

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Start loose, intimate, and genuinely delighted, with laughter naturally interrupting the sentence. Keep the playful party momentum and do not anticipate the prank; end mid-thought so the next part can collide directly with it.
SCRIPT:
(laughing freely, teasing through the words) "No, no, that is absolutely not what happened—(Chuckle) I was being completely reasonable, and you know it. Stop staring at me, why are you all looking behind me—"
```

```
No, no, that is absolutely not what happened I was being completely reasonable, and you know it. Stop staring at me, why are you all looking behind me
```

**part 1 — cold impact stealing the breath** · targets: Astonishment_Surprise, Fear, Pain · turn_from: Amusement · adapters: `Scream` @ 0.5; `Astonishment_Surprise` @ 0.65; `Fear` @ 0.55

temp 1.05 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Continue directly from the laughter with no reset. The water hits from behind and the physical cold takes over: breath locks, the voice jumps upward, and speech becomes clipped, wet, and broken by shivering. The shriek must turn immediately into audible words about the cold, not into a long empty scream.
SCRIPT:
(the water crashes over you; laughter cuts off as the cold seizes your breath) "—what are you—(Scream) Aaaah! It's ice! I can't—I can't talk—my whole back is freezing! Who did that?!"
```

```
what are you Aaaah It's ice I can't I can't talk my whole back is freezing Who did that
```

**part 2 — exhale into relieved laughter** · targets: Relief, Amusement · turn_from: Fear · adapters: `Gasp` @ 0.5; `Relief` @ 0.7; `Amusement` @ 0.55

temp 1.03 · top_p 0.95 · top_k 30 · max_new_frames 400

```
GENERAL: Stop being trapped in cold panic and let the body visibly recover: shoulders drop, you take one deep involuntary breath, and the tight broken speech opens into helpless amused laughter. Keep a trace of shivering outrage, then finish with warm, relieved forgiveness rather than polished comedy.
SCRIPT:
(shaking, then lowering your shoulders; take a deep relieved breath and laugh helplessly) "You absolute monsters—I was terrified! (Gasp) Ohhh—okay, I can breathe. I'm still freezing, but that was actually hilarious. Give me a towel, and maybe I forgive you."
```

```
You absolute monsters I was terrified Ohhh okay I can breathe I'm still freezing but that was actually hilarious Give me a towel and maybe I forgive you
```

### X4_ice_water · v7 · round 1 (agent score 0.667, supervisor mean 6.00)

*Scene:* At a joyful party, a laughing guest is suddenly drenched in ice water from behind, then tries to reassure their friends while shock, fear, amusement, and relief collide.

**part 0 — part 1 — carefree laughter** · targets: Amusement · adapters: `Amusement` @ 0.45

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400 · tempo_target 3 · chunk_target 3 · prosody_turn False

```
GENERAL: A bright, playful adult with a warm, naturally expressive voice, speaking clearly in a relaxed conversational register.
SCRIPT:
(Loose, delighted, laughing freely mid-sentence; let the sentence feel spontaneous and warmly social.) "You should have seen your face when you— honestly, I can't— you're killing me, stop, stop, I can't breathe!"
```

```
You should have seen your face when you honestly I can't you're killing me stop stop I can't breathe!
```

**part 1 — part 2 — the icy shock** · targets: Astonishment_Surprise, Fear · turn_from: Amusement · adapters: `Scream` @ 0.5; `Astonishment_Surprise` @ 0.5; `Fear` @ 0.45

temp 1.05 · top_p 0.95 · top_k 30 · max_new_frames 400 · tempo_target 4 · chunk_target 2 · prosody_turn True

```
GENERAL: A bright, playful adult with a warm, naturally expressive voice, speaking clearly in a relaxed conversational register.
SCRIPT:
(The carefree laughter is violently interrupted by freezing water from behind; the breath catches, the body recoils, and shock becomes a frightened shriek, but keep the words after the burst audible.) "Wait— what—" (Scream) "Oh my God, it's freezing! Who did that? I can't feel my back!"
```

```
Wait what Oh my God it's freezing! Who did that? I can't feel my back!
```

**part 2 — part 3 — trembling relief and delight** · targets: Relief, Amusement · turn_from: Fear · adapters: `Relief` @ 0.7; `Amusement` @ 0.6; `Chuckle` @ 0.5

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 400 · tempo_target 3 · chunk_target 2 · prosody_turn True

```
GENERAL: A bright, playful adult with a warm, naturally expressive voice, speaking clearly in a relaxed conversational register.
SCRIPT:
(The fright finally drains out instead of escalating: still shivering and breathless, you turn toward your friends, discover the prank is harmless, and collapse into helpless, relieved laughter while protesting.) "I thought I was dying! You absolute monsters—" (Chuckle) "No, no, don't touch me, I'm soaked! Oh, thank God, I'm okay... that was awful. That was amazing. I hate you—come here!"
```

```
I thought I was dying! You absolute monsters No no don't touch me I'm soaked! Oh thank God I'm okay that was awful. That was amazing. I hate you come here!
```

*Caption actually sent for the continuation parts* (the harness appends the same-speaker / still-acting / no-onset-burst sentences and, when `turn_from` is set, an explicit turn sentence):

part `part 2 — the icy shock` — effective caption:

```
GENERAL: A bright, playful adult with a warm, naturally expressive voice, speaking clearly in a relaxed conversational register. The same speaker from the preceding audio continues without interruption: identical voice, identical person, same microphone and same room -- no cut, no new narrator, no change of casting. Across this passage the same voice moves out of Amusement and into Astonishment_Surprise, Fear.
SCRIPT:
(The carefree laughter is violently interrupted by freezing water from behind; the breath catches, the body recoils, and shock becomes a frightened shriek, but keep the words after the burst audible.) "Wait— what—" (Scream) "Oh my God, it's freezing! Who did that? I can't feel my back!"
```

### X4_ice_water · v7 · round 2 (agent score 0.682, supervisor mean 7.20)

*Scene:* At a joyful party, a laughing guest is suddenly drenched in ice water from behind, then steadies their voice as shock, fright, helpless amusement, and relief melt together.

**part 0 — part 1 — contained party laughter** · targets: Amusement · adapters: `Amusement` @ 0.45

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 450 · tempo_target 3 · chunk_target 3 · prosody_turn False

```
GENERAL: A bright, playful adult with a warm, naturally expressive voice, speaking clearly in a relaxed conversational register.
SCRIPT:
(Keep the same buoyant social energy, but let the laughter stay controlled and intelligible; speak in easy, complete breath groups rather than rushing.) "You should have seen your face when you tried that dance. Honestly, I can't believe you did it. You're killing me—stop, stop, I need a second!"
```

```
You should have seen your face when you tried that dance. Honestly, I can't believe you did it. You're killing me stop stop I need a second!
```

**part 1 — part 2 — controlled shock rupture** · targets: Astonishment_Surprise, Fear · turn_from: Amusement · adapters: `Scream` @ 0.5; `Astonishment_Surprise` @ 0.5; `Fear` @ 0.45

temp 1.05 · top_p 0.95 · top_k 30 · max_new_frames 450 · tempo_target 3 · chunk_target 2 · prosody_turn True

```
GENERAL: A bright, playful adult with a warm, naturally expressive voice, speaking clearly in a relaxed conversational register.
SCRIPT:
(The laughter stops as freezing water hits from behind; the breath catches and the voice jolts into a sharp frightened shriek, then immediately regains enough control to make every following word clear. Use short urgent groups, but do not sprint.) "Wait—what was—" (Scream) "Oh my God, it's freezing! Who did that? My whole back is ice! I can't feel my shirt, I can't feel anything!"
```

```
Wait what was Oh my God it's freezing! Who did that? My whole back is ice! I can't feel my shirt I can't feel anything!
```

**part 2 — part 3 — fear draining into relieved delight** · targets: Relief, Amusement · turn_from: Fear · adapters: `Relief` @ 0.7; `Amusement` @ 0.6; `Chuckle` @ 0.5

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 500 · tempo_target 3 · chunk_target 2 · prosody_turn True

```
GENERAL: A bright, playful adult with a warm, naturally expressive voice, speaking clearly in a relaxed conversational register.
SCRIPT:
(The frightened recoil gradually loosens rather than snapping away; still shivering and breathless, you recognize the harmless prank, let relief enter the voice, and fold into helpless affectionate laughter while protesting.) "I thought I was dying! You absolute monsters—" (Chuckle) "No, no, don't touch me, I'm soaked! Wait... I'm okay. I'm actually okay. Oh, thank God. That was horrible, and I hate you, but that was also the funniest thing you've ever done. Come here, you idiots!"
```

```
I thought I was dying! You absolute monsters No no don't touch me I'm soaked! Wait I'm okay. I'm actually okay. Oh thank God. That was horrible and I hate you but that was also the funniest thing you've ever done. Come here you idiots!
```

*Caption actually sent for the continuation parts* (the harness appends the same-speaker / still-acting / no-onset-burst sentences and, when `turn_from` is set, an explicit turn sentence):

part `part 2 — controlled shock rupture` — effective caption:

```
GENERAL: A bright, playful adult with a warm, naturally expressive voice, speaking clearly in a relaxed conversational register. The same speaker from the preceding audio continues without interruption: identical voice, identical person, same microphone and same room -- no cut, no new narrator, no change of casting. Across this passage the same voice moves out of Amusement and into Astonishment_Surprise, Fear.
SCRIPT:
(The laughter stops as freezing water hits from behind; the breath catches and the voice jolts into a sharp frightened shriek, then immediately regains enough control to make every following word clear. Use short urgent groups, but do not sprint.) "Wait—what was—" (Scream) "Oh my God, it's freezing! Who did that? My whole back is ice! I can't feel my shirt, I can't feel anything!"
```

### X4_ice_water · v7 · round 3 (agent score 0.687, supervisor mean 6.80)

*Scene:* At a joyful party, a laughing guest is suddenly drenched in ice water from behind, then slowly exhales as shock gives way to unmistakable relief, affection, and delighted laughter.

**part 0 — part 1 — buoyant party laughter** · targets: Amusement · adapters: `Amusement` @ 0.45

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 450 · tempo_target 3 · chunk_target 3 · prosody_turn False

```
GENERAL: A bright, playful adult with a warm, naturally expressive voice, speaking clearly in a relaxed conversational register.
SCRIPT:
(Keep a consistent buoyant social energy; laugh naturally but remain intelligible, using comfortable complete breath groups without rushing.) "You should have seen your face when you tried that dance. Honestly, I can't believe you did it. You're killing me—stop, stop, I need a second!"
```

```
You should have seen your face when you tried that dance. Honestly, I can't believe you did it. You're killing me stop stop I need a second!
```

**part 1 — part 2 — shock held under control** · targets: Astonishment_Surprise, Fear · turn_from: Amusement · adapters: `Scream` @ 0.5; `Astonishment_Surprise` @ 0.5; `Fear` @ 0.45

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 450 · tempo_target 3 · chunk_target 3 · prosody_turn True

```
GENERAL: A bright, playful adult with a warm, naturally expressive voice, speaking clearly in a relaxed conversational register.
SCRIPT:
(The laughter is cut off by freezing water; shock and fright burst through the same voice, but the pacing stays measured and the short phrases remain clearly separated rather than accelerating.) "Wait—what was—" (Scream) "Oh my God, it's freezing! Who did that? My whole back is ice! I can't feel my shirt, I can't feel anything!"
```

```
Wait what was Oh my God it's freezing! Who did that? My whole back is ice! I can't feel my shirt I can't feel anything!
```

**part 2 — part 3 — full relieved delight** · targets: Relief, Amusement · turn_from: Fear · adapters: `Relief` @ 0.75; `Amusement` @ 0.55; `Chuckle` @ 0.5; `Sigh` @ 0.5

temp 1.0 · top_p 0.95 · top_k 30 · max_new_frames 500 · tempo_target 3 · chunk_target 3 · prosody_turn True

```
GENERAL: A bright, playful adult with a warm, naturally expressive voice, speaking clearly in a relaxed conversational register.
SCRIPT:
(The fear steadily drains instead of carrying forward; keep the same vocal identity and conversational pace, soften the body and tone, then release a genuine relieved sigh into warm helpless laughter. Let the final lines relax and open into affectionate delight.) "I thought I was dying! You absolute monsters—" (Chuckle) "No, no, don't touch me, I'm soaked!" (Sigh) "Wait... I'm okay. I'm actually okay. Oh, thank God. That was horrible, but I'm safe. You idiots, that was the funniest thing you've ever done. Come here!"
```

```
I thought I was dying! You absolute monsters No no don't touch me I'm soaked! Wait I'm okay. I'm actually okay. Oh thank God. That was horrible, but I'm safe. You idiots, that was the funniest thing you've ever done. Come here!
```

*Caption actually sent for the continuation parts* (the harness appends the same-speaker / still-acting / no-onset-burst sentences and, when `turn_from` is set, an explicit turn sentence):

part `part 2 — shock held under control` — effective caption:

```
GENERAL: A bright, playful adult with a warm, naturally expressive voice, speaking clearly in a relaxed conversational register. The same speaker from the preceding audio continues without interruption: identical voice, identical person, same microphone and same room -- no cut, no new narrator, no change of casting. Across this passage the same voice moves out of Amusement and into Astonishment_Surprise, Fear.
SCRIPT:
(The laughter is cut off by freezing water; shock and fright burst through the same voice, but the pacing stays measured and the short phrases remain clearly separated rather than accelerating.) "Wait—what was—" (Scream) "Oh my God, it's freezing! Who did that? My whole back is ice! I can't feel my shirt, I can't feel anything!"
```

---

