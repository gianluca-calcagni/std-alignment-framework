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
| stable | neither the scope nor a premise's or definition's Statement changes for three consecutive steps, a step being a merged pull request (Q46) | not met: v13 changes the core's Statements (Q52); met once three pull requests merged after the one that brings v13 into `main` change no Statement and no scope |
| easy to import into | every item of the archive has a recorded fate | met |
| makes testable predictions | one empirical prediction, pre-registered and tested on data not seen before; a refutation counts | **met**: W1 refuted a prediction about the literature's curve; W3 tested the framework's bet itself, on a model tuned by PPO, and the bet held in part (one prediction held, one refuted). Three predictions tested on unseen data, one held |
| supports diagnostics, and shows its limits | one worked case, reported to `STANDARD.md` with intervals, run end to end by an outside reader | **not met**: W1 is reported to `STANDARD.md` with intervals, from public data and code (`cases/w1-best-of-n-slope/REPORT.md`), and its environment is pinned; no outside reader has run it. The hold on review is lifted for one mathematical reader (Q33), and the reader package is ready (H2) |

**What matters now** (Q35, Q37): contact with the world, and a bridge from theory to practice. Contact means tests that
can fail and readers who are not the executor; the bridge means estimates a reader can compute, with intervals, from the
access a case really has. The PI asked for the bridge's engineering to be solid before some steps are actioned (Q37): a
library that computes what the standard asks, a report that can be checked as data, and a case anyone can rerun. All
three are in place (Q41). The theory grows where one of these needs it, and the archive of what is done is in `NOTES.md`
§4.

## Where we are (2026-10-15)

- **On `main`**, since pull request #33 was merged (Q55), the core is v13, approved by the PI (Q52, `NOTES.md` §17) and
  built by the method of reverse physics: three axioms imported from probability theory, four background conditions
  assumed without loss of generality, three premises, each with its Status ([A1] behaviour suffices, [A4] misalignment
  is evidence, [A5] declared before), and eleven definitions, each with its Interpretation, declared and justified.
  v12's A2 and A3 are reasons of [D2], as no result used them; the draft's A6 was not adopted. [D3] defines the ordinal
  specification, which `STANDARD.md` asks to report beside the standard one. Then, at the PI's seven requests (Q53,
  `NOTES.md` §18): a table of conventions, each justified, which lint R17 holds; [A4] on the record's counts, which
  needs no independence of the actor, with [P54] for what dependence and drift add; families of targets in [D3], with
  [P53] for every family; [P55], tests and intervals from counts, exact at every size, with Genin and Kelly's
  verifiability; the general core's draft 4 on v13's kinds; the ontologies' declarations; and H38 on activations. The PI
  accepted it all (Q54): case C5 ran, all held, and the docs were swept (`NOTES.md` §19, the last handover). No result
  cites a premise in its Statement or Proof (`probes/review/premise_reach.py`). 55 propositions; 102 checks of the
  items, and 148 tests of the tools, the scenario, the library and the quickstart, pass on both paths. v12, which v13
  replaced, had five premises and 52 propositions.
- **The focus now** (Q56): the mathematics first, and the general core made correct and coherent rather than split or
  restructured; then a real-life simple case where the framework gives true insight, diagnosis or prediction, for which
  the engineering must be rethought. A rewrite into a more digestible structure is the PI's hunch, not a decision
  (`NOTES.md`, H39). The general core is draft 4 on v13's kinds; its transfer lemma is proved (`general/transfer.md`,
  TR1–TR5): misalignment, the supremum over the descriptions a record can decide, is the least divergence over the
  closure of the intended behaviours whenever that closure is compact, whatever the nearness, and under that compactness
  "misaligned" is verifiable in chance. The dimension law is proved too (TR6), and [P16] and [P54] carry to standard
  Borel spaces (TR7, TR8). None of the eight runs in CI yet. Every import of the general core is read in an open text or
  replaced; the last two, Kuratowski's and the Lusin–Souslin theorems, in Tserunyan's notes once the PI allowed their
  host (R14). Nine results of the finite core are diagnostics ([P43]–[P51]); five were used in a case, all in W4, and
  [P46], [P49], [P50] and [P51] in none yet.
- **The labels** (Q57, `NOTES.md` §21): whether each label means what its word says, tested for the first time by L1,
  registered before it ran (`probes/labels/`). Of twelve labels, masking, overoptimization and misalignment under the
  ordinal specification agreed with their words on every case; nine disagreed on at least one, most because the standard
  specification reads "pursue `F`" as one way of pursuing; one prediction failed, on a threshold without its scale (§1).
  The renames the executor recommends, and the common-sense verdicts, wait on the PI (`REQUESTS.md`, R15).
- **v14, begun** (Q59, `NOTES.md` §23): on the branch `claude/core-v14`, a draft in `v14/` beside the core, not in it.
  Constraints as a concept of the core (forbidden sets, rate limits, budgets); misalignment read as the growth rate of
  the best bet against acceptability, equal to v13's measure on convex sets, with a test that keeps its level under any
  dependence; three verdicts under a ranking against a reference; optimization moved to a derived module, where a budget
  enters as a shadow price. Twelve results proved here, none in CI yet. The PI's decisions on R15 and R16 wait for it;
  L2 comes next.
- **Engineering** (Q37, Q41): `stdalign` 0.2, the library, holds misalignment, the revealed intensity and the split of
  the departure ([P5], [P6]), the estimates by access with their intervals ([P23], [P47], [P52]), and the diagnostics
  [P43]–[P51] with the projection of [P15]; the checks of those items run on it, its own tests cover its interface, and
  its functions are mutation-tested. A report can be written as data and checked by `stdalign/report.py`; lint R16 holds
  every case's report to it, and W1's is the first. `examples/quickstart.py` runs a case on simulated data, from the
  declaration to a valid report, in under a minute, and CI runs it. Every case pins its environment, which lint R14
  checks against its scripts' imports. Stakes, the evaluator's results and feasibility are still computed by helpers
  inside `checks/` (E1(c)). The review of 2026-10-10 (`NOTES.md` §15) found two errors at the library's edges, an
  infinite misalignment for an actor of full support near the best outcomes and [P23]'s χ² reference used at `t = 0`,
  and intervals from log-ratios that cover about 85% at 32 draws: E1(d). The executor's tools are in the repository
  (Q40): `tools/mdwrap.py`, `tools/mutate.py` with the mutant lists of `tools/mutants/`, `tools/overview.py`, and
  `CLAUDE.md`.
- **The reader package** (H1, H2): `OVERVIEW.md`, about fifteen pages for a mathematical reader since v13, generated
  from the items; the quickstart; W1's folder with its pinned environment. It is ready for the readers of `REQUESTS.md`
  R1. Writing it found that A2 and [D2] rested on a theorem never read in an open text; that is fixed, and so are the
  seven other sources step 8 listed: each theorem is now read in an open text or derived where it is used (Q44).
- **Contact with the world:** one of three framework predictions tested on data not seen before held (`RECORD.md`): W1
  refuted, W3 one held and one refuted. W4 was diagnostic, and two simulation cases, C1 and C2, each revised a
  prediction before its data were read (`cases/`). Too few tests to say more than that the framework can fail. The
  review of 2026-10-10 found that these predictions bear on the optimum of KL-regularized training and on a fitted curve
  more than on the framework, and that `M` alone can rank an exact pursuit of a wrong proxy below a faithful optimizer
  of the right target (`NOTES.md` §15, points 1 and 2; `REQUESTS.md`, R8 and R10).
- **Imports:** what the framework can import, ranked (`NOTES.md` §9): the heaviest is statistics (misspecified fits,
  reweighting, what samples certify). How the imports treat the continuum (`general/dictionary.md`); cooperative inverse
  reinforcement learning and its variants, mapped, with a request made without full consideration read in the core's
  objects (`NOTES.md` §10).
- **Frozen** (`NOTES.md`, Q26, Q27, Q33): new disciplines, any widening of the scope, and the general core except for
  outcomes that are not finite and estimation guarantees (step 3).
- **Licences** (Q27): the repository keeps code, aggregates and citations only: no third-party data, weights, papers, or
  item-by-item derivatives. Its own licence, the GNU Affero GPL, is kept for the framework and the library, to be
  revisited if the framework gains predictive or diagnostic power (Q38). Its aim while the work is research is that
  progress on the framework be shared by everyone, and the adoption it costs is accepted (Q50); what a copyleft licence
  reaches, and what gets closer, is in `NOTES.md` §11, and a package for the second waits on the PI (`REQUESTS.md`,
  R11).
- **Waiting on the PI:** `REQUESTS.md`, which lists every request with the step it unblocks, and the hosts allowed.

## Next, by priority

Each step names the row it serves and what it waits for. A step that serves no row is not on this list. The PI approved
ending this phase with a handover (Q40): the close-out, E1(b), E2, E3, H1 and H2 are done (Q41), and the work passes to
readers and to a fresh session, which starts the next phase with W5. E1(c), E4, E5, C3 and the steps after them belong
to that next phase. Steps 4–6 wait on the PI.

| # | Step | Row | Waits for |
|---|---|---|---|
| E1 | **The library, `stdalign`**: the quantities `STANDARD.md` asks for, one implementation each, which the checks verify, so that what a case imports is what was proved and mutation-tested. Done (a): misalignment, its split and its estimates by access ([P5], [P6], [P23], [P47], [P52]); (b), 2026-10-09: the diagnostics [P43]–[P51] and the projection of [P15]. Next: (c) stakes, the evaluator's results and the rest of feasibility; each moved with its check pointed at it and its functions mutation-tested; (d), from the review of 2026-10-10 (`NOTES.md` §15): the revealed intensity's third case taken only when no mass lies off the best outcomes; the χ̄² law at `t = 0` in `from_counts`; an `Estimate` flagged when its effective draws fall below a threshold calibrated by coverage; the ordinal misalignment of [P36] with the credits of [P53], which `STANDARD.md` asks for since v13 (Q52); and a clear error from `project_linear` when no full-support behaviour has the averages asked for (`NOTES.md` §17); the exact test and interval of [P55], for any specification; then W1's report, `SCENARIO.md` and the quickstart brought up to the standard of v13, which none of them meets yet: none reports the ordinal misalignment beside the standard one, and W1's report cites v12's premises | 5 | nothing; the next phase (Q40) |
| E2 | **The report as data**: a schema for `STANDARD.md`'s three sections, a validator run by lint on every case's report, and W1's report migrated to it; a reader can then check a report field by field. Done, 2026-10-09: `stdalign/report.py`, lint R16, `cases/w1-best-of-n-slope/standard-report.json` | 5 | done |
| E3 | **A case anyone can rerun in a minute**: a synthetic declaration, its draws, the library, a report and the validator, run end to end by CI; the first thing an outside reader runs. With it, every world case's environment pinned in its folder, so that W1 can be rerun as `REQUESTS.md` R1 asks (`NOTES.md` §11). Done, 2026-10-10: `examples/quickstart.py`; a `requirements.txt` in every case, which lint R14 checks against the scripts' imports. The versions were read from the environment the cases ran in, after the runs, which did not record them | 5 | done |
| H1 | **An overview for a mathematical reader**: about ten pages, with the core, the five results the rest depends on most ([P1], [P2], [P4], [P5], [P14]) and their proofs, and one case; what the reading of `REQUESTS.md` R1 starts from (`NOTES.md` §12). Done, 2026-10-09: `OVERVIEW.md`, generated from the items by `tools/overview.py` and checked fresh by CI, with [P6] added and the places a reader should push | 5 | done |
| H2 | **Handover**: the package of E1–E3 and H1 to the readers (`REQUESTS.md`, R1), and the work to a fresh session, which reads `CLAUDE.md` and `NOTES.md` §13 and starts the next phase with W5. Done, 2026-10-10: §13 and `REQUESTS.md` updated, and the pull request of Q41 | 5 | done |
| E4 | **Adapters for sequence models**: log-ratios and objectives from two causal language models, by sums over tokens, and the departure by Amini et al.'s Rao–Blackwellized estimator; an optional dependency, on which W5 runs | 4, 5 | E1 |
| E5 | **A guide for practitioners**: which access to declare, which function to call, how to read each field of the report; written from E3 | 5 | E3 |
| O1 | **Estimating the ordinal misalignment** (v13, Q52): its law from counts, the analogue of [P23] for the cone of [P36], an order-restricted likelihood ratio whose limit is a mixture of χ² laws, and the analogue of [P52]'s intervals; until then the ordinal misalignment that `STANDARD.md` asks for has the exact but conservative interval of [P55](iv), and a bootstrap, which under-covers near zero. Into the library with its check, mutation-tested | 5 | nothing: the theorems read in an open text or derived (Q36) |
| C5 | **Activations** (simulation, reopened by the PI with H33 and H38, Q54): on a small network whose internals are known, whether probes on its last hidden layer verify that it tells evaluation from use, whether their silence certifies anything, and what [P17]'s bound fed a probe's estimate does. Done, 2026-10-11: all eight predictions held, as the rehearsal had shown; a demonstration of H38, not a hard test (`cases/c5-activations/RESULTS.md`) | 5 | done |
| C4 | **Known groups** (simulation, proposed by the review of 2026-10-10, `NOTES.md` §15): optimizers of the right objective by several routes (policy gradient, best-of-`n`, PPO with and without a KL term) and of proxies at known correlations, several runs of each; registered: [P36], [P44] and [P45] separate the groups at stated error rates, and `M` alone does not. Minutes of computation; it can fail, and it reads what `M` means for a trained model where the truth is known | 5; a row "valid", if R10 | the PI's approval (`REQUESTS.md`, R8) |
| 1 | **W5, the stopping rule of [P20] on trained policies** (machine learning): along a sweep of `β`, the gold peaks where the covariance of proxy and gold under the optimized policy crosses zero, with several runs per `β` (as revised after C2). No public sweep exists; one is made here, on W3's reference, with W3's reward as the proxy and W4's other reward as the gold: `3.8` s per step, about 4 to 10 hours per sweep (`probes/cases/`). Next: calibrate how many steps bring each run near its optimum, then design, rehearse and register from `cases/TEMPLATE.md` | 4 | E1, E4 (Q37); the next phase (Q40) |
| 2 | **C3, tampering** (simulation, Q32): a small environment, built here, where the actor can change the world or its measurement, as in the tomato-watering gridworld [@leike2017]. It checks [P51]'s bounds from finite samples against a known truth, and whether a learner trained on the signal tampers as [P50](iii) says. Second arm (H34, Q33): a monitor reading a channel the actor can influence, trained against, as Baker et al. found with chain-of-thought monitors. Light enough to run while W5 computes | 5 | E1 (Q37); the next phase (Q40) |
| 3 | **Estimation, then the general core** (Q33, Q36). Draft 4 is written, on v13's kinds (Q53), and its transfer lemma under compactness is proved and probed (TR1–TR5, Q56), with the dimension law (TR6) and [P16] and [P54] on general spaces (TR7, TR8); every import is read in an open text or replaced (R14 done). Next for the general core: checks in CI for TR1–TR8, and the rows of `general/transfer.md` still expected, first those the standard would use ([P53] through Csiszár's I-projection, [P54], [P23] at a record's resolution). Done for misalignment on finite outcomes: [P52], its limit law under each access, derived rather than imported. Next, the same for the other quantities a report gives (the pursuit part, named misalignment, [P48]'s interval), with the sample sizes they imply; then outcomes that are not finite, where [P52]'s laws need χ² divergences finite, with the conditions on tails and on existence that `general/dictionary.md` lists | 5; 2 (the count restarts) | nothing: open texts or derivations (Q36) |
| 4 | **Readers:** a person reruns W1's report end to end from `STANDARD.md`, the case folder and the public data; a mathematician reads `CORE.md` and `derived/` | 5 | the PI finds them (`REQUESTS.md`, R1), with the package of H2 (Q40) |
| 5 | **[P41], irreversibility of play** (experimental economics): the Jensen–Shannon divergence of a group's record of transitions from its reversal is zero within sampling error in a potential game, and positive in Rock–Paper–Scissors. The potential arm is the risky one; no public record under a comparable protocol was found (D13) | 4 | the records, from the authors (`REQUESTS.md`, R2) |
| 6 | **W2**, industrial organization: register the revised prediction from [P39] (both stations adopted, against one); then run it once | 4 | the German price archive's credentials (`REQUESTS.md`, R3) |
| O2 | **Ordinal diagnostics** (v13, Q52): the splits of [P44]–[P46] for the ordinal specification, where the nearest intended behaviour is a projection onto a cone rather than a linear family, so named, drift and run-specific parts may not add up exactly; derived, checked, and mutation-tested only when a case needs them | 5 | O1; a case that needs it |
| 7 | Three steps with no change of scope, premise or definition, a step being a merged pull request (Q46) | 2 | nothing: the count starts with the first pull request merged after the one that brings v13 into `main` |
| 8 | **Sources of imported theorems** (Q36). Done, 2026-10-10: Wilks ([P23]) and Aumann ([D4]) read in their scans on Project Euclid; the Neyman–Pearson lemma ([D11]), Chernoff's exponent ([P22]) and Pinsker's inequality ([P51]) in Polyanskiy and Wu's open draft; the entropy bound of [P32] and the projection facts of [P36] derived in their proofs; Laguerre's rule, which [P25] already proved, and Manski's term ([D9]) cited as attributions; [P23]'s proof gained the change of coordinates Wilks's statement needs | 1 | done |

**Why this order.** The PI approved ending this phase with a handover (Q40), and it is done (Q41): the reader package is
what a reader and a fresh executor need. The PI asked for a solid engineering side first (Q37), and row 5's criterion is
itself an engineering one: an outside reader must be able to run a case end to end. E1–E3 gave that reader a library, a
report that can be checked, and a case that runs in a minute; E4 and E5 serve W5 and the readers. W5 and C3 are then the
only tests the executor can run without waiting, and each can fail; built on the library, they test it too. If the PI
approves C4, it comes before them: it takes minutes, can fail, and says what `M` means for a trained model where the
truth is known, which W5's reading needs (`NOTES.md` §15). E1(d) fixes errors in what cases already import, so it comes
before any new function. Step 3 turns the remaining diagnostics into numbers with intervals, and feeds E1; it would also
replace the quickstart's bootstrap intervals that under-cover near zero. Step 8 clears the last sources not read in open
texts. The readers are the binding constraint on row 5, and only the PI can find them. [P41] and W2 are good tests,
blocked on data that only the PI can obtain.

## What the PI can supply

In `REQUESTS.md`: every open request, with the step it unblocks and how to hand it over, the hosts the PI has allowed,
and what is done. Since Q36 no paper behind a paywall is asked for.

## Not now, and why

- New disciplines and wider scope: frozen by the PI (Q26, Q27). Activations as observations, H33 and H38, were reopened
  by the PI (Q54), and case C5 is their first step.
- New results in `derived/`: only when a step above needs one. Waiting candidates: H34 (C3's second arm will test it),
  H35 (a request as evidence, a declared family), H36 (the default from how a population usually acts) (`NOTES.md`
  §5.4).
- More simulation cases: only to gate a world test, or when the PI approves one, as for C3.
- Hunches (`NOTES.md` §5.4): recorded, not pursued, unless a step above needs them.
- Mechanistic accounts of when a model's output tips, such as Johnson and Huo's competition for attention (Q43,
  `NOTES.md` §14): out of scope ([A1]). The behavioural question they raise, misalignment along a conversation, is H37:
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
| 2026-10-08 | the PI has no academic access (Q36): imported theorems are read in open texts or derived; [P52], what a sample certifies about misalignment by what is known of each draw, derived with Huber's open paper, checked, and mutation-tested (eight mutants); the field Access in `STANDARD.md`; the requests to the PI are now hosts and data, not papers | 5 (step 3: estimation); 1 (a new check, mutation-tested) |
| 2026-10-08 | the PI asked for one file of requests and a more solid engineering side before some steps are actioned (Q37): `REQUESTS.md`; the engineering steps E1–E5 put first; `stdalign` 0.1, misalignment, its split and its estimates by access, with the checks of [P5], [P6], [P23] and [P52] pointed at it, tests of its interface, and its functions mutation-tested; the Caltech record given on 2026-10-08 corrected | 5 (E1); 1 (the library mutation-tested) |
| 2026-10-08 | the licence decided (Q38): the GNU Affero GPL kept, to be revisited if the framework gains predictive or diagnostic power; what the licence does not cover, and what a later change needs, recorded in `NOTES.md` §11 | none: a decision of the PI's, recorded |
| 2026-10-08 | a review of the whole framework (Q39, `NOTES.md` §12): 153 broken paragraphs rewrapped, stale statements fixed in `RECORD.md`, these notes, `ontologies/README.md` and `README.md`; nine open findings and six pieces of advice; `CONTRIBUTING.md`, its terms proposed; two decisions asked of the PI (`REQUESTS.md`, R4 and R5) | 2 (a unit for stability proposed); 5 (the path to readers) |
| 2026-10-09 | close-out for the handover (Q40): `tools/mdwrap.py` and `tools/mutate.py` with tests, the mutant lists of the library, of [P52]'s check and of `mdwrap` (all caught), `CLAUDE.md`, and the handover note (`NOTES.md` §13); the reader package and the handover set as steps H1 and H2 | 5 (H2 prepared); 1 (mutation testing reproducible from the repository) |
| 2026-10-10 | the handover finished, as the PI asked (Q41): E1(b), the diagnostics in `stdalign` 0.2, mutation-tested, one equivalent mutant explained; E2, the report as data, its validator, lint R16, W1's report migrated; E3, `examples/quickstart.py` run by CI, its intervals' coverage measured (90% for three parts near zero, stated in its report), and every case's environment pinned, which lint R14 checks against the scripts' imports; H1, `OVERVIEW.md`, generated from the items; H2, `NOTES.md` §13 and `REQUESTS.md` (R1's package ready, R6 asked). Writing H1 found that A2 and [D2] rested on an unread paywalled source: fixed with open texts read, a failure-mode row, and step 8 for the seven sources left | 5 (the reader package); 1 (sources, mutants) |
| 2026-10-10 | doc hygiene before the handover is merged, at the PI's request (Q42): a scripted sweep of counts, paths, links, wrapping, spelling and whitespace, and a reading for statements the handover made stale; fixed in this file, `NOTES.md` §2 and §13, `REQUESTS.md`, `README.md` (R12) and `cases/README.md` (three lessons and what holds them) | 2 (the records true); 5 (the package) |
| 2026-10-10 | Johnson and Huo (2026) reviewed at the PI's request (Q43, `NOTES.md` §14): its formula is exact for its one-head toy, but the evidence does not test that mechanism, and the mechanism is out of scope ([A1]); not a step. The behavioural question it raises recorded as H37, after E4 and below W5 and C3; the paper in `RELATED.md` | none: the priorities are kept |
| 2026-10-10 | the handover strengthened before it is used (Q44–Q47): A2 says "a Riemannian geometry", so the core is v12; step 8 done, every imported theorem now read in an open text or derived; the contribution terms approved; a step for "stable" is a merged pull request, counted after v12; no release tag | 1 (sources); 2 (a unit for stability; the count restarts); 5 (the package) |
| 2026-10-10 | handover (Q48): a starting message for the independent reviewer of `REQUESTS.md` R1, given to the PI to relay; the pull request that brings Q43–Q47 into `main` opened, so that the reviewer reads v12 | 5 (readers) |
| 2026-10-10 | a review of the whole framework at the PI's request (Q49, `NOTES.md` §15), in twelve focus areas, by the executor, not independent: the six results the rest stands on read without an error; `M` charges an optimizer of the right target by a route that is not a tilt (median share `0.16` for policy gradient) and can rank an exact pursuit of a wrong proxy below it (AUC `0.35`), where [P36]'s ordinal misalignment separates them; two errors at the library's edges and an under-covering interval, as E1(d); `OVERVIEW.md`'s count of predictions fixed; C4, a row "valid" and the licence asked of the PI (R8–R10); probes in `probes/review/`; the order of the commands before a push fixed. It changes no Statement and no scope | 1 (the library's errors); 5 (what the diagnostics measure); 2 (if merged, the first step after v12) |
| 2026-10-10 | the licence's aim recorded (Q50): progress shared by everyone while the work is research, the Affero GPL kept for the code and the text, R9 declined and the executor's recommendation withdrawn; `NOTES.md` §11 says what the licence reaches (published and served copies) and what it does not (private copies, ideas, and perhaps text a model wrote), and what gets closer: notices under section 7, a request to agents that work on copies, credit and early publication (R11). A §1 row extended: links passed on unopened | none: a decision of the PI's, recorded |
| 2026-10-10 | the hunches and insights of past executors read at the PI's request, the archive's included: the review's first finding was v7.10's H8, its review item 2 and its identification rule, lost at the restart; credited in `NOTES.md` §15, and §1's row on lineage amnesia extended. The assessment was given to the PI, not yet recorded | none: the record kept true |
| 2026-10-10 | on a new branch, `claude/core-reframe`, a draft v13 at the PI's request (Q51): [A4] as evidence, A6, the ordinal and matched specifications in [D3], [P6](ii) checked and mutation-tested; lint R5 caught circular reasons in the first draft (§1). Its review (`NOTES.md` §16): adopt [A4], [P6](ii), the ordinal option and the paired report; not A6, which conflicts with [A1] (R12) | 2 (a version, if adopted); 5 (what misalignment charges) |
| 2026-10-11 | v13 approved (Q52) and built on `claude/core-reframe` by the method of reverse physics: imported axioms (M1–M3), background conditions assumed without loss of generality (B1–B4), three premises with their Status ([A1], [A4], [A5]), and an Interpretation, declared and justified, for every definition; v12's A2 and A3 became reasons of [D2], A6 was not adopted; [P53], misalignment as the departure beyond what a specification credits, checked and mutation-tested (8 of 8); lint R1, R3–R5 for the new kinds and fields, mutation-tested (8 of 8); the paired report in `STANDARD.md`; the dependencies measured again (no result cites a premise in its Statement or Proof); steps O1 and O2 for the ordinal specification (`NOTES.md` §17) | 2 (the count restarts at the merge); 1 (new checks, mutation-tested); 5 (the paired report) |
| 2026-10-11 | the PI's seven requests (Q53, `NOTES.md` §18): conventions justified in a table that lint R17 holds; independence of the actor dropped from [A4], with [P54]; families of targets, with [P53] for every family; [P55], exact tests and intervals from counts, and statistical verifiability after Genin and Kelly; `CORE-GENERAL.md` draft 4 on v13's kinds, misalignment as what records can decide, with the dictionary and the transfer table; the ontologies' slots and declarations; H38 on activations, reopening H33 asked of the PI (R13). Every new check and lint rule mutation-tested | 1 (new checks, mutation-tested); 5 (tests exact at every size; the paired report's interval); 2 (v13's Statements, not yet merged) |
| 2026-10-11 | all accepted (Q54): draft 4's continuous misalignment decided; activations reopened, and case C5 registered, pushed, run and held in all eight predictions, a demonstration rather than a hard test; a push without the pre-push block turned one CI run red, recorded (§1); doc hygiene by a sweep now kept in `probes/review/doc_sweep.py`, six stale statements fixed; `NOTES.md` §19 is the new handover | 5 (C5: what activations verify); 2 (the records true) |
| 2026-10-11 | a reread of the branch before its pull request, at the PI's request: `CORE.md`'s count of kinds, its table of symbols (record, `𝓚`) and the conventions row on pursuit corrected; `README.md`'s format of an item brought to v13 (Interpretation, Status); `NOTES.md` §19's claim that every Statement changed corrected to the ones that did; `STANDARD.md` and E1(d) now say that W1's report, `SCENARIO.md` and the quickstart do not yet meet v13's standard; a subagent's reading of [P53]–[P55] found no false Statement, and two overclaims in their Notes, both fixed: that the counts certify the misalignment of a dependent actor's average behaviour (they do not: `probes/review/p55_dependence.py`), and Sanov's theorem without its interior; with smaller fixes to [P54](ii), [P55](iv)'s proof, the plain terms and the conventions row on independence (`NOTES.md` §1, §19) | 2 (the records true) |
| 2026-10-11 | pull request #33 merged by the PI (Q55): v13 is on `main`; the records that said it was not yet merged updated, and the count for "stable" restarts at 0 of 3 | 2 (the count restarts; the records true) |
| 2026-10-11 | the PI's priorities (Q56): the general core correct and coherent first. Its transfer lemma proved, TR1–TR5 in `general/transfer.md`, with the dimension law TR6 and [P16] and [P54] on standard Borel spaces, TR7 and TR8, and probed (`probes/general/t8_transfer.py`); Csiszár (1984), Massart (1990), Polyanskiy and Wu's disintegration and Haghighatshoar and Abbe's account of Rényi read; the unread citations replaced or derived; `CORE-GENERAL.md` corrected where it overclaimed (verifiability under a nearness); one host requested (R14); hunches H39–H42; a subagent's reading of TR1–TR6 found one error, TR6's grid, and ten gaps or overclaims in the sentences around the proofs, all verified and fixed (`NOTES.md` §20) | 5 (the general core); 2 (the records true) |
| 2026-10-14 | R14 done: the last imports of the general core read in Tserunyan's notes. The PI asked whether the labels mean what their words say (Q57): L1 registered and pushed before computing (`probes/labels/`), then run: 46 of 47 predictions held, the failure a threshold without its scale (§1); three labels agree with their words on every case, nine disagree on at least one, most through the standard specification's narrow reading of "pursue `F`"; renames recommended for the PI to decide (R15, `NOTES.md` §21); `TERMS.md` warns of the disagreeing labels meanwhile | 5 (what the framework's quantities mean); 2 (the records true) |
| 2026-10-14 | the PI asked whether L1's recommendations survive on a continuum (`NOTES.md` §21, end): the ordinal reading of "pursue `F`" is stronger there, since with a heavy upper tail the tilted specification intends only the default; a new failure, near misses infinitely misaligned at full precision, so misalignment on a continuum is to be reported at a declared resolution or precision; measurement distortion beyond `log n` or with a singular part can only be tampering; R15 refined | 5 (what the quantities mean); 2 (the records true) |
| 2026-10-15 | the PI is open to a major revamp for words that mean what they say (Q58): a brainstorm in `NOTES.md` §22, the request separated from the actor's mechanism and from the record, misalignment and gain as two numbers, effects named as effects, everything at a declared resolution; a decision waits on the PI (R16) | 2 (a version, if adopted); 5 (what the quantities mean) |
| 2026-10-15 | the PI challenged bins on a continuum and asked for an optimization-free core; the discussion recorded in `NOTES.md` §22: any exact forgiveness can be cheated, so measures must grade small shifts as small and stakes be reported over the horizon; distribution functions serve the order part exactly; optimization moves to a derived module; a reference or an absolute standard is needed by any ranking | 2 (a version, if adopted) |
| 2026-10-15 | second thoughts in `NOTES.md` §22: an undetectable loss of order `√n` over `n` decisions whatever the resolution (H43); a ranking and a reference certify three verdicts, and the ordinal specification calls a greedy decoder at the 0.9 quantile misaligned (H44); ranks under a reference per context pool over prompts, accusing but not exonerating; three questions added to R16 | 2 (a version, if adopted); 5 (what the quantities mean) |
| 2026-10-15 | the PI asked for a pull request with the latest changes, and for the core to be reworked on a branch as the executor recommends, with constraints as a new concept of the core (Q59); R15 and R16 postponed until the rework absorbs them | 2 (a version) |
| 2026-10-15 | v14 begun on `claude/core-v14` (Q59, `NOTES.md` §23): `v14/README.md`, the structure and a map from v13; `v14/evidence.md`, `v14/constraints.md` and `v14/order.md`, twelve results proved here and probed (`probes/v14/`); lint reads `v14/`; R17 asks the PI to read the direction | 2 (a version) |
| 2026-10-16 | the PI's position on constraints and fees, and the question of what else leaves the core (Q60): `NOTES.md` §24, a discussion; agreed that fees belong to the optimization module, challenged that severity lives in probabilities, and proposed a core whose only declared object is a list of requirements | 2 (a version, if adopted) |
| 2026-10-16 | the forms of misalignment and the layers they need (Q61, `NOTES.md` §25): an interface layer, views, actions and an environment kernel, proposed between `CORE` and `OPTIMIZERS`; factoring by nested interfaces; two candidates for culpability; the full list by layer | 2 (a version, if adopted) |
| 2026-10-16 | three layers with their twins decided (Q62); `v14/factorization.md`, the factorization proved two ways, the earlier splits sorted by mechanism and layer, and the labels' verification status (VF1–VF3); `v14/LIMITS.md`; [P15](v)'s label found to overclaim (§1, R18) | 2 (a version); 5 (what the quantities mean) |
