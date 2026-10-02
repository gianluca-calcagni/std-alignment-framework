---
kind: proposition
id: P30
aliases: ["P30"]
source: "derived/evaluator.md"
---
# P30 — No separable bound on the worst case
> [!info] Generated from [derived/evaluator.md](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/derived/evaluator.md#p30--no-separable-bound-on-the-worst-case). Edit the source, not this note.

## Statement
Let `E₁` be non-constant and `A` a set of outcomes with `q(A) = r ∈ (0, 1)`.
(i) As `δ → 0`, `w_δ(E₁)/w_δ(1_A) → (Var_q(E₁)/(r·(1 − r)))^{1/2}`; and `w_δ(E₁)/w_δ(1_A) = max E₁ − min E₁` for every
`δ ≥ δ̄ = max{−log q(argmax E₁), −log q(argmin E₁), −log r, −log(1 − r)}`.
(ii) Hence any bound `a(E)·b(δ)` on the worst case `w_δ(E)` of [[P29 — The width is the exact worst case|P29]] that holds within a factor `L` for the pair
`{E₁, M·1_A}`, for some `M > 0`, over budgets that include arbitrarily small ones and one at least `δ̄`, has
`L ≥ (K)^{1/2}` with `K ≥ Var_q(E₁)^{1/2} / ((max E₁ − min E₁)·(r·(1 − r))^{1/2})`; and this grows without bound as
`q(A) → 0` with `Var_q(E₁)/(max E₁ − min E₁)²` bounded away from `0`.

## In plain terms
At a small budget, the error that does more damage is the one with more spread under the default;
at a large budget, it is the one with the wider range. An error confined to a rare region has little spread but a full
range, so it is harmless at small budgets and as bad as any at large ones. No ranking of errors holds at every budget,
and no bound that scores the error once and the budget once can be accurate at every budget.

## Proof
(i) By [[P28 — The width of a departure budget|P28]](ii), `w_δ(E) = 2·(2δ·Var_q(E))^{1/2} + O(δ^{3/2})` for both, and `Var_q(1_A) = r·(1 − r)`. By
[[P28 — The width of a departure budget|P28]](iii), once `δ ≥ δ̄` each width is its range: `max E₁ − min E₁`, and `1` for `1_A`, whose largest value is taken on
`A` and smallest on its complement. (ii) The width is multiplied by `M` when the function is ([[P28 — The width of a departure budget|P28]], Notes), so the
ratio for `{E₁, M·1_A}` is that of (i) divided by `M`, and `K` does not depend on `M`. The supremum of the ratio over
the budgets is at least its limit at `0` and its value at `δ̄`, and the infimum at most either, so `K` is at least their
quotient. [[L1 — Separable bounds are loose when two quantities change rank|L1]] with `Q(E, δ) = w_δ(E)`, the worst case by [[P29 — The width is the exact worst case|P29]](ii), gives the bound on `L`.

## Notes
Main measured the same effect for one fixed target, not only for the worst case: a dense error and a
one-outcome spike swap ranks between small and large budgets, by a factor of about a hundred. The statement in the core
is about the worst case only.

## Lineage
v7.10: Thm 9 (the worst-case regret is not separable), with its check V5, and §11.1 (no capacity-free
ranking of errors).

## Checks
- [`checks/test_evaluator.py::test_no_separable_bound_on_the_worst_case`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_evaluator.py)

## Depends on
- [[P28 — The width of a departure budget|P28]] — The width of a departure budget
- [[P29 — The width is the exact worst case|P29]] — The width is the exact worst case
- [[L1 — Separable bounds are loose when two quantities change rank|L1]] — Separable bounds are loose when two quantities change rank

## Used by
- no later item
