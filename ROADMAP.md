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
| makes testable predictions | one empirical prediction, pre-registered and tested on data not seen before; a refutation counts | **met, by a refutation**: case W1. Narrowly: it tested the literature's curve against the framework's initial slope, not the framework's bet that optimizers pursue |
| supports diagnostics, and shows its limits | one worked case, reported to `STANDARD.md` with intervals, run end to end by an outside reader | **not met**: W1's data and code are public and could serve; no report to `STANDARD.md` yet, and no outside reader |

**The one thing that matters now is the fifth row**, and then a test of the framework's own bet. Everything else waits
unless it serves one of them.

## Where we are (2026-10-03)

- The core is v11: five premises, eleven definitions, 42 propositions; 163 checks pass on both paths.
- **W1**, the first test on data not seen before (`cases/w1-best-of-n-slope/`): the machine-learning prediction from
  [P13], refuted. On 12.6 million answers, the literature's fitted best-of-`n` coefficient overstates the initial slope
  by 22%; the curve keeps the framework's initial slope up to `n = 16`, then saturates (exploratory).
- **Frozen** (`NOTES.md`, Q26): the general core at draft 3, new disciplines, any widening of the scope. Q26 set the
  freeze "until a prediction has been tested on data not seen before", which W1 now meets; lifting it is the PI's
  decision. The executor recommends keeping it until the fifth row is met as well.
- Two simulation cases checked instruments before they met the world, and each revised a prediction before its data were
  read (`cases/`): C1, coordination does not detect collusion; C2, the stopping rule finds the peak of the curve of
  optima, the first of several peaks.
- `SCENARIO.md` shows the framework applied, three ways; it is an illustration, not evidence.
- **Blocked on the PI:** the German price archive (credentials), and an outside reader (`NOTES.md` §3.2).

## Next, in order

Each step names the row it serves and what it waits for. A step that serves no row is not on this list.

| # | Step | Row | Waits for |
|---|---|---|---|
| 1 | W1 reported to `STANDARD.md`, with every field and interval, as the worked case an outside reader can rerun from public data | 5 | nothing |
| 2 | An outside reader reruns that report end to end, from `STANDARD.md`, the case folder and the public data alone | 5 | the PI finds a reader who is a person, not a Claude model |
| 3 | A test of the framework's bet, that an optimizer's behaviour is a pursuit of what it is rewarded on: trained policies with their reference model and log-probabilities, small enough for this machine, or published | 4, beyond the letter | a decision by the PI on which, and data |
| 4 | **W2**, industrial organization: register the revised prediction from [P39] (both stations adopted, against one); then run it once | 4 | the German price archive's credentials |
| 5 | Three steps with no change of scope, premise or definition | 2 | nothing: the freeze provides it |

## Not now, and why

- The general core, new disciplines, wider scope: frozen until row 4 is met.
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
