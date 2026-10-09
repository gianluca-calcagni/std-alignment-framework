---
kind: proposition
id: P29
aliases: ["P29"]
source: "derived/evaluator.md"
---
# P29 — The width is the exact worst case
> [!info] Generated from [derived/evaluator.md](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/derived/evaluator.md#p29--the-width-is-the-exact-worst-case). Edit the source, not this note.

## Statement
Let `F` be the target, `F̂` an evaluator known in the units of `F` ([[D10 — Evaluator, regression and residual|D10]]), and `E = F̂ − F` its error,
non-constant. Let `δ > 0`, and for `G = F` and `G = F̂` let `p*_G` be a behaviour with the largest average of `G` over
the departure budget `𝓑_δ` ([[P27 — The best use of a departure budget|P27]](ii)). Let `L = E_{p*_F}[F] − E_{p*_F̂}[F]`: the target lost by pursuing the evaluator
instead of the target within the budget.
(i) `0 ≤ L ≤ E_{p*_F̂}[E] − E_{p*_F}[E] ≤ w_δ(E)`, the width of the budget along the error ([[P28 — The width of a departure budget|P28]]).
(ii) Over all targets `F` with the same error, the supremum of `L` is `w_δ(E)`: `F = −c·E` gives `L = c·w_δ(E)`, for
every `0 < c < 1`. So no bound on `L` that depends only on the error and the budget is smaller than `w_δ(E)`.
(iii) If the budget binds for both, `δ < −log q(argmax F)` and `δ < −log q(argmax F̂)`, then `L` is the shortfall of
`p*_F̂` ([[D5 — Stakes|D5]]).

## In plain terms
An actor that has a fixed budget of departure and spends it on the evaluator instead of the
principal's objective loses some of it. The loss is never more than how far the budget lets the average of the error
move, up and down together; and for some objective it is that much. So the width is not a loose bound: it is the worst
case. When both pursuits use up the budget, the loss is the actor's stakes.

## Proof
(i) `p*_F` has the largest average of `F` over the budget and `p*_F̂` is in it, so `L ≥ 0`. `p*_F̂` has the
largest average of `F̂ = F + E` and `p*_F` is in the budget, so
`E_{p*_F̂}[F] + E_{p*_F̂}[E] ≥ E_{p*_F}[F] + E_{p*_F}[E]`, which rearranges to the middle inequality. Both behaviours
are in the budget, so `E_{p*_F̂}[E] − E_q[E] ≤ σ_δ(E)` and `E_q[E] − E_{p*_F}[E] ≤ σ_δ(−E)`, whose sum is `w_δ(E)`. (ii)
With `F = −c·E`, `F̂ = (1 − c)·E`. A positive multiple of an objective has the same best behaviours in the budget, since
`λ_δ(a·G) = λ_δ(G)/a` and `p_{aG, λ/a} = p_{G,λ}` ([[P27 — The best use of a departure budget|P27]](ii)). So `p*_F̂` raises the average of `E` by `σ_δ(E)` and
`p*_F` lowers it by `σ_δ(−E)`, and `L = c·(σ_δ(E) + σ_δ(−E)) = c·w_δ(E)`. With (i), the supremum over `c < 1` is
`w_δ(E)`. (iii) When the budget binds for `F̂`, `KL(p*_F̂‖q) = δ` ([[P27 — The best use of a departure budget|P27]](ii)), so the matched intensity of `p*_F̂` is
`λ_δ(F)` and its matched pursuit is `p_{F,λ_δ(F)} = p*_F` ([[D5 — Stakes|D5]], [[P27 — The best use of a departure budget|P27]](ii)); the shortfall is then `L`.

## Notes
The error `E = F̂ − F` needs the evaluator's scale, which behaviour never identifies ([[D10 — Evaluator, regression and residual|D10]]); this result is
about evaluators known in the target's units, such as a reward model trained to predict the target. The comparison is at
an equal budget, as stakes are ([[D5 — Stakes|D5]]); v7.10 also compared net values at a declared price, which the core does not use.
Typical losses sit well inside the width: in the check, the median of `L/w_δ(E)` is below one half.

## Lineage
v7.10: Thm 5 (the width is the exact worst case), parts (i) and (ii) at `β = ∞`; part (iii), at a declared
price, is not imported. New: (iii) here, the loss as the shortfall of [[D5 — Stakes|D5]].

## Checks
- [`checks/test_evaluator.py::test_the_width_is_the_exact_worst_case`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_evaluator.py)

## Depends on
- [[D5 — Stakes|D5]] — Stakes
- [[D10 — Evaluator, regression and residual|D10]] — Evaluator, regression and residual
- [[P27 — The best use of a departure budget|P27]] — The best use of a departure budget
- [[P28 — The width of a departure budget|P28]] — The width of a departure budget

## Used by
- [[P30 — No separable bound on the worst case|P30]] — No separable bound on the worst case
- [[P33 — Error bounds for a known evaluator|P33]] — Error bounds for a known evaluator
- [[C1 — No ranking of errors holds at every budget|C1]] — No ranking of errors holds at every budget
