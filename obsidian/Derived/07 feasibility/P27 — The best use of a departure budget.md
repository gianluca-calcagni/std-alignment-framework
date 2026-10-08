---
kind: proposition
id: P27
aliases: ["P27"]
source: "derived/feasibility.md"
---
# P27 — The best use of a departure budget
> [!info] Generated from [derived/feasibility.md](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/derived/feasibility.md#p27--the-best-use-of-a-departure-budget). Edit the source, not this note.

## Statement
Let `G` be non-constant, `A` the set of outcomes where `G` is largest, and `δ > 0`. The
**departure budget** `𝓑_δ = {p ∈ Δ : KL(p‖q) ≤ δ}` is a convex feasible set ([[D7 — Feasibility|D7]]) that contains `q`. Let
`λ_δ = inf{t ≥ 0 : KL(p_{G,t}‖q) ≥ δ}`, with `λ_δ = ∞` when the set is empty, which happens exactly when
`δ ≥ −log q(A)`; and `p_{G,∞} = q(·|A)`.
(i) For every `t > 0`, the net value `J_t` of `G` ([[P4 — What KL measures|P4]]) has exactly one maximizer over `𝓑_δ`,
`p* = p_{G, min(t, λ_δ)}`, and `J_t(p*) − J_t(p) ≥ KL(p‖p*)/min(t, λ_δ)` for every `p ∈ 𝓑_δ`, with equality when
`t ≤ λ_δ`. So `p*` is the best feasible behaviour of [[P15 — Misalignment splits into what the actor could avoid and what it could not|P15]](i) for `r = p_{G,t}`: the pursuit, cut off where the budget
runs out.
(ii) The largest average of `G` over `𝓑_δ` is reached at `p_{G,λ_δ}`, and only there when `δ ≤ −log q(A)`. When
`δ > −log q(A)`, it is `max G`, reached exactly by the behaviours on `A` within the budget, `q(·|A)` among them.
(iii) **The budget as a price.** `V(δ) = max_{p∈𝓑_δ} E_p[G]` is non-decreasing and concave in `δ`. For
`0 < δ < −log q(A)` it is differentiable, with `V'(δ) = 1/λ_δ`; for `δ ≥ −log q(A)`, `V(δ) = max G`.

## In plain terms
Suppose the actor may depart from the default by at most a fixed amount. Then the best it can do,
for any objective and any price of departing, is to pursue the objective and stop where the budget runs out: either the
budget does not bind, or it fixes the intensity. The last unit of budget buys `1/λ_δ` units of the objective, so a
budget and a price are one quantity in two forms: a budget is spent exactly by pursuit at the intensity `λ_δ`.

## Proof
Write `d(t) = KL(p_{G,t}‖q)`. By the proof of [[P9 — What is at stake|P9]](i), `d` increases continuously and strictly from `0`
toward `−log q(A)`, with `d'(t) = t·Var_{p_{G,t}}(G)`; so `λ_δ` is finite exactly when `δ < −log q(A)`, and then
`d(λ_δ) = δ`. (i) If `t ≤ λ_δ`, then `d(t) ≤ δ`, so `p_{G,t}` is in the budget, and [[P4 — What KL measures|P4]](i) gives
`J_t(p_{G,t}) − J_t(p) = KL(p‖p_{G,t})/t` for every `p`. If `t > λ_δ = λ`, then for `p ∈ 𝓑_δ`, [[P4 — What KL measures|P4]](i) at intensity `λ`
gives `E_p[G] − KL(p‖q)/λ = E_{p*}[G] − δ/λ − KL(p‖p*)/λ`, so
`J_t(p) = J_t(p*) − KL(p‖p*)/λ + (KL(p‖q) − δ)·(1/λ − 1/t) ≤ J_t(p*) − KL(p‖p*)/λ`, since `KL(p‖q) ≤ δ` and `1/λ > 1/t`.
In both cases the maximizer is unique. And since `J_t(p) = J_t(p_{G,t}) − KL(p‖p_{G,t})/t` for every `p` ([[P4 — What KL measures|P4]](i)),
maximizing `J_t` over `𝓑_δ` is minimizing `KL(p‖p_{G,t})` over it. (ii) If `δ < −log q(A)`, the argument of
(i) with `1/t` replaced by `0` gives `E_{p*}[G] − E_p[G] ≥ KL(p‖p*)/λ_δ` for every `p ∈ 𝓑_δ`. Otherwise `q(·|A)` is in
the budget, since its departure is `−log q(A)`, and has the average `max G`; a behaviour reaches `max G` exactly when it
puts all its mass on `A`, and such a behaviour departs by `KL(p‖q) = −log q(A) + KL(p‖q(·|A))`, so at `δ = −log q(A)`
only `q(·|A)` fits. (iii) For `0 < δ < −log q(A)`, `V(δ) = m(λ_δ)` with `m(t) = E_{p_{G,t}}[G]`, and
`m'(t) = Var_{p_{G,t}}(G)` by [[P13 — What the start of a change gains|P13]](i), since the revealed objective of the pursuit is `G` centred. By the inverse
function theorem, `V'(δ) = m'(λ_δ)/d'(λ_δ) = 1/λ_δ`. As `δ` grows, `λ_δ` grows, so `V'` falls; as `δ → −log q(A)`,
`λ_δ → ∞`, `V(δ) → max G` and `V'(δ) → 0`, which joins the constant `max G` beyond with a continuous, non-increasing,
non-negative derivative.

## Notes
A departure budget is convex but not linear, so [[P15 — Misalignment splits into what the actor could avoid and what it could not|P15]](ii) gives only an inequality for it. It is called a
departure budget, not v7.10's "capacity", because [[D7 — Feasibility|D7]] uses capacity for limits such as parametric families. Main's
capacity model, an actor that is the best budget-`δ` pursuit of its evaluator, is the case `G = F̂` of (ii). When its
budget binds, its matched pursuit ([[D5 — Stakes|D5]]) is the best budget-`δ` pursuit of `F`, so v7.10's capacity regret is the
shortfall of [[D5 — Stakes|D5]], split into its causes by [[P9 — What is at stake|P9]](ii). (iii) makes the matched intensity of [[D5 — Stakes|D5]] an exchange rate: at
the margin, `λ_δ` nats of departure buy one unit of the objective.

## Lineage
v7.10: Def 5 (the capacity actor), Lemma 5.1 (its form), Def 15 (the capacity model), Cor 5.2 (the exchange
rate is a shadow price) and Cor 17.1 (the capacity actor's regret); R076 (they assume nothing about the actor). New: the
budget as a feasible set of [[D7 — Feasibility|D7]], and its best behaviour as the one of [[P15 — Misalignment splits into what the actor could avoid and what it could not|P15]](i).

## Checks
- [`checks/test_feasibility.py::test_the_best_use_of_a_departure_budget`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_feasibility.py)

## Depends on
- [[D7 — Feasibility|D7]] — Feasibility
- [[P4 — What KL measures|P4]] — What KL measures
- [[P9 — What is at stake|P9]] — What is at stake
- [[P13 — What the start of a change gains|P13]] — What the start of a change gains
- [[P15 — Misalignment splits into what the actor could avoid and what it could not|P15]] — Misalignment splits into what the actor could avoid and what it could not

## Used by
- [[P28 — The width of a departure budget|P28]] — The width of a departure budget
- [[P31 — Budgets of other shapes|P31]] — Budgets of other shapes
- [[P29 — The width is the exact worst case|P29]] — The width is the exact worst case
- [[C2 — A KL budget does not contain a rare, large error|C2]] — A KL budget does not contain a rare, large error
