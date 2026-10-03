# Roadmap

The anchor against drift. Read it first in every session, and before starting any new piece of work; update it at the
end of every turn. `NOTES.md` holds the executor's working notes and the history; this file holds only the goal, where
the framework stands against it, and what comes next.

## The goal

A standard formal framework for alignment problems in general, not only in machine learning: solid enough to build on,
substrate-independent, easy to import existing theorems into, and able to make testable predictions, support
diagnostics, and show its own limits (`README.md`). The framework is a standard, not only a checked calculus, when every
row of the finish line is met.

| Goal | Criterion (`README.md`) | State |
|---|---|---|
| solid | lint and every check pass on both SIMD paths; new checks are mutation-tested | met |
| stable | neither the scope nor a premise's or definition's Statement changes for three consecutive steps | not met: the scope changed in v11 |
| easy to import into | every item of the archive has a recorded fate | met |
| makes testable predictions | one empirical prediction, pre-registered and tested on data not seen before; a refutation counts | **met**: W1 refuted a prediction about the literature's curve; W3 tested the framework's bet itself, on a model tuned by PPO, and the bet held in part (one prediction held, one refuted). Three predictions tested on unseen data, one held |
| supports diagnostics, and shows its limits | one worked case, reported to `STANDARD.md` with intervals, run end to end by an outside reader | **not met**: W1 is reported to `STANDARD.md` with intervals, from public data and code (`cases/w1-best-of-n-slope/REPORT.md`); no outside reader has run it, and external review is on hold (Q27) |

**What matters now:** confidence, as the PI asked (Q27): more tests of the framework's bet on public data, each
registered before it is computed, until the base rate says something; then the outside reader, when the PI lifts the
hold. Everything else waits unless it serves one of them.

## Where we are (2026-10-03)

- The core is v11: five premises, eleven definitions, 47 propositions; 172 checks pass on both paths. The five new
  results are diagnostics (`derived/diagnostics.md`, Q28): misalignment at any intensity and across conditions at one
  intensity; what named objectives explain; drift between runs; what runs share between evaluation and use; the cost of
  reweighting. Each follows from earlier results; no premise or definition changed.
- **Base rate: one of three** predictions tested on data not seen before held (`RECORD.md`). Too few to say anything,
  beyond that the framework can fail.
- **W1** (`cases/w1-best-of-n-slope/`): the prediction from [P13] about best-of-`n`, refuted. On 12.6 million answers,
  the literature's fitted coefficient overstates the initial slope by 22%; the curve keeps the framework's initial slope
  up to `n = 16`, then saturates (exploratory). Reported to `STANDARD.md` in `REPORT.md`, exploratory, since its
  declaration was written after the data were seen: about three quarters of best-of-`n`'s departure from the default is
  misalignment against the gold, at every `n`.
- **W3** (`cases/w3-ppo-pursuit/`), the first test of the bet that an optimizer pursues what it is rewarded on: a public
  GPT-2 tuned by PPO on a sentiment reward. It pursues the reward in the reward's own scale (S2 held), with a slope near
  `1/β`, but within prompts the reward explains only `0.358` of what the tuning changed (S1 refuted: the registered
  threshold was a half), and `0.10` to `0.12` within each model's own continuations (exploratory). By the framework's
  own measure, most of that model's departure from its reference is misalignment against its reward.
- **Frozen** (`NOTES.md`, Q26, Q27): the general core at draft 3, new disciplines, any widening of the scope. Q26's
  condition is met; the PI keeps the freeze, to build more confidence first. No external reviews yet.
- **Licences** (Q27): the repository keeps code, aggregates and citations only; no third-party data, weights, papers, or
  item-by-item derivatives. W1's proxy weights and per-prompt statistics were removed from the tree; they remain in two
  earlier commits until the PI decides on a force-push.
- Two simulation cases checked instruments before they met the world, and each revised a prediction before its data were
  read (`cases/`): C1 and C2.
- `SCENARIO.md` shows the framework applied, three ways; it is an illustration, not evidence.
- **Blocked on the PI:** the German price archive (credentials, W2); the history purge (a force-push); the outside
  reader (on hold).

## Next, in order

Each step names the row it serves and what it waits for. A step that serves no row is not on this list.

| # | Step | Row | Waits for |
|---|---|---|---|
| 1 | **W4**, where W3 left the bet: is W3's off-reward change systematic or drift? Two public PPO runs from one reference, `lvwerra/gpt2-imdb`: `gpt2-imdb-pos-v2` (W3's, 2023, DistilBERT reward) and `gpt2-imdb-pos` (2020, BERT reward `lvwerra/bert-imdb`, 5-token prompts, 15-token answers; provenance read in TRL's history, commit `f299b5c`). Not replicates: their rewards differ, so the design names the other reward as an objective. On 5-token prompts and 15-token continuations, inside both training distributions: the drift between the runs ([P45], in nats, from their own draws), and the named misalignment of W3's model ([P44]) with, in order, `log π_ref` (sharpening), the other reward, and the other run's revealed objective; costs set by [P47]. Directions, with estimates and intervals; no round thresholds (`cases/README.md`, design rules) | 4, beyond the letter | the rehearsal on synthetic data (rule 4), which also tells whether reweighting is affordable on this machine; then registration and one run |
| 2 | **W2**, industrial organization: register the revised prediction from [P39] (both stations adopted, against one); then run it once | 4 | the German price archive's credentials |
| 3 | An outside reader reruns W1's report end to end, from `STANDARD.md`, the case folder and the public data alone | 5 | the PI lifts the hold on external review (Q27) and finds a reader who is a person |
| 4 | Three steps with no change of scope, premise or definition | 2 | nothing: the freeze provides it |

## Not now, and why

- The general core, new disciplines, wider scope: frozen by the PI (Q26, Q27), although row 4 is met.
- New results in `derived/`: only if a test on the list above needs one to be stated.
- More simulation cases: only to gate a named world test, at most one per test, before that test runs.
- Hunches (`NOTES.md` §5.4): recorded, not pursued, unless a step above needs them.

## Drift checks

Before starting any piece of work, answer these; if an answer is "no", stop and ask the PI.
1. Which row of the finish line does this advance, through which step above?
2. Is that step unblocked? If it waits on the PI, say so once, and move to the next unblocked step.
3. Is it the smallest piece of work that moves the step? Exploration beyond it goes into a hunch, not into the turn.
4. For a test: is every threshold calibrated on the design's noise-free case, with seeds the test will not use, before
   the registration is pushed (`NOTES.md` §1)?
5. At the end of the turn: is this file's "Where we are" true, and does the log below have a line?

## Log

One line per turn: date, what changed, which row it served.

| Date | Change | Row |
|---|---|---|
| 2026-10-03 | consolidation; v11; the freeze; `cases/` and R14; cases C1 and C2, both revising a prediction before data; `SCENARIO.md`; this roadmap | 4 (instruments checked); 5 (scenario) |
| 2026-10-03 | the PI supplied Coste et al.'s paper; read; W1's data located, and its access blocked on one network domain | 4 (step 1) |
| 2026-10-03 | W1: proxy trained and frozen; procedure calibrated on synthetic prompts; registered; run once on 12.6 million unseen answers; refuted. The framework's first test on unseen data | 4: met, by a refutation |
| 2026-10-03 | licence rule applied (Q27); W1 reported to `STANDARD.md`; W3 designed, calibrated, registered and run once on a public PPO model: the bet held in part; consolidation | 4 (the bet tested); 5 (the report) |
| 2026-10-03 | retrospective of W1 and W3 (`NOTES.md` §6); five design rules for cases; five diagnostic results derived from the core, P43–P47 (Q28); W4 designed, its second run's provenance traced | 4 (W4); 5 (diagnostics) |
