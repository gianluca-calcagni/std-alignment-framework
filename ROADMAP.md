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
| supports diagnostics, and shows its limits | one worked case, reported to `STANDARD.md` with intervals, run end to end by an outside reader | **not met**: W1 is reported to `STANDARD.md` with intervals, from public data and code (`cases/w1-best-of-n-slope/REPORT.md`); no outside reader has run it. The hold on review is lifted for one mathematical reader (Q33) |

**What matters now** (Q35, Q37): contact with the world, and a bridge from theory to practice. Contact means tests that
can fail and readers who are not the executor; the bridge means estimates a reader can compute, with intervals, from the
access a case really has. The PI asked for the bridge's engineering to be solid before some steps are actioned (Q37): a
library that computes what the standard asks, a report that can be checked as data, and a case anyone can rerun. The
theory grows where one of these needs it, and the archive of what is done is in `NOTES.md` §4.

## Where we are (2026-10-08)

- **The core** is v11: five premises, eleven definitions, 52 propositions; 184 checks pass on both paths. Nine results
  are diagnostics ([P43]–[P51]); five were used in a case, all in W4, and [P46], [P49], [P50] and [P51] in none yet.
  [P52] says what a sample certifies about misalignment, by what is known of each draw, and `STANDARD.md` now asks each
  case to declare that access. The general core is at draft 3, with a dictionary of every object from finite to
  continuous outcomes (`general/dictionary.md`).
- **Engineering** (Q37): `stdalign` 0.1, the library, holds misalignment, the revealed intensity and the split of the
  departure ([P5], [P6]), and the estimates by access with their intervals ([P23], [P47], [P52]); the checks of those
  items now run on it, and its own tests cover its interface. The rest of the standard's quantities are still computed
  by helpers inside `checks/`, and each case still carries scripts of its own.
- **Contact with the world:** one of three framework predictions tested on data not seen before held (`RECORD.md`): W1
  refuted, W3 one held and one refuted. W4 was diagnostic, and two simulation cases, C1 and C2, each revised a
  prediction before its data were read (`cases/`). Too few tests to say more than that the framework can fail.
- **Imports:** what the framework can import, ranked (`NOTES.md` §9): the heaviest is statistics (misspecified fits,
  reweighting, what samples certify). How the imports treat the continuum (`general/dictionary.md`); cooperative inverse
  reinforcement learning and its variants, mapped, with a request made without full consideration read in the core's
  objects (`NOTES.md` §10).
- **Frozen** (`NOTES.md`, Q26, Q27, Q33): new disciplines, any widening of the scope, and the general core except for
  outcomes that are not finite and estimation guarantees (step 3).
- **Licences** (Q27): the repository keeps code, aggregates and citations only: no third-party data, weights, papers, or
  item-by-item derivatives.
- **Waiting on the PI:** `REQUESTS.md`, which lists every request with the step it unblocks, and the hosts allowed.

## Next, by priority

Each step names the row it serves and what it waits for. A step that serves no row is not on this list. The engineering
steps E1–E5 come first (Q37); W5 and C3 are then built on the library rather than on scripts of their own, which also
tests the library. Steps 4–6 wait on the PI.

| # | Step | Row | Waits for |
|---|---|---|---|
| E1 | **The library, `stdalign`**: the quantities `STANDARD.md` asks for, one implementation each, which the checks verify, so that what a case imports is what was proved and mutation-tested. Done (a): misalignment, its split and its estimates by access ([P5], [P6], [P23], [P47], [P52]). Next: (b) the diagnostics [P43]–[P51]; (c) stakes, the evaluator's results and feasibility; each moved with its check pointed at it and its functions mutation-tested | 5 | nothing |
| E2 | **The report as data**: a schema for `STANDARD.md`'s three sections, a validator run by lint on every case's report, and W1's report migrated to it; a reader can then check a report field by field | 5 | E1 (b) |
| E3 | **A case anyone can rerun in a minute**: a synthetic declaration, its draws, the library, a report and the validator, run end to end by CI; the first thing an outside reader runs. With it, every world case's environment pinned in its folder, so that W1 can be rerun as `REQUESTS.md` R1 asks (`NOTES.md` §11) | 5 | E1, E2 |
| E4 | **Adapters for sequence models**: log-ratios and objectives from two causal language models, by sums over tokens, and the departure by Amini et al.'s Rao–Blackwellized estimator; an optional dependency, on which W5 runs | 4, 5 | E1 |
| E5 | **A guide for practitioners**: which access to declare, which function to call, how to read each field of the report; written from E3 | 5 | E3 |
| 1 | **W5, the stopping rule of [P20] on trained policies** (machine learning): along a sweep of `β`, the gold peaks where the covariance of proxy and gold under the optimized policy crosses zero, with several runs per `β` (as revised after C2). No public sweep exists; one is made here, on W3's reference, with W3's reward as the proxy and W4's other reward as the gold: `3.8` s per step, about 4 to 10 hours per sweep (`probes/cases/`). Next: calibrate how many steps bring each run near its optimum, then design, rehearse and register from `cases/TEMPLATE.md` | 4 | E1, E4 (Q37) |
| 2 | **C3, tampering** (simulation, Q32): a small environment, built here, where the actor can change the world or its measurement, as in the tomato-watering gridworld [@leike2017]. It checks [P51]'s bounds from finite samples against a known truth, and whether a learner trained on the signal tampers as [P50](iii) says. Second arm (H34, Q33): a monitor reading a channel the actor can influence, trained against, as Baker et al. found with chain-of-thought monitors. Light enough to run while W5 computes | 5 | E1 (Q37) |
| 3 | **Estimation, then the general core's draft 4** (Q33, Q36). Done for misalignment on finite outcomes: [P52], its limit law under each access, derived rather than imported. Next, the same for the other quantities a report gives (the pursuit part, named misalignment, [P48]'s interval), with the sample sizes they imply; then outcomes that are not finite, where [P52]'s laws need χ² divergences finite, with the conditions on tails and on existence that `general/dictionary.md` lists | 5; 2 (the count restarts) | nothing: open texts or derivations (Q36) |
| 4 | **Readers:** a person reruns W1's report end to end from `STANDARD.md`, the case folder and the public data; a mathematician reads `CORE.md` and `derived/` | 5 | the PI finds them (`REQUESTS.md`, R1), once E1–E3 are done (Q37) |
| 5 | **[P41], irreversibility of play** (experimental economics): the Jensen–Shannon divergence of a group's record of transitions from its reversal is zero within sampling error in a potential game, and positive in Rock–Paper–Scissors. The potential arm is the risky one; no public record under a comparable protocol was found (D13) | 4 | the records, from the authors (`REQUESTS.md`, R2) |
| 6 | **W2**, industrial organization: register the revised prediction from [P39] (both stations adopted, against one); then run it once | 4 | the German price archive's credentials (`REQUESTS.md`, R3) |
| 7 | Three steps with no change of scope, premise or definition | 2 | step 3, once it has changed what it changes |

**Why this order.** The PI asked for a solid engineering side first (Q37), and row 5's criterion is itself an
engineering one: an outside reader must be able to run a case end to end. E1–E3 give that reader a library, a report
that can be checked, and a case that runs in a minute; E4 and E5 serve W5 and the readers. W5 and C3 are then the only
tests the executor can run without waiting, and each can fail; built on the library, they test it too. Step 3 turns the
remaining diagnostics into numbers with intervals, and feeds E1. The readers are the binding constraint on row 5, and
only the PI can find them. [P41] and W2 are good tests, blocked on data that only the PI can obtain.

## What the PI can supply

In `REQUESTS.md`: every open request, with the step it unblocks and how to hand it over, the hosts the PI has allowed,
and what is done. Since Q36 no paper behind a paywall is asked for.

## Not now, and why

- New disciplines and wider scope: frozen by the PI (Q26, Q27).
- New results in `derived/`: only when a step above needs one. Waiting candidates: H34 (C3's second arm will test it),
  H35 (a request as evidence, a declared family), H36 (the default from how a population usually acts) (`NOTES.md`
  §5.4).
- More simulation cases: only to gate a world test, or when the PI approves one, as for C3.
- Hunches (`NOTES.md` §5.4): recorded, not pursued, unless a step above needs them.

## Drift checks

Before starting any piece of work, answer these; if an answer is "no", stop and ask the PI.
1. Which row of the finish line does this advance, through which step above?
2. Is that step unblocked? If it waits on the PI, say so once, and move to the next unblocked step.
3. Is it the smallest piece of work that moves the step? Exploration beyond it goes into a hunch, not into the turn.
4. For a test: is every threshold calibrated on the design's noise-free case, with seeds the test will not use, before
   the registration is pushed (`NOTES.md` §1)?
5. At the end of the turn: is this file's "Where we are" true, does the log below have a line, and does `REQUESTS.md`
   list every open request?

## Log

One line per turn: date, what changed, which row it served. Earlier lines are archived in `NOTES.md` §4.1.

| Date | Change | Row |
|---|---|---|
| 2026-10-07 | cooperative inverse reinforcement learning and its variants mapped to the core, and a request made without full consideration read as an evaluator coarser than the target, not a resolution (`NOTES.md` §10, Q35); the roadmap reworked: what is done archived, the next steps re-prioritized, and what the PI can supply listed | 4, 5 (priorities); 3 (imports) |
| 2026-10-08 | the PI has no academic access (Q36): imported theorems are read in open texts or derived; [P52], what a sample certifies about misalignment by what is known of each draw, derived with Huber's open paper, checked, and mutation-tested (eight mutants); the field Access in `STANDARD.md`; the requests to the PI are now hosts and data, not papers | 5 (step 3: estimation); 1 (a new check, mutation-tested) |
| 2026-10-08 | the PI asked for one file of requests and a more solid engineering side before some steps are actioned (Q37): `REQUESTS.md`; the engineering steps E1–E5 put first; `stdalign` 0.1, misalignment, its split and its estimates by access, with the checks of [P5], [P6], [P23] and [P52] pointed at it, tests of its interface, and its functions mutation-tested; the Caltech record given on 2026-10-08 corrected | 5 (E1); 1 (the library mutation-tested) |
