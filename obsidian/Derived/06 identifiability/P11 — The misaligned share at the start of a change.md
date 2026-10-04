---
kind: proposition
id: P11
aliases: ["P11"]
source: "derived/identifiability.md"
---
# P11 — The misaligned share at the start of a change
> [!info] Generated from [derived/identifiability.md](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/derived/identifiability.md#p11--the-misaligned-share-at-the-start-of-a-change). Edit the source, not this note.

## Statement
Let `F` be non-constant, and let `s ↦ p_s`, for `s ≥ 0`, be a twice continuously differentiable path in
`Δ°` with `p_0 = q`, whose revealed objective `G` at `s = 0` is non-constant. The **angle** `θ` between `G` and `F`
is given by `cos θ = Cov_q(G, F) / (Var_q(G)·Var_q(F))^{1/2}`. Under the standard specification of `F`, as `s → 0`,
`M(p_s)/KL(p_s‖q) → sin²θ` if `cos θ ≥ 0`, and `→ 1` if `cos θ < 0`. If `cos θ < 0`, then `M(p_s) = KL(p_s‖q)` for
every small enough `s > 0`.

## In plain terms
Whenever a behaviour starts to move away from the default, the share of its departure that is
misaligned is set by one angle: the angle between the objective its change reveals and the declared objective, whose
cosine is the correlation of the two under the default. Moving straight along the objective is no misalignment; moving
at a right angle to it is all misalignment, and so is moving against it.

## Proof
Since the path is twice continuously differentiable with `p_0 = q`, `p_s = tilt(q, a_s)` with
`a_s = s·G + O(s²)`. Expanding the log-normalizer `Λ(c) = log E_q[e^c]` to second order gives
`KL(tilt(q, a)‖tilt(q, b)) = ½·Var_q(a − b) + O(‖a‖³ + ‖b‖³)` for small `a`, `b`, so
`KL(p_s‖q) = ½·s²·Var_q(G) + O(s³)`, which is positive for small `s > 0`. Let
`ψ(s) = E_{p_s}[F] − E_q[F] = s·Cov_q(G, F) + O(s²)`.
If `cos θ < 0`, then `ψ(s) < 0` for small `s > 0`, and the first case of [[P5 — Misalignment is attained, and zero exactly on the intended behaviours and their limits|P5]](iv) gives `M(p_s) = KL(p_s‖q)`.
Otherwise, whenever `ψ(s) ≤ 0` the same case gives a share of `1`. When `ψ(s) > 0`, it is also below `max F − E_q[F]`
for small `s`, so the second case applies: `M(p_s) = KL(p_s‖p_{F,t*})` with `E_{p_{F,t*}}[F] = E_{p_s}[F]`. Since
`t ↦ E_{p_{F,t}}[F]` has derivative `Var_q(F) > 0` at `t = 0`, the inverse function theorem gives
`t* = ψ(s)/Var_q(F) + O(ψ(s)²) = s·ρ + O(s²)`, with `ρ = Cov_q(G, F)/Var_q(F)`. Then
`M(p_s) = ½·Var_q(s·G − t*·F) + O(s³) = ½·s²·Var_q(G − ρ·F) + O(s³)`, and
`Var_q(G − ρ·F) = Var_q(G) − Cov_q(G, F)²/Var_q(F) = Var_q(G)·sin²θ`. Dividing by `KL(p_s‖q)` gives `sin²θ` in the
limit. If `cos θ = 0`, then `ρ = 0` and `sin²θ = 1`, which agrees with the cases where `ψ(s) ≤ 0`.

## Notes
The angle needs only two things, both at the default: the first change of behaviour and the declared
objective. The actor's own objective is never needed. [[P8 — An actor that cannot tell outcomes apart|P8]](iv)'s small-effort law is the case `G = F̄`, where
`Cov_q(F̄, F) = Var_q(F̄)`. The curvature of the path does not affect the limit, and the convergence is first order in
`s` (the check uses curved paths).

## Lineage
v7.10: ROADMAP §6 I1 and NOTES §9 (the dynamic angle, `D_⊥ ≈ sin²θ·KL`, conjectured there), and Prop 22
(the first-order effect of any smooth path). New: the statement and its proof, including the case against the objective.

## Checks
- [`checks/test_identifiability.py::test_initial_share_is_sin_squared`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_identifiability.py)

## Depends on
- [[P5 — Misalignment is attained, and zero exactly on the intended behaviours and their limits|P5]] — Misalignment is attained, and zero exactly on the intended behaviours and their limits

## Used by
- [[P13 — What the start of a change gains|P13]] — What the start of a change gains
- [[P44 — What named objectives explain|P44]] — What named objectives explain
- [[P49 — Outer and inner misalignment|P49]] — Outer and inner misalignment
