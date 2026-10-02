---
kind: proposition
id: P38
aliases: ["P38"]
source: "derived/value.md"
---
# P38 — Any convex cost
> [!info] Generated from [derived/value.md](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/derived/value.md#p38--any-convex-cost). Edit the source, not this note.

## Statement
Let `t > 0`, and let `U` and `φ` be functions on `Δ` such that `Ψ = φ/t − U`, extended to the positive
functions on `X`, is convex. Let `p*` maximize `J = U − φ/t` over `Δ`, with `Ψ` differentiable at `p*`, and let
`B_Ψ(p, p*) = Ψ(p) − Ψ(p*) − ⟨∇Ψ(p*), p − p*⟩` be its Bregman divergence. Then for every `p ∈ Δ`,
`J(p*) − J(p) = B_Ψ(p, p*) − ⟨∇J(p*), p − p*⟩ ≥ B_Ψ(p, p*)`, with equality when `p*` has full support. In particular:
(i) for `U(p) = E_p[F]` and `φ = KL(·‖q)`, `B_Ψ(p, p*) = KL(p‖p*)/t`: this is [[P4 — What KL measures|P4]](i);
(ii) for `U(p) = E_p[F]` and `φ(p) = χ²(p‖q) = Σ_x (p(x) − q(x))²/q(x)`, `B_Ψ(p, p*) = Σ_x (p(x) − p*(x))²/(t·q(x))`,
and the best behaviour can rule outcomes out, where the identity becomes an inequality;
(iii) for `U(p) = E_p[F] − κ·(E_p[G])²` with `κ > 0`, a concave value that is not the average of any function, and
`φ = KL(·‖q)`, `B_Ψ(p, p*) = KL(p‖p*)/t + κ·(E_p[G] − E_{p*}[G])²`.

## In plain terms
Whatever convex cost an actor pays for departing from its default, and whatever concave value it
seeks, every other behaviour gives up at least a divergence built from the cost, exactly that much when the actor's
best behaviour rules nothing out. KL is one such cost, and [[P4 — What KL measures|P4]] is the case. This result is about actors that pay other
costs: the measure of misalignment stays KL ([[P14 — The cost of departing from the default is forced|P14]]).

## Proof
`J = −Ψ`, so `J(p*) − J(p) = Ψ(p) − Ψ(p*) = B_Ψ(p, p*) + ⟨∇Ψ(p*), p − p*⟩`, and `∇Ψ(p*) = −∇J(p*)`. At a
maximum of the concave `J` over the convex `Δ`, `⟨∇J(p*), p − p*⟩ ≤ 0` for every `p ∈ Δ`, which gives the inequality.
If `p*` has full support, the first-order condition makes `∇J(p*)` constant on `X`, and `Σ_x (p − p*)(x) = 0`, so the
term vanishes. For (i)–(iii), the Bregman divergence of a sum is the sum of the Bregman divergences; that of a linear
function is `0`; that of `Σ_x p(x)·log(p(x)/q(x))` is `KL(p‖p*)` on behaviours; that of `Σ_x (p(x) − q(x))²/q(x)` is
`Σ_x (p(x) − p*(x))²/q(x)`; and that of `κ·(E_p[G])²` is `κ·(E_p[G] − E_{p*}[G])²`.

## Notes
The budgets of other shapes in [[P31 — Budgets of other shapes|P31]] are the hard-limit forms of such costs. (ii) shows why a `χ²` cost can
make an actor rule outcomes out entirely, which a KL cost never does.

## Lineage
v7.10: Prop 15 (the identity for any convex regularizer).

## Checks
- [`checks/test_value.py::test_any_convex_cost`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_value.py)

## Depends on
- [[P4 — What KL measures|P4]] — What KL measures

## Used by
- no later item
