---
kind: proposition
id: P28
aliases: ["P28"]
source: "derived/feasibility.md"
---
# P28 — The width of a departure budget
> [!info] Generated from [derived/feasibility.md](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/derived/feasibility.md#p28--the-width-of-a-departure-budget). Edit the source, not this note.

## Statement
Let `E : X → ℝ` be non-constant, `δ > 0`, `𝓑_δ` the departure budget of [[P27 — The best use of a departure budget|P27]], and
`Λ(u) = log E_q[e^{u·(E − E_q[E])}]`. Let `σ_δ(E) = max_{p∈𝓑_δ} E_p[E] − E_q[E]`, how far the budget lets the average
of `E` rise. The **width** of the budget along `E` is `w_δ(E) = σ_δ(E) + σ_δ(−E)`.
(i) `σ_δ(E) = inf_{u>0} (δ + Λ(u))/u`, attained at `u = λ_δ(E)` when it is finite.
(ii) As `δ → 0`, `σ_δ(E) = √(2δ·Var_q(E)) + κ₃·δ/(3·Var_q(E)) + O(δ^{3/2})`, with `κ₃ = E_q[(E − E_q[E])³]`. So
`w_δ(E) = 2·√(2δ·Var_q(E)) + O(δ^{3/2})`.
(iii) `σ_δ(E) = max E − E_q[E]` once `δ ≥ −log q(argmax E)`, and `w_δ(E) = max E − min E` once `δ` also reaches
`−log q(argmin E)`.

## In plain terms
A budget of departure lets the average of any function move only so far, up or down; the width is
the whole range it can move over. For a small budget the range is set by the function's spread under the default: about
twice the square root of twice the budget times the variance. A skewed function moves further toward its long tail, but
that shifts the range without widening it, to second order. A budget that reaches the best and the worst outcomes lets
the average move over the function's whole range.

## Proof
Write `Ẽ = E − E_q[E]`. (i) For `u > 0`, [[P4 — What KL measures|P4]](i) for the objective `Ẽ` at intensity `u` says that no
behaviour has more net value than its pursuit, whose net value is `Λ(u)/u`; so for every `p ∈ 𝓑_δ`,
`E_p[Ẽ] ≤ (KL(p‖q) + Λ(u))/u ≤ (δ + Λ(u))/u`. By [[P27 — The best use of a departure budget|P27]](ii) with `G = E`, the maximum is reached at `p_{E,λ}`,
`λ = λ_δ(E)`, when `λ` is finite. There `KL(p_{E,λ}‖q) = δ` and `KL(p_{E,λ}‖q) = λ·E_{p_{E,λ}}[Ẽ] − Λ(λ)`, so the bound
at `u = λ` is an equality. When `λ = ∞`, the maximum is `max E − E_q[E]` ([[P27 — The best use of a departure budget|P27]](ii)), and `(δ + Λ(u))/u` tends to it
as `u → ∞`, because `Λ(u)/u` does. (ii) At `λ = λ_δ(E)`, `σ_δ(E) = E_{p_{E,λ}}[Ẽ] = Λ'(λ)` and
`δ = λ·Λ'(λ) − Λ(λ)`, with `λ → 0` as `δ → 0`. With `V = Var_q(E)`, `Λ(u) = V·u²/2 + κ₃·u³/6 + O(u⁴)`, so
`δ = V·λ²/2 + κ₃·λ³/3 + O(λ⁴)`, which inverts to `λ = √(2δ/V) − 2κ₃·δ/(3V²) + O(δ^{3/2})`. Then
`σ_δ(E) = V·λ + κ₃·λ²/2 + O(λ³) = √(2δV) + κ₃·δ/(3V) + O(δ^{3/2})`. For `−E`, `κ₃` changes sign and `V` does not, so
the terms in `δ` cancel in `w_δ(E)`. (iii) By [[P27 — The best use of a departure budget|P27]](ii), the largest average of `E` over the budget is `max E` once
`δ ≥ −log q(argmax E)`; applied to `−E`, the smallest is `min E` once `δ ≥ −log q(argmin E)`.

## Notes
`σ_δ(E)` is the worst-case average of `E` over all behaviours within KL `δ` of the default, and (i) is its
dual form: the quantity robust optimization computes over a KL ambiguity set (`TERMS.md`, the width). The width is
unchanged by adding a constant to `E`, and multiplied by `c` when `E` is, for `c > 0`. It is the quantity the worst-case
results imported next are built on (`IMPORT.md`, N3 and N4).

## Lineage
v7.10: Def 6 (the width) and Prop 6 (the width, computed; its check V4). New: the term in `δ` of (ii), and
with it the symmetry of the width to that order.

## Checks
- [`checks/test_feasibility.py::test_the_width_of_a_departure_budget`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_feasibility.py)

## Depends on
- [[P4 — What KL measures|P4]] — What KL measures
- [[P27 — The best use of a departure budget|P27]] — The best use of a departure budget

## Used by
- [[P31 — Budgets of other shapes|P31]] — Budgets of other shapes
- [[P29 — The width is the exact worst case|P29]] — The width is the exact worst case
- [[P30 — No separable bound on the worst case|P30]] — No separable bound on the worst case
- [[P33 — Error bounds for a known evaluator|P33]] — Error bounds for a known evaluator
- [[C1 — No ranking of errors holds at every budget|C1]] — No ranking of errors holds at every budget
