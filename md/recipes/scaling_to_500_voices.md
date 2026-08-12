# Scaling the voice-profile corpus to 500 voices

*Reproducible build note, Aug 2026. Self-contained: no other page in this manual is needed to
follow it. Everything below is measured on one complete reference build (voice `emolia_c1675`,
842 groups, 40,247 candidates, Slurm jobs 1305809 and 1305909) unless it is explicitly labelled
an estimate.*

## 0. What this document is

We generate, for each of a set of **reference voices**, a corpus of conditioned speech: the same
speaker rendered under 832 named conditions (emotions, perceptual voice dimensions, non-verbal
edge cases, character archetypes, sports commentary, adult register), in English and German, with
many candidate takes per condition, every candidate stored and scored. One voice exists today.
This page is the plan and the cost model for **500**, written so an outside reader can reproduce
it, and so that the one defect that would silently ruin the run is caught before compute is spent.

**Model**: `laion/moss-tts-local-transformer-4.55b-voice-acting-v2`, a 4.55 B expressive
voice-acting TTS. Conditions are expressed as a natural-language caption plus a set of LoRA
adapters merged at measured strengths. **Hardware**: JUPITER (JSC), GH200 nodes, 4 GPUs per node.

| | value |
|---|--:|
| Conditions per voice | **832** |
| Candidates per condition | **48** (subset A 32 + subset B 16) |
| Candidates per voice | **39,936** nominal, **39,927** measured (99.98 % yield) |
| Voices | **500** |
| **Total candidates** | **19,963,500** |
| Total generated audio | **40,408 h** |
| Distinct written sentence pairs (EN/DE) per voice | **15,312** for the matrix, 15,472 including the burst addendum |
| Stage 1 (text) | **146 GPU-h** = 10,478 core-h |
| Stage 2 (audio) | **15,731 GPU-h** = 1,132,642 core-h |
| **Total** | **15,877 GPU-h = 1,143,120 core-h** |
| Fraction of REFORMO remainder (68,709,721 core-h) | **1.66 %** |
| Fraction of LAIONIZE remainder (37,569,231 core-h) | **3.04 %** |
| Storage | **3.02 TB** |
| Wall clock on 64 nodes | **2.6 days** |

---

## 1. What the corpus is

### 1.1 The 832 conditions

Built by `vpspec.build_matrix()`. Every block is crossed with `{EN, DE}`.

| block | conditions | groups |
|---|---|--:|
| Emotions | 40 emotions × {intense, moderate} × {free, contained} × 2 languages | **320** |
| VoiceNet dimensions | 57 perceptual dimensions × 4 levels × 2 languages | **456** |
| Edge cases | 14 non-verbal deliveries (screams, groans, sobbing, shivering, laughter, whimpering) × 2 | **28** |
| Character clusters | 12 character LoRAs × 2 | **24** |
| Sports commentator | × 2 | **2** |
| Explicitness | × 2, behind an age safety gate | **2** |
| **total per voice** | | **832** |

The four emotion conditions are labelled `A` intense/free, `B` moderate/free, `C`
intense/contained, `D` moderate/contained. The four VoiceNet levels are `extremely_low`,
`moderately_low`, `moderately_high`, `very_high`.

A separate **10-group addendum** (`vpspec.build_burst_isolated`) covers the 5 vocal-burst classes
that measurably never fire mid-utterance (`hiss`, `kissing_noises`, `lip_smack`,
`person_whistling_playfully`, `slurping_noises`) as isolated events, × 2 languages. It is
deliberately **not** part of the 832 so the matrix count cannot drift.

### 1.2 The two subsets, which are the whole point

Each group produces **48 candidates in two subsets that answer different questions**.

| | subset A | subset B |
|---|---|---|
| candidates per group | **32** | **16** |
| sentence source | that **condition's own** pool (`cond_key`) | that condition's **parent** pool (`parent_key`) |
| sentences | **32 different** sentences, one per candidate | **16** sentences, **shared across all sub-conditions of the parent** |
| purpose | breadth: 32 usable pre-training samples per condition | controllability: minimal pairs, same words under a different condition |
| pools per voice | 416 language-independent conditions (+5 addendum) | 125 parents |
| written pairs | 416 × 32 = **13,312** | 125 × 16 = **2,000** |

`cond_key` drops the language component of the group id, so **EN and DE draw the same pool index
and are therefore parallel translations of one another**. `parent_key` additionally drops the
condition or level, so `E|Bitterness|A`, `|B`, `|C`, `|D` all share one B pool: the same 16
sentences are spoken intensely and freely, then moderately and contained, and the difference in
the audio is the condition and nothing else.

Both are ranked **within subset** (`vpgen.py`, `for sub in ("A", "B")`), because A's 32 distinct
sentences and B's 16 shared ones are not comparable pools and a single ranking would let one
crowd out the other.

The plan's own arithmetic for why A exists: today 32 generations yield **one** selected take.
Under subset A those same 32 generations yield **32** usable samples, which is roughly 17× less
compute per usable pre-training sample, at the cost of each individual clip sitting at the
distribution mean rather than its maximum.

---

## 2. The defect that blocks the run, and how it is verified

> **Verified 2026-08-12.** The profile published today was generated **without any A/B split at
> all**. It is 32 takes of a single sentence per group. The correct artefacts exist for a
> different voice, and the 500-voice run must use that path.

### 2.1 What went wrong

`vpgen.py::_build_plan` has a deliberate early-return for groups that carry their own single
line, used by ablation arms and hand-written groups:

```python
if "cond_key" not in g:
    ...
    line = g["text"]
    for k in range(args.cands):
        plan.append(dict(subset="A", sub_idx=k, text=line, ...))
    return plan
```

The published profile `k325_age3_bg1` was generated from
`$NB/vprof/work/groups_k325_age3_bg1.rewritten.json`. Measured:

| file | groups | with `cond_key` | with `caption_tmpl` | distinct texts |
|---|--:|--:|--:|--:|
| `groups_k325_age3_bg1.rewritten.json` | 808 | **0** | **0** | 224 |
| `groups_k325_age3_bg1.json` | 808 | **0** | **0** | 221 |
| `groups_emolia_c1675.json` | **832** | **832** | **832** | (pool-driven) |

Because no group carries `cond_key`, **every group took the early return**, `--texts` was never
consulted, and each group became 32 identical-text takes. The visible consequence, measured per
block on the published file:

| block | groups | distinct texts | texts per group |
|---|--:|--:|--:|
| VoiceNet | 456 | **114** | one per dimension × language, shared across all four levels |
| Emotions | 320 | **80** | one per emotion × language, shared across A/B/C/D |
| Edge | 28 | 26 | |

114 = 57 dimensions × 2 languages. So the demo grid shows **the same sentence down every level of
every VoiceNet dimension**, and the ladder that page is supposed to demonstrate is being asked to
show itself with the words held constant by accident rather than by design. That is subset B's
job, on 16 sentences, alongside subset A's 32 different ones. Here it is the only thing present.

The failure is silent in one direction and loud in the other, which is why it survived: a group
list **without** `cond_key` run without `--texts` produces a plausible-looking corpus, whereas a
group list **with** `cond_key` run without `--texts` raises
`RuntimeError: no texts for <gid>` on the first group.

### 2.2 The artefacts the 500-voice run will use

Both verified by direct inspection:

| artefact | measured |
|---|---|
| `$NB/vprof/work/groups_emolia_c1675.json` | 832 groups; **832/832** carry `cond_key`, `parent_key` and `caption_tmpl`; 416 distinct `cond_key`, 125 distinct `parent_key`; 169 distinct adapter keys |
| `$NB/vprof/work/texts_emolia_c1675.json` | `A`: **421 pools × exactly 32** entries = 13,472; `B`: **125 pools × exactly 16** = 2,000; 15,472 entries total |

(421 = the 416 matrix conditions plus the 5 isolated-burst conditions of the addendum.)

Every pool entry carries `en`, `de`, `en_tagged`, `de_tagged`, `n_words_en`, `n_words_de`,
`burst`, `domain`, `hard`, `safety_blocked`, plus `sid`, `subset`, `key`, `idx`, `block`,
`target_words`, `seed_en`.

This path has been **run end to end**: `$NB/vprof/full/emolia_c1675/PFULL` is a complete build,
842 groups, 40,247 candidates, and its parquet confirms the split held in production.

| check on the completed run | result |
|---|--:|
| groups with subset A = 32 | 838 of 842 |
| groups with subset A = 31 | 4 (all DE; see §3.4) |
| groups with subset B = 16 | 827 of 842 |
| groups with subset B = 15 | 5 (all DE) |
| groups with subset B = 0 | 10, the isolated-burst addendum (no B pool exists for it, by construction) |
| distinct texts, VoiceNet block | **16,405** across 456 groups (was 114) |
| distinct texts, emotion block | **11,515** across 320 groups (was 80) |
| errors | **0** |

**The 500-voice run uses the `vpprep2.py` → `vptext.py` → `vptextmerge.py` → `vpgen.py --texts`
path.** The pre-flight checklist in §8 asserts it, and every assertion there has been executed
against these files.

---

## 3. Stage 1: text generation

**Text generation must complete before any audio is generated.** The pools are an input to
`vpgen.py`, not a by-product of it. Owner: `vptext.py` (per-GPU shards) and `vptextmerge.py`
(merge and verify). Model: `google/gemma-4-E4B-it`, batch 128.

### 3.1 What each slot is asked for

Every one of the 15,472 slots gets a length target, a domain, and a brief. 90 % are **paraphrases
seeded by a different FineTranslations sentence**, drawn domain-round-robin so that one
condition's 32 sentences span the taxonomy instead of clustering; the prompt asks for a rewrite
whose *content* gives a real reason that the condition holds ("the speaker genuinely feels
bitterness", "it would naturally be spoken with a very high degree of TEMP"). The seeding exists
because a freely-prompted model collapses each emotion onto one topic and destroys domain
balance. Measured: 14 seed domains at 994–995 slots each.

### 3.2 The 10 % hard-for-TTS split

10 % of slots are generated from ten domains that are hard to *say*, at 1 % each. Measured on the
built pools: **1,547 of 15,472 = 10.00 %**, split 154–155 per domain.

| hard domain | measured slots |
|---|--:|
| `mathematics` | 155 |
| `numbers_units` | 155 |
| `dates_times` | 155 |
| `abbreviations` | 155 |
| `homographs` | 155 |
| `proper_nouns` | 155 |
| `code_switching` | 155 |
| `urls_code` | 154 |
| `slang_profanity` | 154 |
| `jargon` | 154 |

These are written in **spoken form**, which is the entire point: the model must learn to *say*
"the square root of two", so the text must contain those words and not the glyph. The prompt
forbids symbols and digits explicitly, and `SYMBOL_RE` post-filters, because a model told not to
emit symbols still does. Measured: **11 of 1,547 hard lines** still contained a symbol on the
first pass, all 11 were retried with a blunter instruction, and **0 hard lines remained
symbol-bearing**. Three non-hard lines still contain a digit or symbol out of 15,472; they have
not been repaired.

### 3.3 Length control and bucketing

Each slot is assigned one of three word-count buckets, 13 / 21 / 31 words, so that a batch of 64
has a narrow length spread. This is not cosmetic: a sub-batch runs to the frame budget of its
longest member, so an unsorted batch of different sentences costs **1.86×** the same-text batch
while a word-count-sorted one costs **1.35×**. Measured on the built pools: EN mean 18.7 words,
median 18; DE mean 18.6, median 18.

### 3.4 EN/DE parallelism

German is **translated from the English rewrite**, never rewritten independently, so the two are
the same sentence. Verified on the built pools:

| check | measured |
|---|--:|
| entries with both EN and DE non-empty | 15,466 / 15,472 |
| DE byte-identical to its seed, i.e. translation failed and the fallback fired | **0** |
| true translation pairs | **15,466 = 99.961 %** |
| entries with an empty DE line | **6** |

All six empty DE lines are `urls_code` hard-domain slots where the translator returned nothing
for a spelled-out URL. `vpgen` skips a candidate whose line is blank, which is exactly the 4
groups at A=31 and 5 groups at B=15 in §2.2. This is a known, bounded, 0.04 % loss.

### 3.5 Vocal bursts

Inline burst tags are placed **after** translation, so the translator cannot mangle them, and only
at a strictly interior position (never opening or closing a line). Per-class quotas over the 59
inline-capable classes are fixed **first**; emotion fit then decides only *where* each class's
quota is spent. Doing it the other way round concentrates the common classes and starves the rest.
One class per text key, because a burst-carrying take swaps the emotion adapter for the burst
adapter and sprinkling 12 classes through one group's 48 candidates would mean 12 adapter loads
per group.

| check | measured |
|---|--:|
| entries carrying a burst | **2,635 / 15,472 = 17.0 %** |
| distinct classes used | **59 / 59** |
| per-class count | min 25, max 62 |
| never-fire classes leaked into the inline rotation | **none** |

**Correction to the plan.** `corpusplan.py` states a density of "every second sentence carries
1–2 bursts". What is implemented and what shipped is `BURST_TEXT_FRACTION = 0.25` per key, and the
measured realised density is **17.0 %**, not 50 %. The shortfall between 25 % and 17 % is bursts
dropped because no interior position existed in *both* languages. Either the plan text or the
constant should be changed before the 500-voice run; they currently disagree and the constant
wins.

### 3.6 The safety rule

Two gates, both measured:

- **Before generation.** A seed sentence that `mentions_minor()` is **re-paired away** from any
  sexual or romantic slot (`P|` explicitness, and the `Infatuation`, `Sexual_Lust`,
  `Pleasure_Ecstasy`, `Affection`, `Teasing` emotion keys) and replaced with a clean pool
  sentence. Measured: **18 seeds re-paired** across the four shards (7 / 4 / 3 / 4).
- **After generation.** `unsafe_output()` rejects any rewrite combining a minor reference with
  sexual content; the slot falls back to its seed and is flagged `safety_blocked`. Measured:
  **3 rejections** across 15,472 slots.

Separately, the **explicitness block is gated on the reference voice, not on the text**: three
independent checks must all pass (Empathic-Insight Age head on the reference audio ≥ 2.0, VoiceNet
`AGEV` ≥ 2.40, and the voice card must not match `UNDERAGE_WORDS`). The gate result is written to
`safety_gate.json` per shard and the 2 explicitness groups are skipped when it fails. The AGEV
cutoff is 2.40 rather than the anchor-implied 3.0 because the regressor is measurably biased low
against the human-written age cards: measured over all 6,064 reference voices, AGEV separates
card-labelled minors from adults at AUC 0.843, and a 3.0 cutoff would exclude 49.3 % of
card-labelled adults while still passing 7.2 % of card-labelled minors.

### 3.7 Stage 1 cost

Measured on Slurm job 1305809, one node, 4 GPUs, 4 shards of 3,868 slots each:

| quantity | measured |
|---|--:|
| generations per voice | 15,472 EN + 15,472 DE + 11 retries = **30,955** |
| pure generation time, summed over the 4 GPUs | **926 GPU-s = 0.2573 GPU-h** |
| throughput | **120,315 generations / GPU-h** (≈ 33 lines/s/GPU) |
| job as actually billed (1 node × 11 min 31 s) | 0.192 node-h = **0.768 GPU-h** = 55.3 core-h |

The gap between 0.257 and 0.768 GPU-h is model loading plus the deliberate 150 s stagger (§7.3),
which is 63 % of a one-voice job and amortises to nothing when work is packed.

**500 unique text sets**: 15,477,500 generations, **128.6 GPU-h** of pure generation. Packed as
32 single-node array tasks, each node runs 1.14 h wall, so **145.5 GPU-h billed = 10,478 core-h**.

A single shared text set for all 500 voices would cost 0.77 GPU-h instead of 146. The text stage
is **0.92 % of the total GPU-hours either way**, so there is no cost argument for sharing, and 500
distinct sets is the recommendation. What has *not* been decided, and cannot be read off any
artefact, is whether the corpus wants 500 distinct sets or a smaller number sampled across voices;
this page prices the 500-set option and flags the choice as open.

---

## 4. Stage 2: audio generation

### 4.1 The worker model

`vpgen.py`: **one process owns one GPU and one shard of one voice's group list**. Groups are
sorted by `(block, emotion|dim|edge, condition|level, lang)` and sliced **contiguously**, not by
stride, so consecutive groups share adapters. A stride would hand each worker groups
`nshards` apart in the sorted order and thrash the LoRA loader on every single group, which is
exactly what the sorting exists to prevent. At most `MAX_RESIDENT_ADAPTERS = 24` adapters stay
loaded, LRU-evicted.

Within a group, candidates are bucketed by **adapter stack**, not by index: the group's own stack
runs as one sub-batch and the burst-carrying candidates (which drop the emotion adapter and add
`burst_<class>@0.5`) run as another. Inside a sub-batch, items are sorted by word count before
batching, which is where the 1.35× rather than 1.86× premium comes from.

Batch size is **64** (`--batch 64`). Note that the *effective* batch is bounded by the sub-batch
size, so a 48-candidate group with one burst stack runs roughly 40 + 8, not 64. The batch-64
microbenchmark below therefore over-states the achievable rate, and §5 uses the measured
end-to-end rate instead.

### 4.2 What is scored, per candidate

Every candidate is sensed and stored, not just the winner: 57 VoiceNet dimension regressions and
buckets, 40 EmoNet emotion heads, 4 quality heads, a 768-d VoiceCLAP embedding, a 192-d ECAPA
speaker embedding and its cosine to the reference, Whisper `large-v3-turbo` ASR and WER
(`large-v3-turbo` and not `small`, because half this corpus is German and small's German WER
becomes the ranking signal instead of a check on it), duration, words-per-second, and a procedural
caption written from what was *measured* rather than what was asked for.

### 4.3 The ranking formula actually in use

Verbatim from `vpgen.py`, with `w_blend = 0.6` for contained conditions and `1.0` otherwise:

```
reward = (genuineness + w_blend * blend + 1.25 * strength) * (1 - min(WER, 1))
reward += 0.5 * z(-VULN)                       # contained conditions only

over    = dur / clip(n_words / 2.8, 1.5, None)
durceil = 1 / (1 + clip(over - 1.6, 0, None)**2)     # length-fit ceiling
durmul  = clip(dur / 3.0, 0, 1)**2                   # duration floor, MIN_DUR = 3.0 s
idrank  = 0.81 + 0.19 * clip(spk_sim, 0, 1) / 0.7    # identity is RANKED, weight 0.19
idmul   = 0.25 if spk_sim < 0.40 else 1.0            # only the floor rejects

score   = reward * durmul * durceil * idrank * idmul
```

`strength` is the target emotion head for emotion groups, the signed target dimension for VoiceNet
groups, a **band fit** rather than a maximum for the moderate conditions (they are scored for
*landing*, not for maximising), and **zero** for character groups, whose target is a voice and not
a feeling.

Three properties are deliberate and each was paid for:

- **Raw, not z-scored.** Re-ranking 28,698 stored candidates showed z-scoring normalises blend
  *within* a group, so a group whose takes are all poorly blended still hands its best one a good
  z-score and blend stops competing across groups. Raw moved median winner blend 3.65 → 4.74
  (+30 %) and emotion strength 1.78 → 1.87. The cost is genuineness: median winner 0.738 → 0.626,
  about 15 %. That is a real trade and it is recorded rather than buried.
- **`× (1 − WER)`, not the manual's `/ (1 + WER)`.** Measured on the same 28,698 candidates, the
  inverse form is too lenient to hold a runaway take down: swapping the forms moved 28 of 808
  winners and made runaway takes *more* common (18 vs 14 over 2.5× expected length).
- **A length-fit ceiling instead.** With it, takes over 2.5× expected length drop 14 → 7 while the
  blend gain from raw scoring is kept in full.

The older z-scored score is still computed and stored as `score_z` so nothing already measured
becomes unreproducible.

### 4.4 Where the time actually goes

Measured over all 842 groups of the reference build:

| stage | GPU-h | share of billed |
|---|--:|--:|
| generation (`t_gen`) | **24.22** | 76.4 % |
| sensing and scoring (`t_score`) | **0.76** | 2.4 % |
| adapter load, mp3 encode, tar and parquet writes | 2.39 | 7.5 % |
| model + sensor loading and the 150 s stagger | 4.34 | 13.7 % |
| **billed total** | **31.71** | 100 % |

Scoring is **3.1 % of generation + scoring**, which is why no effort has been spent on it. Per
block, cost per candidate is between 1.2 s (sports) and 3.0 s (explicitness), with VoiceNet at
2.33 s and emotions at 2.15 s.

---

## 5. Cost model, in GPU-hours

### 5.1 The conversion, stated once

JUPITER's booster nodes carry **4 GH200 GPUs**, and Slurm bills the **whole node** at **288
core-hours per node-hour** regardless of how many GPUs are busy. Therefore:

```
1 node-hour = 4 GPU-hours = 288 core-hours
1 GPU-hour  = 72 core-hours
```

Always pack 4 workers per node. Running one GPU per node quadruples every core-hour figure below
for identical output.

### 5.2 Batch size is the largest single lever

Measured on this exact workload (LoRA merged, reference conditioning, `pipe_bench_b*.json`):

| batch | × realtime | ms / clip |
|---|--:|--:|
| 8 | 3.92 | 1254 |
| 16 | 5.69 | 859 |
| 32 | 7.69 | 637 |
| **64** | **8.88** | **543** |

2.3× for a one-line change, no new engine, LoRA adapters still working. Batch 64 is the default.

A retracted claim, kept so it is not re-derived: an earlier version of the cost page carried a
"pipelined decode, 18.8×" column taken from a benchmark of a *different* workload (one repeated
prompt, batch 256, no adapters, no reference conditioning). The port was written and measured on
the real workload and produced **1.01×**. Decode is not a meaningful share of this loop.

### 5.3 The measured throughput to plan with

| run | texts per group | in-worker gen/GPU-h | × realtime | mean take |
|---|---|--:|--:|--:|
| `rewritten` (`k325_age3_bg1`) | 1 sentence, 32 takes | 1,814 | 3.98 | 7.89 s |
| **`full` (`emolia_c1675`), A+B** | **32 + 16 different** | **1,471** | **2.99** | **7.31 s** |

The ratio of the two realtime figures is **3.98 / 2.99 = 1.33×**, which independently confirms the
1.35× word-count-bucketing premium the plan assumed. It also means that premium is **already
inside** the 1,471 figure and must not be applied again. `corpusplan.py` takes 1,500 gen/GPU-h
from the *slowest single shard* of the same-text run and then multiplies the cost by 1.35, which
double-counts; its 500-voice estimate of 1.36 M core-h is about 19 % above what the completed A+B
build actually cost.

**The planning rate used here is the billed one**, because it is the only number that maps to
Slurm accounting:

| | value |
|---|--:|
| candidates | 40,247 |
| in-worker wall (`throughput-*.json`) | 27.37 GPU-h → 1,471 gen/GPU-h |
| Slurm elapsed × 4 GPUs (jobs 1305909_0..3) | **31.71 GPU-h → 1,269 gen/GPU-h** |
| billed core-hours for one complete voice | **2,283** |

### 5.4 Stage costs for 500 voices

| | candidates | GPU-h | core-h | % REFORMO | % LAIONIZE |
|---|--:|--:|--:|--:|--:|
| Stage 1, text (500 distinct sets) | 15,477,500 lines | **146** | **10,478** | 0.02 % | 0.03 % |
| Stage 2, audio | 19,963,500 | **15,731** | **1,132,642** | 1.65 % | 3.01 % |
| **Total** | | **15,877** | **1,143,120** | **1.66 %** | **3.04 %** |

Against the two budgets combined (106,278,952 core-h remaining) the build is **1.08 %**.

Per voice: **31.75 GPU-h, 2,286 core-h, 6.04 GB**.

| budget | remaining core-h | expires | this build |
|---|--:|---|--:|
| REFORMO | 68,709,721 | 2026-12-31 | 1.66 % |
| LAIONIZE | 37,569,231 | 2027-04-30 | 3.04 % |

REFORMO expires first and is the larger pool, so spend REFORMO. On the current run-rate a large
part of it will otherwise expire unspent.

### 5.5 Wall clock

3,933 node-hours of audio generation.

| nodes | wall clock |
|---|--:|
| 32 | 5.1 days |
| **64** | **2.6 days** |
| 128 | 1.3 days |

---

## 6. Output data formats

### 6.1 Never loose files

At 500 voices the corpus is **19,963,500 audio objects**. Written as individual files on a shared
parallel filesystem that is a metadata denial-of-service against yourself and everyone else on the
machine. Everything goes into **WebDataset tar shards plus parquet**:

| | loose | as built |
|---|--:|--:|
| objects for 500 voices | 19,963,500 | **8,000 tars + 8,000 parquet = 16,000** |

One tar and one or more parquet files per shard, 16 shards per voice.

### 6.2 Audio

**MP3, 160 kbps CBR, 48 kHz, mono, at the model's native rate.** Encoded with `libmp3lame`
directly, because libsndfile's MP3 writer takes a 0–1 "compression level" rather than a bitrate.

The scorers all want 16 kHz, so a 16 kHz copy is what gets *scored*, but the 16 kHz copy is not
what gets *stored*: an earlier version stored the downsampled signal, band-limiting the corpus to
8 kHz, and the HTML builders then re-encoded that to 40 kbps, giving two lossy passes over an
already band-limited signal. Pages now embed the stored bytes unchanged.

Measured: **20,265 bytes per second of audio** including tar headers, against the 20,000 B/s a
160 kbps stream implies.

### 6.3 Metadata: one parquet row per candidate

The current worker writes **76 columns**. (The reference build predates the length-fit ceiling and
carries 71; the five added since are `dur_mult`, `dur_ceil`, `over_len`, `score_z`, `reward`.)

| group | columns |
|---|---|
| identity | `gid`, `voice`, `profile`, `block`, `lang`, `emotion`, `condition`, `dim`, `level`, `edge`, `character`, `cond_key`, `parent_key`, `subset`, `sub_idx`, `cand`, `audio_key`, `ref_variant`, `ref_spk_emb_ref` |
| text | `text`, `text_en`, `text_de`, `text_slot`, `caption`, `domain`, `hard_domain`, `burst_class`, `emotion_adapter_dropped` |
| recipe | `adapters` (JSON), `sampling` (JSON), `mediathek` |
| audio | `dur`, `empty`, `wps` |
| ASR | `asr`, `wer` |
| perceptual, summarised | `genuineness`, `blend`, `quality`, `emo_strength`, `emo_argmax` |
| perceptual, full | `emonet` (**40** EmoNet heads, JSON), `voicenet` (**57** dimensions, JSON), `voicenet_bucket` (57), `quality_full` (4 heads: `content_enjoyment`, `overall_quality`, `speech_quality`, `background_quality`) |
| VoiceNet shortcuts | `vuln`, `tempo`, `chunk`, `dflu`, `arou`, `expl`, `tens`, `narration`, `dim_target` |
| embeddings | `voiceclap` (**768**-d, fp16), `spk_emb` (**192**-d ECAPA, fp16), `spk_sim` |
| ranking | `rank`, `score`, `reward`, `score_z`, `core`, `strength_raw`, `z_genuineness`, `z_blend`, `z_strength`, `z_containment`, `naturalness`, `id_mult`, `dur_mult`, `dur_ceil`, `over_len`, `w_blend`, `contained`, `moderate` |
| caption | `caption_gen`, the procedural caption written from measurements |

The reference speaker embedding is identical on every row of a shard, so it is stored once as
`ref_spk_emb.npy` rather than 40,000 times.

### 6.4 Total bytes

Measured on the complete reference build and scaled by candidate count:

| | per candidate | per voice (832 groups) | **500 voices** |
|---|--:|--:|--:|
| audio (tar) | 148,122 B | 5.91 GB | **2.96 TB** |
| metadata (parquet) | 3,217 B | 0.128 GB | **64 GB** |
| sidecars (`groupstats`, `identity`, `throughput`, `safety_gate`, `ref_spk_emb`) | | 0.6 MB | 0.3 GB |
| **total** | **151,339 B** | **6.04 GB** | **3.02 TB** |

Alongside: 40,408 hours of audio, and 7.74 M written EN/DE sentence pairs (15.5 M lines), which
are a few hundred MB of JSON and do not move the total.

---

## 7. Reproducibility

`$NB` is `/e/data1/datasets/playground/mmlaion/schuhmann1/dramabox`. All Python runs under
`$NB/env_transcribe/bin/python`.

### 7.1 Environment, identical in every job

```bash
NB=/e/data1/datasets/playground/mmlaion/schuhmann1/dramabox
export HF_HOME=$NB HF_HUB_CACHE=$NB/hfcache/.cache/dramabox
export HUGGINGFACE_HUB_CACHE=$NB/hfcache/.cache/dramabox
export HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 TMPDIR=$NB/tmp
export XDG_CACHE_HOME=$NB/hfcache/xdg TRITON_CACHE_DIR=$NB/hfcache/triton
export TOKENIZERS_PARALLELISM=false PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True
```

**Compute nodes have no outbound internet.** Every Hugging Face asset must be fetched on the login
node first, and `HF_HUB_OFFLINE=1` makes a missing asset fail immediately with a cache error
instead of hanging on a connection timeout. Prefetch is `$NB/vprof/code/prefetch.py` and
`prefetch2.py`. The assets are: the base model, the MOSS audio tokenizer, 40 emotion LoRAs, 114
VoiceNet dimension LoRAs, 64 vocal-burst LoRAs, the character LoRA repo, the sports and
explicitness LoRAs, `openai/whisper-large-v3-turbo`, `speechbrain/spkrec-ecapa-voxceleb`,
`laion/Empathic-Insight-Voice-Plus`, `google/gemma-4-E4B-it`, the reference-voice dataset and the
FineTranslations German subset.

### 7.2 The four commands, in order

**Step 0, login node, per voice.** Builds the 832-group matrix, the 10-group addendum and a
per-voice manifest, and extracts the reference audio at the best-DNSMOS variant.

```bash
$NB/env_transcribe/bin/python $NB/vprof/code/vpprep2.py --voice <cid> --cands-a 32 --cands-b 16
# asserts len(groups) == 832; writes work/groups_<cid>.json, groupsiso_<cid>.json,
#                                    manifest_<cid>.json
```

`vpprep2.py` writes a **per-voice** manifest. There used to be one shared `manifest.json`, which
every running worker re-reads at startup, so preparing a second voice while a job was in flight
swapped the reference wav out from under it.

**Step 1, text.** 4 GPUs, 4 shards, then merge and verify.

```bash
for i in 0 1 2 3; do
  CUDA_VISIBLE_DEVICES=$i $NB/env_transcribe/bin/python -u $NB/vprof/code/vptext.py \
    --voice <cid> --shard $i --nshards 4 --batch 128 > logs/vptext_g$i.log 2>&1 &
  sleep 150
done; wait
$NB/env_transcribe/bin/python -u $NB/vprof/code/vptextmerge.py <cid>
# writes work/texts_<cid>.json and prints the EN/DE pairing rate, hard-domain symbol
# leakage, burst balance, safety rejections and short-pool report
```

**Step 2, smoke test.** One GPU, a handful of groups from every block including character and a
burst-carrying one, at small N. Two full runs were burned by skipping this.

```bash
$NB/env_transcribe/bin/python -u $NB/vprof/code/vpgen.py --voice <cid> --profile SMOKE \
  --manifest $NB/vprof/work/manifest_<cid>.json \
  --groups   $NB/vprof/work/groups_smoke_<cid>.json \
  --texts    $NB/vprof/work/texts_<cid>.json \
  --mth-lambda 0 --cands 4 --cands-b 2 --batch 8 --shard 0 --nshards 1 --out $NB/vprof/smoke
```

**Step 3, the full build.** 4 array tasks × 1 node × 4 GPUs = 16 shards, per voice.

```bash
#SBATCH --account=reformo --partition=booster --nodes=1 --gres=gpu:4
#SBATCH --ntasks=1 --cpus-per-task=64 --time=10:00:00 --array=0-3
for i in 0 1 2 3; do
  SHARD=$(( SLURM_ARRAY_TASK_ID * 4 + i ))
  CUDA_VISIBLE_DEVICES=$i $NB/env_transcribe/bin/python -u $NB/vprof/code/vpgen.py \
    --voice <cid> --profile FULL \
    --manifest $NB/vprof/work/manifest_<cid>.json \
    --groups   $NB/vprof/work/groups_all_<cid>.json \
    --texts    $NB/vprof/work/texts_<cid>.json \
    --mth-lambda 0 --cands 32 --cands-b 16 --batch 64 \
    --shard $SHARD --nshards 16 --out $NB/vprof/full &
  sleep 150
done; wait
```

`--mth-lambda 0`: the Mediathek German LoRA is **not** merged. A 13,760-generation sweep found
0.25 / 0.50 / 0.75 indistinguishable from zero and λ = 1.00 producing runaway takes 69 % of the
time; the apparent +0.815 genuineness gain was a scorer artefact.

### 7.3 The 150 s stagger, which is not politeness

Four concurrent `import transformers` plus four model loads off the `/e` filesystem put **every**
worker into uninterruptible D state. At a 45 s stagger this cost a 45-minute dead job. 150 s per
worker within a node is the working value. The stagger is **per node**, so array tasks still start
in parallel and only the four workers inside one node are staggered.

### 7.4 Sharding and seeds

Groups are sliced contiguously: `chunk = ceil(len(groups) / nshards)`, worker `s` takes
`groups[s*chunk : (s+1)*chunk]`. Seeds are derived from the group id, so a shard boundary moving
does not change any group's output:

```python
seed = (zlib.crc32(g["gid"].encode()) % 100000) * 1000 + 7000 + gi
torch.manual_seed(seed + 7919 * sub_batch_index)
```

`gi` is the group's index *within the shard*, so re-sharding does perturb the seed; the group id
term dominates and reproducibility is at the level of "the same shard layout reproduces exactly".

### 7.5 Resume

A worker writes `shard<NNN>.DONE` and appends one JSON line per group to
`groupstats-<NNN>.jsonl`. On restart it reads that file and skips completed groups. A **failed**
group is explicitly *not* counted as done: it writes a row carrying its gid, and an earlier
unconditional `done.add(d["gid"])` turned any transient failure into a permanent hole no restart
could fill.

---

## 8. Pre-flight checklist

Run all of it on the login node before submitting 500 voices. Every command below has been
executed against the reference artefacts and the expected outputs are what those runs printed.

### 8.1 The group list carries the A/B keys

```bash
$NB/env_transcribe/bin/python - <<'EOF'
import json, collections
W="/e/data1/datasets/playground/mmlaion/schuhmann1/dramabox/vprof/work"
g=json.load(open(f"{W}/groups_emolia_c1675.json"))
assert len(g)==832, len(g)
for k in ("cond_key","parent_key","caption_tmpl"):
    n=sum(1 for x in g if k in x)
    assert n==len(g), f"{k}: only {n}/{len(g)}"
print("groups", len(g), collections.Counter(x["block"] for x in g))
print("cond_key", len({x["cond_key"] for x in g}), "parent_key", len({x["parent_key"] for x in g}))
EOF
```

```
groups 832 Counter({'voicenet': 456, 'emotion': 320, 'edge': 28, 'character': 24, 'sports': 2, 'explicit': 2})
cond_key 416 parent_key 125
```

**If `cond_key` is 0, stop.** That is the defect in §2 and the run will silently produce 32 takes
of one sentence per group.

### 8.2 Pool sizes, EN/DE parallelism, word floor, bursts, hard-domain share

```bash
$NB/env_transcribe/bin/python - <<'EOF'
import json, collections, statistics
W="/e/data1/datasets/playground/mmlaion/schuhmann1/dramabox/vprof/work"
T=json.load(open(f"{W}/texts_emolia_c1675.json")); A,B=T["A"],T["B"]
assert all(len(v)==32 for v in A.values()), "A pool not 32"
assert all(len(v)==16 for v in B.values()), "B pool not 16"
assert all(sorted(x["idx"] for x in v)==list(range(32)) for v in A.values())
assert all(sorted(x["idx"] for x in v)==list(range(16)) for v in B.values())
e=[x for s in (A,B) for v in s.values() for x in v]; n=len(e)
print(f"A {len(A)} pools x32 = {sum(map(len,A.values()))}, B {len(B)} pools x16 = {sum(map(len,B.values()))}")
both=sum(1 for x in e if x["en"].strip() and x["de"].strip())
fell=sum(1 for x in e if x["de"].strip()==(x.get("seed_de") or "").strip() and x["de"].strip())
print(f"EN/DE pairs {both-fell}/{n} = {100*(both-fell)/n:.3f}%  empty DE {n-both}  seed-fallback {fell}")
short=sum(1 for x in e if x["n_words_en"]<10 or x["n_words_de"]<10)
print(f"under the 10-word floor in either language: {short} = {100*short/n:.2f}%")
bc=collections.Counter(x["burst"][0] for x in e if x["burst"])
print(f"bursts {sum(bc.values())} = {100*sum(bc.values())/n:.1f}%, {len(bc)} classes, "
      f"min {min(bc.values())} max {max(bc.values())}")
hd=collections.Counter(x["hard"] for x in e if x["hard"])
print(f"hard {sum(hd.values())} = {100*sum(hd.values())/n:.2f}%, {len(hd)} domains {sorted(hd.values())}")
print(f"safety_blocked {sum(1 for x in e if x['safety_blocked'])}")
EOF
```

```
A 421 pools x32 = 13472, B 125 pools x16 = 2000
EN/DE pairs 15466/15472 = 99.961%  empty DE 6  seed-fallback 0
under the 10-word floor in either language: 298 = 1.93%
bursts 2635 = 17.0%, 59 classes, min 25 max 62
hard 1547 = 10.00%, 10 domains [154, 154, 154, 155, 155, 155, 155, 155, 155, 155]
safety_blocked 3
```

**The word floor does not currently pass.** `vpspec.MIN_WORDS = 10` is documented and enforced on
every hand-written text table (`chartexts.py`, `expltexts2.py`, `mkexp3.py` all assert it), but
`vptext.py` does **not** enforce it on generated lines: 82 English and 261 German lines fall below
10 words, 298 entries in total. The shortest English line is 6 words. See §11.

### 8.3 Every adapter key resolves in the local cache

There is no outbound internet on the compute nodes, so an unresolved key is a dead job, and PEFT's
error for a config-without-weights directory is `Repo id must be in the form 'repo_name'...`,
which points nowhere near the cause.

```bash
HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 $NB/env_transcribe/bin/python - <<'EOF'
import json, sys
NB="/e/data1/datasets/playground/mmlaion/schuhmann1/dramabox"
sys.path.insert(0, f"{NB}/vprof/code"); import vpgen
W=f"{NB}/vprof/work"
keys=set()
for f in ("groups_emolia_c1675.json","groupsiso_emolia_c1675.json"):
    for g in json.load(open(f"{W}/{f}")): keys |= set(g["adapters"])
T=json.load(open(f"{W}/texts_emolia_c1675.json"))
for s in ("A","B"):
    for v in T[s].values():
        for x in v:
            if x["burst"]: keys.add("burst_"+x["burst"][0])
bad=[]
for k in sorted(keys):
    try: vpgen.adapter_dir(k)
    except Exception as ex: bad.append((k, str(ex)[:100]))
print(f"resolved {len(keys)-len(bad)}/{len(keys)}"); [print("MISSING",*b) for b in bad]
EOF
```

```
resolved 233/233
```

**169** of those come from the 832-group matrix itself (40 emotion + 114 VoiceNet + 12 character +
`char_human` + `sports` + `explicit`), 5 from the isolated-burst addendum, and **59** are burst
adapters reachable only through the text pools. Checking the matrix alone would miss a third of
them.

### 8.4 Safety gate on the reference voice

```bash
grep -h SAFETY $NB/vprof/full/<cid>/PFULL/../*/*.log | head
cat  $NB/vprof/full/<cid>/PFULL/safety_gate.json
```

Expect `explicit_allowed` true or a `reason` naming which of `ei_age_ok`, `agev_ok`, `card_ok`
failed. A failing gate skips exactly the 2 explicitness groups and is not an error.

### 8.5 After the smoke run, before the array

```bash
$NB/env_transcribe/bin/python - <<'EOF'
import glob, pandas as pd
d=sorted(glob.glob("/e/data1/datasets/playground/mmlaion/schuhmann1/dramabox/vprof/smoke/*/PSMOKE/meta-*.parquet"))
df=pd.concat([pd.read_parquet(p) for p in d], ignore_index=True)
print("columns", len(df.columns))
print(df.groupby(["gid","subset"]).size().unstack(fill_value=0))
print("distinct texts per group:", df.groupby("gid").text.nunique().describe())
EOF
```

`distinct texts per group` **must equal the candidate count**, not 1. A count of 1 is the §2
defect reappearing.

---

## 9. Quality control

| control | value | where |
|---|---|---|
| Duration floor | `MIN_DUR = 3.0 s`, applied as `clip(dur/3, 0, 1)**2` | ranking |
| Length-fit ceiling | expected `words / 2.8` wps, free up to 1.6×, quadratic falloff beyond | ranking |
| Minimum words per line | `MIN_WORDS = 10` | text side, **not currently enforced by `vptext.py`** |
| Speaker floor | `SPK_FLOOR = 0.40`, score × 0.25 below it; identity otherwise **ranked** at weight 0.19 | ranking |
| Resample flag | `SPK_RESAMPLE = 0.58` | recorded, not acted on automatically |
| Empty decode | detected, counted per group as `n_empty`, never assumed away | worker |
| All-caps guard | every plan line passes `denorm_caps`; only the quoted SCRIPT line, never `GENERAL:`/`SCRIPT:` | worker |
| WER reference | inline tags stripped in **all three** notations before scoring | `BURST_TAG_RE` |

The duration floor crushes short takes rather than banning them, so a group where every candidate
is short still resolves to its best member instead of ranking arbitrarily. It exists because
nothing in the older score preferred a longer take and short takes had a perverse advantage: fewer
words means fewer chances to misread, so WER trends to zero and the perceptual terms are computed
over a nearly silent clip.

### 9.1 The publishing rule that is easy to get wrong

`audio_key` is only `<gid>.cNNN.mp3` and is **not unique across runs**: two different run
directories mint the same names. Exporting the winning take by matching `audio_key` alone means
whichever tar is scanned first wins, and the result is a page whose scores come from the current
run and whose audio comes from an older one. That happened: 89 regenerated groups played their
pre-regeneration take under a "NEW" badge, with metadata claiming 5.76 s over a 0.24 s clip.

**Match on the pair `(source_dir, audio_key)`, clear the output directory before writing, and
assert each exported file's size is consistent with the duration its metadata claims** (≈ 20 kB
per second at 160 kbps). `profilepage.py` does all three.

### 9.2 Per-cell adoption, on group means

When a regeneration recipe is evaluated against a baseline, adoption is decided **per cell**
(recipe × language) on the **mean over all 32 candidates of each group**, not on the top-1 take,
and the decision is then applied blind to every group in that cell. Cells whose delta is not
positive revert to the original take with no badge.

Two reasons, both recorded in `mkupdated3.py`: the ranking formula changed between rounds, so
top-1 would measure the recipe and the ranker together; and picking the better run group-by-group
selects on exactly the noise being measured. A cell is a rule decided by 32 to 2,048 candidates
and then applied blind. Note honestly that the threshold is literally `delta > 0` with no
significance test and no margin.

---

## 10. Voice conversion is not in the default path

The profiles sound best **without** Chatterbox voice conversion. VC is **not** run in the
500-voice build. It exists only as an optional repair for an individual group whose selected take
falls below `SPK_VC = 0.45` speaker similarity, and even then it is kept only if ECAPA similarity
rises **and** DNSMOS does not fall. `costmodel.py` still budgets a VC twin for the top-3 of every
character group; that budget is **not** carried into the figures in §5, and the character block is
generated once, straight.

---

## 11. Risks and open problems

**Blocking, must be fixed or consciously accepted before the run.**

1. **The word floor is not enforced on generated text.** 298 of 15,472 pool entries (1.93 %) fall
   below `MIN_WORDS = 10` in at least one language: 82 EN, 261 DE, shortest 6 words. At ~2.8
   words/s a line under 8 words cannot fill three seconds however slowly it is read, and the
   duration floor then crushes those candidates in the ranking. Measured on the completed build,
   **482 of 39,927 candidates (1.21 %)** were spoken from a line under 10 words; their mean score
   is **0.084 against 0.137** for the rest, and 39 of them landed under `MIN_DUR`. Across 500
   voices that is **241,000 substantially devalued generations**. The fix is a post-filter and
   re-ask in `vptext.py`, mirroring the retry loop the hard domains already have.
2. **`vpgen.py` does not verify that `--texts` was supplied and matches the group list.** Omitting
   it is loud for a correct group list and silent for a legacy one. A three-line assertion at
   startup (`if any("cond_key" in g for g in groups): assert TEXTS["A"]`) removes the entire class
   of failure that produced today's published profile.
3. **The burst density in the plan and in the code disagree** (50 % vs `BURST_TEXT_FRACTION =
   0.25`, realised 17.0 %). Decide which is intended.

**Known and accepted.**

4. **Six empty German lines** per text set, all `urls_code` hard-domain slots, costing 9 groups one
   candidate each. 0.04 %.
5. **The character block draws from the generic sentence pool.** `chartexts.py` holds 24
   hand-written in-character lines precisely because a pool sentence about a gym membership fights
   a dragon adapter, but it is not wired into `vptext.py`. Measured: the `C|dragon` A-pool opens
   with a sentence about a Higher Regional Court judgment. 24 of 832 groups.
6. **Speaker identity degrades at high emotion λ.** `LAMBDA_INTENSE` reaches 1.9 for seven
   emotions, and ECAPA similarity to the reference falls sharply above ~1.25; the intense
   conditions of those emotions average **below** the 0.40 reject floor. Nothing is dropped, every
   take is stored and flagged, and a downstream user must filter on `spk_sim`. Over the reference
   build the mean `spk_sim` is 0.322 and **72.9 %** of candidates sit below 0.40. This is the
   single largest quality caveat on the corpus and it is not fixed by scale.
7. **German conditioning is weaker than English.** Measured over 323,200 candidates on the earlier
   build: mean speaker similarity **0.376 DE vs 0.578 EN**. Half the corpus is the weaker half.
8. **No human listening study.** Everything called "quality" here is the automatic sensor stack,
   which agrees with a human listener at roughly ρ ≈ +0.21 on spoken material. Every ranking claim
   inherits that.
9. **The hard-domain list is a taxonomy, not a literature review.** Ten domains chosen from known
   TTS normalisation failure modes; no fresh survey was done.
10. **The character-cluster selection is editorial.** The plan budgets 12 character LoRAs and never
    names them; the public mirror ships 120 adapters with no per-adapter metadata to select on. The
    12 were chosen by rule (drop the numbered `voice-NN` timbres, drop `human` because it is
    already the scaffold, then take 12 maximally distinct archetypes with at most one of any
    near-duplicate family). There is no measured quality signal behind that choice.
11. **Throughput is measured on one voice.** The 1,269 gen/GPU-h billed figure comes from a single
    complete build. Group-to-group and voice-to-voice variance is real; the four array tasks of
    that build ranged 1.92 h to 2.02 h wall, so the spread is small, but 500 voices will include
    references that behave differently.
12. **Sensor and adapter versions must be pinned.** 500 voices is days of wall clock across many
    jobs. A silently updated Whisper, ECAPA or VoiceNet head part-way through makes the corpus
    internally incomparable, which is the one failure mode that cannot be repaired after the fact.
    `HF_HUB_OFFLINE=1` plus a frozen cache directory is the mechanism; verify the cache is not
    refreshed between jobs.

---

*Part of the [MOSS voice-acting manual](../index.html). See also
[prompt notation](prompt_notation.html) for the bracket, capitalisation and line-length rules the
text pipeline has to satisfy, and [text carries the condition](text_carries_the_condition.html)
for what the written line can and cannot do for a condition.*
