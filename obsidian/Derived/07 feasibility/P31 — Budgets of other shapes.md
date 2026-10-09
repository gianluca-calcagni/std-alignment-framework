---
kind: proposition
id: P31
aliases: ["P31"]
source: "derived/feasibility.md"
---
# P31 — Budgets of other shapes
> [!info] Generated from [derived/feasibility.md](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/derived/feasibility.md#p31--budgets-of-other-shapes). Edit the source, not this note.

## Statement
Let `E : X → ℝ` and `p ∈ Δ`. Write `TV(p, q) = ½·Σ_x |p(x) − q(x)|`,
`χ²(p‖q) = Σ_x (p(x) − q(x))²/q(x)`, `D_α(p‖q) = log(Σ_x p(x)^α·q(x)^{1−α})/(α − 1)` for `α > 1`, and
`D_∞(p‖q) = log max_x p(x)/q(x)`.
(i) `|E_p[E] − E_q[E]| ≤ (max E − min E)·TV(p, q)`.
(ii) `E_p[E] − E_q[E] ≤ (KL(p‖q) + Λ(u))/u` for every `u > 0`, with `Λ` as in [[P28 — The width of a departure budget|P28]].
(iii) `|E_p[E] − E_q[E]| ≤ (χ²(p‖q)·Var_q(E))^{1/2}`.
(iv) For `α > 1` and `α* = α/(α − 1)`, `E_p[|E|] ≤ e^{D_α(p‖q)/α*}·(E_q[|E|^{α*}])^{1/α*}`; and
`E_p[|E|] ≤ e^{D_∞(p‖q)}·E_q[|E|] ≤ E_q[|E|]/min_x q(x)`.
(v) For non-constant `E`, the bounds (i) and (iii) are attained by some `p` at every small enough value of the
divergence, and (ii) at the minimizing `u` ([[P28 — The width of a departure budget|P28]](i)).
(vi) For an outcome `x` with `q(x) = r`, putting all mass on `x` costs `log(1/r)` in KL and `1/r − 1` in `χ²`. So for
`E = M·1_x`, the largest rise of the average of `E` over the departure budget `δ` ([[P27 — The best use of a departure budget|P27]]) is at least
`min(1, δ/log(1/r))·M·(1 − r)`, while over the `χ²` budget `δ` it is at most `(δ·M²·r·(1 − r))^{1/2}`. With the
variance `M²·r·(1 − r)` held fixed, the first grows without bound as `r → 0`, and the second does not.

## In plain terms
Every way of limiting how far an actor departs from the default controls how far an average can move
through one measure of the function's size: total variation through its range, KL through its exponential moments, `χ²`
through its variance, a Rényi divergence through a power mean. Choosing the limit is choosing which size of an error
matters. A KL limit lets an actor reach a rare outcome at a cost that grows only with the logarithm of its rarity, so a
rare, large error can do unbounded harm under a KL limit and bounded harm under a `χ²` limit of the same size.

## Proof
(i) With `c` the midpoint of the range of `E`, `E_p[E] − E_q[E] = Σ_x (p(x) − q(x))·(E(x) − c)`, where
`|E(x) − c| ≤ (max E − min E)/2` and `Σ_x |p(x) − q(x)| = 2·TV(p, q)`. (ii) is the first inequality in the proof of
[[P28 — The width of a departure budget|P28]](i). (iii) `E_p[E] − E_q[E] = E_q[(p/q − 1)·(E − E_q[E])]`, and Cauchy–Schwarz under `q` bounds it by
`(E_q[(p/q − 1)²]·Var_q(E))^{1/2}`, where `E_q[(p/q − 1)²] = χ²(p‖q)`. (iv) Hölder's inequality under `q`:
`E_p[|E|] = E_q[(p/q)·|E|] ≤ (E_q[(p/q)^α])^{1/α}·(E_q[|E|^{α*}])^{1/α*}`, and `(E_q[(p/q)^α])^{1/α} = e^{D_α(p‖q)/α*}`;
for `α = ∞`, `E_q[(p/q)·|E|] ≤ max_x (p/q)·E_q[|E|]`, and `max_x p(x)/q(x) ≤ 1/min_x q(x)`. (v) For (i), with `δ` at
most the default's mass on the lowest values of `E` and at most its mass off the highest, move mass `δ` from the lowest
values to the highest, in proportion to `q`: the total variation is `δ` and the average rises by `δ·(max E − min E)`.
For (iii), `p = q·(1 + s·Ẽ/Var_q(E)^{1/2})`, with `Ẽ = E − E_q[E]` and `s` small enough for `p` to stay positive, has
`χ²(p‖q) = s²` and raises the average by `s·Var_q(E)^{1/2}`. (vi) For the point mass `1_x`, `KL(1_x‖q) = log(1/r)` and
`χ²(1_x‖q) = (1 − r)²/r + (1 − r) = 1/r − 1`. The mixture `(1 − ε)·q + ε·1_x` with `ε = min(1, δ/log(1/r))` has
`KL ≤ ε·log(1/r) ≤ δ`, since KL is convex in its first argument, and raises the average of `E` by `ε·M·(1 − r)`; (iii)
gives the `χ²` bound, with `Var_q(E) = M²·r·(1 − r)`. With that variance held at `v`, `M = (v/(r·(1 − r)))^{1/2}`, and
`δ·M·(1 − r)/log(1/r) → ∞` as `r → 0`.

## Notes
Each budget is a convex feasible set ([[D7 — Feasibility|D7]]), so [[P15 — Misalignment splits into what the actor could avoid and what it could not|P15]](ii) applies to all of them. The pairs (divergence,
measure of size) are conjugate: each bound is attained, at small budgets, which makes the measure of size the right one
for that divergence and not merely a valid one. (vi) is the form on finitely many outcomes of a statement that needs
infinitely many: on a continuum, an error whose tail is heavier than exponential makes the KL rise infinite at every
budget, while a finite variance keeps the `χ²` rise finite. That statement is out of the core's scope (`CORE.md` §0) and
is recorded in `IMPORT.md`. The measure of misalignment stays KL ([[P14 — The cost of departing from the default is forced|P14]]); the shapes here are limits on what an actor
can do, or costs an actor pays, not ways of measuring.

## Lineage
v7.10: Prop 10 (the conjugate pairings), Prop 11 (the order is structural; here its form on finite
outcomes) and the dictionary's entry B2 (the conjugacy scale). New: (v), the bounds attained, and (vi) in finite form.

## Checks
- [`checks/test_feasibility.py::test_feasible_sets_of_other_shapes`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_feasibility.py)

## Depends on
- [[P27 — The best use of a departure budget|P27]] — The best use of a departure budget
- [[P28 — The width of a departure budget|P28]] — The width of a departure budget

## Used by
- [[C2 — A KL budget does not contain a rare, large error|C2]] — A KL budget does not contain a rare, large error
