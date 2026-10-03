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

A case is of one of two kinds.
- **World**: on data from the world, not seen before the registration. Its predictions come from an ontology, have rows
  in `RECORD.md`, and count toward the finish line and the base rate.
- **Simulation**: on a system built to know the truth, such as learning algorithms whose collusion is known. It tests an
  instrument or a reading before the instrument meets the world, and counts toward neither.

| Case | Kind | Question | State |
|---|---|---|---|
| `c1-collusion-simulation/` | simulation | does the coordination of [P39] tell algorithms that learned to collude from players that only adapt? | done: V1, V2, S3 and S4 held; S1 and S2 failed. Coordination detects learning algorithms reacting to each other, not collusion |
