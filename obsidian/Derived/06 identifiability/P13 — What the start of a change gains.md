---
kind: proposition
id: P13
aliases: ["P13"]
source: "derived/identifiability.md"
---
# P13 — What the start of a change gains
> [!info] Generated from [derived/identifiability.md](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/derived/identifiability.md#p13--what-the-start-of-a-change-gains). Edit the source, not this note.

## Statement
Let `F` be non-constant, and let `s ↦ p_s`, for `s ≥ 0`, be a continuously differentiable path in `Δ°`
with revealed objectives `F_s`.
(i) **The average moves at the covariance rate.** For every `s`, `d/ds E_{p_s}[F] = Cov_{p_s}(F_s, F)`.
(ii) **At the start, the gain is set by the angle.** Let the path be as in [[P11 — The misaligned share at the start of a change|P11]], with angle `θ`, and let
`σ_q(F) = Var_q(F)^{1/2}`. As `s → 0`, `(E_{p_s}[F] − E_q[F]) / (2·KL(p_s‖q))^{1/2} → cos θ·σ_q(F)` and
`S(p_s) / (2·KL(p_s‖q))^{1/2} → (1 − cos θ)·σ_q(F)`, where `S` is the shortfall of [[D5 — Stakes|D5]].

## In plain terms
As behaviour changes, the average of any objective moves at a rate equal to the covariance, under
the current behaviour, between that objective and the objective the change reveals. At the start of a change away from
the default, each unit of departure gains the objective's spread times the cosine of the angle of [[P11 — The misaligned share at the start of a change|P11]]. Pursuing the
objective itself, with the same departure, gains the full spread, so the shortfall is the rest: one minus the cosine,
times the spread. No change gains more per unit of departure at the start than pursuit of the objective, and a change
against the objective loses.

## Proof
(i) By [[P2 — Every change of behaviour follows a replicator equation|P2]], `∂_s p_s(x) = p_s(x)·F_s(x)`, so `d/ds E_{p_s}[F] = Σ_x p_s(x)·F_s(x)·F(x) = E_{p_s}[F_s·F]`.
Since `Σ_x p_s(x) = 1` for every `s`, `E_{p_s}[F_s] = Σ_x ∂_s p_s(x) = 0`, so `E_{p_s}[F_s·F] = Cov_{p_s}(F_s, F)`.
(ii) Write `G = F_0` and `ε(s) = (2·KL(p_s‖q))^{1/2}`. The proof of [[P11 — The misaligned share at the start of a change|P11]] gives `KL(p_s‖q) = ½·s²·Var_q(G) + O(s³)`, so
`ε(s) = s·σ_q(G)·(1 + O(s))`. By (i) and Taylor's theorem, `E_{p_s}[F] − E_q[F] = s·Cov_q(G, F) + O(s²)`. Dividing, the
first ratio tends to `Cov_q(G, F)/σ_q(G) = cos θ·σ_q(F)`. For the shortfall, let `A` be the set where `F` is largest.
Along the ray, `d(t) = KL(p_{F,t}‖q) = t·E_{p_{F,t}}[F] − log E_q[e^{tF}]` is continuous and `0` at `t = 0`. The ray's
revealed objective is `F − E_{p_{F,t}}[F]`, so (i) gives `d/dt E_{p_{F,t}}[F] = Var_{p_{F,t}}(F)`, and
`d'(t) = t·Var_{p_{F,t}}(F) > 0` for `t > 0`: `d` is increasing. Its limit as `t → ∞` is `KL(q(·|A)‖q) = −log q(A) > 0`,
since `F` is non-constant. So for small `s`, the matched intensity `λ` of [[D5 — Stakes|D5]] is finite, `d(λ) = KL(p_s‖q)`, and
`λ → 0` as `s → 0`. The same second-order expansion applied to the ray gives `d(λ) = ½·λ²·Var_q(F) + O(λ³)`, so
`λ·σ_q(F) = ε(s)·(1 + O(λ))`, and `λ = O(s)`. By (i) on the ray,
`E_{p_{F,λ}}[F] − E_q[F] = λ·Var_q(F) + O(λ²) = ε(s)·σ_q(F) + O(s²)`. Subtracting the actual gain,
`S(p_s) = ε(s)·σ_q(F)·(1 − cos θ) + O(s²)`, and dividing by `ε(s)` gives the second limit.

## Notes
(i) is the Price equation [[References|@price1970]] in continuous time without its transmission term, with `F_s` in the
role of Malthusian fitness: it holds at every `s`, for any path, with no default. Along any path, the average of `F` is
stationary exactly where `Cov_{p_s}(F_s, F) = 0`. So when an actor pursues a proxy, the average of the objective peaks
only where the proxy and the objective are uncorrelated under the actor's current behaviour. (ii) is a law in the
square root of the departure, with a finite slope at zero departure, bounded by `σ_q(F)` for every smooth path, since
`|cos θ| ≤ 1`. Together with [[P11 — The misaligned share at the start of a change|P11]]: at the start of a change, `sin²θ` of the departure is misaligned, and `1 − cos θ` of
the attainable gain is lost.

## Lineage
v7.10: B §4 (for a jointly Gaussian target and evaluator, the gold gain along the Gibbs path is exactly
`√2·ρ_q(F, F̂)·sd_q(F)` times `√KL`, which (ii) generalizes to the first order of any smooth path), Prop 14 and Prop 22
(the initial effect has the sign of the covariance), ROADMAP §6 I1 (the dynamic angle) and Def 22 (the value shortfall).
New: (i) as a statement about any path, and the shortfall in (ii). The v9 restart first credited none of the first
three, which `NOTES.md` §1 records as a failure mode.

## Checks
- [`checks/test_identifiability.py::test_average_moves_at_the_covariance_rate`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_identifiability.py)
- [`checks/test_identifiability.py::test_start_gains_cos_theta_of_the_spread`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_identifiability.py)

## Depends on
- [[D5 — Stakes|D5]] — Stakes
- [[P2 — Every change of behaviour follows a replicator equation|P2]] — Every change of behaviour follows a replicator equation
- [[P11 — The misaligned share at the start of a change|P11]] — The misaligned share at the start of a change

## Used by
- [[P27 — The best use of a departure budget|P27]] — The best use of a departure budget
- [[P19 — A monotone regression rules out overoptimization|P19]] — A monotone regression rules out overoptimization
- [[P20 — Where overoptimization starts, and how it ends|P20]] — Where overoptimization starts, and how it ends
- [[P26 — The regression on bins governs at small intensity|P26]] — The regression on bins governs at small intensity
- [[C5 — The first effect of optimization depends on the optimizer; its end, on the evaluator's top|C5]] — The first effect of optimization depends on the optimizer; its end, on the evaluator's top
