---
kind: proposition
id: P15
aliases: ["P15"]
source: "derived/feasibility.md"
---
# P15 — Misalignment splits into what the actor could avoid and what it could not
> [!info] Generated from [derived/feasibility.md](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/derived/feasibility.md#p15--misalignment-splits-into-what-the-actor-could-avoid-and-what-it-could-not). Edit the source, not this note.

## Statement
Let `𝓕` be a convex feasible set ([[D7 — Feasibility|D7]]) that contains a full-support behaviour, and let `r ∈ Δ°`.
(i) **The best feasible behaviour.** Exactly one `p* ∈ 𝓕` minimizes `KL(p‖r)` over `𝓕`, and it has full support.
(ii) **Convex limits.** For every `p ∈ 𝓕`, `KL(p‖r) ≥ KL(p‖p*) + KL(p*‖r)`.
(iii) **Linear limits.** If `𝓕` is linear, with functions `f_1, …, f_m`, then `p* = tilt(r, Σ_i θ_i·f_i)` for some
numbers `θ_i`, and equality holds in (ii) for every `p ∈ 𝓕`.
(iv) **Value.** If `r = p_{F,t}` with `t > 0`, then `p*` is the unique maximizer over `𝓕` of the net value `J_t`
of [[P4 — What KL measures|P4]];
for every `p ∈ 𝓕`, `t·(J_t(p*) − J_t(p)) ≥ KL(p‖p*)`, with equality when `𝓕` is linear; and
`t·(J_t(p_{F,t}) − J_t(p*)) = KL(p*‖p_{F,t})`.
(v) **The split.** Under the standard specification of a non-constant `F`, let `𝓕` be linear, let `p̂ ∈ 𝓕` have a finite
revealed intensity `t*` with nearest intended behaviour `p° = p_{F,t*}` ([[P5 — Misalignment is attained, and zero exactly on the intended behaviours and their limits|P5]](iv)), and let `p*°` be the best feasible
behaviour for `r = p°`. Then `M(p̂) = KL(p̂‖p*°) + KL(p*°‖p°)`: the **avoidable misalignment** `KL(p̂‖p*°)`, plus the
**unavoidable misalignment** `KL(p*°‖p°)`.

## In plain terms
Among the behaviours an actor can produce, exactly one comes closest to any given intended
behaviour. When the actor's limits take the form "these averages cannot change", how far the actor is from what was
intended splits exactly into two parts: how far it is from the best it could have done, and how far that best is from
what was intended. The first is what the actor would not do, and the second what it could not. In value, the first is
what the actor left unclaimed, and the second what no feasible behaviour reaches. For limits of other shapes the split
is
only an inequality, or fails.

## Proof
(i) Since `r` has full support, `KL(·‖r)` is continuous on `Δ` and strictly convex. `𝓕` is closed in the
compact `Δ`, so a minimizer exists, and it is unique because `𝓕` is convex. Let `p̃ ∈ 𝓕` have full support, and
suppose `p*(x) = 0` for some `x`. Along `p_λ = (1 − λ)·p* + λ·p̃`, which stays in `𝓕`, the terms of `KL(p_λ‖r)` at the
outcomes where `p*` vanishes have derivative `−∞` as `λ → 0+` (the derivative of `u·log u` at `0`), while the other
terms have finite derivatives. So `KL(p_λ‖r) < KL(p*‖r)` for small `λ > 0`, a contradiction.
(ii) For `p ∈ 𝓕` the segment `p_λ = (1 − λ)·p* + λ·p` stays in `𝓕`, so the derivative of `KL(p_λ‖r)` at `λ = 0+` is
not negative. Since `p*` has full support and `Σ_x (p(x) − p*(x)) = 0`, that derivative is
`Σ_x (p(x) − p*(x))·log(p*(x)/r(x))`, so `E_p[log(p*/r)] ≥ KL(p*‖r)`. For every `p ∈ Δ`,
`KL(p‖r) − KL(p‖p*) = E_p[log(p*/r)]`, which gives (ii).
(iii) Near `p*`, which has full support, `𝓕` coincides with the affine set `{p : Σ_x p(x) = 1, E_p[f_i] = a_i}`, and
`p*` minimizes `KL(·‖r)` on it locally. So the derivative of `KL(·‖r)` at `p*` vanishes along every `v` with
`Σ_x v(x) = 0` and `Σ_x f_i(x)·v(x) = 0` for all `i`: `log(p*/r) + 1` is orthogonal to that subspace, hence in
`span{1, f_1, …, f_m}`, and `p* = tilt(r, Σ_i θ_i·f_i)`. Then for every `p ∈ 𝓕`,
`E_p[log(p*/r)] = Σ_i θ_i·a_i − log E_r[e^{Σ_i θ_i f_i}]`, the same number for every `p ∈ 𝓕`, so it equals its value at
`p*`, `KL(p*‖r)`, and the identity in the proof of (ii) holds with equality.
(iv) By [[P4 — What KL measures|P4]](i), `t·J_t(p) = log E_q[e^{tF}] − KL(p‖p_{F,t})` for every `p`. So maximizing `J_t` over `𝓕` is minimizing
`KL(·‖p_{F,t})` over `𝓕`, which (i) does at `p*` alone, and the two value differences are (ii), (iii) and the identity
at `p = p*`.
(v) By [[P5 — Misalignment is attained, and zero exactly on the intended behaviours and their limits|P5]](iv), `M(p̂) = KL(p̂‖p°)` with `p° ∈ Δ°`. Apply (iii) with `r = p°`.

## Notes
(ii) and (iii) are Csiszár's Pythagorean theorem for I-projections [[References|@csiszar1975]]; (iv) reads it as an exact
accounting of net value. Three limits met in practice are linear, and the checks confirm each.
- *Contexts*: situations whose frequencies the actor does not choose, `f = 1_C` for each group `C` of outcomes. The best
  feasible behaviour is pursuit within each context at one shared intensity, and the unavoidable part is
  `KL(q_𝒞‖(p_{F,t})_𝒞)`: how much the unconstrained pursuit would have reweighted the contexts.
- *An actor's resolution* ([[D4 — Resolution|D4]]): `p(x)·q(y) − p(y)·q(x) = 0` for `x`, `y` in one cell. The best feasible behaviour is
  `tilt(q, t·F̄)`, the best effort of [[P8 — An actor that cannot tell outcomes apart|P8]](ii), and the unavoidable part is the Jensen gap of [[P8 — An actor that cannot tell outcomes apart|P8]](iii).
- *Acting in a random environment*: trajectory distributions with fixed transition probabilities. The best feasible
  behaviour is the maximum-entropy policy, computed backward with the expectation over the environment's moves. The
  unavoidable part is positive when the environment is random and zero when it is deterministic: the actor is not
  blamed for the dice.
A limit of capacity, such as a parametric family, is not convex; the third check shows a curved family on which even
(ii) fails. Then only `M(p̂) ≥ inf_{p∈𝓕} M(p)` remains.

## Lineage
New. v7.10: Def 23's feasibility slot, B1 and ROADMAP §6 G2 (retention), and the v8 design question on
contexts (`NOTES.md`), which (v) answers: across contexts, the shared intensity is derived, not chosen.

## Checks
- [`checks/test_feasibility.py::test_linear_limits_split_exactly`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_feasibility.py)
- [`checks/test_feasibility.py::test_convex_limits_give_an_inequality`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_feasibility.py)
- [`checks/test_feasibility.py::test_curved_limits_can_break_the_split`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_feasibility.py)
- [`checks/test_feasibility.py::test_the_split_is_the_accounting_of_net_value`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_feasibility.py)
- [`checks/test_feasibility.py::test_misalignment_splits_into_avoidable_and_unavoidable`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_feasibility.py)
- [`checks/test_feasibility.py::test_contexts_and_coarse_actors_are_linear_limits`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_feasibility.py)
- [`checks/test_feasibility.py::test_a_random_environment_is_a_linear_limit`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_feasibility.py)

## Depends on
- [[D7 — Feasibility|D7]] — Feasibility
- [[P4 — What KL measures|P4]] — What KL measures
- [[P5 — Misalignment is attained, and zero exactly on the intended behaviours and their limits|P5]] — Misalignment is attained, and zero exactly on the intended behaviours and their limits

## Used by
- [[P27 — The best use of a departure budget|P27]] — The best use of a departure budget
