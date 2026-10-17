# Probes for the v14 draft

Exploratory scripts behind the numbers in `v14/`. They are not checks: CI does not run them, and every result they
compute is proved in its file, except VK4(iii), which they only support. Run `python3 probes/v14/v14_probe.py` from the
repository's root; it takes a few minutes. Its output, as run once, is in `RESULTS.md`.

| Section | Result | What it computes |
|---|---|---|
| VE1 | `v14/evidence.md` | the best bet against v13's ordinal specification, on random instances |
| VE2 | `v14/evidence.md` | an actor that mixes intensities, judged against the ray and against the ordinal specification; tests from bets and from counts, on actors whose decisions are independent or depend on each other |
| VK2–VK5 | `v14/constraints.md` | the closed forms and duals against numerical minimization; the constrained optimizer and its shadow price |
| VO3 | `v14/order.md` | the greedy decoder's verdicts |
| `culpability.py` | `v14/factorization.md` (FA2's Notes), `v14/LIMITS.md`, `NOTES.md` §25 | the excess misalignment against the evidence of culpability, when a breach is unavoidable; output in `RESULTS-culpability.md` |
| `factorization.py` | `v14/factorization.md` | v13's [P15](v) split against the least misalignment of the feasible set; FA2's identity `K = E + R`; FA3 on nested linear sets; output in `RESULTS-factorization.md` |
