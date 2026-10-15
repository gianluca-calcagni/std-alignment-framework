# Probes for the v14 draft

Exploratory scripts behind the numbers in `v14/`. They are not checks: CI does not run them, and every result they
compute is proved in its file. Run `python3 probes/v14/v14_probe.py` from the repository's root; it takes a few minutes.
Its output, as run once, is in `RESULTS.md`.

| Section | Result | What it computes |
|---|---|---|
| VE1 | `v14/evidence.md` | the best bet against v13's ordinal specification, on random instances |
| VE2 | `v14/evidence.md` | an actor that mixes intensities, judged against the ray and against the ordinal specification; tests from bets and from counts, on actors whose decisions are independent or depend on each other |
| VK2–VK5 | `v14/constraints.md` | the closed forms and duals against numerical minimization; the constrained optimizer and its shadow price |
| VO3 | `v14/order.md` | the greedy decoder's verdicts |
