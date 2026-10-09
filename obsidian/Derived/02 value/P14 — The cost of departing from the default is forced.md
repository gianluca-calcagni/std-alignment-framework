---
kind: proposition
id: P14
aliases: ["P14"]
source: "derived/value.md"
---
# P14 — The cost of departing from the default is forced
> [!info] Generated from [derived/value.md](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/derived/value.md#p14--the-cost-of-departing-from-the-default-is-forced). Edit the source, not this note.

## Statement
Let `q ∈ Δ°` and let `c : Δ° → ℝ` be differentiable. For every `F : X → ℝ` and every `t > 0`, the pursuit
`p_{F,t}` maximizes `E_p[F] − c(p)/t` over `Δ°` if and only if `c(p) = KL(p‖q) + C` for a constant `C`.

## In plain terms
If pursuing an objective by the steepest route ([[A2 — Pursuit is the steepest climb|A2]]) is also the best trade-off between the
objective and a cost of change ([[A3 — Pursuit is the best trade-off|A3]]), then the cost of change can only be the KL divergence from the default. No other
cost makes the two agree.

## Proof
Write `Dc(p)·v` for the derivative of `c` at `p` along a tangent vector `v`, one with `Σ_x v(x) = 0`. If
`c = KL(·‖q) + C`, then `E_p[F] − c(p)/t = J_t(p) − C/t`, which [[P4 — What KL measures|P4]](i) maximizes at `p_{F,t}`. Conversely, `p_{F,t}`
has full support, so it is an interior point of the plane `Σ_x p(x) = 1`, and at a maximizer the derivative along every
tangent `v` vanishes: `Σ_x t·F(x)·v(x) = Dc(p_{F,t})·v`. Since `log(p_{F,t}/q) = t·F − log E_q[e^{tF}]` and
`Σ_x v(x) = 0`, this says `Dc(p)·v = Σ_x log(p(x)/q(x))·v(x)` at `p = p_{F,t}`, and the right side is `D KL(·‖q)(p)·v`.
Every `p ∈ Δ°` is such a pursuit: `p = p_{G,1}` with `G = log(p/q)` ([[P1 — Every behaviour is a tilt of any other|P1]](i)). So `h = c − KL(·‖q)` has zero derivative
along every tangent direction at every point of `Δ°`. `Δ°` is convex, so `h` is constant along every segment in it,
hence constant.

## Notes
[[A2 — Pursuit is the steepest climb|A2]] says what pursuit is geometrically, and [[A3 — Pursuit is the best trade-off|A3]] economically. [[P2 — Every change of behaviour follows a replicator equation|P2]] shows that the first gives the
reweighting of [[D2 — Pursuit of an objective|D2]]; this result shows that the second agrees with it for exactly one cost. [[A3 — Pursuit is the best trade-off|A3]] reads the intensity as
the reciprocal of the price of departure. Without that reading, asking only that the best trade-offs lie on the pursuit
ray at some intensity, any increasing function of KL would also do; the second check shows `KL + KL²`, whose best
trade-off at price `1/t` is the pursuit at intensity `t/(1 + 2·KL)`. The first check shows that χ², reverse KL and
squared Hellinger make no point of the ray a best trade-off, with three or more outcomes. Hobson reached KL from other
conditions [[References|@hobson1969]].

## Lineage
v7.10: Def 2 (the bounded actor, with the KL cost assumed) and Thm 1. New: the cost is derived.

## Checks
- [`checks/test_value.py::test_the_cost_is_forced`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_value.py)
- [`checks/test_value.py::test_a_function_of_kl_moves_only_the_intensity`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_value.py)

## Depends on
- [[P1 — Every behaviour is a tilt of any other|P1]] — Every behaviour is a tilt of any other
- [[P4 — What KL measures|P4]] — What KL measures

## Used by
- [[D3 — Specification, declaration and misalignment|D3]] — Specification, declaration and misalignment
