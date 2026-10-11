---
kind: proposition
id: P53
aliases: ["P53"]
source: "derived/misalignment.md"
---
# P53 — Misalignment is the departure beyond what the specification credits
> [!info] Generated from [derived/misalignment.md](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/derived/misalignment.md#p53--misalignment-is-the-departure-beyond-what-the-specification-credits). Edit the source, not this note.

## Statement
Let `T_1, …, T_d` be functions on `X`, write `θ·T = Σ_i θ_i·T_i` for `θ ∈ ℝ^d`, and let
`𝓔_T = {tilt(q, θ·T) : θ ∈ ℝ^d}`, the pursuits of `T` from `q` in every direction. Let `p̂ ∈ Δ°`, and let
`L = {p ∈ Δ : E_p[T_i] = E_{p̂}[T_i] for every i}`, the behaviours that reproduce the actor's averages of `T`.
(i) Exactly one `p* ∈ L` has the least departure from the default, `KL(p*‖q) = min_{p∈L} KL(p‖q)`. It has full support,
it lies in `𝓔_T`, and it is the only behaviour in both `L` and `𝓔_T`. For every `p ∈ L` and `r ∈ 𝓔_T`,
`KL(p‖r) = KL(p‖p*) + KL(p*‖r)`.
(ii) `𝓔_T` is closed in `Δ°`, so `(q, 𝓔_T)` is a specification ([[D3 — Specification, declaration and misalignment|D3]]). Its misalignment is attained at `p*` only, and
`M_T(p̂) = KL(p̂‖p*) = KL(p̂‖q) − min_{p∈L} KL(p‖q)`: the departure spent beyond the cheapest behaviour that reproduces
the averages of `T`.
(iii) **What the standard specification credits.** The standard specification of a non-constant `F` credits the average
of `F` when the actor does better than the default, and nothing otherwise. If `E_{p̂}[F] > E_q[F]`, the nearest intended
behaviour is the `p*` of `T = F`, and `M(p̂) = KL(p̂‖q) − min{KL(p‖q) : p ∈ Δ, E_p[F] = E_{p̂}[F]}`. If
`E_{p̂}[F] ≤ E_q[F]`, `M(p̂) = KL(p̂‖q)`.
(iv) **What the ordinal specification credits.** The ordinal specification of a non-constant `F` credits the masses of
the blocks `B_1, …, B_k` that its regression pools ([[P36 — Ordinal objectives|P36]]):
`M_ord(p̂) = KL(p̂‖q) − min{KL(p‖q) : p ∈ Δ, p(B_j) = p̂(B_j) for every j}`, and the minimum is attained only by the
behaviour that gives each block the actor's mass and spreads it inside the block as the default does.

## In plain terms
Each specification credits the actor with some statistics of its behaviour, and charges it only for
the departure from the default beyond the cheapest behaviour that reproduces them. A family of pursuits of named
statistics credits their averages. "Pursue `F`" credits the average of `F`, but only when the actor does better than
the default; otherwise all of its departure is charged. The order of `F` credits how often the actor lands in each group
of outcomes that the order pools.

## Proof
(i) `L` is closed, bounded and convex, and contains `p̂`. `KL(·‖q)` is continuous on `Δ`, since `q ∈ Δ°`, so
it attains its minimum on `L`, and it is strictly convex, so at one point `p*`. If `p*(x) = 0` for some `x`, let
`p_s = (1 − s)·p* + s·p̂`, in `L` for `s ∈ [0, 1]`. As `s → 0+`, the derivative of `KL(p_s‖q)` in `s` has, for each such
`x`, the term `p̂(x)·(log(s·p̂(x)/q(x)) + 1)`, which tends to `−∞`, while its other terms stay bounded; so
`KL(p_s‖q) < KL(p*‖q)` for small `s > 0`, against the minimality of `p*`. So `p* ∈ Δ°`. Let `V` be the span of
`1, T_1, …, T_d` in the functions on `X`. For every `v` with `Σ_x v(x)·g(x) = 0` for all `g ∈ V`, `p* + ε·v` lies in
`L` for small `|ε|`, so the derivative of the departure at `ε = 0`, `Σ_x v(x)·(log(p*(x)/q(x)) + 1)`, vanishes; as
`Σ_x v(x) = 0`, `log(p*/q)` is orthogonal to every `v` orthogonal to `V`, so it lies in `V`, and `p* = tilt(q, θ*·T)`
for some `θ*`. For `r = tilt(q, θ·T)`, `log(p*/r) = (θ* − θ)·T + c` for a number `c`, so its average under `p` depends
on `p` only through `p`'s averages of `T`, and is the same for every `p ∈ L`. Hence, for `p ∈ L`,
`KL(p‖r) − KL(p‖p*) = E_p[log(p*/r)] = E_{p*}[log(p*/r)] = KL(p*‖r)`. If `s ∈ L ∩ 𝓔_T`, the identity with `p = r = s`
gives `0 = KL(s‖p*) + KL(p*‖s)`, so `s = p*` (Gibbs' inequality).
(ii) If `r_n ∈ 𝓔_T` tends to `r ∈ Δ°`, then `log(r_n/q)`, which lies in `V`, tends to `log(r/q)`. A linear subspace of
the finite-dimensional space of functions on `X` is closed, so `log(r/q) = θ·T + c` for some `θ` and `c`, and
normalization gives `r = tilt(q, θ·T) ∈ 𝓔_T`. By (i) with `p = p̂`, `KL(p̂‖r) = KL(p̂‖p*) + KL(p*‖r) ≥ KL(p̂‖p*)` for
every `r ∈ 𝓔_T`, with equality only at `r = p*` (Gibbs' inequality). With `r = q`, which is in `𝓔_T` at `θ = 0`,
`KL(p̂‖q) = KL(p̂‖p*) + KL(p*‖q)`, and `KL(p*‖q)` is the minimum over `L`.
(iii) If `E_{p̂}[F] ≤ E_q[F]`, this is [[P6 — The departure from the default splits into pursuit and misalignment|P6]](i). Otherwise, let `T = F`. The average of `F` under `tilt(q, θ·F)` has the
derivative `Var(F) > 0` in `θ`, the variance under that tilt, which has full support, of the non-constant `F`; so it is
strictly increasing in `θ`, and equals `E_q[F]` at `θ = 0`. As `p*` has the average `E_{p̂}[F] > E_q[F]`, its `θ*` is
positive, and `p*` lies on the pursuit ray `R_F ⊆ 𝓔_F`. The infimum over `R_F` is then at least the one over `𝓔_F`,
which `p*` attains, so `M(p̂) = KL(p̂‖p*)` with `p*` the nearest intended behaviour, and (ii) gives the formula.
(iv) For `p ∈ Δ` with `p(B_j) = p̂(B_j)` for every `j`, the chain rule [[P4 — What KL measures|P4]](iii) gives
`KL(p‖q) = Σ_j p̂(B_j)·log(p̂(B_j)/q(B_j)) + Σ_j p̂(B_j)·KL(p(·|B_j)‖q(·|B_j))`, least exactly when
`p(·|B_j) = q(·|B_j)` on every block. So `KL(p̂‖q)` minus the minimum is `Σ_j p̂(B_j)·KL(p̂(·|B_j)‖q(·|B_j))`, which is
`M_ord(p̂)` by [[P36 — Ordinal objectives|P36]](ii).

## Notes
(i) is Csiszár's I-projection of `q` onto a linear family, with its Pythagorean identity; [[P6 — The departure from the default splits into pursuit and misalignment|P6]](ii) is its
case `T = F`, extended there to behaviours that rule outcomes out, and [[P15 — Misalignment splits into what the actor could avoid and what it could not|P15]](iii) and [[P44 — What named objectives explain|P44]] use it for feasibility and
for named objectives. What it adds is one reading of three specifications: misalignment never charges what the
specification credits, and charges all the rest of the departure. The credits differ. A family of named statistics
credits their averages whatever their direction, the standard specification only an average of `F` above the default's,
and the ordinal one the masses of blocks that depend on the actor's behaviour. The cheapest behaviour of (iv) is the
`p°` of [[P36 — Ordinal objectives|P36]], by the proof of [[P36 — Ordinal objectives|P36]](iii), where `r°` is the default's average of `p̂/q` on each block. So the paired
report of `STANDARD.md` reads as two credits for one departure: the standard one credits less, and the difference
between the two misalignments is departure that the order of `F` credits and its values do not. With several named
statistics, `M_T` is the misalignment against "pursue some combination of `T`", the specification of [[P44 — What named objectives explain|P44]]'s named
pursuit when `p°` is replaced by `q`.

## Lineage
New in v13 (`NOTES.md` §17): the excess-departure reading of [[P6 — The departure from the default splits into pursuit and misalignment|P6]](ii) (`NOTES.md` §16), extended to the
ordinal specification and to families of named statistics, so that one identity reads the specifications the core
defines.

## Checks
- [`checks/test_misalignment.py::test_credited_statistics`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_misalignment.py)

## Depends on
- [[D3 — Specification, declaration and misalignment|D3]] — Specification, declaration and misalignment
- [[P4 — What KL measures|P4]] — What KL measures
- [[P6 — The departure from the default splits into pursuit and misalignment|P6]] — The departure from the default splits into pursuit and misalignment
- [[P36 — Ordinal objectives|P36]] — Ordinal objectives

## Used by
- no later item
