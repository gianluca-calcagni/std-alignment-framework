---
kind: proposition
id: P45
aliases: ["P45"]
source: "derived/diagnostics.md"
---
# P45 — Drift: what runs share, and what they do not
> [!info] Generated from [derived/diagnostics.md](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/derived/diagnostics.md#p45--drift-what-runs-share-and-what-they-do-not). Edit the source, not this note.

## Statement
Let `p̂_1, …, p̂_m ∈ Δ`, with `m ≥ 2`, be **runs**, such as the behaviours left by separate runs of one
training procedure, with weights `w_i > 0` that add up to `1`. Let `p̄ = Σ_i w_i·p̂_i`, and let the **drift** of the
runs be `D = Σ_i w_i·KL(p̂_i‖p̄)`. Let `(q, 𝓘)` be a specification.
(i) For every `r ∈ Δ°`, `Σ_i w_i·KL(p̂_i‖r) = KL(p̄‖r) + D`. So the **shared misalignment** of the runs,
`inf_{r∈𝓘} Σ_i w_i·KL(p̂_i‖r)`, their misalignment against one intended behaviour, is `M(p̄) + D`, and it is at least
`Σ_i w_i·M(p̂_i)`.
(ii) `0 ≤ D ≤ −Σ_i w_i·log w_i ≤ log m`. `D = 0` exactly when all the runs are equal, and `D = −Σ_i w_i·log w_i` exactly
when no two runs give positive probability to the same outcome.
(iii) **Few runs.** Let the runs be `m` independent draws, with equal weights, of a random behaviour `P` whose mean
`p̄_∞ = E[P]` has full support, and let `D_∞ = E[KL(P‖p̄_∞)]`, the drift of the procedure. Then
`E[D] = D_∞ − E[KL(p̄‖p̄_∞)]`, and `0 ≤ E[KL(p̄‖p̄_∞)] ≤ E[χ²(P‖p̄_∞)]/m`, where `χ²(p‖r) = Σ_x (p(x) − r(x))²/r(x)`. So
few runs underestimate the drift, on average.
(iv) **Small drift.** If `P = p̄_∞ + ε·V` for a bounded random function `V` with `Σ_x V(x) = 0`, `E[V] = 0`, and `V ≠ 0`
with positive probability, then `E[D]/D_∞ → 1 − 1/m` as `ε → 0`. So `m·D/(m − 1)` corrects few runs for small drift.

## In plain terms
Train the same way several times and the runs differ. Judged against one intended behaviour, their
misalignment splits exactly into the misalignment of their average and the drift: how much an outcome tells about which
run produced it. Drift cannot exceed what the run's label can tell, at most `log m` nats for `m` runs, so a few runs see
only small drift in full. On average they see less drift than there is, about a fraction `1 − 1/m` of it when it is
small.

## Proof
(i) Where `p̂_i(x) > 0`, `log(p̂_i(x)/r(x)) = log(p̂_i(x)/p̄(x)) + log(p̄(x)/r(x))`; averaging under `p̂_i`
and weighting by `w_i` gives the identity, since `Σ_i w_i·p̂_i = p̄`. Equivalently, it is [[P39 — Several actors: coordination plus individual misalignment|P39]](i) for two actors, the
run label with behaviour `w` and the outcome, whose coordination is `D`. Taking the infimum over `r ∈ 𝓘` of both sides
gives `M(p̄) + D` ([[D3 — Specification, declaration and misalignment|D3]]), and the infimum of a weighted sum is at least the weighted sum of the infima.
(ii) `D ≥ 0` as a weighted sum of divergences, and `D = 0` exactly when every `p̂_i = p̄`. Where `p̂_i(x) > 0`,
`p̄(x) ≥ w_i·p̂_i(x)`, so `log(p̂_i(x)/p̄(x)) ≤ −log w_i`, with equality exactly when no other run gives `x` positive
probability; averaging gives `D ≤ −Σ_i w_i·log w_i`, which is at most `log m` (Gibbs' inequality).
(iii) (i) with `r = p̄_∞` gives `(1/m)·Σ_i KL(p̂_i‖p̄_∞) = KL(p̄‖p̄_∞) + D`; the expectation of the left side is `D_∞`.
By Jensen's inequality, `KL(p‖r) = E_p[log(p/r)] ≤ log E_p[p/r] = log(1 + χ²(p‖r)) ≤ χ²(p‖r)`. Since the runs are
independent with mean `p̄_∞`, `E[(p̄(x) − p̄_∞(x))²] = Var(P(x))/m` for each `x`, so `E[χ²(p̄‖p̄_∞)] = E[χ²(P‖p̄_∞)]/m`.
(iv) For `p = r + δ` with `r ∈ Δ°` and `Σ_x δ(x) = 0`,
`KL(p‖r) = Σ_x (r(x) + δ(x))·log(1 + δ(x)/r(x)) = ½·Σ_x δ(x)²/r(x) + O(‖δ‖³)`. With `δ = ε·V`,
`D_∞ = ½·ε²·E[Σ_x V(x)²/p̄_∞(x)] + O(ε³)`, where the expectation is positive. The average of the runs is `p̄_∞ + ε·V̄`,
with `V̄` the average of `m` independent copies of `V`, so `E[KL(p̄‖p̄_∞)] = ½·ε²·E[Σ_x V(x)²/p̄_∞(x)]/m + O(ε³)`. By
(iii), `E[D]/D_∞ → 1 − 1/m`.

## Notes
Drift is the mutual information between the run and the outcome [[References|@cover2006]]. With finitely many runs,
`M(p̄)` is not purely what the runs share: the average keeps part of each run's drift, and as `m` grows it tends to
`M(p̄_∞)`, the misalignment of what the procedure does on average. When drift is large, `D` saturates near `log m` and
the average absorbs the rest, so two runs can confirm a small drift but only bound a large one from below: telling drift
of `d` nats from what runs share needs `m` of order `e^d` runs. The same split applies to any repetitions that should
not matter to the principal: random seeds, data orders, or sampling at another time.

## Lineage
New. It is [[P39 — Several actors: coordination plus individual misalignment|P39]](i) with the run label as a second actor; (iii) and (iv) are the information-theoretic
counterpart of the bias of the sample variance.

## Checks
- [`checks/test_diagnostics.py::test_drift_splits_shared_misalignment`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_diagnostics.py)
- [`checks/test_diagnostics.py::test_drift_from_few_runs`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_diagnostics.py)

## Depends on
- [[D3 — Specification, declaration and misalignment|D3]] — Specification, declaration and misalignment
- [[P39 — Several actors: coordination plus individual misalignment|P39]] — Several actors: coordination plus individual misalignment

## Used by
- [[P46 — What runs share between conditions, and what they do not|P46]] — What runs share between conditions, and what they do not
