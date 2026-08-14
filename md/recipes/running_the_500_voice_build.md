# Running the 500-voice build on a supercomputer

*Execution note, Aug 2026. The companion to [Scaling the voice-profile corpus to 500
voices](scaling_to_500_voices.md), which is the plan and the cost model. This page is what
actually happened when the plan was run: the Slurm array shape, the worker stagger, how a voice
that dies is made re-runnable, the throughput measured at scale, and the two defects the run
found in the corpus that had already shipped.*

Hardware: JUPITER (JSC), `booster` partition, GH200 nodes, 4 GPUs per node, whole-node billing.

---

## 0. The shape in one table

| | value |
|---|---|
| Voices | **500** |
| Groups per voice | **842** (832 matrix + 10 burst-isolated) |
| Candidates per voice | **40,256** (832 x 48, 10 x 32) |
| Candidates total | **20,128,000** |
| Slurm arrays | **2** — text, then generation |
| Array elements | **one voice each**, `0-499` |
| Nodes held concurrently | **160** (`%160` throttle) |
| GPUs per element | 4, one worker each via `CUDA_VISIBLE_DEVICES` |
| Worker stagger inside a node | **150 s** (generation), 210 s (text) |
| Measured generation throughput | **1,405–1,481 gen/GPU-h** |
| Measured cost per voice | **28.65 GPU-h** in-process, **31.2 GPU-h** billed |
| Storage per voice | 5.7–6.1 GB (4 WebDataset tars + parquet) |

---

## 1. One voice per array element

The obvious design is to slice: 500 voices over 64 elements, 8 voices each. Don't.

`MaxArraySize` on this cluster is 1001, so 500 elements is **one job**, not 500 jobs, and it
costs the scheduler nothing extra. What it buys is that **the unit of failure equals the unit of
re-queue**. A 26-hour run across 160 nodes *will* lose nodes. With 8-voice slices, one bad node
orphans seven healthy voices along with the one that was mid-flight, and the sweeper's only
options are to redo all eight or to open up the slice. With one voice per element, a dead node
costs exactly one voice.

```bash
#SBATCH --nodes=1
#SBATCH --gres=gpu:4
#SBATCH --cpus-per-task=64
#SBATCH --time=12:00:00
#SBATCH --array=0-499%160

V=$(python -c "import json;print(json.load(open('voices_all500.json'))[$SLURM_ARRAY_TASK_ID])")
```

**Sizing the throttle.** Total node-hours are fixed by the work, so the throttle only chooses
wall clock and how much of the machine you hold at once. 500 x 7.79 node-h = 3,895 node-h, so
128 nodes is ~30.5 h and 160 is ~24.4 h. Pick against the QOS wall limit, not against the
partition size: here `part_boost` caps an element at **12 h** while an element needs **7.8 h**,
so the run is throughput-limited, not wall-limited, and there is 4 h of headroom for a slow voice
before anything has to be re-queued at all.

---

## 2. The 150-second stagger, and why it is not optional

Four workers starting at once on one node each load, from a shared parallel filesystem: a 4.55 B
TTS model, Whisper-large-v3-turbo, ECAPA, and the perceptual scorer stack. Doing that
concurrently puts **every worker on the node into uninterruptible sleep (D state)**. Not slow —
wedged. On this project a 45-second stagger produced a dead 45-minute job.

```bash
for i in 0 1 2 3; do
  CUDA_VISIBLE_DEVICES=$i python -u vpgen.py --shard $i --nshards 4 ... &
  sleep 150
done
wait
```

The cost is real and worth stating: 450 s of the ~7.8 h element is spent sleeping, about 1.6 %.
On the **text** stage, where the actual work per GPU is only ~2 minutes, a 3 x 210 s stagger is
**10.5 of the 17 minutes**. That looks like an obvious thing to optimise — run four *different*
voices on the node instead, one per GPU, at `--nshards 1`. Don't do that either: the shard index
decides which slots each worker owns, so changing it changes the generated texts. Pay the
stagger; it is 2.5 % of the run.

---

## 3. Per-voice resumability

Three layers, and they do different jobs.

**Layer 1 — shard markers, written by the worker.** Each of the 4 workers writes
`shard00N.DONE` on clean exit and returns immediately if it finds one. This makes a re-submitted
element cheap.

**Layer 2 — group-level resume, from the data.** Each worker appends one JSON line per finished
group to `groupstats-00N.jsonl` and, on start, reads it back to skip what it already did. The
subtlety that cost this project three runs:

> A **failed** group must not count as done. It writes a row carrying its `gid` too, so an
> unconditional `done.add(d["gid"])` turns any transient failure — a missing adapter, an OOM —
> into a permanent hole that no restart can ever fill.

```python
if d.get("error") or d.get("skipped") == "retry":
    n_err += 1
    continue          # will be retried
done.add(d["gid"])
```

**Layer 3 — the voice-level gate, written by a verifier and by nothing else.** A clean process
exit is not the same as a whole voice. `VOICE.DONE` is written only when **all five** hold:

1. four shard markers present;
2. 842 distinct gids in the groupstats;
3. 40,256 parquet rows, all `audio_key` distinct;
4. 40,256 tar members, no duplicates;
5. **the parquet key set and the tar member set are the same set.**

Check 5 is not implied by 3 and 4. A restart that wrote one group's audio twice and its rows once
passes both counts and fails only the set comparison. Verify per voice and report the short ones
by name — an aggregate hides exactly what it should surface, since 499 whole voices and one at
12,000 candidates still reports 99.95 % of the expected total.

**The sweeper.** After the array drains, re-verify all 500 from the data, write the short ones to
a fresh list, submit a new array over exactly those, repeat. Two rules make it safe:

* **never two writers on one voice.** The tar is opened in append mode; two processes appending
  interleave members and produce a file whose members are individually readable and collectively
  wrong. So the sweeper waits for the previous round to leave the queue, and it is the only
  submitter.
* **stop when a round makes no progress twice.** That means the failure is systematic and a human
  should look, rather than the sweeper burning another 160 nodes on it.

---

## 4. Adapter cache: sort the groups, not the queue

With 114 dimension adapters, 40 emotion adapters and an LRU of resident adapters, thrashing the
loader is the easiest way to waste a GPU-hour. Sort each voice's groups so consecutive groups
share adapters, then hand each worker a **contiguous** slice:

```python
groups.sort(key=lambda g: (g["block"], g.get("emotion") or g.get("dim") or g.get("edge") or "",
                           g.get("condition") or g.get("level") or "", g["lang"]))
chunk = -(-len(groups) // args.nshards)
groups = groups[args.shard * chunk:(args.shard + 1) * chunk]
```

A **stride** (`groups[shard::nshards]`) is the trap: it hands each worker groups N apart in the
sorted order, so no two consecutive groups share an adapter and the loader thrashes on every
single group — undoing the sort completely. Ordering the *voices* across the array does nothing,
because each element is a fresh process with a cold adapter cache either way.

---

## 5. Measured throughput

From the ten `throughput-*.json` files of one complete 10-voice build, all at 40,256 candidates
over 842 groups:

| voice | GPU-h | gen/GPU-h |
|---|--:|--:|
| emolia_c1699 | 26.31 | 1,530 |
| k91_age5_bg0 | 27.28 | 1,476 |
| emolia_c1682 | 27.44 | 1,467 |
| anime_088 | 27.90 | 1,443 |
| emolia_c0542 | 27.98 | 1,439 |
| k325_age3_bg1 | 28.22 | 1,426 |
| k10_age3_bg1 | 28.91 | 1,393 |
| k395_age3_bg1 | 29.06 | 1,385 |
| emolia_c2570 | 31.07 | 1,296 |
| mediathek_0184 | 32.34 | 1,245 |

Mean **28.65 GPU-h** per voice at **1,405 gen/GPU-h**.

**Report the billed number, not this one.** Whole-node billing counts wall clock, and `sacct`
gives the same ten elements a mean elapsed of **7.79 h x 4 GPUs = 31.2 GPU-h** — about **9 %**
above the in-process figure. The gap is model load, the stagger, and the node waiting on the
slowest of its four shards. Budget with the billed number.

Text stage: **~17 min per voice per node** = 1.13 node-h, of which ~10.5 min is stagger.

---

## 6. Two defects this run found in the corpus that had already shipped

Both were found by comparing the new build against the previous one **at the same stage with the
same measurement**, which is the only comparison worth making. Both were silent.

### 6.1 Title-Case burst tags — the model spells them out

The manual's [prompt notation](prompt_notation.md) rule is *never capitalise a tag*: `(SCREAM)`
is read out letter by letter instead of performed. The text generator was emitting
**Title Case** — `(Snort)`, `(Hiccup)`, `(Deep Breathing)` — and the generation stage was run
with `tag_case=keep`, which faithfully kept them.

Measured: **5,157 to 5,220 Title-Case tags per voice**, across every voice in the shipped build.
Every one is a burst the model spelled out instead of performing. Combined with the WER trap on
the same page — the reference stripper only removes `\(...\)`, so a mis-formed tag stays in the
reference and the take is charged word-error for not pronouncing "snort" — the ranker was
actively **selecting against** the takes the tags were added to help.

The fix is one line at the text stage (emit lowercase at source), and it is invisible unless you
count tag case explicitly. **Count it.**

### 6.2 Burst density falling ~30 % short of the configured value

`BURST_TEXT_FRACTION = 0.50` — every second sentence carries a burst. The realised density was
**33.3 %**. The quota is set by `assign_bursts`, but `place_bursts` silently drops a burst
whenever it cannot find an interior position **in both languages** (the position rule is: never
open or close a line on a burst). Short lines have no interior position, so they lose their
burst — and nothing logs a failure, because a dropped burst is a normal outcome of the placement
rule.

Enforcing the 10-word minimum on generated lines lifted the realised density to **44.1 %**,
measured identically. Still short of 0.50, which is the honest state of it.

**The general lesson:** a knob whose realised value is produced by a *lossy* downstream step is
not a setting, it is a request. Measure the realised value, not the configured one, and put the
measurement where someone will see it.

---

## 7. Provenance when the code is not in git

The corpus should record, per voice: the reference clip, the seed, the recipe version and the
generator's commit. If the code tree is not version-controlled, do not skip the field — record a
**SHA-256 of every source that can change a candidate** plus a combined fingerprint. That is
strictly more precise than a commit id, because it also pins the spec module and the scorer.

Two details worth copying:

* **Exclude the job scripts from the fingerprint.** They choose *which* voice runs with *which*
  flags, not what a candidate becomes. Including them makes the fingerprint move on a comment
  edit — which is how one run nearly ended up split across two fingerprints for a reason that
  never touched the data. Pin the flags by value in a frozen recipe file instead.
* **Freeze the recipe by value, not by reference.** Reading a live `recipe.json` at job start is
  right when the ablation that chooses it has not finished yet. Over a 24-hour run it is a
  hazard: one edit halfway through and the corpus is quietly two recipes. Snapshot it, and abort
  rather than guess if the snapshot is missing.

Seeds are **derived, not drawn** — `seed = (crc32(gid) % 100000) * 1000 + 7000 + group_index`,
then `torch.manual_seed(seed + 7919*b)` per sub-batch. Record the *rule*; that is the
reproducible part.

---

## 8. Store every candidate, and every component of its score

Not just the winner. The corpus keeps all 40,256 candidates per voice with 76 columns: every
VoiceNet score, EmoNet, genuineness, blend, the VoiceCLAP embedding, the speaker embedding and
its cosine to the reference, the ASR transcript, the procedural caption — and **every component
of the score** separately (`strength_raw`, `w_blend`, `z_containment`, `contained`, `dur`, `wer`,
`spk_sim`, `dur_mult`, `id_mult`, `over_len`, …), not only the total.

That is what makes a re-ranking free. This corpus was re-ranked onto a new objective
(target-weight 2.0) **with zero regeneration**, because every input to the old score was still on
disk. A corpus that stores only the winner and the final score cannot do that, and re-earning the
option costs the full 15,000 GPU-h.

Format: WebDataset tar for audio (MP3, **48 kHz, 160 kbps CBR** — verify with a probe, not with
the spec) plus parquet for metadata. No loose files: 20 M small files on a parallel filesystem is
its own outage.

> **`audio_key` is `<gid>.cNNN.mp3` and is NOT unique across runs.** The same key is minted by
> every run of the same voice. Key on **(run directory, audio_key)** everywhere audio is matched
> to metadata, and keep separate runs in separate directories so the distinction is physical
> rather than a convention. This has already shipped as a bug once: 89 regenerated groups served
> their *pre*-regeneration audio under a "NEW improved" badge, and one group whose metadata said
> 5.76 s played 0.24 s.

---

## 9. Pre-flight, in the order that catches things cheapest

1. **Count the work list and check it against its source.** `set(all) - set(done)` should
   reproduce the todo list exactly.
2. **Resolve every input on the login node.** Compute nodes have no internet. Three of twelve
   reference shards were missing from the local cache here, covering 78 voices — which would have
   surfaced as 78 elements dying hours in. Open every tar and confirm every member you will need
   is actually in it.
3. **Reconstruct any undocumented input and verify the reconstruction byte-for-byte** against
   existing artefacts before trusting it. One required file was produced by an un-scripted
   one-liner; `json.dumps(a + b, ensure_ascii=False)` reproduced all eleven existing copies
   exactly, which is what made it safe to generate 500 more.
4. **Smoke 2–3 voices end to end**, chosen to cover *source types the previous build did not*.
   Verify parquet rows, tar members, the two as sets, the column list, and the audio bitrate with
   a probe. Confirm the completeness gate **refuses** the smoke run — a gate only proven to
   accept is not proven.
5. **Never `pip install` without `--no-deps`** on a shared venv. It has silently downgraded torch
   here.
6. Only then submit the array.
