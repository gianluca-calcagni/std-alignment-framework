---
kind: proposition
id: P52
aliases: ["P52"]
source: "derived/estimation.md"
---
# P52 — What a sample certifies about misalignment, by access
> [!info] Generated from [derived/estimation.md](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/derived/estimation.md#p52--what-a-sample-certifies-about-misalignment-by-access). Edit the source, not this note.

## Statement
Under the standard specification of a non-constant `F`, let `p ∈ Δ°` have revealed intensity `0 < t* < ∞`
and nearest intended behaviour `p° = p_{F,t*}` ([[P5 — Misalignment is attained, and zero exactly on the intended behaviours and their limits|P5]](iv)), and let `w = p°/p` and `M = M(p) = KL(p‖p°)`. Draws are
independent; `x_1, …, x_n` are draws of `p`, and bars denote averages over them.
(i) **Counts.** With `q` and `F` known, let `p̂_n` be the empirical behaviour of the draws and `t̂_n` its revealed
intensity. As `n → ∞`, `√n·(M(p̂_n) − M)` converges in distribution to a normal law with mean `0` and variance
`Var_p(log w)`, and `√n·(t̂_n − t*)` to one with mean `0` and variance `Var_p(F)/Var_{p°}(F)²`.
(ii) **Log-ratios.** With only `ℓ_i = log(p(x_i)/q(x_i))` and `F_i = F(x_i)` known for each draw, let
`M̂_n = min_{s≥0} [ℓ̄ − s·F̄ + log((1/n)·Σ_i e^{s·F_i − ℓ_i})]`. Then `M̂_n ≥ 0`, with equality if and only if, for some
`s ≥ 0`, `ℓ_i − s·F_i` is the same for every draw; so `M̂_n = 0` for every sample of an actor on the ray. As `n → ∞`,
`√n·(M̂_n − M)` converges to a normal law with mean `0` and variance `Var_p(w − log w)`.
(iii) **Two samples.** With, besides (ii), `m` draws `y_1, …, y_m` of `q` and their `F(y_j)`, let
`M̃ = min_{s≥0} [ℓ̄ − s·F̄ + log((1/m)·Σ_j e^{s·F(y_j)})]`. As `n, m → ∞` with `m/n` fixed, `(M̃ − M)/σ` converges to
the standard normal law, with `σ² = Var_p(log w)/n + χ²(p°‖q)/m`. This holds on the ray too, where `M = 0` and `M̃` is
negative with probability tending to one half.

## In plain terms
How sharply a record pins down misalignment depends on what the observer can compute, not only on
how much is recorded. Counting outcomes, the error shrinks like one over the square root of the number of draws, as for
any average. Knowing how much more likely the actor made each draw than the default would have, as for a language model
scored by both policies, the estimate is never negative, is exactly zero for an actor that pursues the objective, and is
far sharper near it; but it reweights the actor's own draws, which costs samples once the actor is far from its nearest
intended behaviour, and then counting does better. With draws of the default as well, the estimate can be negative, and
its noise does not vanish even for an actor that does pursue the objective: it grows with how far that pursuit has moved
from the default.

## Proof
Let `A(s) = log E_q[e^{s·F}]`, so that `A'(s) = E_{p_{F,s}}[F]`, `A''(s) = Var_{p_{F,s}}(F) > 0`, and, with
`ℓ = log(p/q)`, `log w = t*·F − A(t*) − ℓ`. Each estimate is `min_{s≥0} Ψ(r̂, s)`, where `r̂` is the empirical behaviour
of the draws and `Ψ` is smooth in both arguments: in (i), `Ψ(r, s) = KL(r‖p_{F,s})`; in (ii),
`Ψ(r, s) = Σ_x r(x)·(ℓ(x) − s·F(x)) + log Σ_x r(x)·e^{s·F(x) − ℓ(x)}`; in (iii), with `r = (r_p, r_q)` the two empirical
behaviours, `Ψ(r, s) = Σ_x r_p(x)·(ℓ(x) − s·F(x)) + log Σ_x r_q(x)·e^{s·F(x)}`. At the true behaviours, all three equal
`KL(p‖p_{F,s})`, since `E_p[e^{s·F − ℓ}] = E_q[e^{s·F}] = e^{A(s)}`: strictly convex in `s`, with second derivative
`A''(s)`, and minimized at `t* > 0` with the value `M`. By the implicit function theorem the minimizer is a smooth
function of `r` near the true behaviours, and interior to `s ≥ 0`; so with probability tending to one the estimate is
`Ψ` at `r̂` and at that minimizer. By the envelope theorem, its derivative along a change `h` of `r`, with
`Σ_x h(x) = 0` in each sample, is that of `Ψ(·, t*)`:
- in (i), `Σ_x h(x)·(log(p(x)/p°(x)) + 1) = −Σ_x h(x)·log w(x)`;
- in (ii), `Σ_x h(x)·(ℓ(x) − t*·F(x) + e^{t*·F(x) − ℓ(x) − A(t*)}) = Σ_x h(x)·(w(x) − log w(x))`, since
  `e^{t*·F − ℓ − A(t*)} = p°/p = w` and constants drop;
- in (iii), `−Σ_x h_p(x)·log w(x) + Σ_x h_q(x)·p°(x)/q(x)`, by the same identities.
By the central limit theorem, `√n·(r̂ − r)` converges to a normal law with covariance `diag(r) − r·rᵀ`, independently
for the two samples of (iii); the delta method gives normal limits with the variances `Var_p(log w)`,
`Var_p(w − log w)`, and `Var_p(log w)/n + Var_q(p°/q)/m`, where `Var_q(p°/q) = χ²(p°‖q)`. In (i), with probability
tending to one, `t̂_n = (A')^{−1}(E_{p̂_n}[F])` ([[P5 — Misalignment is attained, and zero exactly on the intended behaviours and their limits|P5]](iv)), and the delta method, with `√n·(E_{p̂_n}[F] − E_p[F])` of
limit variance `Var_p(F)` and the derivative `1/A''(t*) = 1/Var_{p°}(F)`, gives its law. In (ii), by Jensen's
inequality, `log Σ_x r̂(x)·e^{s·F(x) − ℓ(x)} ≥ Σ_x r̂(x)·(s·F(x) − ℓ(x))`, so `Ψ(r̂, s) ≥ 0`, with equality exactly when
`s·F − ℓ` is constant on the outcomes drawn. `Ψ(r̂, ·)` is constant when every outcome drawn has the same `F`, and grows
without bound as `s → ∞` otherwise, so its minimum over `s ≥ 0` is attained, and is `0` exactly when such an `s ≥ 0`
exists. On the ray, `ℓ = t*·F − A(t*)`. In (iii), on the ray `log w = 0`, and the limit is the reference's term alone, a
normal law centred at `0`.

## Notes
*How the regimes compare.* Counting, and the actor's half of (iii), carry `Var_p(log w)`, about `2M` near the
ray. Knowing the log-ratios replaces it by `Var_p(w − log w)`: near the ray `w − log w = 1 + (w − 1)²/2 + O((w − 1)³)`,
so the variance is of the order of `M²` rather than `M`, and the relative error of order `1/√n` rather than `1/√(n·M)`.
In five instances near the ray (`probes/diagnostics/probe_access.py`) it is 4.5 to 24 times smaller than by counting.
Far from the ray the order reverses, since `Var_p(w) = χ²(p°‖p) ≥ e^{KL(p°‖p)} − 1` ([[P47 — The cost of reweighting|P47]](i)) measures a reweighting of
the actor's draws towards its nearest intended behaviour. In the probe's survey of 4,000 random actors, the log-ratios
gave the smaller variance for 84% of those with `M` below `0.01` nats, 45% between `0.1` and `0.3`, and 14% above `1`;
by the reweighting, for 86% of those with `χ²(p°‖p)` below `0.5`, and 5% above `2`. So an actor far from its nearest
intended behaviour is better estimated with draws of the default as well, as in (iii); both variances are estimable from
the draws, and which estimate a case reports is declared before. At a known `t*`, the estimate of (ii) is
`log((1/n)·Σ_i w_i) − (1/n)·Σ_i log w_i`, which agrees to first order with `(1/n)·Σ_i (w_i − 1 − log w_i)`, the
control-variate estimator of KL with coefficient `1`, Schulman's; Amini, Vieira and Cotterell show that it can have
enormous variance, larger than the plain average's when the best coefficient is below one half [[References|@amini2025]]. Here the
coefficient is not chosen. With log-ratios alone, each `w_i = e^{t*·F_i − ℓ_i − A(t*)}` is known only up to the common
factor `e^{−A(t*)}`, and an estimate built from the averages of `log w_i` and of `w_i` that does not change when every
`w_i` is multiplied by one constant is a function of `log((1/n)·Σ_i w_i) − (1/n)·Σ_i log w_i`: to first order, its
coefficient is `1`. The plain average, `ℓ̄ − t̂·F̄ + A(t̂)`, needs `A`, that is, the default's draws or its full
distribution, as in (iii) and (i). For outcomes generated step by step, as text is, with each step's distribution known
in full, the departure `KL(p‖q)` is estimated more sharply by averaging each step's exact divergence along the draws,
their Rao–Blackwellized estimator [[References|@amini2025]]; the normalizer of a pursuit of an objective on whole outcomes is not.
*Intervals.* Each variance is an average, under `p` or `q`, of a function of `w`, and its plug-in at the estimated
intensity is consistent; so the estimate plus or minus `1.96` estimated standard errors is an interval of asymptotic
level `95%` wherever the variance is positive. On the ray, (i) has variance `0` and [[P23 — The estimated misalignment of an actor that pursues the objective|P23]] gives its law at the scale
`1/n`; the estimate of (ii) is `0` exactly; the interval of (iii) stays valid, and a negative estimate there is noise,
not an error. The laws are asymptotic: they say nothing of the bias of the self-normalized averages at a few draws. Case
W3, in regime (iii) with 32 draws of the reference per prompt, reported its split as an order of magnitude for that
reason.
*Imports.* (i) is the corollary to Theorem 3 of Huber [[References|@huber1967]], read in its scan, for `ψ(x, s) = F(x) − A'(s)`:
`λ(s) = E_p[F] − A'(s)`, `Λ = −Var_{p°}(F)`, and `C = Var_p(F)`, with `p` not assumed to lie on the ray; its covariance
`Λ^{−1}·C·Λ^{−1}` is the sandwich that White's theorem gives for misspecified likelihoods [[References|@white1982]], known here from
its record. The dichotomy of (i), a normal law at the scale `1/√n` off the ray and [[P23 — The estimated misalignment of an actor that pursues the objective|P23]]'s χ² law at the scale `1/n` on
it, is the one Vuong's abstract states for likelihood-ratio tests between models [[References|@vuong1989]]; read only in its
abstract, it is not used.
*Beyond finite outcomes.* The estimates of (ii) and (iii) are functions of a few averages, so their laws should carry
over to general spaces under conditions on moments and on the minimizer, such as Huber's; not derived here. Among them,
`E_p[w²]` and `E_q[(p°/q)²]` must be finite, χ² divergences that can be infinite when the KL divergences are finite:
existence becomes conditional (`general/dictionary.md`, finding 5). (i) has no analogue, since counting fails on a
continuum (GD11).

## Lineage
New. (i) specializes Huber's corollary; (ii) and (iii) are new as results here, from the access regimes of
`general/dictionary.md` (finding 7).

## Checks
- [`checks/test_estimation.py::test_what_a_sample_certifies_by_access`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_estimation.py)

## Depends on
- [[P5 — Misalignment is attained, and zero exactly on the intended behaviours and their limits|P5]] — Misalignment is attained, and zero exactly on the intended behaviours and their limits

## Used by
- no later item
