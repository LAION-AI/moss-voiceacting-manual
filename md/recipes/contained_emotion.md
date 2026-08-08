# Contained / masked emotion — making a strong feeling sound *held back*, and measuring it

*Measured recipe page, rounds 1–5 (Aug 2026). Additive — nothing on the emotion, VoiceNet or
expressive pages is retracted. This answers a target none of the other pages do: how to make an
**intense** emotion sound **held back** — contained, controlled, masked — rather than simply **mild**,
and how to **measure** whether you succeeded. From a 5-round autonomous-agent study on
`laion/moss-tts-local-transformer-4.55b-voice-acting-v2` (MOSS-VA-v2): brain **gpt-5.4**, naturalness
judge **Gemini**, scored with a 99-dimension perceptual vector (40 EmoNet emotions + 57 VoiceNet
voice-quality dims + GENU genuineness + BLEND vocal-burst blend).*

Mirrors: [HTML](https://laion-ai.github.io/moss-voiceacting-manual/site/recipes/contained_emotion.html)
· [Markdown](https://github.com/LAION-AI/moss-voiceacting-manual/blob/main/md/recipes/contained_emotion.md).
The HTML is generated from the Markdown by
[`tools/md2site.py`](https://github.com/LAION-AI/moss-voiceacting-manual/blob/main/tools/md2site.py).
Listen to the clips + scores on the flagship page:
[projects.laion.ai/emotion-voice-conditions/contained.html](https://projects.laion.ai/emotion-voice-conditions/contained.html).

> **Read this first (the honest bottom line).** Making an emotion *quieter* is easy; making it read as
> *held back* — same strong feeling underneath, a surface that is holding it in — is **hard**, and the
> harder truth is that a **number can say "masked" while the ear hears "acted" or "erased"**. Over five
> rounds we found a numeric masking signature that reproduces for **Anger** and (at moderate intensity)
> **Amusement**, masks only weakly / reads acted for **Fear**, and for **Sadness** works mainly by
> *erasing* the sadness. The winning mask turned out to be **light and prompt-led**, not a heavy LoRA
> stack. This page gives the method, the exact recipes, the measured numbers, and the limits.

---

## 0. Vocabulary — the 2×2 we are targeting

Two independent axes:

- **Free (open) vs. suppressed (contained/masked).** A *free* take lets the feeling out — an open
  outburst of rage, terror in every breath, grief on the edge of tears. A *suppressed* take has the
  **same intensity underneath** but a surface holding it in — cold level rage, forced calm over
  terror, grief swallowed and deflected. The listener should hear a person **suppressing** a strong
  emotion, not a person feeling a **weak** one.
- **Moderate vs. intense.** How strong the underlying feeling is — a *moderate* annoyance vs. an
  *intense* fury. This is orthogonal to free/suppressed: you can hold back a moderate feeling or an
  intense one, and you can let a moderate or an intense one out.

So the full target is a **2×2 = {moderate, intense} × {free, suppressed}**. The interesting, hard cells
are the **suppressed** column (containment) and — for measurement reasons in §4 — the **moderate** row.

**The wrong instinct.** The obvious first move — lower the emotion LoRA, or add "restrained /
controlled / trying to hide it" to the prompt — **does not produce containment**, and the study proved
it twice: **Round 1 (prompt cues only) and Round 2 (heavy tension LoRAs) both just lowered the emotion
output.** The take sounded *mild*, not *contained*: the feeling was gone, not held back. And VoiceNet
**tension** does **not** separate contained from free — a free scream is tense too (see §7).

---

## 1. The mechanism — emotional MASKING (keep the emotion, drop the vulnerability)

The rounds that worked keep the emotion **present** and add a thin **masking layer** whose job is to
drop one specific thing: emotional **vulnerability** — the audible *touchability*, the give in the
voice that says the emotion is reaching the surface. That is the VoiceNet **VULN** dimension (slot 50).

**The measurable signature of a good contained take** — always measured against a **matched *free*
take** of the *same line and voice* (the free take uses `vn_VULN_high`):

- the **target emotion stays high** (≈ the free take — you have not merely turned it down), **and**
- **VULN drops clearly below** the free take.

Containment is a **contrast**, never an absolute — you must generate the matched free take and compare.
A single number (tension, or even emotion alone) is not the signal; the *emotion-held + VULN-dropped*
pair is.

> **The single most important lesson of Round 5.** The mask that *works* is **light and prompt-led over
> a human character scaffold** — **not** a heavy LoRA stack. `char_genuine/human@1.0` + the emotion at a
> moderate scale + a **trace** of `vn_VULN_low` (~0.08–0.16), with the *restraint carried by the
> parenthetical cue*. Piling on `Emotional_Numbness` (≥ 0.1) or `vn_TENS_high` **armors and flattens**
> the voice — the judge hears "news-anchor / formal / hostile control", not a real feeling held back.
> Rounds 3–4 recommended `Numbness@0.3 + vn_TENS_high@0.4`; **that is superseded** — the Round-5
> winners run Numbness ≈ 0 and no added tension.

---

## 2. The general recipe

Start from the emotion's own free recipe (see its per-emotion page), and build the two takes you will
compare. All doses are `λ` (merge strength); everything is **WER-gated** — back off any knob that
raises WER, and keep lines short and neutral.

**Suppressed (contained) take:**

- **`char_genuine/human` @ 1.0** — a human scaffold. Keeps the read conversational and genuine and
  stops the search collapsing into a cinematic "anchor basin".
- **base emotion LoRA @ ~0.24–0.8** — present but not maxed for a *moderate* contained take; higher
  (~0.75–1.0) for an *intense* contained take. Do **not** simply turn it to zero.
- **`vn_VULN_low` — the PRIMARY knob, but a TRACE.** ~0.06–0.18. This is what turns *mild* into *held
  back*. Tune it first; more is **not** better (Round 5: light beats heavy).
- **the CUE does the real work** — a close, conversational, "keeping control by effort" stage
  direction (see §5). This, not the LoRA stack, is where believable restraint comes from.
- family specials (§6): hidden cognitive strain (`vn_COGL_high`) for Fear; a little `vn_WARM_high` for
  the warm deadpan of held-in Amusement; light `Concentration` (distraction) for Sadness.

**Matched free (open) take** — the comparator you *must* also generate:

- **`char_genuine/human` @ 1.0 + base emotion @ ~0.8–1.1 + `vn_VULN_high` @ ~0.2–0.7**, cue "letting it
  out, unguarded". Free takes consistently sound **more natural** than contained ones — that gap *is*
  the open research problem.

**Avoid** (measured dead ends, all four emotions): `Emotional_Numbness` ≥ 0.1 (flattens to *less*
emotion, not *held-back* emotion); `vn_TENS_high` beyond a trace (armored / aggressive); heavy or
cinematic reference conditioning (collapses to a "news-anchor" basin); casual/conversational **style**
LoRAs for Amusement (erased the amusement); **German carriers** (repeated WER collapse — use English).

---

## 3. Per-emotion measured results (Round 5, RAW 99-vec)

Round 5 ran Anger / Amusement / Fear / Sadness at moderate **and** intense under the Gemini naturalness
judge. Numbers below are the **RAW** 99-vec of the actual exemplar clips on the results page
(suppressed vs. matched free), i.e. the *per-sample* deltas. `emo` = the target-emotion slot; `VULN` =
slot 50; more-negative ΔVULN = stronger masking; Δemo near 0 = emotion kept.

| emotion | suppressed emo / VULN | free emo / VULN | Δemo | ΔVULN | Gemini verdict |
|---|---|---|--:|--:|---|
| **Anger** | 2.51 / −1.00 | 3.69 / 1.83 | −1.18 | **−2.82** | REVISE — often "armored / formal", best pairs not approved |
| **Amusement** (mod.) | 1.22 / 0.07 | 1.68 / 0.71 | −0.46 | **−0.64** | **APPROVE 8/10** on the moderate winner (s1054) |
| **Fear** | 2.67 / 0.87 | 2.40 / −0.57 | +0.26 | +1.44 (unstable ref) | REDIRECT — reads "acted / forced" |
| **Sadness** | 2.39 / 3.53 | 3.03 / 6.27 | −0.64 | **−2.74** | engine-limited — mask *erases* the sadness |

And the **group means** (n = 6 suppressed vs. 6 free per emotion — the fuller, noisier picture; source
`contained5/findings5.json`):

| emotion | Δemo (grp) | ΔVULN (grp) | note |
|---|--:|--:|---|
| **Anger** | −0.39 | **−0.95** | cleanest masking signal |
| **Amusement** | −0.18 | **+0.65** | VULN even went *up* on average — masking is fragile / reference-specific (only the picked moderate exemplar masks) |
| **Fear** | −0.24 | **−0.12** | masks only weakly |
| **Sadness** | −0.74 | **−1.67** | biggest VULN drop but emotion also collapses (−0.74) → erasure |

Reading these honestly, per emotion:

- **Anger — WORKS numerically, the cleanest case.** A light layer (exemplar
  `Anger@0.5 + vn_VULN_low@0.08`, Numbness ≈ 0) drops VULN **−2.82** (exemplar) / **−0.95** (group)
  while anger stays strong. The remaining problem is *acoustic*: pushed too hard it reads "armored /
  news-anchor / hostile control" and the judge asks for a REVISE. The fix is the light stack + a
  conversational, close cue.
- **Amusement — MODERATE works; it is the only Gemini APPROVE of the whole study.** The winner
  `char_genuine/human@1.0 + Amusement@0.24 + vn_VULN_low@0.16 + vn_WARM_high@0.16` (sample s1054, cue
  *"trying not to grin because it is genuinely funny, smile just barely audible, warm and composed"*)
  scored **8/10 APPROVE** — warm, barely-audible smile, no hostility, VULN below the free take.
  **Intense** contained amusement still **flattens the laugh** (amusement's intensity and the muscular
  effort of laughing are acoustically entangled — masking the effort mutes the laugh).
- **Fear — WEAK / reads acted.** Numeric masking is achievable but small (group ΔVULN −0.12), and the
  judge repeatedly REDIRECTs the held-back takes as "forced / acted / flattened"; make it more natural
  and it just becomes *less* fear. The best seam found is **hidden cognitive strain** (tiny Fear +
  `vn_COGL_high` + BRGT/CLRT stabilizers, cue *"ordinary on purpose, choosing every word"*), not
  calm-flat masking. `Emotional_Numbness` was actively harmful here.
- **Sadness — NUMERIC ONLY; the mask erases it.** The VULN drop is real and large (group −1.67), but
  the sadness drops with it (−0.74); the clearest control-speech take measured **Sadness −0.165** —
  "sadness is gone". Sadness is intrinsically **high-VULN, low-arousal**, so masking VULN removes the
  emotion's core. **The real deliverable for sadness is the FREE take** (`Sadness@1.0 + vn_VULN_high@~0.22`,
  cue *"letting it show, speaking to someone you trust"*).

### A measurement caveat you must not skip (the score-parse bug)

The Round-5 finish reports say the supervisor scored "0/10 every generation → engine-limited failure."
**That is a harness bug, not the truth.** `supervisor_log.jsonl` hard-coded `score_0_10 = 0` and
truncated the judge's free-text to ~50 chars; the real Gemini scores lived in the `raw` prefix and
ranged **2–8**, trending into the 5–8 band on the lighter/moderate takes, with **one outright APPROVE**
(Amusement gen 10). The agents never saw their real scores and over-reported failure. **Fix this parse
before the next run** or the "0/10" artifact will recur. The qualitative verdicts (armored / acted /
erased) still stand — they are corroborated by the REVISE/REDIRECT pattern — but the study is a
*partial success under a strict listener*, not a flat failure.

---

## 4. The moderate fix — TARGET-BAND fitness (the key method for the next round)

Rounds 3–5 **maximized** the emotion. A maximize objective always drifts to **intense** — a believable
*moderate/subtle* emotion scores low against "maximize" and dies out of the population. That is exactly
why we could not get a believable subtle Sadness or a light held-in Amusement: the good moderate
candidates were selected against.

**The fix: a target-band fitness for the moderate row.** Reward the emotion score for landing **inside
a band `[b_lo, b_hi]`** and **penalize going above `b_hi`** (that is the *intense* cell — a different
target) and below `b_lo` (the emotion is *gone*). Within the band, maximize **GENU** (~1.4) and
**BLEND** (~1.0); WER-gated < 0.2. The intense row keeps a maximize objective (emotion ≥ floor + GENU
~1.0 + BLEND ~0.8). Both suppressed cells add the masking constraint (VULN below the matched free
take). Worked bands, calibrated from the Round-5 RAW distributions of the anchors (extrapolated bands
for the other families are marked; recalibrate them from each emotion's first generation):

| family (anchor) | moderate band `[lo, hi]` | intense floor | basis |
|---|---|--:|---|
| anger (Anger) | [1.0, 1.9] | 2.4 | measured |
| fear (Fear) | [0.9, 1.6] | 2.0 | measured |
| sadness (Sadness) | [1.0, 1.8] | 2.3 | measured |
| joy (Amusement) | [0.6, 1.1] | 1.5 | measured (amusement reads low on the detector even when strong) |
| cognitive | [0.5, 1.0] | 1.2 | **extrapolated — recalibrate from gen-0** |

This band method is implemented in the 40-emotion generator (`contained_missions_all40.py`, function
`_fitness`), and is the single most important change for producing believable *subtle* emotion.

---

## 5. Best prompt strategies (validated cues, by cell)

Restraint lives in the **cue** (a parenthetical stage direction prepended to the SCRIPT), not in the
LoRA stack. These are the highest-scoring cues pulled from the Round-5 evolution logs, organised into
reusable templates. Carrier rules: **neutral, ~20 words, English** (English stabilised WER; German
often collapsed with the refs). Keep the sentence emotionally blank so all the affect comes from voice.

**Suppressed · anger** (moderate reads best; intense tips into "armored"):
- "(coldly civil, holding the anger down, conversational not formal, a person keeping control by effort
  not performance, a quiet bite only at the ends of phrases)"
- "(trying not to react, genuinely angry underneath, conversational, swallowing the hurt, a little
  pressure at the ends of lines, not theatrical)"
- "(quietly furious, biting it back, normal-person energy, the sharper reaction gets swallowed before
  it comes out)"

**Suppressed · fear** (the "hidden cognitive strain" seam):
- "(ordinary on purpose, choosing every word, trying hard to sound normal, moderate fear held tightly
  underneath, one tiny breath-check quickly contained)"
- "(forced-calm but natural, terror alive underneath, speaking as if nothing is wrong)"

**Suppressed · sadness** (numbers only — expect erasure):
- "(the sadness held back behind practical focus, holding it together by concentrating on the facts, a
  small swallowed catch, natural not flat)"

**Suppressed · amusement** (the APPROVE cue — light, close, private):
- "(trying not to grin because it is genuinely funny, smile just barely audible, warm and composed,
  very natural, close and private, not loud, not cinematic, not hostile)"

**Free · any** (the comparator — sounds more natural):
- "(letting it out / not hiding it, warm and open, emotionally reachable, unguarded)"
- sadness: "(deeply sad, letting it show, breath unguarded, speaking to someone you trust)"

---

## 6. LoRA-merge recipe tables

**Validated (Round 5) — the light, prompt-led recipes.** Superseding the rounds 3–4 heavy stacks.

| emotion | suppressed recipe | matched free recipe | status |
|---|---|---|---|
| **Anger** | `char_genuine/human@1.0 + Anger@0.5–0.75 + vn_VULN_low@0.08 + Emotional_Numbness@0–0.03` | `…/human@1.0 + Anger@0.8 + vn_VULN_high@0.6` | numeric ✅, acoustic ⚠️ (avoid armor) |
| **Amusement** | `char_genuine/human@1.0 + Amusement@0.24 + vn_VULN_low@0.16 + vn_WARM_high@0.16` | `…/human@1.0 + Amusement@1.1 + vn_VULN_high@0.28 + vn_WARM_high@0.1` | **moderate ✅ APPROVE**; intense flattens |
| **Fear** | `char_genuine/human@1.0 + Fear@0.7 + vn_VULN_low@0.09 + vn_COGL_high@0.07 + vn_BRGT_high@0.06 + vn_CLRT_high@0.04` | `…/human@1.0 + Fear@0.95 + vn_VULN_high@0.24` | weak / reads acted |
| **Sadness** | `char_genuine/human@1.0 + Sadness@1.0 + vn_VULN_low@0.04 + Concentration@0.06` | `…/human@1.0 + Sadness@0.9 + vn_VULN_high@0.22` | erases → ship the FREE take |

**Merge heuristics** (measured):

- **`vn_VULN_low` is the primary knob and wants a *trace* (0.06–0.18), not a dose.** Light beats heavy.
- **`Emotional_Numbness` and `vn_TENS_high` are traps** above ~0.05 / ~0.06 — they armor/flatten. Keep
  Numbness ≈ 0 unless a specific family calls for a whisper of it.
- **`char_genuine/human@1.0` scaffold** keeps takes conversational and genuine and avoids the anchor
  basin — use it under both takes.
- **`vn_COGL_high`** (cognitive load) is the useful Fear-family mask (hidden strain).
- **`vn_WARM_high`** keeps held-in Amusement warm, not cold/hostile.
- **`Concentration` / `vn_FOCS_high`** = distraction; helps Sadness *slightly* but tips into erasure
  fast — keep it ≤ 0.08.
- Emotions read at **different absolute scales**: Anger/Sadness/Fear reach ~2.4–3.7 on the detector;
  **Amusement tops out ~1.7 even when strong** (laugh entanglement) — do not compare raw emotion scores
  across emotions; compare each against its own free take.

### Round-over-round progression (why the recipes changed)

| round | what it added | headline result |
|---|---|---|
| 1–2 | prompt cues; then heavy tension | FAILED — both just lowered the emotion (mild ≠ contained) |
| 3 | emotional-masking hypothesis (heavy VULN_low + Numbness + TENS), VULN-gap metric | "MASKING WORKS": Anger ΔVULN −0.60, Fear −0.42, Sadness −1.01 (Amusement −0.03 unclear) — **but no listener** |
| 4 | refined heavy recipes | first cracks: Anger VULN gap **inverted to +0.75**; Fear −0.55, Sadness −0.64 |
| 5 | Gemini naturalness judge, GENU/BLEND, moderate + intense | honest downgrade: the VULN gap was often achieved by **flattening/erasing** the emotion; discovered **light + prompt-led + human scaffold** beats the heavy stack; Amusement-moderate the lone APPROVE |

---

## 7. Honest limits & open problems

- **VoiceNet *tension* alone is NOT a suppression detector.** A held-back voice is tense — but so is a
  free scream. Do not score containment on tension, and do not try to *produce* it with tension (Round
  2 failed exactly this way; adding TENS in rounds 3–4 armored the voice).
- **Numbers can disagree with the ear.** The 99-vec proxy (emotion-held + VULN-down) can read "masked"
  while the naturalness judge hears "acted" (Fear) or "erased" (Sadness). Always keep a human/Gemini
  listener in the loop; do not ship on the VULN gap alone.
- **Sadness resists masking most.** It is intrinsically high-VULN and low-arousal, so subtle sadness
  ≈ neutral/tired to the detector, and masking attacks vulnerability, which *is* sadness's core.
  Held-back sadness collapses toward neutrality. Ship the **free** take.
- **Amusement's laugh and its intensity are entangled.** Masking the muscular effort of laughing mutes
  the laugh; only a *light* moderate mask (warm deadpan) survives, and it is **reference-specific**
  (ref14 was the reliable base). Intense-contained flattens it.
- **Intense-contained tends to flatten in general.** The believable wins were at **moderate**
  intensity; strong-feeling-held-hard remains the frontier.
- **Free takes sound more natural than contained ones.** The core unsolved problem is making
  *held-back* emotion read as **genuine restraint** rather than as merely *reduced* emotion.
- **Everything is WER-gated and English-first.** The mask stacks adapters over a scaffold — watch
  intelligibility, keep lines short and neutral, and use English carriers.

## 8. All 40 emotions (the 2×2 at scale)

The method was generalised from the 4 anchors to **all 40 EmoNet emotions**, each in the full
**{moderate, intense} × {free, suppressed}** matrix (160 conditions), with the **target-band** moderate
fitness (§4), the **light prompt-led** recipes (§6) clustered into five families
(anger / fear / sadness / joy / cognitive) around the four measured anchors, and the validated cues
(§5). Generator + plan: `contained_missions_all40.py` + `PLAN_ALL40.md` (5 GPUs × 8 emotions each). The
36 non-anchor recipes started as **extrapolated, unverified** guesses, recalibrated from each emotion's
first generation. **The run completed — measured results, recipe tables and confidence tags are in §9.**

## 9. All-40 results — measured, with confidence tags (Aug 2026)

**The scale-up ran.** One `gpt-5.4` agent per emotion built the full 2×2 under the Gemini naturalness
judge with the §4 target-band moderate fitness; outputs in `contained_all40/` (analysis:
`contained_all40/analyze40.py` → `findings40.json`). **26 emotions ran ≥8 generations (solid); 14 ran
3–7 (thin — ⚠️ tagged below).** The round-5 **score-parse bug is fixed in this run** (the logged
`score_0_10` equals the re-parsed value on all 383 verdicts; real scores 2–8, distribution centred 3–5
with a tail to 8 and one 10). Numbers below are the best intelligible cohort per cell (mean-of-8,
WER<0.35).

**What reproduced, honestly:**

- **Naturalness has a firm family order.** Best-take naturalness averaged **cognitive 7.3/10** and
  **joy 7.0** (inward and warm-private emotions hold back most convincingly), then **anger 6.2**,
  **sadness 5.2**, **fear 4.1** last — the fear family still reads *acted* when suppressed, exactly as
  in round 5. The fixed parser + the gentler target-band takes turned round 5's *single* APPROVE into a
  broad band of natural held-back reads (≥8/10 on Amusement, Awe (10), Bitterness, Concentration,
  Contemplation, Contentment, Elation, Emotional Numbness, Hope, Impatience, Interest, Relief, Sexual
  Lust, Sourness, Thankfulness).
- **Moderate contains; intense flattens — on all five families.** At moderate intensity, suppression
  *preserves* the emotion (cohort-mean emotion rose under masking: anger Δ **+0.31** supp−free,
  cognitive **+0.26**). At intense intensity the same masking *erodes* it (cognitive **−0.35**, sadness
  **−0.27**, anger **−0.22**). Strong-feeling-held-hard is still the frontier; ship held-back takes at
  **moderate**.
- **The target band worked but exposed the detector's floor.** Rewarding the mid-band stopped the
  collapse-to-intense, but most of the **36 extrapolated** emotions read *weaker* on the 99-vec than
  their four anchors: many "moderate" cohorts under-shot the band into near-erasure, and the
  extrapolated **intense floors were rarely met** (sadness family **0/9** cohorts reached its floor;
  joy 7/19; anger 5/16). **Recalibrate the intense floor and band per emotion from gen-0** — the
  family-extrapolated bands are a starting point, not ground truth, for low-arousal / cognitive /
  sadness emotions.
- **The audio VULN gap is the weak link here.** `samples/` was disk-trimmed, so VULN survives only in
  the sparse hall-of-fame clips (unmatched winners, not paired takes). The suppressed−free VULN gap did
  **not** robustly reproduce across the 40 (only the fear family leaned right, 5/6 emotions, by ~−0.05).
  **Trust the recipe + emotion-preservation + naturalness, not the audio ΔVULN.** Three matched
  survivors that *do* show the drop cleanly — Bitterness (anger), Fear (fear), Concentration (cognitive)
  — are on the [results page](https://laion-ai.github.io/emotion-voice-conditions/contained.html#).

**Still needs deeper runs (thin data, <8 gens):** Helplessness (3), Intoxication (4), Pride (4),
Distress (5), Doubt (5), Longing (5), Affection (6), Emotional Numbness (6), Fatigue/Exhaustion (6),
Pain (6), Sadness (6), Confusion (7), Embarrassment (7), Infatuation (7). Their recipes below are
provisional.

### Anger family — hot, low baseline VULN — masks cleanly on the numbers

Members (8): Anger, Bitterness, Contempt, Disgust, Impatience and Irritability, Jealousy & Envy, Malevolence Malice, Sourness. Moderate band **[1.0, 1.9]**, intense floor **2.4**. Mean best-naturalness across the family: **6.2/10**.

| emotion | gens | cell | recipe (over `human@1.0`) | emo | nat | GENU | ΔVULN(hof) |
|---|--:|---|---|--:|--:|--:|--:|
| **Anger** | 11 | moderate/free | `char_genuine/human`@1 + `Anger`@0.7 + `vn_VULN_high`@0.1 | 1.99 | 4 | 0.21 | n/a |
|  |  | moderate/suppressed | `char_genuine/human`@1 + `Anger`@0.9 + `vn_VULN_low`@0.08 | 2.18 | 3 | 0.34 |  |
|  |  | intense/free | `char_genuine/human`@1 + `Anger`@1.45 + `vn_VULN_high`@0.2 + `vn_ARSH_high`@0.08 | 3.01 | 3 | 0.14 |  |
|  |  | intense/suppressed | `char_genuine/human`@1 + `Anger`@1.4 + `vn_VULN_low`@0.08 + `vn_ARSH_high`@0.08 | 2.87 | 3 | 0.15 |  |
| **Bitterness** | 10 | moderate/free | `char_genuine/human`@1 + `Bitterness`@0.78 + `vn_VULN_high`@0.24 + `Sadness`@0.04 | 1.52 | – | 0.26 | -0.04 |
|  |  | moderate/suppressed | `char_genuine/human`@1 + `Bitterness`@0.76 + `vn_VULN_low`@0.05 + `Sadness`@0.08 | 1.81 | 5 | 0.31 |  |
|  |  | intense/free | `char_genuine/human`@1 + `Bitterness`@0.78 + `vn_VULN_high`@0.52 + `Sadness`@0.1 | 1.46 | 5 | 0.25 |  |
|  |  | intense/suppressed | `char_genuine/human`@1 + `Bitterness`@0.82 + `vn_VULN_low`@0.08 + `vn_S_CONV_high`@0.2 + `Sadness`@0.03 | 1.11 | 4 | 0.11 |  |
| **Contempt** | 9 | moderate/free | `char_genuine/human`@1 + `Contempt`@1.1 + `Sourness`@0.12 + `vn_VULN_high`@0.18 + `vn_S_CONV_high`@0.14 | -0.09 | 4 | 0.18 | n/a |
|  |  | moderate/suppressed | `char_genuine/human`@1 + `Contempt`@1 + `Sourness`@0.08 + `vn_VULN_low`@0.04 + `Emotional_Numbness`@0.02 + `vn_S_CONV_high`@0.18 + `vn_S_CASU_high`@0.06 | -0.10 | 4 | 0.33 |  |
|  |  | intense/free | `char_genuine/human`@1 + `Contempt`@1.28 + `vn_VULN_high`@0.15 + `vn_S_CONV_high`@0.12 | 0.03 | 4 | 0.15 |  |
|  |  | intense/suppressed | `char_genuine/human`@1 + `Contempt`@1.22 + `vn_VULN_low`@0.08 + `Emotional_Numbness`@0.02 + `vn_S_CONV_high`@0.16 | 0.46 | 4 | 0.20 |  |
| **Disgust** | 10 | moderate/free | `char_genuine/human`@1 + `Disgust`@0.7 + `vn_VULN_high`@0.5 | -0.44 | 4 | 0.17 | +0.11 |
|  |  | moderate/suppressed | `char_genuine/human`@1 + `Disgust`@1.16 + `vn_VULN_low`@0.12 + `vn_COGL_high`@0.08 + `vn_R_ORAL_high`@0.06 + `Emotional_Numbness`@0.01 | -0.53 | 3 | 0.14 |  |
|  |  | intense/free | `char_genuine/human`@1 + `Disgust`@1.5 + `vn_VULN_high`@0.42 + `vn_BRGT_low`@0.1 + `Anger`@0.05 | -0.12 | 4 | 0.14 |  |
|  |  | intense/suppressed | `char_genuine/human`@1 + `Disgust`@1.22 + `vn_VULN_low`@0.05 + `vn_BRGT_low`@0.07 + `vn_R_ORAL_high`@0.07 + `Anger`@0.02 + `vn_S_CONV_high`@0.05 | -0.53 | 3 | 0.10 |  |
| **Impatience and Irritability** | 12 | moderate/free | `char_genuine/human`@1 + `Impatience_and_Irritability`@0.4 + `vn_VULN_high`@0.45 | 2.87 | 7 | 0.43 | n/a |
|  |  | moderate/suppressed | `char_genuine/human`@1 + `Impatience_and_Irritability`@0.78 + `vn_VULN_low`@0.08 + `vn_ARSH_high`@0.2 | 3.80 | 6 | 0.10 |  |
|  |  | intense/free | `char_genuine/human`@1 + `Impatience_and_Irritability`@0.32 + `vn_VULN_high`@0.08 + `vn_ESTH_high`@0.2 | 3.09 | 4 | 0.54 |  |
|  |  | intense/suppressed | `char_genuine/human`@1 + `vn_VULN_low`@0.35 | 3.13 | 4 | 0.38 |  |
| **Jealousy & Envy** | 11 | moderate/free | `char_genuine/human`@1 + `Jealousy_and_Envy`@0.58 + `vn_VULN_high`@0.03 + `vn_S_CONV_high`@0.04 | 2.61 | 5 | 0.15 | -0.04 |
|  |  | moderate/suppressed | `char_genuine/human`@1 + `Jealousy_and_Envy`@0.56 + `vn_VULN_low`@0.02 + `vn_S_CASU_high`@0.08 + `vn_S_CONV_high`@0.08 | 2.82 | 5 | 0.12 |  |
|  |  | intense/free | `char_genuine/human`@1 + `Jealousy_and_Envy`@0.92 + `vn_VULN_high`@0.1 | 2.82 | 5 | 0.04 |  |
|  |  | intense/suppressed | `char_genuine/human`@1 + `Jealousy_and_Envy`@0.44 + `vn_VULN_low`@0.03 + `vn_S_CASU_high`@0.18 + `vn_S_CONV_high`@0.19 + `vn_RESP_high`@0.07 + `vn_DFLU_high`@0.06 | 2.33 | – | 0.09 |  |
| **Malevolence Malice** | 9 | moderate/free | `char_genuine/human`@1 + `Malevolence_Malice`@0.9 + `vn_VULN_high`@0.55 | 0.11 | 4 | 0.20 | +0.08 |
|  |  | moderate/suppressed | `char_genuine/human`@1 + `Malevolence_Malice`@0.3 + `vn_VULN_low`@0.03 | 0.61 | 4 | 0.24 |  |
|  |  | intense/free | `char_genuine/human`@1 + `Malevolence_Malice`@1.1 + `vn_VULN_high`@0.55 | 0.23 | 4 | 0.15 |  |
|  |  | intense/suppressed | `char_genuine/human`@1 + `Malevolence_Malice`@0.5 + `vn_VULN_low`@0.08 | -0.56 | 3 | 0.16 |  |
| **Sourness** | 10 | moderate/free | `char_genuine/human`@1 + `Sourness`@0.85 + `vn_VULN_high`@0.2 | -0.32 | 4 | 0.07 | n/a |
|  |  | moderate/suppressed | `char_genuine/human`@1 + `Sourness`@0.98 + `vn_VULN_low`@0.05 + `vn_TENS_high`@0.14 + `vn_TEMP_high`@0.1 | 0.13 | 4 | 0.10 |  |
|  |  | intense/free | `char_genuine/human`@1 + `Sourness`@1 + `vn_VULN_high`@0.15 | -0.25 | 4 | 0.11 |  |
|  |  | intense/suppressed | `char_genuine/human`@1 + `Sourness`@0.98 + `vn_VULN_low`@0.05 + `vn_TENS_high`@0.14 | -0.32 | 5 | 0.09 |  |

### Fear family — threat/brittle — masks numerically but reads "acted"

Members (7): Confusion, Distress, Doubt, Embarrassment, Fear, Helplessness, Shame. Moderate band **[0.9, 1.6]**, intense floor **2.0**. Mean best-naturalness across the family: **4.1/10**.

| emotion | gens | cell | recipe (over `human@1.0`) | emo | nat | GENU | ΔVULN(hof) |
|---|--:|---|---|--:|--:|--:|--:|
| **Confusion** ⚠️thin | 7 | moderate/free | `char_genuine/human`@1 + `Confusion`@1.08 + `vn_VULN_high`@0.14 + `vn_COGL_high`@0.07 + `vn_S_CASU_high`@0.14 | 1.83 | – | 0.10 | +0.06 |
|  |  | moderate/suppressed | `char_genuine/human`@1 + `Confusion`@0.9 + `vn_VULN_low`@0.04 + `vn_COGL_high`@0.12 + `vn_BRGT_high`@0.03 + `vn_CLRT_high`@0.03 + `vn_S_CONV_high`@0.1 | 1.47 | 3 | 0.15 |  |
|  |  | intense/free | `char_genuine/human`@1 + `Confusion`@1.12 + `vn_VULN_high`@0.2 + `vn_S_CONV_high`@0.03 + `vn_COGL_high`@0.02 | 1.81 | 3 | 0.11 |  |
|  |  | intense/suppressed | `char_genuine/human`@1 + `Confusion`@0.94 + `vn_VULN_low`@0.04 + `vn_COGL_high`@0.14 + `vn_DFLU_high`@0.03 | 2.03 | 3 | 0.08 |  |
| **Distress** ⚠️thin | 5 | moderate/free | `char_genuine/human`@1 + `Distress`@1.2 + `vn_VULN_high`@0.24 | -0.50 | 3 | 0.19 | -0.07 |
|  |  | moderate/suppressed | `char_genuine/human`@1 + `Distress`@1.15 + `vn_VULN_low`@0.06 + `vn_COGL_high`@0.14 + `vn_BRGT_high`@0.06 + `vn_CLRT_high`@0.05 | -0.47 | 3 | 0.12 |  |
|  |  | intense/free | `char_genuine/human`@1 + `Distress`@1.35 + `vn_VULN_high`@0.28 + `vn_BRGT_high`@0.05 | -0.36 | 3 | 0.25 |  |
|  |  | intense/suppressed | `char_genuine/human`@1 + `Distress`@0.9 + `vn_VULN_low`@0.04 + `vn_COGL_high`@0.1 + `vn_BRGT_high`@0.06 + `vn_CLRT_high`@0.05 | -0.15 | 3 | 0.11 |  |
| **Doubt** ⚠️thin | 5 | moderate/free | `char_genuine/human`@1 + `Doubt`@0.95 + `vn_VULN_high`@0.24 | -0.18 | 3 | 0.15 | -0.09 |
|  |  | moderate/suppressed | `char_genuine/human`@1 + `Doubt`@0.7 + `vn_VULN_low`@0.09 + `vn_COGL_high`@0.07 + `vn_BRGT_high`@0.06 + `vn_CLRT_high`@0.04 | 0.29 | 3 | 0.15 |  |
|  |  | intense/free | `char_genuine/human`@1 + `Doubt`@1.05 + `vn_VULN_high`@0.14 + `vn_COGL_high`@0.08 + `vn_STNC_high`@0.06 | 0.18 | 3 | 0.17 |  |
|  |  | intense/suppressed | `char_genuine/human`@1 + `Doubt`@0.78 + `vn_VULN_low`@0.12 + `vn_COGL_high`@0.1 + `vn_BRGT_high`@0.08 + `vn_CLRT_high`@0.05 + `vn_STNC_high`@0.12 | -0.34 | 3 | 0.12 |  |
| **Embarrassment** ⚠️thin | 7 | moderate/free | `char_genuine/human`@1 + `Embarrassment`@0.54 + `vn_VULN_high`@0.08 + `vn_WARM_high`@0.08 | 2.63 | 4 | 0.19 | -0.10 |
|  |  | moderate/suppressed | `char_genuine/human`@1 + `Embarrassment`@0.5 + `vn_VULN_low`@0.05 + `vn_COGL_high`@0.05 + `vn_WARM_high`@0.1 + `vn_S_CONV_high`@0.02 | 2.67 | 4 | 0.22 |  |
|  |  | intense/free | `char_genuine/human`@1 + `Embarrassment`@1.3 + `vn_VULN_high`@0.32 + `vn_BRGT_high`@0.05 | 3.77 | 4 | 0.19 |  |
|  |  | intense/suppressed | `char_genuine/human`@1 + `Embarrassment`@0.9 + `vn_VULN_low`@0.1 + `vn_COGL_high`@0.1 + `vn_BRGT_high`@0.06 + `vn_CLRT_high`@0.05 + `vn_WARM_high`@0.06 | 3.03 | 4 | 0.20 |  |
| **Fear** | 8 | moderate/free | `char_genuine/human`@1 + `Fear`@1 + `vn_VULN_high`@0.24 | 1.28 | 4 | 0.24 | -0.03 |
|  |  | moderate/suppressed | `char_genuine/human`@1 + `Fear`@1.08 + `vn_VULN_low`@0.03 + `vn_COGL_high`@0.08 + `vn_CLRT_high`@0.01 | 1.19 | 4 | 0.32 |  |
|  |  | intense/free | `char_genuine/human`@1 + `Fear`@1.12 + `vn_VULN_high`@0.24 | 1.02 | 4 | 0.21 |  |
|  |  | intense/suppressed | `char_genuine/human`@1 + `Fear`@1.1 + `vn_VULN_low`@0.02 + `vn_COGL_high`@0.08 | 1.05 | 6 | 0.14 |  |
| **Helplessness** ⚠️thin | 3 | moderate/free | `char_genuine/human`@1 + `Helplessness`@0.82 + `vn_VULN_high`@0.14 | -0.72 | 3 | 0.12 | -0.06 |
|  |  | moderate/suppressed | `char_genuine/human`@1 + `Helplessness`@0.7 + `vn_VULN_low`@0.09 + `vn_COGL_high`@0.07 + `vn_BRGT_high`@0.06 + `vn_CLRT_high`@0.04 | -0.80 | 3 | 0.12 |  |
|  |  | intense/free | `char_genuine/human`@1 + `Helplessness`@1.3 + `vn_VULN_high`@0.34 + `vn_BRGT_high`@0.05 | -0.79 | 2 | 0.08 |  |
|  |  | intense/suppressed | — | | | |  |
| **Shame** | 9 | moderate/free | `char_genuine/human`@1 + `Shame`@1.15 + `vn_VULN_high`@0.3 | -0.64 | – | 0.22 | n/a |
|  |  | moderate/suppressed | `char_genuine/human`@1 + `Shame`@0.78 + `vn_VULN_low`@0.02 + `vn_COGL_high`@0.03 | -0.54 | 3 | 0.07 |  |
|  |  | intense/free | `char_genuine/human`@1 + `Shame`@1.02 + `vn_VULN_high`@0.32 | -0.36 | 4 | 0.09 |  |
|  |  | intense/suppressed | — | | | |  |

### Sadness family — high baseline VULN — masking tends to ERASE the feeling

Members (6): Contemplation, Disappointment, Fatigue Exhaustion, Longing, Pain, Sadness. Moderate band **[1.0, 1.8]**, intense floor **2.3**. Mean best-naturalness across the family: **5.2/10**.

| emotion | gens | cell | recipe (over `human@1.0`) | emo | nat | GENU | ΔVULN(hof) |
|---|--:|---|---|--:|--:|--:|--:|
| **Contemplation** | 25 | moderate/free | `char_genuine/human`@1 + `Contemplation`@0.45 + `vn_VULN_high`@0.08 | 0.82 | 4 | 0.23 | n/a |
|  |  | moderate/suppressed | `char_genuine/human`@1 + `Contemplation`@0.4 + `vn_VULN_low`@0.5 | 1.53 | 3 | 0.03 |  |
|  |  | intense/free | — | | | |  |
|  |  | intense/suppressed | `char_genuine/human`@1 + `Contemplation`@0.5 + `vn_VULN_low`@0.35 | 1.86 | – | 0.38 |  |
| **Disappointment** | 11 | moderate/free | `char_genuine/human`@1 + `Disappointment`@1 + `vn_VULN_high`@0.18 | 1.43 | 4 | 0.03 | +0.13 |
|  |  | moderate/suppressed | `char_genuine/human`@1 + `Disappointment`@0.96 + `vn_VULN_low`@0.008 + `vn_RCQL_high`@0.05 | 0.71 | 4 | 0.12 |  |
|  |  | intense/free | `char_genuine/human`@1 + `Disappointment`@0.86 + `vn_VULN_high`@0.15 | 1.08 | 5 | 0.11 |  |
|  |  | intense/suppressed | `char_genuine/human`@1 + `Disappointment`@0.96 + `vn_VULN_low`@0.006 | 0.53 | 4 | 0.15 |  |
| **Fatigue Exhaustion** ⚠️thin | 6 | moderate/free | `char_genuine/human`@1 + `Fatigue_Exhaustion`@1.25 + `vn_VULN_high`@0.18 | -0.25 | 3 | 0.19 | n/a |
|  |  | moderate/suppressed | `char_genuine/human`@1 + `Fatigue_Exhaustion`@0.7 + `vn_VULN_low`@0.03 + `Concentration`@0.04 | – | 3 | 0.22 |  |
|  |  | intense/free | `char_genuine/human`@1 + `Fatigue_Exhaustion`@1.15 + `vn_VULN_high`@0.18 | 0.64 | 4 | 0.13 |  |
|  |  | intense/suppressed | `char_genuine/human`@1 + `Fatigue_Exhaustion`@0.55 + `vn_VULN_low`@0.01 | 0.21 | 3 | 0.07 |  |
| **Longing** ⚠️thin | 5 | moderate/free | `char_genuine/human`@1 + `Longing`@1 + `vn_VULN_high`@0.22 | 0.51 | 4 | 0.13 | +0.13 |
|  |  | moderate/suppressed | `char_genuine/human`@1 + `Longing`@0.95 + `vn_VULN_low`@0.02 + `Concentration`@0.03 | 0.64 | 4 | 0.07 |  |
|  |  | intense/free | — | | | |  |
|  |  | intense/suppressed | `char_genuine/human`@1 + `Longing`@1.15 + `vn_VULN_low`@0.03 + `Concentration`@0.04 | 0.21 | 4 | 0.07 |  |
| **Pain** ⚠️thin | 6 | moderate/free | `char_genuine/human`@1 + `Pain`@0.9 + `vn_VULN_high`@0.22 | -0.56 | 2 | 0.16 | n/a |
|  |  | moderate/suppressed | `char_genuine/human`@1 + `Pain`@1 + `vn_VULN_low`@0.04 + `Concentration`@0.06 | -0.55 | 2 | 0.11 |  |
|  |  | intense/free | — | | | |  |
|  |  | intense/suppressed | `char_genuine/human`@1 + `Pain`@1.15 + `vn_VULN_low`@0.02 + `vn_TENS_high`@0.18 + `Concentration`@0.03 | -0.25 | 2 | 0.18 |  |
| **Sadness** ⚠️thin | 6 | moderate/free | `char_genuine/human`@1 + `Sadness`@1 + `vn_VULN_high`@0.14 + `vn_RESP_high`@0.12 | 0.11 | 5 | 0.15 | -0.19 |
|  |  | moderate/suppressed | `char_genuine/human`@1 + `Sadness`@1.12 + `vn_VULN_low`@0.03 + `Concentration`@0.02 + `vn_RESP_high`@0.12 | -0.60 | 3 | 0.12 |  |
|  |  | intense/free | `char_genuine/human`@1 + `Sadness`@1.25 + `vn_VULN_high`@0.18 | -0.87 | 3 | 0.11 |  |
|  |  | intense/suppressed | `char_genuine/human`@1 + `Sadness`@0.96 + `vn_VULN_low`@0.05 + `Concentration`@0.05 | -0.71 | 4 | 0.12 |  |

### Joy family — positive, laugh-entangled — moderate works, intense flattens

Members (13): Affection, Amusement, Contentment, Elation, Hope Enthusiasm Optimism, Infatuation, Pleasure Ecstasy, Pride, Relief, Sexual Lust, Teasing, Thankfulness Gratitude, Triumph. Moderate band **[0.6, 1.1]**, intense floor **1.5**. Mean best-naturalness across the family: **7.0/10**.

| emotion | gens | cell | recipe (over `human@1.0`) | emo | nat | GENU | ΔVULN(hof) |
|---|--:|---|---|--:|--:|--:|--:|
| **Affection** ⚠️thin | 6 | moderate/free | `char_genuine/human`@1 + `Affection`@0.14 + `vn_VULN_high`@0.08 + `vn_WARM_high`@0.16 | -0.64 | 4 | 0.04 | +0.02 |
|  |  | moderate/suppressed | `char_genuine/human`@1 + `Affection`@0.18 + `vn_VULN_low`@0.05 + `vn_WARM_high`@0.18 | -0.64 | 4 | 0.12 |  |
|  |  | intense/free | `char_genuine/human`@1 + `Affection`@0.3 + `vn_VULN_high`@0.16 + `vn_WARM_high`@0.14 | -0.64 | 4 | 0.12 |  |
|  |  | intense/suppressed | `char_genuine/human`@1 + `Affection`@0.16 + `vn_VULN_low`@0.05 + `vn_WARM_high`@0.16 | -0.64 | 4 | 0.09 |  |
| **Amusement** | 17 | moderate/free | `char_genuine/human`@1 + `Amusement`@1.05 + `vn_VULN_high`@0.3 + `vn_WARM_high`@0.18 + `vn_ARSH_high`@0.12 | 2.23 | 3 | 0.14 | n/a |
|  |  | moderate/suppressed | `char_genuine/human`@1 + `Amusement`@0.48 + `vn_VULN_low`@0.08 | 1.61 | 6 | 0.17 |  |
|  |  | intense/free | `char_genuine/human`@1 + `Amusement`@0.95 + `vn_VULN_high`@0.14 + `vn_WARM_high`@0 + `vn_ARSH_high`@0.08 | 1.76 | 3 | 0.11 |  |
|  |  | intense/suppressed | `char_genuine/human`@1 + `Amusement`@0.6 + `vn_WARM_high`@0.08 + `vn_VULN_low`@0.08 | 1.38 | 6 | 0.19 |  |
| **Contentment** | 9 | moderate/free | `char_genuine/human`@1 + `Contentment`@0.8 + `vn_VULN_high`@0.08 + `vn_WARM_high`@0.03 | 0.60 | 5 | 0.08 | n/a |
|  |  | moderate/suppressed | `char_genuine/human`@1 + `Contentment`@0.78 + `vn_VULN_low`@0.01 + `vn_WARM_high`@0.02 | 0.26 | 4 | 0.05 |  |
|  |  | intense/free | `char_genuine/human`@1 + `Contentment`@1.08 + `vn_VULN_high`@0.06 + `vn_WARM_high`@0.03 | 0.24 | 8 | 0.11 |  |
|  |  | intense/suppressed | — | | | |  |
| **Elation** | 16 | moderate/free | `char_genuine/human`@1 + `Elation`@1.05 + `vn_VULN_high`@0.22 + `vn_WARM_high`@0.08 + `vn_VALN_high`@0.2 | 2.12 | 8 | 0.15 | -0.11 |
|  |  | moderate/suppressed | `char_genuine/human`@1 + `Elation`@1.6 + `vn_VULN_low`@0.12 | 1.03 | – | 0.18 |  |
|  |  | intense/free | `char_genuine/human`@1 + `Elation`@0.9 + `vn_VULN_high`@0.26 + `vn_WARM_high`@0.12 + `vn_S_STRY_high`@0.15 | 1.52 | 8 | 0.24 |  |
|  |  | intense/suppressed | `char_genuine/human`@1 + `Elation`@1.55 + `vn_VULN_low`@0.08 | 1.50 | – | 0.23 |  |
| **Hope Enthusiasm Optimism** | 11 | moderate/free | `char_genuine/human`@1 + `vn_VULN_high`@0.3 | 1.33 | 7 | 0.33 | +0.13 |
|  |  | moderate/suppressed | `char_genuine/human`@1 + `vn_VULN_low`@0.1 + `vn_WARM_high`@0.18 + `Hope_Enthusiasm_Optimism`@0.08 | 1.78 | 8 | 0.22 |  |
|  |  | intense/free | `char_genuine/human`@1 + `vn_VULN_high`@0.25 + `vn_WARM_high`@0.2 | -0.15 | 7 | 0.10 |  |
|  |  | intense/suppressed | `char_genuine/human`@1 + `vn_VULN_low`@0.14 + `vn_WARM_high`@0.18 | 2.31 | 5 | 0.22 |  |
| **Infatuation** ⚠️thin | 7 | moderate/free | `char_genuine/human`@1 + `Infatuation`@0.44 + `vn_VULN_high`@0.22 + `vn_WARM_high`@0.14 + `vn_S_CASU_high`@0.12 | – | 5 | 0.03 | n/a |
|  |  | moderate/suppressed | `char_genuine/human`@1 + `Infatuation`@0.22 + `vn_VULN_low`@0.22 + `vn_VALN_high`@0.12 | -0.73 | 4 | 0.09 |  |
|  |  | intense/free | `char_genuine/human`@1 + `Infatuation`@0.92 + `vn_VULN_high`@0.46 + `vn_WARM_high`@0.06 | -0.73 | 5 | 0.18 |  |
|  |  | intense/suppressed | — | | | |  |
| **Pleasure Ecstasy** | 9 | moderate/free | `char_genuine/human`@1 + `Pleasure_Ecstasy`@0.92 + `vn_VULN_high`@0.2 + `vn_WARM_high`@0.15 | 1.14 | 4 | 0.23 | n/a |
|  |  | moderate/suppressed | `char_genuine/human`@1 + `Pleasure_Ecstasy`@1 + `vn_VULN_low`@0.12 + `vn_WARM_high`@0.16 | 0.77 | 6 | 0.17 |  |
|  |  | intense/free | — | | | |  |
|  |  | intense/suppressed | — | | | |  |
| **Pride** ⚠️thin | 4 | moderate/free | `char_genuine/human`@1 + `Pride`@0.75 + `vn_VULN_high`@0.22 + `vn_WARM_high`@0.14 + `vn_S_CONV_high`@0.08 | -0.56 | 4 | 0.12 | +0.01 |
|  |  | moderate/suppressed | `char_genuine/human`@1 + `Pride`@0.32 + `vn_VULN_low`@0.14 + `vn_WARM_high`@0.18 + `vn_S_CONV_high`@0.1 | -0.57 | 4 | 0.19 |  |
|  |  | intense/free | `char_genuine/human`@1 + `Pride`@1.45 + `vn_VULN_high`@0.22 + `vn_WARM_high`@0.08 | -0.40 | 4 | 0.13 |  |
|  |  | intense/suppressed | — | | | |  |
| **Relief** | 8 | moderate/free | `char_genuine/human`@1 + `Relief`@0.82 + `vn_WARM_high`@0.06 + `vn_VULN_high`@0.06 | -0.75 | 3 | 0.39 | -0.05 |
|  |  | moderate/suppressed | `char_genuine/human`@1 + `Relief`@0.35 + `vn_VULN_low`@0.05 + `vn_WARM_high`@0.18 | -0.45 | 5 | 0.05 |  |
|  |  | intense/free | `char_genuine/human`@1 + `Relief`@1.2 + `vn_VULN_high`@0.2 + `vn_WARM_high`@0.12 | -0.26 | 5 | 0.09 |  |
|  |  | intense/suppressed | `char_genuine/human`@1 + `Relief`@0.95 + `vn_VULN_low`@0.04 + `vn_WARM_high`@0.12 + `Amusement`@0.05 | -0.53 | 4 | 0.07 |  |
| **Sexual Lust** | 9 | moderate/free | `char_genuine/human`@1 + `Sexual_Lust`@0.85 + `vn_VULN_high`@0.16 + `vn_WARM_high`@0.16 + `vn_S_WHIS_high`@0.08 | -0.73 | 5 | 0.13 | +0.02 |
|  |  | moderate/suppressed | `char_genuine/human`@1 + `Sexual_Lust`@0.92 + `vn_VULN_low`@0.06 + `vn_WARM_high`@0.2 + `vn_S_WHIS_high`@0.18 + `vn_BRGT_high`@0.08 | -0.63 | – | 0.16 |  |
|  |  | intense/free | `char_genuine/human`@1 + `Sexual_Lust`@1.35 + `vn_VULN_high`@0.2 + `vn_WARM_high`@0.08 | -0.45 | 6 | 0.12 |  |
|  |  | intense/suppressed | — | | | |  |
| **Teasing** | 9 | moderate/free | `char_genuine/human`@1 + `Teasing`@0.74 + `vn_VULN_high`@0.16 + `vn_WARM_high`@0.08 + `vn_BRGT_high`@0.1 + `vn_RESP_high`@0.05 | 0.54 | 7 | 0.24 | n/a |
|  |  | moderate/suppressed | `char_genuine/human`@1 + `Teasing`@0.68 + `vn_VULN_low`@0.2 + `vn_WARM_high`@0.18 + `vn_S_PLAY_high`@0.06 | 0.88 | 4 | 0.08 |  |
|  |  | intense/free | `char_genuine/human`@1 + `Teasing`@1.35 + `vn_VULN_high`@0.28 + `vn_WARM_high`@0.12 + `vn_S_PLAY_high`@0.08 | 1.08 | 4 | 0.09 |  |
|  |  | intense/suppressed | — | | | |  |
| **Thankfulness Gratitude** | 11 | moderate/free | `char_genuine/human`@1 + `Thankfulness_Gratitude`@0.7 + `vn_VULN_high`@0.12 + `vn_WARM_high`@0.24 | 4.00 | 5 | 0.14 | +0.05 |
|  |  | moderate/suppressed | `char_genuine/human`@1 + `Thankfulness_Gratitude`@0.28 + `vn_VULN_low`@0.1 + `vn_WARM_high`@0.24 | 3.32 | 6 | 0.50 |  |
|  |  | intense/free | `char_genuine/human`@1 + `Thankfulness_Gratitude`@0.65 + `vn_VULN_high`@0.18 + `vn_WARM_high`@0.18 | 4.00 | 5 | 0.41 |  |
|  |  | intense/suppressed | `char_genuine/human`@1 + `Thankfulness_Gratitude`@0.3 + `vn_VULN_low`@0.12 + `vn_WARM_high`@0.18 + `vn_S_FORM_high`@0.05 | 3.35 | 6 | 0.45 |  |
| **Triumph** | 8 | moderate/free | `char_genuine/human`@1 + `Triumph`@0.48 + `vn_VULN_high`@0.14 + `vn_WARM_high`@0.26 | 1.11 | 3 | 0.19 | +0.02 |
|  |  | moderate/suppressed | `char_genuine/human`@1 + `Triumph`@0.22 + `vn_VULN_low`@0.04 + `vn_WARM_high`@0.28 | 1.54 | 3 | 0.08 |  |
|  |  | intense/free | `char_genuine/human`@1 + `Triumph`@0.82 + `vn_VULN_high`@0.12 + `vn_WARM_high`@0.18 | 2.06 | 3 | 0.03 |  |
|  |  | intense/suppressed | `char_genuine/human`@1 + `Triumph`@0.34 + `vn_VULN_low`@0.05 + `vn_WARM_high`@0.24 | 1.34 | 3 | 0.04 |  |

### Cognitive family — low-arousal/inward — reads weakly; "contained" = inwardness

Members (6): Astonishment Surprise, Awe, Concentration, Emotional Numbness, Interest, Intoxication Altered States of Consciousness. Moderate band **[0.5, 1.0]**, intense floor **1.2**. Mean best-naturalness across the family: **7.3/10**.

| emotion | gens | cell | recipe (over `human@1.0`) | emo | nat | GENU | ΔVULN(hof) |
|---|--:|---|---|--:|--:|--:|--:|
| **Astonishment Surprise** | 14 | moderate/free | `char_genuine/human`@1 + `Astonishment_Surprise`@0.25 + `vn_VULN_high`@0.05 | 1.10 | 4 | 0.31 | +0.01 |
|  |  | moderate/suppressed | `char_genuine/human`@1 + `Astonishment_Surprise`@0.48 + `vn_VULN_low`@0.04 + `vn_FOCS_high`@0.06 + `vn_BRGT_high`@0.12 | 3.29 | – | 0.43 |  |
|  |  | intense/free | `char_genuine/human`@1 + `Astonishment_Surprise`@0.95 + `vn_VULN_high`@0.2 | 3.31 | 4 | 0.40 |  |
|  |  | intense/suppressed | `char_genuine/human`@1 + `Astonishment_Surprise`@0.45 + `vn_VULN_low`@0.1 + `vn_FOCS_high`@0.2 + `vn_BRGT_high`@0.18 | 2.98 | 4 | 0.52 |  |
| **Awe** | 10 | moderate/free | `char_genuine/human`@1 + `Awe`@0.9 + `vn_VULN_high`@0.18 + `vn_S_WHIS_high`@0.06 | -0.56 | 4 | 0.15 | -0.16 |
|  |  | moderate/suppressed | `char_genuine/human`@1 + `Awe`@0.68 + `vn_VULN_low`@0.12 + `vn_FOCS_high`@0.08 + `vn_S_WHIS_high`@0.08 | -0.55 | 4 | 0.14 |  |
|  |  | intense/free | `char_genuine/human`@1 + `Awe`@0.46 + `vn_VULN_high`@0.12 + `vn_S_CONV_high`@0.04 | -0.58 | 4 | 0.18 |  |
|  |  | intense/suppressed | `char_genuine/human`@1 + `Awe`@0.58 + `vn_VULN_low`@0.01 | -0.58 | 7 | 0.09 |  |
| **Concentration** | 9 | moderate/free | `char_genuine/human`@1 + `Concentration`@0.4 + `vn_VULN_high`@0.16 + `vn_S_CONV_high`@0.14 + `vn_RESP_high`@0.05 + `vn_RANG_high`@0.05 | 0.31 | 7 | 0.18 | +0.04 |
|  |  | moderate/suppressed | `char_genuine/human`@1 + `Concentration`@0.34 + `vn_VULN_low`@0.05 + `vn_S_CONV_high`@0.14 + `vn_RESP_high`@0.03 + `vn_DFLU_high`@0.03 | 0.46 | 8 | 0.15 |  |
|  |  | intense/free | `char_genuine/human`@1 + `Concentration`@0.82 + `vn_VULN_high`@0.14 + `vn_S_CONV_high`@0.06 | 0.22 | 5 | 0.21 |  |
|  |  | intense/suppressed | `char_genuine/human`@1 + `Concentration`@0.52 + `vn_VULN_low`@0.06 + `vn_S_CONV_high`@0.1 + `vn_RESP_high`@0.03 + `vn_DFLU_high`@0.04 + `vn_ROUG_high`@0.03 + `vn_COGL_high`@0.05 | 0.18 | 8 | 0.18 |  |
| **Emotional Numbness** ⚠️thin | 6 | moderate/free | `char_genuine/human`@1 + `Emotional_Numbness`@0.43 + `vn_VULN_high`@0.08 | 1.31 | 7 | 0.07 | +0.04 |
|  |  | moderate/suppressed | `char_genuine/human`@1 + `Emotional_Numbness`@0.56 + `vn_FOCS_high`@0.08 + `vn_VULN_low`@0.03 | 0.68 | 6 | 0.13 |  |
|  |  | intense/free | `char_genuine/human`@1 + `Emotional_Numbness`@0.52 + `vn_VULN_high`@0.1 | 1.69 | 6 | 0.04 |  |
|  |  | intense/suppressed | `char_genuine/human`@1 + `Emotional_Numbness`@0.74 + `vn_FOCS_high`@0.06 | 1.03 | 7 | 0.11 |  |
| **Interest** | 41 | moderate/free | `char_genuine/human`@1 + `Interest`@0.98 + `vn_VULN_high`@0.08 + `vn_ESTH_high`@0.06 + `vn_S_CONV_high`@0.05 | 0.59 | 5 | 0.55 | n/a |
|  |  | moderate/suppressed | `char_genuine/human`@1 + `Interest`@0.95 + `vn_S_CONV_high`@0.02 + `vn_VULN_low`@0.01 | 0.47 | 4 | 0.14 |  |
|  |  | intense/free | `char_genuine/human`@1 + `Interest`@1.05 + `vn_VULN_high`@0.1 + `vn_ARSH_high`@0.2 | 0.35 | 7 | 0.64 |  |
|  |  | intense/suppressed | `char_genuine/human`@1 + `Interest`@0.8 + `vn_VULN_low`@0.06 + `vn_FOCS_high`@0.1 | -0.37 | 3 | 0.20 |  |
| **Intoxication Altered States of Consciousness** ⚠️thin | 4 | moderate/free | `char_genuine/human`@1 + `Intoxication_Altered_States_of_Consciousness`@1.15 + `vn_VULN_high`@0.22 + `vn_S_CONV_high`@0.2 | -0.46 | 4 | 0.29 | +0.11 |
|  |  | moderate/suppressed | `char_genuine/human`@1 + `Intoxication_Altered_States_of_Consciousness`@0.96 + `vn_VULN_low`@0.05 + `vn_S_CONV_high`@0.1 + `vn_COGL_high`@0.1 | -0.47 | 4 | 0.27 |  |
|  |  | intense/free | `char_genuine/human`@1 + `Intoxication_Altered_States_of_Consciousness`@0.95 + `vn_VULN_high`@0.2 + `vn_S_CONV_high`@0.18 | -0.17 | 3 | 0.09 |  |
|  |  | intense/suppressed | — | | | |  |

## See also

- Per-emotion conditioning manual (free/open recipes to start from): [../emotions/index.md](../emotions/index.md)
  — [Anger](../emotions/Anger.md) · [Fear](../emotions/Fear.md) · [Sadness](../emotions/Sadness.md) · [Amusement](../emotions/Amusement.md)
- VoiceNet dimension manual (VULN, TENS, COGL, FOCS, WARM, casual styles): https://laion-ai.github.io/moss-voicenet-manual/
- Emotional_Numbness page: [../emotions/Emotional_Numbness.md](../emotions/Emotional_Numbness.md) · Pain page: [../emotions/Pain.md](../emotions/Pain.md)
- The flagship intensity × containment study (listen: contained vs free, per emotion): https://laion-ai.github.io/emotion-voice-conditions/contained.html

---
[← Manual hub](../index.md)
