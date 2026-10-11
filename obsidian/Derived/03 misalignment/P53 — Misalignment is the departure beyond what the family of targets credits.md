---
kind: proposition
id: P53
aliases: ["P53"]
source: "derived/misalignment.md"
---
# P53 — Misalignment is the departure beyond what the family of targets credits
> [!info] Generated from [derived/misalignment.md](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/derived/misalignment.md#p53--misalignment-is-the-departure-beyond-what-the-family-of-targets-credits). Edit the source, not this note.

## Statement
Let `𝓚` be a family of targets and `(q, 𝓘_𝓚)` its specification ([[D3 — Specification, declaration and misalignment|D3]]), and let `p̂ ∈ Δ°`.
(i) `𝓘_𝓚` is closed in `Δ°`, so `(q, 𝓘_𝓚)` is a specification. Exactly one intended behaviour `p°` is nearest to `p̂`;
it is `tilt(q, G°)` for some `G° ∈ 𝓚`.
(ii) `E_{p°}[G] ≥ E_{p̂}[G]` for every `G ∈ 𝓚`, with equality at `G = G°`: the nearest intended behaviour does at least
as well as the actor on every target of the family, and exactly as well on its own.
(iii) For every `p ∈ 𝓘_𝓚`, `KL(p̂‖p) ≥ M(p̂) + KL(p°‖p)`, with equality at `p = q`: `KL(p̂‖q) = KL(p°‖q) + M(p̂)`.
(iv) Let `C = {p ∈ Δ : E_p[G] ≥ E_{p̂}[G] for every G ∈ 𝓚}`, the behaviours that do at least as well as the actor on
every target of the family. For every `p ∈ C`, `KL(p‖q) ≥ KL(p°‖q) + KL(p‖p°)`, so `p°` is the one behaviour of least
departure in `C`, and `M(p̂) = KL(p̂‖q) − min_{p∈C} KL(p‖q)`: the departure spent beyond the cheapest behaviour that
does at least as well as the actor on every target.
(v) **What each family credits.** For the span of functions `T_1, …, T_d` and the constants, `C` is the set of
behaviours with the actor's averages of every `T_i`. For the standard specification of a non-constant `F`, `C` is the
set of behaviours with `E_p[F] ≥ E_{p̂}[F]`: if `E_{p̂}[F] ≤ E_q[F]`, then `q ∈ C`, nothing is credited and
`M(p̂) = KL(p̂‖q)`; otherwise the minimum is reached where `E_p[F] = E_{p̂}[F]`. For the ordinal specification, `C` is
the set of behaviours that **dominate** `p̂` in the order of `F`, `p(F ≥ v) ≥ p̂(F ≥ v)` for every `v`; `p°` is the
nearest behaviour of [[P36 — Ordinal objectives|P36]], and the minimum is also the least departure among the behaviours that give each block of
[[P36 — Ordinal objectives|P36]] the actor's mass.

## In plain terms
A principal may accept a whole family of targets: one objective, only its order, or any mix of
several candidates. Every such family credits the actor with what it achieves on the family's targets, and misalignment
charges only the departure from the default beyond the cheapest behaviour that achieves at least as much on every one of
them. "Pursue `F`" credits the average of `F`, and only when the actor beats the default; the order of `F` credits doing
at least as well at every threshold of `F`; a span of candidates credits their averages exactly. The nearest acceptable
behaviour is itself the cheapest such behaviour.

## Proof
Write `f(G) = log E_q[e^G] − E_{p̂}[G]`, so that `KL(p̂‖tilt(q, G)) = KL(p̂‖q) + f(G)`. `f` is convex, its
derivative at `G` along `H` is `E_{tilt(q,G)}[H] − E_{p̂}[H]`, and it is strictly convex along every non-constant `H`,
whose variance under `tilt(q, G)` is positive. `f(G + c) = f(G)` for every constant `c`, and `𝓚` contains the constants.
(i) If `tilt(q, G_m) → p ∈ Δ°` with `G_m ∈ 𝓚`, then `G_m − log E_q[e^{G_m}] = log(tilt(q, G_m)/q)`, which is in `𝓚`,
converges to `log(p/q)`, which is then in `𝓚` since `𝓚` is closed, so `p = tilt(q, log(p/q)) ∈ 𝓘_𝓚`. Minimize `f` over
`𝓚_0 = {G ∈ 𝓚 : E_q[G] = 0}`, which loses nothing, as `f` ignores constants. With `a = min_x p̂(x)` and
`b = min_x q(x)`, `f(G) ≥ max G + log b − E_{p̂}[G] ≥ a·(max G − min G) + log b`, and on `𝓚_0` the range `max G − min G`
bounds `|G|`, so `f` attains its minimum on the closed set `𝓚_0`. Two minimizers that differ by a non-constant function
would give, at their midpoint, which is in `𝓚`, a smaller value, so the minimizer `G°` is unique up to a constant, and
`p° = tilt(q, G°)` is the unique nearest intended behaviour. (ii) For `G ∈ 𝓚`, `G° + s·(G − G°) ∈ 𝓚` for `s ∈ [0, 1]`,
so the derivative of `f` at `G°` along `G − G°` is not negative: `E_{p°}[G − G°] ≥ E_{p̂}[G − G°]`. With `G = 0` and
`G = 2·G°`, both in the cone, `E_{p°}[G°] = E_{p̂}[G°]`, and then `E_{p°}[G] ≥ E_{p̂}[G]`. (iii) For `p = tilt(q, G)`,
`log(p°/p) = G° − G` plus a constant, and since `p̂` and `p°` both add up to one,
`KL(p̂‖p) − KL(p̂‖p°) − KL(p°‖p) = (E_{p̂} − E_{p°})[G° − G] = E_{p°}[G] − E_{p̂}[G] ≥ 0` by (ii); at `p = q`, `G = 0`
and it is `0`. (iv) For `p ∈ C`, `KL(p‖q) − KL(p‖p°) = E_p[G°] − log E_q[e^{G°}]`, which is at least
`E_{p̂}[G°] − log E_q[e^{G°}]`, and that is `E_{p°}[G°] − log E_q[e^{G°}] = KL(p°‖q)`, using `p ∈ C` and (ii). By (ii),
`p° ∈ C`, and by Gibbs' inequality `p°` is the only minimizer; (iii) at `p = q` gives the formula. (v) For the span,
`±T_i ∈ 𝓚`, so `C` asks for equal averages. For the standard specification, `𝓚 = {t·F + c : t ≥ 0}`, so `C` asks
`E_p[F] ≥ E_{p̂}[F]`; if `q ∈ C`, the least departure in `C` is `0`; otherwise `p° ≠ q` has, by (ii),
`E_{p°}[F] = E_{p̂}[F]`, since `G° = t°·F + c` with `t° > 0`. For the ordinal specification, a non-decreasing function
of `F`, with values `g_1 ≤ … ≤ g_m` on the levels `v_1 < … < v_m`, is `g_1 + Σ_{j≥2} (g_j − g_{j−1})·1{F ≥ v_j}`, a
non-negative combination of the indicators `1{F ≥ v_j}` plus a constant, so `C` asks `p(F ≥ v_j) ≥ p̂(F ≥ v_j)` for
every `j`; `p°` is [[P36 — Ordinal objectives|P36]]'s, by uniqueness in
(i) and [[P36 — Ordinal objectives|P36]](ii). On each block `B` of [[P36 — Ordinal objectives|P36]], a behaviour with the actor's mass `p̂(B)` departs by
`Σ_B p̂(B)·log(p̂(B)/q(B)) + Σ_B p̂(B)·KL(p(·|B)‖q(·|B))` (the chain rule [[P4 — What KL measures|P4]](iii)), least when each `p(·|B) = q(·|B)`;
the excess of `KL(p̂‖q)` over that least value is `Σ_B p̂(B)·KL(p̂(·|B)‖q(·|B)) = M(p̂)` by [[P36 — Ordinal objectives|P36]](ii).

## Notes
(iv) is Csiszár's I-projection of `q` onto the convex set `C`, with its Pythagorean inequality
([[References|@polyanskiy2025]], Theorem 15.10), and (iii) is the matching inequality for the reverse projection onto `𝓘_𝓚`; the cone
is what joins them. [[P6 — The departure from the default splits into pursuit and misalignment|P6]] is the case of one objective; [[P48 — Misalignment when the target is uncertain|P48]] is the span, where the least misalignment over the
principals whose target lies in it is the misalignment against the whole family, since the union of their rays is `𝓘_𝓚`;
[[P44 — What named objectives explain|P44]]'s named pursuit is the span of `F` and the named objectives, taken from `p°` rather than from `q`. That `C` is
stochastic dominance for the ordinal specification says what the order credits: how often the actor reaches every
threshold of `F`. Misalignment is the departure beyond the cheapest behaviour that reaches each threshold at least as
often as the actor does. So the paired report of `STANDARD.md` reads as two credits for one departure, and their
difference is departure that the order of `F` credits and its values do not. A family that is not convex, such as two
candidate targets that may not be mixed, is the union of the specifications of its convex parts, and its misalignment is
the least of theirs. Read with Sanov's theorem ([[P55 — What a record of counts certifies, at every size|P55]], Notes), the credited departure is the rate at which a default
actor would do at least as well as the actor on every target, and misalignment the rate of the actor's shares given
that. This needs `C` to have an interior, as it has under the standard and the ordinal specification for an actor of
full support. For a span, `C` is a set of equalities, which empirical behaviours may never meet exactly; the credited
departure is then the limit, as the margin shrinks, of the rate of doing as well within a margin.

## Lineage
New in v13 (`NOTES.md` §17, §18): the excess-departure reading of [[P6 — The departure from the default splits into pursuit and misalignment|P6]](ii) (`NOTES.md` §16), extended first
to the ordinal specification and to families of named statistics, then, at the PI's question whether a family of targets
is more general than one target (Q53), to every family; the most charitable principal of [[P48 — Misalignment when the target is uncertain|P48]] (H32, §5.4) and the
declared family of H35 are its cases.

## Checks
- [`checks/test_misalignment.py::test_credited_statistics`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_misalignment.py)

## Depends on
- [[D3 — Specification, declaration and misalignment|D3]] — Specification, declaration and misalignment
- [[P4 — What KL measures|P4]] — What KL measures
- [[P36 — Ordinal objectives|P36]] — Ordinal objectives

## Used by
- no later item
