---
kind: proposition
id: P2
aliases: ["P2"]
source: "derived/tilts-and-paths.md"
---
# P2 — Every change of behaviour follows a replicator equation
> [!info] Generated from [derived/tilts-and-paths.md](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/derived/tilts-and-paths.md#p2--every-change-of-behaviour-follows-a-replicator-equation). Edit the source, not this note.

## Statement
Let `s ↦ p_s` be a continuously differentiable path in `Δ°`, over an interval containing `0`, and let
`F_s = ∂_s log p_s`, the **revealed objective** at time `s`.
(i) **Replicator form.** `ṗ_s = p_s·(F_s − E_{p_s}[F_s])`. A function `G` satisfies `ṗ_s = p_s·(G − E_{p_s}[G])` if and
only if `G − F_s` is constant.
(ii) **Steepest climb.** Give `Δ°` the Fisher metric `g_p(u, v) = Σ_x u(x)·v(x)/p(x)` on tangent vectors, those with
`Σ_x u(x) = 0`. For every `F : X → ℝ`, the field `p·(F − E_p[F])` is the gradient of `p ↦ E_p[F]`. If `F` is not
constant, then among tangent directions of unit length it is the one along which `E_p[F]` rises fastest.
(iii) **The flow of a fixed objective.** For every `r ∈ Δ°` and `F : X → ℝ`, the path `s ↦ tilt(r, s·F)`, for `s ∈ ℝ`,
is the unique solution of `ṗ = p·(F − E_p[F])` with `p_0 = r`.

## In plain terms
Any change of behaviour over time can be described as climbing an objective that may itself change
over time, and that objective can be read off the change, except for a constant. When distances between behaviours are
measured the way statistics measures them, this form of change is the steepest possible climb of the objective's
average. Climbing a fixed objective this way from a starting behaviour is exactly reweighting that behaviour by the
objective, more and more strongly.

## Proof
(i) Differentiating `Σ_x p_s(x) = 1` gives `E_{p_s}[F_s] = Σ_x ṗ_s(x) = 0`, so
`p_s·(F_s − E_{p_s}[F_s]) = p_s·∂_s log p_s = ṗ_s`. If `G` satisfies the equation, then
`G − E_{p_s}[G] = ṗ_s/p_s = F_s`, so `G − F_s` is constant. Conversely, a constant cancels in `G − E_{p_s}[G]`.
(ii) The derivative of `f(p) = E_p[F]` along a tangent vector `u` is `Σ_x F(x)·u(x)`. The field `v = p·(F − E_p[F])` is
tangent, because it sums to `0`, and `g_p(v, u) = Σ_x (F(x) − E_p[F])·u(x) = Σ_x F(x)·u(x)` for every tangent `u`. So
`v` is the gradient of `f`. If `F` is not constant, then `v ≠ 0`, and for `g_p(u, u) = 1` Cauchy–Schwarz gives
`Σ_x F(x)·u(x) = g_p(v, u) ≤ g_p(v, v)^{1/2}`, with equality at `u = v / g_p(v, v)^{1/2}`.
(iii) `log tilt(r, s·F) = log r + s·F − log E_r[e^{sF}]`, so `∂_s log tilt(r, s·F) = F − c(s)` for a number `c(s)`, and
by (i) the path satisfies the equation; it starts at `r`. The field `p·(F − E_p[F])` is a polynomial in `p`, hence
locally Lipschitz on `Δ°`, so the solution through `r` is unique.

## Notes
"Revealed" is meant as in revealed preference: read from behaviour, not assumed about the actor. In
population genetics the revealed objective is the Malthusian fitness of each type (its per-capita growth rate), up to a
constant, and the replicator equation is the gradient of mean fitness in this metric, known there as the Shahshahani
metric [[References|@shahshahani1979]].

## Lineage
New as a proposition. v7.10: NOTES §2.1 ("everything is a tilt") and ROADMAP §6 I1 (dynamics: increments
cancel the default).

## Checks
- [`checks/test_paths.py::test_replicator_form_of_any_path`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_paths.py)
- [`checks/test_paths.py::test_replicator_is_fisher_gradient`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_paths.py)
- [`checks/test_paths.py::test_pursuit_ray_solves_the_replicator_flow`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_paths.py)

## Depends on
- nothing

## Used by
- [[D2 — Pursuit of an objective|D2]] — Pursuit of an objective
- [[P13 — What the start of a change gains|P13]] — What the start of a change gains
- [[P19 — A monotone regression rules out overoptimization|P19]] — A monotone regression rules out overoptimization
- [[P23 — The estimated misalignment of an actor that pursues the objective|P23]] — The estimated misalignment of an actor that pursues the objective
