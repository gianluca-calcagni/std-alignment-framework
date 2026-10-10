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
| stable | neither the scope nor a premise's or definition's Statement changes for three consecutive steps, a step being a merged pull request (Q46) | not met: [[A2 — Pursuit is the steepest climb\|A2]]'s Statement changed in v12 (Q44); met once three pull requests merged after the one that made v12 change no Statement and no scope |
| easy to import into | every item of the archive has a recorded fate | met |
| makes testable predictions | one empirical prediction, pre-registered and tested on data not seen before; a refutation counts | **met**: W1 refuted a prediction about the literature's curve; W3 tested the framework's bet itself, on a model tuned by PPO, and the bet held in part (one prediction held, one refuted). Three predictions tested on unseen data, one held |
| supports diagnostics, and shows its limits | one worked case, reported to `STANDARD.md` with intervals, run end to end by an outside reader | **not met**: W1 is reported to `STANDARD.md` with intervals, from public data and code (`cases/w1-best-of-n-slope/REPORT.md`), and its environment is pinned; no outside reader has run it. The hold on review is lifted for one mathematical reader (Q33), and the reader package is ready (H2) |

**What matters now** (Q35, Q37): contact with the world, and a bridge from theory to practice. Contact means tests that
can fail and readers who are not the executor; the bridge means estimates a reader can compute, with intervals, from the
access a case really has. The PI asked for the bridge's engineering to be solid before some steps are actioned (Q37): a
library that computes what the standard asks, a report that can be checked as data, and a case anyone can rerun. All
three are in place (Q41). The theory grows where one of these needs it, and the archive of what is done is in `NOTES.md`
§4.

## Where we are (2026-10-10)

- **The core** is v12, [[A2 — Pursuit is the steepest climb|A2]] now saying that the geometry of pursuit is Riemannian (Q44): five premises, eleven
  definitions, 52 propositions; 98 checks of the items, and 130 tests of the tools, the scenario, the library and the
  quickstart, pass on both paths. Nine results are diagnostics ([[P43 — Misalignment at any intensity|P43]]–[[P51 — What signals, audits and re-measurements reveal of tampering|P51]]); five were used in a case, all in W4, and
  [[P46 — What runs share between conditions, and what they do not|P46]], [[P49 — Outer and inner misalignment|P49]], [[P50 — Tampering: a change of the measurement, not of the world|P50]] and [[P51 — What signals, audits and re-measurements reveal of tampering|P51]] in none yet. [[P52 — What a sample certifies about misalignment, by access|P52]] says what a sample certifies about misalignment, by what is known of
  each draw, and `STANDARD.md` now asks each case to declare that access. The general core is at draft 3, with a
  dictionary of every object from finite to continuous outcomes (`general/dictionary.md`).
- **Engineering** (Q37, Q41): `stdalign` 0.2, the library, holds misalignment, the revealed intensity and the split of
  the departure ([[P5 — Misalignment is attained, and zero exactly on the intended behaviours and their limits|P5]], [[P6 — The departure from the default splits into pursuit and misalignment|P6]]), the estimates by access with their intervals ([[P23 — The estimated misalignment of an actor that pursues the objective|P23]], [[P47 — The cost of reweighting|P47]], [[P52 — What a sample certifies about misalignment, by access|P52]]), and the diagnostics
  [[P43 — Misalignment at any intensity|P43]]–[[P51 — What signals, audits and re-measurements reveal of tampering|P51]] with the projection of [[P15 — Misalignment splits into what the actor could avoid and what it could not|P15]]; the checks of those items run on it, its own tests cover its interface, and
  its functions are mutation-tested. A report can be written as data and checked by `stdalign/report.py`; lint R16 holds
  every case's report to it, and W1's is the first. `examples/quickstart.py` runs a case on simulated data, from the
  declaration to a valid report, in under a minute, and CI runs it. Every case pins its environment, which lint R14
  checks against its scripts' imports. Stakes, the evaluator's results and feasibility are still computed by helpers
  inside `checks/` (E1(c)). The executor's tools are in the repository (Q40): `tools/mdwrap.py`, `tools/mutate.py` with
  the mutant lists of `tools/mutants/`, `tools/overview.py`, and `CLAUDE.md`.
- **The reader package** (H1, H2): `OVERVIEW.md`, about ten pages for a mathematical reader, generated from the items;
  the quickstart; W1's folder with its pinned environment. It is ready for the readers of `REQUESTS.md` R1. Writing it
  found that [[A2 — Pursuit is the steepest climb|A2]] and [[D2 — Pursuit of an objective|D2]] rested on a theorem never read in an open text; that is fixed, and so are the seven other
  sources step 8 listed: each theorem is now read in an open text or derived where it is used (Q44).
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
  item-by-item derivatives. Its own licence, the GNU Affero GPL, is kept for the framework and the library, to be
  revisited if the framework gains predictive or diagnostic power (Q38).
- **Waiting on the PI:** `REQUESTS.md`, which lists every request with the step it unblocks, and the hosts allowed.

## Next, by priority

Each step names the row it serves and what it waits for. A step that serves no row is not on this list. The PI approved
ending this phase with a handover (Q40): the close-out, E1(b), E2, E3, H1 and H2 are done (Q41), and the work passes to
readers and to a fresh session, which starts the next phase with W5. E1(c), E4, E5, C3 and the steps after them belong
to that next phase. Steps 4–6 wait on the PI.

| # | Step | Row | Waits for |
|---|---|---|---|
| E1 | **The library, `stdalign`**: the quantities `STANDARD.md` asks for, one implementation each, which the checks verify, so that what a case imports is what was proved and mutation-tested. Done (a): misalignment, its split and its estimates by access ([[P5 — Misalignment is attained, and zero exactly on the intended behaviours and their limits\|P5]], [[P6 — The departure from the default splits into pursuit and misalignment\|P6]], [[P23 — The estimated misalignment of an actor that pursues the objective\|P23]], [[P47 — The cost of reweighting\|P47]], [[P52 — What a sample certifies about misalignment, by access\|P52]]); (b), 2026-10-09: the diagnostics [[P43 — Misalignment at any intensity\|P43]]–[[P51 — What signals, audits and re-measurements reveal of tampering\|P51]] and the projection of [[P15 — Misalignment splits into what the actor could avoid and what it could not\|P15]]. Next: (c) stakes, the evaluator's results and the rest of feasibility; each moved with its check pointed at it and its functions mutation-tested | 5 | nothing; the next phase (Q40) |
| E2 | **The report as data**: a schema for `STANDARD.md`'s three sections, a validator run by lint on every case's report, and W1's report migrated to it; a reader can then check a report field by field. Done, 2026-10-09: `stdalign/report.py`, lint R16, `cases/w1-best-of-n-slope/standard-report.json` | 5 | done |
| E3 | **A case anyone can rerun in a minute**: a synthetic declaration, its draws, the library, a report and the validator, run end to end by CI; the first thing an outside reader runs. With it, every world case's environment pinned in its folder, so that W1 can be rerun as `REQUESTS.md` R1 asks (`NOTES.md` §11). Done, 2026-10-10: `examples/quickstart.py`; a `requirements.txt` in every case, which lint R14 checks against the scripts' imports. The versions were read from the environment the cases ran in, after the runs, which did not record them | 5 | done |
| H1 | **An overview for a mathematical reader**: about ten pages, with the core, the five results the rest depends on most ([[P1 — Every behaviour is a tilt of any other\|P1]], [[P2 — Every change of behaviour follows a replicator equation\|P2]], [[P4 — What KL measures\|P4]], [[P5 — Misalignment is attained, and zero exactly on the intended behaviours and their limits\|P5]], [[P14 — The cost of departing from the default is forced\|P14]]) and their proofs, and one case; what the reading of `REQUESTS.md` R1 starts from (`NOTES.md` §12). Done, 2026-10-09: `OVERVIEW.md`, generated from the items by `tools/overview.py` and checked fresh by CI, with [[P6 — The departure from the default splits into pursuit and misalignment\|P6]] added and the places a reader should push | 5 | done |
| H2 | **Handover**: the package of E1–E3 and H1 to the readers (`REQUESTS.md`, R1), and the work to a fresh session, which reads `CLAUDE.md` and `NOTES.md` §13 and starts the next phase with W5. Done, 2026-10-10: §13 and `REQUESTS.md` updated, and the pull request of Q41 | 5 | done |
| E4 | **Adapters for sequence models**: log-ratios and objectives from two causal language models, by sums over tokens, and the departure by Amini et al.'s Rao–Blackwellized estimator; an optional dependency, on which W5 runs | 4, 5 | E1 |
| E5 | **A guide for practitioners**: which access to declare, which function to call, how to read each field of the report; written from E3 | 5 | E3 |
| 1 | **W5, the stopping rule of [[P20 — Where overoptimization starts, and how it ends\|P20]] on trained policies** (machine learning): along a sweep of `β`, the gold peaks where the covariance of proxy and gold under the optimized policy crosses zero, with several runs per `β` (as revised after C2). No public sweep exists; one is made here, on W3's reference, with W3's reward as the proxy and W4's other reward as the gold: `3.8` s per step, about 4 to 10 hours per sweep (`probes/cases/`). Next: calibrate how many steps bring each run near its optimum, then design, rehearse and register from `cases/TEMPLATE.md` | 4 | E1, E4 (Q37); the next phase (Q40) |
| 2 | **C3, tampering** (simulation, Q32): a small environment, built here, where the actor can change the world or its measurement, as in the tomato-watering gridworld [[References\|@leike2017]]. It checks [[P51 — What signals, audits and re-measurements reveal of tampering\|P51]]'s bounds from finite samples against a known truth, and whether a learner trained on the signal tampers as [[P50 — Tampering: a change of the measurement, not of the world\|P50]](iii) says. Second arm (H34, Q33): a monitor reading a channel the actor can influence, trained against, as Baker et al. found with chain-of-thought monitors. Light enough to run while W5 computes | 5 | E1 (Q37); the next phase (Q40) |
| 3 | **Estimation, then the general core's draft 4** (Q33, Q36). Done for misalignment on finite outcomes: [[P52 — What a sample certifies about misalignment, by access\|P52]], its limit law under each access, derived rather than imported. Next, the same for the other quantities a report gives (the pursuit part, named misalignment, [[P48 — Misalignment when the target is uncertain\|P48]]'s interval), with the sample sizes they imply; then outcomes that are not finite, where [[P52 — What a sample certifies about misalignment, by access\|P52]]'s laws need χ² divergences finite, with the conditions on tails and on existence that `general/dictionary.md` lists | 5; 2 (the count restarts) | nothing: open texts or derivations (Q36) |
| 4 | **Readers:** a person reruns W1's report end to end from `STANDARD.md`, the case folder and the public data; a mathematician reads `CORE.md` and `derived/` | 5 | the PI finds them (`REQUESTS.md`, R1), with the package of H2 (Q40) |
| 5 | **[[P41 — Reversibility: the Jensen–Shannon divergence from the reversal\|P41]], irreversibility of play** (experimental economics): the Jensen–Shannon divergence of a group's record of transitions from its reversal is zero within sampling error in a potential game, and positive in Rock–Paper–Scissors. The potential arm is the risky one; no public record under a comparable protocol was found (D13) | 4 | the records, from the authors (`REQUESTS.md`, R2) |
| 6 | **W2**, industrial organization: register the revised prediction from [[P39 — Several actors: coordination plus individual misalignment\|P39]] (both stations adopted, against one); then run it once | 4 | the German price archive's credentials (`REQUESTS.md`, R3) |
| 7 | Three steps with no change of scope, premise or definition, a step being a merged pull request (Q46) | 2 | nothing: the count starts with the first pull request merged after the one that made v12 |
| 8 | **Sources of imported theorems** (Q36). Done, 2026-10-10: Wilks ([[P23 — The estimated misalignment of an actor that pursues the objective\|P23]]) and Aumann ([[D4 — Resolution\|D4]]) read in their scans on Project Euclid; the Neyman–Pearson lemma ([[D11 — Sample and evidence\|D11]]), Chernoff's exponent ([[P22 — No test detects misalignment faster than misalignment\|P22]]) and Pinsker's inequality ([[P51 — What signals, audits and re-measurements reveal of tampering\|P51]]) in Polyanskiy and Wu's open draft; the entropy bound of [[P32 — Regulation costs departure\|P32]] and the projection facts of [[P36 — Ordinal objectives\|P36]] derived in their proofs; Laguerre's rule, which [[P25 — The target's curve turns no more often than the regression\|P25]] already proved, and Manski's term ([[D9 — Observation and identification\|D9]]) cited as attributions; [[P23 — The estimated misalignment of an actor that pursues the objective\|P23]]'s proof gained the change of coordinates Wilks's statement needs | 1 | done |

**Why this order.** The PI approved ending this phase with a handover (Q40), and it is done (Q41): the reader package is
what a reader and a fresh executor need. The PI asked for a solid engineering side first (Q37), and row 5's criterion is
itself an engineering one: an outside reader must be able to run a case end to end. E1–E3 gave that reader a library, a
report that can be checked, and a case that runs in a minute; E4 and E5 serve W5 and the readers. W5 and C3 are then the
only tests the executor can run without waiting, and each can fail; built on the library, they test it too. Step 3 turns
the remaining diagnostics into numbers with intervals, and feeds E1; it would also replace the quickstart's bootstrap
intervals that under-cover near zero. Step 8 clears the last sources not read in open texts. The readers are the binding
constraint on row 5, and only the PI can find them. [[P41 — Reversibility: the Jensen–Shannon divergence from the reversal|P41]] and W2 are good tests, blocked on data that only the PI can
obtain.

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
- Mechanistic accounts of when a model's output tips, such as Johnson and Huo's competition for attention (Q43,
  `NOTES.md` §14): out of scope ([[A1 — Behaviour suffices|A1]]). The behavioural question they raise, misalignment along a conversation, is H37:
  a diagnostic case after E4, below W5 and C3.

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
| 2026-10-08 | the PI has no academic access (Q36): imported theorems are read in open texts or derived; [[P52 — What a sample certifies about misalignment, by access\|P52]], what a sample certifies about misalignment by what is known of each draw, derived with Huber's open paper, checked, and mutation-tested (eight mutants); the field Access in `STANDARD.md`; the requests to the PI are now hosts and data, not papers | 5 (step 3: estimation); 1 (a new check, mutation-tested) |
| 2026-10-08 | the PI asked for one file of requests and a more solid engineering side before some steps are actioned (Q37): `REQUESTS.md`; the engineering steps E1–E5 put first; `stdalign` 0.1, misalignment, its split and its estimates by access, with the checks of [[P5 — Misalignment is attained, and zero exactly on the intended behaviours and their limits\|P5]], [[P6 — The departure from the default splits into pursuit and misalignment\|P6]], [[P23 — The estimated misalignment of an actor that pursues the objective\|P23]] and [[P52 — What a sample certifies about misalignment, by access\|P52]] pointed at it, tests of its interface, and its functions mutation-tested; the Caltech record given on 2026-10-08 corrected | 5 (E1); 1 (the library mutation-tested) |
| 2026-10-08 | the licence decided (Q38): the GNU Affero GPL kept, to be revisited if the framework gains predictive or diagnostic power; what the licence does not cover, and what a later change needs, recorded in `NOTES.md` §11 | none: a decision of the PI's, recorded |
| 2026-10-08 | a review of the whole framework (Q39, `NOTES.md` §12): 153 broken paragraphs rewrapped, stale statements fixed in `RECORD.md`, these notes, `ontologies/README.md` and `README.md`; nine open findings and six pieces of advice; `CONTRIBUTING.md`, its terms proposed; two decisions asked of the PI (`REQUESTS.md`, R4 and R5) | 2 (a unit for stability proposed); 5 (the path to readers) |
| 2026-10-09 | close-out for the handover (Q40): `tools/mdwrap.py` and `tools/mutate.py` with tests, the mutant lists of the library, of [[P52 — What a sample certifies about misalignment, by access\|P52]]'s check and of `mdwrap` (all caught), `CLAUDE.md`, and the handover note (`NOTES.md` §13); the reader package and the handover set as steps H1 and H2 | 5 (H2 prepared); 1 (mutation testing reproducible from the repository) |
| 2026-10-10 | the handover finished, as the PI asked (Q41): E1(b), the diagnostics in `stdalign` 0.2, mutation-tested, one equivalent mutant explained; E2, the report as data, its validator, lint R16, W1's report migrated; E3, `examples/quickstart.py` run by CI, its intervals' coverage measured (90% for three parts near zero, stated in its report), and every case's environment pinned, which lint R14 checks against the scripts' imports; H1, `OVERVIEW.md`, generated from the items; H2, `NOTES.md` §13 and `REQUESTS.md` (R1's package ready, R6 asked). Writing H1 found that [[A2 — Pursuit is the steepest climb\|A2]] and [[D2 — Pursuit of an objective\|D2]] rested on an unread paywalled source: fixed with open texts read, a failure-mode row, and step 8 for the seven sources left | 5 (the reader package); 1 (sources, mutants) |
| 2026-10-10 | doc hygiene before the handover is merged, at the PI's request (Q42): a scripted sweep of counts, paths, links, wrapping, spelling and whitespace, and a reading for statements the handover made stale; fixed in this file, `NOTES.md` §2 and §13, `REQUESTS.md`, `README.md` (R12) and `cases/README.md` (three lessons and what holds them) | 2 (the records true); 5 (the package) |
| 2026-10-10 | Johnson and Huo (2026) reviewed at the PI's request (Q43, `NOTES.md` §14): its formula is exact for its one-head toy, but the evidence does not test that mechanism, and the mechanism is out of scope ([[A1 — Behaviour suffices\|A1]]); not a step. The behavioural question it raises recorded as H37, after E4 and below W5 and C3; the paper in `RELATED.md` | none: the priorities are kept |
| 2026-10-10 | the handover strengthened before it is used (Q44–Q47): [[A2 — Pursuit is the steepest climb\|A2]] says "a Riemannian geometry", so the core is v12; step 8 done, every imported theorem now read in an open text or derived; the contribution terms approved; a step for "stable" is a merged pull request, counted after v12; no release tag | 1 (sources); 2 (a unit for stability; the count restarts); 5 (the package) |
| 2026-10-10 | handover (Q48): a starting message for the independent reviewer of `REQUESTS.md` R1, given to the PI to relay; the pull request that brings Q43–Q47 into `main` opened, so that the reviewer reads v12 | 5 (readers) |
