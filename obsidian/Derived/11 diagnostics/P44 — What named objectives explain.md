---
kind: proposition
id: P44
aliases: ["P44"]
source: "derived/diagnostics.md"
---
# P44 — What named objectives explain
> [!info] Generated from [derived/diagnostics.md](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/derived/diagnostics.md#p44--what-named-objectives-explain). Edit the source, not this note.

## Statement
Under the standard specification of a non-constant `F`, let `p̂ ∈ Δ°`, whose revealed intensity `t*` is
then finite, have nearest intended behaviour `p°` ([[P5 — Misalignment is attained, and zero exactly on the intended behaviours and their limits|P5]](iv)). Let `G_1, …, G_k` be functions on `X`, the
**named objectives**, and let `𝓛 = {p ∈ Δ : E_p[F] = E_{p̂}[F] and E_p[G_j] = E_{p̂}[G_j] for every j}`, a linear set
([[D7 — Feasibility|D7]]) that contains `p̂`. The **named pursuit** `p̃` of `p̂` is the behaviour in `𝓛` nearest to `p°`, that is,
minimizing `KL(·‖p°)` over `𝓛` ([[P15 — Misalignment splits into what the actor could avoid and what it could not|P15]](i)).
(i) `p̃ = tilt(q, a·F + Σ_j b_j·G_j)` for some numbers `a` and `b_j`, and `p̃` has the revealed intensity `t*` and the
nearest intended behaviour `p°`.
(ii) `M(p̂) = KL(p̂‖p̃) + M(p̃)`. The first term, the **unexplained misalignment**, is `0` exactly when `p̂` is itself a
tilt of the default by some `a·F + Σ_j b_j·G_j`; the second is the **named misalignment**.
(iii) Naming more objectives moves misalignment from the first term to the second: if `p̃'` is the named pursuit for
`G_1, …, G_{k'}`, with `k' > k`, then `KL(p̂‖p̃) = KL(p̂‖p̃') + KL(p̃'‖p̃)` and `M(p̃') = M(p̃) + KL(p̃'‖p̃)`.
(iv) **At the start of a change.** Let `s ↦ p_s` be a path as in [[P11 — The misaligned share at the start of a change|P11]], with revealed objective `H` at `s = 0` and
`Cov_q(H, F) > 0`, and let the functions `1, F, G_1, …, G_k` be linearly independent. Let `R²_F` and `R²_{F,G}` be the
squared multiple correlations, under `q`, of `H` with `F` and with `F, G_1, …, G_k`, and `p̃_s` the named pursuit of
`p_s`. As `s → 0`, `KL(p_s‖p̃_s)/KL(p_s‖q) → 1 − R²_{F,G}` and `M(p̃_s)/KL(p_s‖q) → R²_{F,G} − R²_F`.

## In plain terms
When one suspects what else an actor pursues besides the declared objective, such as a second
reward, the length of its answers, or how typical its answers are, its misalignment splits exactly into what those named
objectives explain and what nothing named explains. Naming more objectives only moves misalignment from the unexplained
part to the named part. For small changes, the two parts are the familiar shares of variance that a regression leaves
unexplained and adds.

## Proof
(i) `𝓛` contains `p̂`, which has full support, so [[P15 — Misalignment splits into what the actor could avoid and what it could not|P15]](i) gives one nearest behaviour, and [[P15 — Misalignment splits into what the actor could avoid and what it could not|P15]](iii) gives
`p̃ = tilt(p°, θ_0·F + Σ_j θ_j·G_j)` for some numbers `θ`. As `t*` is finite, `p° = tilt(q, t*·F)`, so
`p̃ = tilt(q, (t* + θ_0)·F + Σ_j θ_j·G_j)`, a behaviour of full support. Since `p̃ ∈ 𝓛`, `E_{p̃}[F] = E_{p̂}[F]`, and
[[P5 — Misalignment is attained, and zero exactly on the intended behaviours and their limits|P5]](iv) depends on a behaviour only through its average of `F` when that average is below `max F`, as it is for a
behaviour of full support: so `p̃` has the same case of [[P5 — Misalignment is attained, and zero exactly on the intended behaviours and their limits|P5]](iv), the same `t*` and the same `p°` as `p̂`.
(ii) [[P15 — Misalignment splits into what the actor could avoid and what it could not|P15]](v) with `𝓕 = 𝓛`, which contains `p̂`, gives `M(p̂) = KL(p̂‖p̃) + KL(p̃‖p°)`, and `KL(p̃‖p°) = M(p̃)` by (i).
If `p̂ = p̃`, it is such a tilt by (i). Conversely, if `p̂ = tilt(q, a·F + Σ_j b_j·G_j)`, then for every `p ∈ 𝓛`,
`KL(p‖p°) − KL(p‖p̂) = E_p[log(p̂/p°)]`, which depends on `p` only through its averages of `F` and the `G_j`, the same
for all of `𝓛`; so `KL(p‖p°)` and `KL(p‖p̂)` have the same minimizer over `𝓛`, which is `p̂`.
(iii) Let `𝓛'` be the linear set for `G_1, …, G_{k'}`, so `p̂ ∈ 𝓛' ⊆ 𝓛`. By [[P15 — Misalignment splits into what the actor could avoid and what it could not|P15]](iii) on `𝓛`,
`KL(p‖p°) = KL(p‖p̃) + KL(p̃‖p°)` for every `p ∈ 𝓛`, so on `𝓛'` the behaviour nearest to `p°` is the behaviour nearest
to `p̃`: `p̃'` is both. [[P15 — Misalignment splits into what the actor could avoid and what it could not|P15]](iii) on `𝓛'`, with `p̃` in the role of `r`, gives `KL(p̂‖p̃) = KL(p̂‖p̃') + KL(p̃'‖p̃)`.
With (ii) for `p̃` and for `p̃'`, `M(p̃') = M(p̂) − KL(p̂‖p̃') = M(p̃) + KL(p̃'‖p̃)`.
(iv) Write `Φ = (F, G_1, …, G_k)` and `C = Cov_q(Φ)`, which is invertible because `1, F, G_1, …, G_k` are linearly
independent. As in the proof of [[P11 — The misaligned share at the start of a change|P11]], `p_s = tilt(q, s·H + O(s²))`, so `E_{p_s}[Φ] = E_q[Φ] + s·Cov_q(Φ, H) + O(s²)`,
and `E_{p_s}[F] > E_q[F]` for small `s > 0`, so the revealed intensity of `p_s` is positive, and finite as `p_s ∈ Δ°`.
The map `c ↦ E_{tilt(q, c·Φ)}[Φ]` has derivative `C` at `c = 0`; by the inverse function theorem and the uniqueness in
[[P15 — Misalignment splits into what the actor could avoid and what it could not|P15]](i), `p̃_s = tilt(q, c_s·Φ)` with `c_s = s·β + O(s²)`, where `β = C^{−1}·Cov_q(Φ, H)` are the coefficients of the
least-squares fit of `H` on `Φ` under `q`. By the second-order expansion in the proof of [[P11 — The misaligned share at the start of a change|P11]],
`KL(p_s‖p̃_s) = ½·s²·Var_q(H − β·Φ) + O(s³) = ½·s²·Var_q(H)·(1 − R²_{F,G}) + O(s³)` and
`KL(p_s‖q) = ½·s²·Var_q(H) + O(s³)`, which gives the first limit. By [[P11 — The misaligned share at the start of a change|P11]], `M(p_s)/KL(p_s‖q) → sin²θ = 1 − R²_F`, since
`cos θ` is the correlation of `H` with `F`; (ii) gives the second limit.

## Notes
Naming `G = log q` asks whether the actor sharpens the default: `tilt(q, a·F + b·log q)` is proportional to
`q^{1+b}·e^{a·F}`, a pursuit of `F` from the default at another temperature, sharper when `b > 0`. Other natural names
in machine learning are the length of an answer, a second reward model, or the log-probability under another model. The
increments of (iii) depend on the order in which objectives are named, as sequential sums of squares do in a regression;
the total named misalignment does not. Named misalignment is not evidence that the actor pursues the named objectives:
it says how much of the misalignment their averages account for. Whether the changes reveal one fixed objective in their
span is the question of [[P3 — A fixed objective is visible in the changes of behaviour|P3]]. Outside small changes, the shares of (iv) are not regression shares: on random instances
with a median departure of `2.6` nats, the `R²` of `log(p̂/q)` on `F` misses the pursuit share by a median `0.22` under
`p̂` and `0.13` under `q`, against `0.005` at departures near `0.005` nats (`probes/diagnostics/probe_named.py`). So a
test should estimate the parts in nats, as `KL` (whose cost [[P47 — The cost of reweighting|P47]] gives), and use a regression only where the departure
is small.

## Lineage
New. It is [[P15 — Misalignment splits into what the actor could avoid and what it could not|P15]](v) with a linear set chosen as a diagnosis, not as a limit of the actor; (iv) extends
[[P11 — The misaligned share at the start of a change|P11]]. v7.10: Def 21 and R7-10 (drift inside cells that the principal's resolution forgives), a different way to leave
part of a change unexplained.

## Checks
- [`checks/test_diagnostics.py::test_named_objectives_split_misalignment`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_diagnostics.py)
- [`checks/test_diagnostics.py::test_named_shares_at_the_start`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_diagnostics.py)

## Depends on
- [[D7 — Feasibility|D7]] — Feasibility
- [[P5 — Misalignment is attained, and zero exactly on the intended behaviours and their limits|P5]] — Misalignment is attained, and zero exactly on the intended behaviours and their limits
- [[P11 — The misaligned share at the start of a change|P11]] — The misaligned share at the start of a change
- [[P15 — Misalignment splits into what the actor could avoid and what it could not|P15]] — Misalignment splits into what the actor could avoid and what it could not

## Used by
- [[P48 — Misalignment when the target is uncertain|P48]] — Misalignment when the target is uncertain
- [[P49 — Outer and inner misalignment|P49]] — Outer and inner misalignment
