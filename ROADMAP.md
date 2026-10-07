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

## Where we are (2026-10-07)

- The core is v11: five premises, eleven definitions, 51 propositions; 183 checks pass on both paths. Nine results are
  diagnostics (`derived/diagnostics.md`, Q28, Q30–Q32): misalignment at any intensity and across conditions at one
  intensity; what named objectives explain; drift between runs; what runs share between evaluation and use; the cost of
  reweighting; the interval of misalignment when the target is known only to lie in a family; outer and inner
  misalignment, with their exact split; and tampering, with what signals, audits and re-measurements reveal of it. Each
  follows from earlier results; no premise or definition changed. Five of the nine were used in a case, all in W4;
  [P46], [P49], [P50] and [P51] in none yet.
- **Grounding** (Q32): with the measurement part of the outcome, the departure splits exactly into the change of the
  world and the tampering, and a target on the world charges all of it ([P50]); from signals alone tampering has an
  attained lower bound and is never ruled out, and an audit raises the bound ([P51]). In W1–W4 tampering was zero by
  construction: their evaluators were fixed functions of the text.
- **Whose target** (`NOTES.md` §7, Q30): W3 and W4 measured the trainer's formal objective, not what any user wants, for
  which no gold exists. Every declaration now names its principal (`STANDARD.md`), and an uncertain target is declared
  as a family, whose interval [P48] gives.
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
- **W4** (`cases/w4-two-runs/`), the first diagnostic case: what PPO changed in W3's model beyond its reward is not a
  sharpening of the reference (S1 refuted), and part of it recurs in a second public run from the same reference (S2
  held): systematic, not all drift. But the shared part is small: naming sharpening, the other reward and the other
  run's change explains `0.14` of the misalignment, and the runs are further apart than either is from the reference.
  Separating drift from procedure needs replicate runs of one procedure; none is public.
- **Lessons as defaults** (Q29): new registrations follow `cases/TEMPLATE.md`, held to it by lint R15; case scripts use
  `tools/casekit.py`; `cases/README.md` maps each lesson to what holds it.
- **Frozen** (`NOTES.md`, Q26, Q27, Q33): new disciplines, any widening of the scope, and the general core except for
  outcomes that are not finite and estimation guarantees, which Q33 unfroze (step 4). External review: one mathematical
  reader of the core and `derived/` is allowed (Q33).
- **Imports** (Q33, `NOTES.md` §9): a survey of what the framework can import found the most weight in statistics: the
  theory of misspecified models (the revealed intensity is White's pseudo-true parameter; Vuong's test compares
  specifications), the `e^{KL}` sample-size law of importance sampling, and what samples alone can certify. In
  alignment, Baker's distortion and risk of a performance measure, Courty and Marschke's test of distortion, and the
  obfuscation of a monitor trained against map onto existing items ([P11], [P50], [P20], H34). Sources were verified
  from records and abstracts; full texts are needed before a theorem is imported (D12).
- **Licences** (Q27): the repository keeps code, aggregates and citations only; no third-party data, weights, papers, or
  item-by-item derivatives. W1's proxy weights and per-prompt statistics were removed from the tree; they remain in two
  earlier commits, and the PI keeps the history as it is (Q33).
- Two simulation cases checked instruments before they met the world, and each revised a prediction before its data were
  read (`cases/`): C1 and C2.
- `SCENARIO.md` shows the framework applied, three ways; it is an illustration, not evidence.
- **Blocked on the PI:** the German price archive (credentials, W2); readers who are people (Q33); the full texts of the
  imports marked "now" (D12).

## Next, in order

Each step names the row it serves and what it waits for. A step that serves no row is not on this list.

| # | Step | Row | Waits for |
|---|---|---|---|
| 1 | **[P41], irreversibility of play** (experimental economics): the Jensen–Shannon divergence of a group's record of transitions from its reversal is zero within sampling error in a potential game, and positive in Rock–Paper–Scissors. The Rock–Paper–Scissors arm alone is weak, since its cycles are known in summary (D9); the risky arm is the potential game, and every two-strategy population game has a potential, so a public continuous-time experiment with two strategies would serve. First check which records are public and not yet read; then register from the template, with a declared principal | 4 | the check of the data, which the executor can make |
| 2 | **[P20], the stopping rule** (machine learning): along a sweep of `β`, the gold peaks where the covariance of proxy and gold under the optimized policy crosses zero. As revised after C2, it needs several runs per `β` on a fine grid, with a gold distinct from the proxy. First check whether such a sweep is public and unseen; otherwise measure what training one on small models costs on this machine, as W3 measured its sampler; then register | 4 | the check of the data, or the measured cost of making them |
| 3 | **C3, tampering** (simulation, approved in Q32): a small environment, built here, where the actor can change the world or its measurement, in the manner of the tomato-watering gridworld (D11). It checks [P51]'s bounds from finite samples against a known truth, and whether a learner trained on the signal tampers as [P50](iii) says, with its share at the start. A second arm (H34, Q33): a monitor that reads a channel the actor can influence, trained against, as Baker et al. found with chain-of-thought monitors | 5 | steps 1 and 2; it gates no named world test yet |
| 4 | **The general core, draft 4** (Q33): outcomes that are not finite, with the condition on tails that finite outcomes hide (Kwa et al.), and estimation guarantees for the core's quantities, imported where they exist: White's and Vuong's theory of misspecified fits, the `e^{KL}` law of reweighting, and the limit on what samples alone certify (`NOTES.md` §9). Drafted alongside steps 1–3, while they wait on data | 5 | the full texts (D12) before any theorem is imported; the stability row's count restarts when a definition changes |
| 5 | **W2**, industrial organization: register the revised prediction from [P39] (both stations adopted, against one); then run it once | 4 | the German price archive's credentials |
| 6 | An outside reader reruns W1's report end to end, from `STANDARD.md`, the case folder and the public data alone; and a mathematician reads the core and `derived/` | 5 | the PI finds readers who are people; the hold is lifted for the mathematician (Q33) |
| 7 | Three steps with no change of scope, premise or definition | 2 | the freeze, once step 4 has changed what it changes |

## Not now, and why

- New disciplines and wider scope: frozen by the PI (Q26, Q27); the general core too, except step 4 (Q33).
- New results in `derived/`: only if a test on the list above needs one to be stated. The rule was set aside, with the
  PI's approval, for [P48]–[P51]; it applies again from here.
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
| 2026-10-03 | lessons as defaults: `cases/TEMPLATE.md`, lint R15, `tools/casekit.py` (Q29); W4 rehearsed, registered and run: no sharpening; a small shared change beyond the reward | 5 (W4, a diagnostic) |
| 2026-10-04 | whose target? W3 and W4 measured the trainer's objective; [P48], the interval of misalignment over a family of targets; the field Principal in the standard, the template and lint R15 (Q30) | 5 (diagnostics) |
| 2026-10-04 | [P49], outer and inner misalignment and their exact split; the archive's five gaps mapped (`IMPORT.md`, section 8), grounding only partly covered (Q31) | 5 (diagnostics) |
| 2026-10-07 | [P50], tampering, and [P51], what signals, audits and re-measurements reveal of it, with checks and mutation tests; the grounding gap mapped as in the core for a declared channel; the two pending framework tests, [P41] and [P20], made steps 1 and 2, and the tampering simulation step 3 (Q32) | 4 (steps 1–3 set); 5 (diagnostics) |
| 2026-10-07 | pull request #29 merged with its history; the PI approved: one mathematical reader, H34 as C3's second arm, the general core unfrozen for outcomes that are not finite and estimation (step 4), the history kept (Q33). A survey of what the framework can import: twenty sources verified from their records, filed in `RELATED.md`, ranked in `NOTES.md` §9 | 5 (imports for the estimation work); 2 (the count restarts with step 4) |
