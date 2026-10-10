# Probes for the review of 2026-10-10

Scripts behind every number of the review in `NOTES.md` §15. They are not checks: CI does not run them, and no result
rests on them. Run them with `python3 probes/review/<probe>` from the repository's root.

| Probe | For | What it showed (2026-10-10) |
|---|---|---|
| `faithful_optimizers.py` | §15, point 1 | optimizers of the right objective, with no proxy, are charged: vanilla policy gradient on `F` leaves a median misaligned share of `0.16` up to step 1,600, best-of-2 `0.15`, best-of-16 `0.036`; under the ordinal specification ([P36]), policy gradient's median share is `0.004`. Ten seconds |
| `known_groups.py` | §15, point 1 | with a proxy that correlates about `0.96` with the target, the misaligned share ranks the exact pursuit of the proxy below best-of-4 on the target in 65% of pairs (AUC `0.35`); the ordinal share separates them (AUC `0.98` to `1.00`). Ten seconds |
| `library_edges.py` | §15, points 3 to 5 | `infinite`: `stdalign` returns `M = ∞` for an actor of full support with mass `10⁻¹²` off the best outcome; `boundary`: the χ² reference of `from_counts` rejects an actor at the default in up to `10.3%` of samples at a nominal 5%, and the χ̄² mixture does not; `counts`: the counts interval covers `94.0%` to `96.5%`; `log-ratios`: the log-ratio interval covers `84%` to `87%` at 32 draws near the ray, and `46%` far from it. About ten minutes in all |
