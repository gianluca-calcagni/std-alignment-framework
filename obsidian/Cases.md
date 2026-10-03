# Cases — tests registered before they are computed

A case is a test of the framework with a registration, a script and a result, in that order (README, rules of evidence
(d) and (e)).
1. `REGISTRATION.md` says what is computed, from which data or simulation, with every threshold and the reading of each
   outcome, and who registered it. It is committed and pushed before any of its quantities is computed.
2. The script computes exactly what the registration says. A departure from it is marked as such in the result, and
   anything that depends on it is not confirmatory.
3. `RESULTS.md` gives each verdict, held or failed, with its numbers, the commit that registered the case, and the
   SHA-256 of `REGISTRATION.md`. Lint rule R14 recomputes the hash, so a registration cannot change after its result is
   written. A failed prediction keeps its row (rule (a)).
4. For a world case, `REPORT.md` may follow: the case reported to `STANDARD.md`, field by field, with intervals. It is
   descriptive, computed after the verdict, and changes no verdict.

Inputs are fetched by each case's scripts, never stored here: the repository keeps only code and aggregates, and each
case says under which licences its inputs were released (README, working agreements).

A case is of one of two kinds.
- **World**: on data from the world, not seen before the registration. Its predictions come from an ontology, have rows
  in `RECORD.md`, and count toward the finish line and the base rate.
- **Simulation**: on a system built to know the truth, such as learning algorithms whose collusion is known. It tests an
  instrument or a reading before the instrument meets the world, and counts toward neither.

| Case | Kind | Question | State |
|---|---|---|---|
| `c1-collusion-simulation/` | simulation | does the coordination of [[P39 — Several actors: coordination plus individual misalignment\|P39]] tell algorithms that learned to collude from players that only adapt? | done: V1, V2, S3 and S4 held; S1 and S2 failed. Coordination detects learning algorithms reacting to each other, not collusion |
| `c2-stopping-rule/` | simulation | does the stopping rule of [[P20 — Where overoptimization starts, and how it ends\|P20]], stop where proxy and gold stop correlating, survive stochastic training, training without a KL term, and estimated covariances? | done: S1, S2 and S3 failed. The rule finds the peak of the curve of optima; the registration's thresholds had no scale, and the rule finds the first of several peaks |
| `w1-best-of-n-slope/` | world | on 12.6 million answers no one had scored with this proxy, is the literature's fitted best-of-`n` coefficient the initial slope of [[P13 — What the start of a change gains\|P13]]? | done: refuted. The fitted coefficient overstates the initial slope by 22%; the curve keeps the predicted slope up to `n = 16`, then saturates. Reported to `STANDARD.md` (`REPORT.md`, exploratory) |
| `w3-ppo-pursuit/` | world | is a public PPO-tuned language model, within each prompt, the pursuit of the reward it was tuned on? | done: S1 refuted (the reward explains a third of the revealed objective, not half, and a tenth within each model's own outputs); S2 held (it follows the reward's own scale) |
