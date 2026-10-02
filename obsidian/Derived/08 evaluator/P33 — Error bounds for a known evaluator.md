---
kind: proposition
id: P33
aliases: ["P33"]
source: "derived/evaluator.md"
---
# P33 — Error bounds for a known evaluator
> [!info] Generated from [derived/evaluator.md](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/derived/evaluator.md#p33--error-bounds-for-a-known-evaluator). Edit the source, not this note.

## Statement
Let `F̂ = F + E` be an evaluator known in the units of `F` ([[D10 — Evaluator, regression and residual|D10]]), with `E` non-constant, and let
`t > 0`, `p̂ = p_{F̂,t}` and `r = p_{F,t}`. Write `Λ_r(u) = log E_r[e^{u·(E − E_r[E])}]`, and `Λ_q` the same under `q`.
(i) `M(p̂) ≤ KL(p̂‖r) = ∫_0^t s·Var_{tilt(r, s·E)}(E) ds`.
(ii) `KL(p̂‖r) ≤ t²·(max E − min E)²/8`, and the constant `1/8` cannot be lowered.
(iii) `KL(p̂‖r) ≤ Λ_r(2t) − 2Λ_r(t)`, which needs no bound on the error's range.
(iv) Within a departure budget `δ`, the target lost by pursuing `F̂` instead of `F` ([[P29 — The width is the exact worst case|P29]]) is at most
`w_δ(E) ≤ (2δ)^{1/2}·(σ₊ + σ₋) ≤ (2δ)^{1/2}·(max E − min E)`, where `σ₊² = sup_{u>0} 2Λ_q(u)/u²` and `σ₋²` is the same
for `−E`.

## In plain terms
An actor that pursues an evaluator with an error is misaligned by at most an eighth of the square of
the error's range, measured in nats at the actor's intensity: small errors cost very little. A second bound needs no
range at all, only how the error spreads under the pursuit of the target. Within a budget of departure, the principal's
loss is at most the square root of twice the budget times the error's sub-Gaussian scales up and down.

## Proof
(i) `r` is on the pursuit ray of `F`, so `M(p̂) ≤ KL(p̂‖r)` ([[D3 — Specification, declaration and misalignment|D3]]). By [[P1 — Every behaviour is a tilt of any other|P1]](iii), `p̂ = tilt(r, t·E)`. With
`g(s) = KL(tilt(r, s·E)‖r) = s·Λ_r'(s) − Λ_r(s)`, `g(0) = 0` and `g'(s) = s·Λ_r''(s) = s·Var_{tilt(r, s·E)}(E)`.
(ii) A function whose values lie in an interval of length `d` has variance at most `d²/4` under any behaviour (the
mean square distance to the interval's midpoint; Popoviciu's inequality, as in [[P26 — The regression on bins governs at small intensity|P26]]), so (i) gives at most
`(d²/4)·t²/2`. If `E` takes two values on sets of `r`-mass one half each, `Var_r(E) = d²/4`, so `g(t) = d²·t²/8 + O(t³)`
and the ratio of the two sides tends to `1` as `t → 0`. (iii) `Λ_r` is convex, so `Λ_r(2t) ≥ Λ_r(t) + t·Λ_r'(t)`, that
is, `g(t) = t·Λ_r'(t) − Λ_r(t) ≤ Λ_r(2t) − 2Λ_r(t)`. (iv) For `u > 0` and `p` in the budget,
`E_p[E] − E_q[E] ≤ (δ + Λ_q(u))/u ≤ δ/u + σ₊²·u/2` (the proof of [[P28 — The width of a departure budget|P28]](i)), which is smallest at
`u = (2δ/σ₊²)^{1/2}`; so `σ_δ(E) ≤ (2δ·σ₊²)^{1/2}`, and likewise `σ_δ(−E) ≤ (2δ·σ₋²)^{1/2}`. [[P29 — The width is the exact worst case|P29]](i) bounds the loss
by their sum. Finally, `Λ_q(u) = ∫_0^u (u − s)·Var_{tilt(q, s·E)}(E) ds ≤ (max E − min E)²·u²/8` by the same variance
bound, so `σ± ≤ (max E − min E)/2`.

## Notes
[[P10 — Sensitivity to the specification|P10]](ii) gives the linear bound `M(p̂) ≤ t·(max E − min E)`; (ii) is the smaller of the two when the error's
range in nats, `t·(max E − min E)`, is below `8`. The bound of (iv) is never looser than the range form, by the last
step of the proof. It has the separable form `a(E)·b(δ)`, which [[P30 — No separable bound on the worst case|P30]] shows cannot be accurate within a fixed factor for
every error and budget; this one grows with `δ` without bound, while the width stops at the range ([[P28 — The width of a departure budget|P28]](iii)). Main's
Prop 3 said that only the error's upper tail matters. For misalignment that holds only in a weaker form: an underrating
also costs nats, but a bounded number of them; an error confined to a set of outcomes costs at most
`max(log(1/a), log(1/(1 − a)))` nats, whatever its sign and size, with `a` the set's mass under `r` ([[C3 — An error confined to one region costs bounded nats|C3]]).

## Lineage
v7.10: Prop 2 (the sharp bound by the range), Prop 3 (only the upper tail matters, weakened: see Notes),
Prop 7 (a bound with realized travel) and Cor 1.3 (the integral form). New: the bounds as bounds on misalignment, not on
regret at a declared price.

## Checks
- [`checks/test_evaluator.py::test_error_bounds_for_a_known_evaluator`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_evaluator.py)

## Depends on
- [[D3 — Specification, declaration and misalignment|D3]] — Specification, declaration and misalignment
- [[D10 — Evaluator, regression and residual|D10]] — Evaluator, regression and residual
- [[P1 — Every behaviour is a tilt of any other|P1]] — Every behaviour is a tilt of any other
- [[P28 — The width of a departure budget|P28]] — The width of a departure budget
- [[P26 — The regression on bins governs at small intensity|P26]] — The regression on bins governs at small intensity
- [[P29 — The width is the exact worst case|P29]] — The width is the exact worst case

## Used by
- no later item
