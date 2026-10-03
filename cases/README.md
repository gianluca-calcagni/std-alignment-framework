# Cases — tests registered before they are computed

A case is a test of the framework with a registration, a script and a result, in that order (README, rules of evidence
(d) and (e)).
1. `REGISTRATION.md` says what is computed, from which data or simulation, with every threshold and the reading of each
   outcome, and who registered it, following the design rules below. It is committed and pushed before any of its
   quantities is computed.
2. The script computes exactly what the registration says. A departure from it is marked as such in the result, and
   anything that depends on it is not confirmatory.
3. `RESULTS.md` gives each verdict, held or failed, with its numbers, the commit that registered the case, and the
   SHA-256 of `REGISTRATION.md`. Lint rule R14 recomputes the hash, so a registration cannot change after its result is
   written. A failed prediction keeps its row (rule (a)).
4. For a world case, `REPORT.md` may follow: the case reported to `STANDARD.md`, field by field, with intervals. It is
   descriptive, computed after the verdict, and changes no verdict.

Inputs are fetched by each case's scripts, never stored here: the repository keeps only code and aggregates, and each
case says under which licences its inputs were released (README, working agreements).

**Design rules**, from what W1 and W3 taught (`NOTES.md` §6; approved by the PI, Q28). Before a registration is pushed:
1. **The declaration first.** The registration contains the declaration of `STANDARD.md`, section 1, field by field. In
   particular it fixes the specification across conditions (each condition at an intensity of its own, or one shared
   intensity) and which outcomes the evaluator scores alike, ties included.
2. **Auxiliary assumptions named.** Each prediction lists what it assumes beyond the framework, such as that a training
   run converged or that a curve from the literature has a given form. The design either tests these assumptions or
   keeps the framework's own claim independent of them, and the reading of each outcome says which of them a verdict
   bears on.
3. **Thresholds with a source.** A threshold is derived from a result or from a stated scale, such as a calibrated noise
   level. A round number with neither is not registered; the prediction is then a direction, reported with its estimate
   and interval.
4. **A rehearsal.** The script runs end to end on synthetic data shaped like the real data, with the degenerate cases
   built in (a regressor that does not vary, ties, intensities at their boundaries, values that underflow), and its run
   time is measured on this machine.
5. **One statistic per source.** When a sample mixes sources, such as the outputs of two models, the registered
   statistic is computed within each source, or the registration says why pooling answers the question.

**Lessons as defaults.** A lesson written down applies only if someone remembers it; it applies by default once a
template asks for it, a tool does it, or a check refuses work without it. Each design rule above, and the failure modes
of the cases (`NOTES.md` §1), is held in one of these places:

| Lesson | Held by |
|---|---|
| the declaration before the data; named objectives and runs declared (rule 1) | `cases/TEMPLATE.md`, and lint R15: a row for every field of `STANDARD.md` |
| auxiliary assumptions named (rule 2) | `cases/TEMPLATE.md`, and lint R15: the section must exist |
| no threshold without a source (rule 3) | lint R15: every prediction fills "Threshold from" |
| a rehearsal with degenerate cases, timed (rule 4) | lint R15: `rehearsal.json` must be in the folder; `tools/casekit.py` (`seconds_per_item`) |
| one statistic per source; shares in nats away from small departures (rule 5; [P44]) | `cases/TEMPLATE.md`; not checkable by lint, so a reader's job |
| per-item results saved before aggregating; a bootstrap that keeps every item | `tools/casekit.py` (`save_rows`, `bootstrap`), tested |
| exact least squares when a regressor does not vary | `tools/casekit.py` (`least_squares`), tested |
| ties broken at random; logarithms of averages without underflow | `tools/casekit.py` (`untie`, `log_mean_exp`), tested |
| a registration does not change after its result | lint R14 |
| stopping a process by its number, never by a pattern | nothing yet: the executor's habit, broken twice (`NOTES.md` §1) |

Lint can check that a section exists, not that its content is right; that is what a reader is for, and none has read a
registration before it was pushed (Q27).

A case is of one of two kinds.
- **World**: on data from the world, not seen before the registration. Its predictions come from an ontology, have rows
  in `RECORD.md`, and count toward the finish line and the base rate.
- **Simulation**: on a system built to know the truth, such as learning algorithms whose collusion is known. It tests an
  instrument or a reading before the instrument meets the world, and counts toward neither.
- **Diagnostic**: on data from the world, a hypothesis about the system that the framework does not itself predict, such
  as what an optimizer changed beyond its reward, measured with the framework's instruments. It counts toward the fifth
  row of the finish line (diagnostics), not toward the base rate, and its predictions have no rows in `RECORD.md`.

| Case | Kind | Question | State |
|---|---|---|---|
| `c1-collusion-simulation/` | simulation | does the coordination of [P39] tell algorithms that learned to collude from players that only adapt? | done: V1, V2, S3 and S4 held; S1 and S2 failed. Coordination detects learning algorithms reacting to each other, not collusion |
| `c2-stopping-rule/` | simulation | does the stopping rule of [P20], stop where proxy and gold stop correlating, survive stochastic training, training without a KL term, and estimated covariances? | done: S1, S2 and S3 failed. The rule finds the peak of the curve of optima; the registration's thresholds had no scale, and the rule finds the first of several peaks |
| `w1-best-of-n-slope/` | world | on 12.6 million answers no one had scored with this proxy, is the literature's fitted best-of-`n` coefficient the initial slope of [P13]? | done: refuted. The fitted coefficient overstates the initial slope by 22%; the curve keeps the predicted slope up to `n = 16`, then saturates. Reported to `STANDARD.md` (`REPORT.md`, exploratory) |
| `w3-ppo-pursuit/` | world | is a public PPO-tuned language model, within each prompt, the pursuit of the reward it was tuned on? | done: S1 refuted (the reward explains a third of the revealed objective, not half, and a tenth within each model's own outputs); S2 held (it follows the reward's own scale) |
| `w4-two-runs/` | diagnostic | is what PPO changed in W3's model beyond its reward systematic, shared by a second public run, or drift? | registered; running |
