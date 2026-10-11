# General results — transfer

What each result of the finite core is expected to become on outcome spaces that are not finite (`CORE-GENERAL.md`), and
the new results that only such spaces have. The status is that of `README.md` in this folder; "T" and "B" numbers are
the probes of `probes/general/`.

| Finite item, or new | Expected on general spaces | Status and evidence |
|---|---|---|
| [[P1 — Every behaviour is a tilt of any other\|P1]], [[P2 — Every change of behaviour follows a replicator equation\|P2]](iii), [[P4 — What KL measures\|P4]] | carry, for tilts that exist; the chain rule with conditional behaviours | expected |
| [[P14 — The cost of departing from the default is forced\|P14]] | carries, by finite determination (GA1) and the Gelfand–Yaglom–Perez theorem ([[References\|@polyanskiy2025]], Theorem 4.5) | expected |
| the transfer lemma (new, restated in draft 4) | misalignment, the supremum over decidable finite descriptions (GD3), is the least divergence over the closure of the intended behaviours whenever that closure is compact for the convergence of every event's probability, with or without a nearness: TR3 below. Compact closures include every family continuous in a compact parameter, and the pursuit ray when its intensities form a closed bounded interval or when the objective's largest value has positive probability under the default (TR4) | proved here (TR1–TR4), not yet checked in CI; probed: `probes/general/t8_transfer.py`, two instances, where the misalignment of finer descriptions rises to the least divergence over the closure (`0.005616` on a circle; `0.105103` on a ray with an atom at its limit, with and without a nearness) |
| [[P5 — Misalignment is attained, and zero exactly on the intended behaviours and their limits\|P5]] | (i) attainment holds on the closure of the intended behaviours when it is compact (TR3); (ii) as in GD3; (iv) gains a fourth case: the ray stops at `t_max` with its average of `F` capped, and a behaviour with a larger average is nearest to the end of the ray, so averages are no longer matched; the third case, the limit `q(·|A)` of the ray, carries when `A` has positive probability under the default (TR4) | proved for (i) and the third case of (iv) (TR3, TR4); probed for the fourth: default with density proportional to `e^{−x}/(1 + x)³` on `x ≥ 0`, and `F(x) = x`: the ray's average is `0.354`, `0.474`, `0.736`, `0.937`, `0.989` at `t = 0`, `0.5`, `0.9`, `0.99`, `0.999`, and stops at `1` at `t = 1`; for an exponential behaviour of mean `2` the divergence to the ray falls all the way to `t = 1` |
| [[P9 — What is at stake\|P9]] | past the end of the ray, the frontier is a straight line of slope `1/t_max`, approached and never attained; with a power-law upper tail, `t_max = 0` and every positive KL budget buys unbounded gain, while a χ² budget `B` buys exactly `√(B·Var)` | probed (GD5's numbers); tested (B4a, B4b): gains `0.24`, `0.85`, `4.9`, `34`, `2127` as the extra probability moves to `10`, …, `10⁶`, under a Pareto default with index `3`; `0.273861` exactly under χ² |
| [[P11 — The misaligned share at the start of a change\|P11]], [[P13 — What the start of a change gains\|P13]]: the alignment plane | with a Gaussian default and linear target and proxy, along the pursuit of the proxy the target gains `√2·sd·cos θ` per square root of departure, and the misalignment is the departure times `sin²θ` (the whole departure when `cos θ < 0`), at every intensity: the departure splits like a right triangle. Under a χ² budget `B` the target gains `√B·ρ·sd` for every default, `ρ` the correlation under the default, the correlated proxy of Laidlaw et al. [[References\|@laidlaw2025]]. Under KL beyond Gaussians the law is local only | tested (B5, B4c): exact to `4·10⁻¹⁵` and `10⁻⁹`. B5's registered exponential case failed as posed: at intensity `2` the pursuit does not exist, and below `1` the law is exact for a product of identical exponentials. An exponential × normal default departs from it: `0.48`, `0.43`, `0.29` against `0.5` (exploratory) |
| [[P53 — Misalignment is the departure beyond what the family of targets credits\|P53]] | carries where the tilts of the family exist: the cheapest behaviour that does at least as well on every target is Csiszár's I-projection onto a convex set, which exists when that set is closed in variation and holds a behaviour of finite divergence [[References\|@csiszar1975]], Theorem 2.1; the cone of targets must then be a cone of functions with an exponential moment under the default | expected |
| [[P15 — Misalignment splits into what the actor could avoid and what it could not\|P15]] | carries for linear limits [[References\|@csiszar1975]]. The unavoidable part is the rate at which the nearest intended behaviour produces, by chance, a record that meets the actor's limits; conditioned on that, its record looks like the best feasible behaviour [[References\|@csiszar1984]]. This reading holds on finite outcomes too, and belongs in the finite core first | probed: exact multinomial sums on three outcomes, rates `0.175`, `0.139`, `0.128` at `n = 50`, `200`, `800`, toward `0.123`; the conditional behaviour of one draw tends to the best feasible behaviour |
| [[P16 — An actor cannot behave more differently than it can tell conditions apart\|P16]], [[P17 — What an unobserved condition can hide\|P17]] | [[P16 — An actor cannot behave more differently than it can tell conditions apart\|P16]] carries, by data processing (TR7); [[P17 — What an unobserved condition can hide\|P17]] is expected to carry with it; regularity across a continuum of conditions comes from the view (GD8) | proved here for [[P16 — An actor cannot behave more differently than it can tell conditions apart\|P16]] (TR7), not yet checked in CI; expected for [[P17 — What an unobserved condition can hide\|P17]] |
| [[P19 — A monotone regression rules out overoptimization\|P19]] | carries: the association inequality holds under any behaviour | expected |
| [[P20 — Where overoptimization starts, and how it ends\|P20]] | the end of pursuit changes when the evaluator's largest value has probability zero, or is never reached | expected |
| [[P21 — The expected evidence is misalignment\|P21]], [[P22 — No test detects misalignment faster than misalignment\|P22]] | carry: both concern the log-ratio, a real number per decision | expected |
| [[P54 — Dependence and drift only add evidence\|P54]] | carries, with the divergence to the nearest intended behaviour in place of misalignment, the two being equal when the intended behaviours are closed with a compact closure (TR8) | proved here (TR8), not yet checked in CI |
| [[P55 — What a record of counts certifies, at every size\|P55]] | holds exactly on the counts of the cells of every finite description, for independent decisions, where it certifies the misalignment at that description; that is a lower bound of misalignment when the description is decidable for the actor, which it always is with no nearness, and whatever the nearness when the closure of the intended behaviours is compact (TR3). Under that compactness, a test on refining descriptions makes "misaligned" verifiable in chance (TR5). Without it, under a nearness, a description fixed in advance can accuse an actor whose misalignment is `0`: the on-target controller, with a cell edge at its target. "Aligned within `ε`" is not verifiable from records alone (GD11), with or without compactness; under a nearness with a countable basis of decidable events, Genin and Kelly's theorem says why: its set is not open in the weak topology [[References\|@genin2017]] | proved here for the compact case (TR5), not yet checked in CI; expected otherwise |
| [[P23 — The estimated misalignment of an actor that pursues the objective\|P23]] | holds only at a record's resolution (GD11) | expected |
| [[P36 — Ordinal objectives\|P36]] | for an evaluator without atoms, once each score is replaced by its rank under the default, the ordinal specification is the set of non-decreasing ratios on `[0, 1]`, the same for every default, and its nearest member is the isotonic regression [[References\|@robertson1988]] | expected |
| [[P37 — A strong incentive masks the actor, and can fake alignment\|P37]](i) | masking decays like `1/φ²` in the pass-through `φ`, not exponentially, when the incentive's best value is approached without a gap | tested (T7): `φ²·KL` is `3.04`, `3.60`, `3.92`, `4.02`, `4.06` at `φ = 10`, `30`, `100`, `300`, `1000`, against a predicted limit of `4.08`, the error shrinking like `1/φ` |
| best-of-`n` | divergence exactly `log n − (n − 1)/n` for an evaluator without atoms [[References\|@beirami2024]], and less with ties; the target's average is `∫₀¹ m(G⁻¹(u))·n·u^{n−1} du`, with `G` the evaluator's distribution function under the default: E8 for best-of-`n` | probed: exact to six digits at `n = 2`, `4`, `16`; with five tied levels, `0.180` against `0.193` at `n = 2` |
| v7.10's Prop 11 | importable: an objective with a heavy upper tail is not pursuable (GD2) | Kwa et al. prove the phenomenon for reward errors, and measured the tails of reward models as light [[References\|@kwa2024]]; see [[P9 — What is at stake\|P9]]'s row for the tests |
| a record shows "at least" (new) | as in GD11: samples alone never certify that misalignment is small, a Bahadur–Savage-type impossibility | expected, with the construction in GD11 |
| tilts and atoms (new) | a tilt cannot create an atom (GD6) | immediate from GD1 |
| the on-target controller (new) | `0` under the usual nearness and `+∞` with none; on a grid of width `w`, `0` or `log 2` depending on where the grid's edges fall, at every `w`; a controller `0.001` off target scores `0` on grids coarser than `0.001`, then grows like `log(1/w)`: `3.72` at `w = 10⁻⁴`, `8.33` at `10⁻⁶` | probed: standard normal default, `F(x) = −x²` |
| the dimension law (new) | against intended behaviours with densities bounded above and below, misalignment at a record of width `w` grows like `(D − d)·log(1/w)`, with `d` the information dimension [[References\|@renyi1959]] (GD3): TR6 below | proved here (TR6), not yet checked in CI; tested (T1): slopes `0.0998`, `1.0000`, `0.9997` and `0.3691` for a pile of a tenth, rounding, a line in the square and the Cantor measure, against `0.10`, `1`, `1` and `log 2/log 3 = 0.369` |
| a robustness degree (new) | an actor that aims deterministically at a margin `r` inside a threshold, blurred by noise of size `σ`, judged by "pass with probability at least `1 − α`" at the pass-or-fail resolution: its misalignment depends on `r/σ` alone, does not increase with `r`, and is `0` from `r = σ·Φ⁻¹(1 − α)`. Robustness in a formal specification, counted in units of the actor's noise, orders behaviours as misalignment does | tested (B6) |

## Proved here

Five statements that the rows above lean on, proved from GM1, the Gelfand–Yaglom–Perez theorem as stated in
[[References|@polyanskiy2025]], Theorem 4.5 (the divergence is the supremum, over all finite partitions into events, of the
divergence between cell probabilities), and results of `derived/`. No check runs them in CI yet; the probe
`probes/general/t8_transfer.py` computes TR3 on two instances. Throughout, `𝒫 = (C_1, …, C_k)` is a finite description,
`p_𝒫 = (p(C_1), …, p(C_k))`, and **τ** is the topology on `Δ` in which a net of behaviours converges when the
probability of every event converges: Csiszár's τ-topology ([[References|@csiszar1984]], (2.14)), the "convergence of every event's
probability" of GA1. It is Hausdorff, since two behaviours differ on some event.

Two facts on finitely many cells are used. (a) For fixed `a`, `b ↦ KL(a‖b)` is continuous from the simplex to `[0, ∞]`:
where `b_i > 0` whenever `a_i > 0` it is a finite sum of continuous terms, and where some `b_i = 0 < a_i` it is `∞` and
the term `a_i·log(a_i/b_i)` tends to `∞` nearby while every other term stays above `a_j − b_j ≥ −1`. (b) `(a, b) ↦
KL(a‖b)` is lower semicontinuous: each term `a·log(a/b)` is continuous where `b > 0`, tends to `∞` where `b → 0 < a`,
and is at least `a − b` everywhere, which handles `a = b = 0`. So `p ↦ KL(a‖p_𝒫)` is τ-continuous for every `𝒫`.

### TR1 — Every tilt is a limit of tilts on finite descriptions
**Statement.** Let `r ∈ Δ` and `F` measurable with `E_r[e^F] < ∞`. There are measurable `F_n`, each taking finitely
many values, with `tilt(r, F_n) → tilt(r, F)` in total variation, and so in τ.

**In plain terms.** Reweighting by any objective is the limit of reweighting by objectives that only sort outcomes into
finitely many grades.

**Proof.** Let `F_n = max(−n, min(n, 2^{−n}·⌊2^n·F⌋))`. It takes finitely many values, `F_n → F` everywhere, and
`F_n ≤ max(F, 0)`, so `e^{F_n} ≤ 1 + e^F`, which is integrable under `r`. By dominated convergence, `e^{F_n} → e^F` in
`L¹(r)` and `E_r[e^{F_n}] → E_r[e^F] > 0`, so the ratios `e^{F_n}/E_r[e^{F_n}]` converge to `e^F/E_r[e^F]` in `L¹(r)`.
The total variation between two behaviours with ratios to `r` is half the `L¹(r)` distance of the ratios.

### TR2 — The descriptions a record can decide suffice
**Statement.** Let `p̂ ∈ Δ`, and let `𝔇` be the finite descriptions decidable for `p̂` (GD3), or the finite partitions
into events of an algebra `𝒜` of events that generates `𝔅`. Any two members of `𝔇` have a common refinement in `𝔇`, and
for every `p ∈ Δ`, `KL(p̂‖p) = sup_{𝒫 ∈ 𝔇} KL(p̂_𝒫‖p_𝒫)`.

**In plain terms.** Asking only the questions a record can answer, as finely as one likes, recovers the whole
divergence between two behaviours.

**Proof.** *The events decidable for `p̂` form an algebra that generates `𝔅`.* With no nearness every event is
decidable. Under a nearness `𝒩`, the boundary of a complement is the boundary of the set, and the boundary of a union or
an intersection of two sets lies in the union of their boundaries, so decidable events form an algebra. Let `d` be a
complete separable metric generating `𝒩` and `D` a countable dense set. For `x ∈ D` the spheres `{y : d(x, y) = ρ}`,
`ρ > 0`, are disjoint, so at most countably many have positive probability under `p̂`; for every other `ρ`, the open
ball of radius `ρ` about `x` is decidable, since its boundary lies in its sphere. Fix a countable dense set of such
radii for each `x ∈ D`. The balls so obtained are countably many and form a base of `𝒩`: for `y` in an open `U`, take
`ε` with the ball of radius `2ε` about `y` inside `U`, then `x ∈ D` within `ε/2` of `y`, and a radius in `(ε/2, ε)`.
Every open set is a countable union of them, so they generate `𝔅`. In both cases, the cells of two members of `𝔇`
intersect into a common refinement in `𝔇`.

*Approximation.* Let `μ = p̂ + p` and `𝒜` an algebra generating `𝔅`. The events `E` such that for every `δ > 0` some
`A ∈ 𝒜` has `μ(E △ A) < δ` contain `𝒜`, are closed under complement (`Eᶜ △ Aᶜ = E △ A`), and under countable union: for
`E = ∪_j E_j`, take `N` with `μ(E ∖ ∪_{j≤N} E_j) < δ/2` and `A_j ∈ 𝒜` with `μ(E_j △ A_j) < δ/2^{j+1}`; then
`A = ∪_{j≤N} A_j` has `μ(E △ A) < δ`. So they form a σ-algebra containing `𝒜`, which is all of `𝔅`.

*The supremum.* Every `𝒫` gives at most `KL(p̂‖p)` (data processing, [[References|@polyanskiy2025]], Theorem 4.5). Conversely, let
`(E_1, …, E_k)` be any finite partition into events, and `A_i ∈ 𝒜` with `μ(E_i △ A_i) < δ`. The cells
`B_i = A_i ∖ (A_1 ∪ … ∪ A_{i−1})` for `i < k`, and `B_k` the rest, are in `𝒜` and partition `X`; since the `E_j` are
disjoint, `E_i △ B_i` lies in the union of the `E_j △ A_j`, `j ≤ i`, so `μ(E_i △ B_i) < k·δ`. The cell probabilities of
`p̂` and of `p` on the `B_i` are then within `k·δ` of those on the `E_i`, and by (b) the divergence between them is, for
`δ` small, at least that on the `E_i` less any given margin, or above any given number when that is `∞`. By
[[References|@polyanskiy2025]], Theorem 4.5, the supremum over all finite partitions is `KL(p̂‖p)`.

### TR3 — Misalignment under compactness
**Statement.** Let `(q, 𝓘, 𝒩)` be a specification, and `𝒦` the closure of `𝓘` in τ. If `𝒦` is τ-compact, then for every
`p̂ ∈ Δ`, `M(p̂) = min_{p ∈ 𝒦} KL(p̂‖p)`, the minimum being attained, whatever the nearness; and the same value is the
supremum of `inf_{p ∈ 𝓘} KL(p̂_𝒫‖p_𝒫)` over the finite partitions of any algebra of events that generates `𝔅`.

**In plain terms.** When the acceptable behaviours, with their limits, form a compact set, what records can show is
exactly the divergence to the nearest acceptable behaviour or limit of acceptable behaviours. Then which outcomes the
principal calls near changes nothing, and any family of questions fine enough to tell all events apart gives the same
answer.

**Proof.** Let `𝔇` be the decidable descriptions, or the partitions of a generating algebra, and
`f_𝒫(p) = KL(p̂_𝒫‖p_𝒫)`. Each `f_𝒫` is τ-continuous, so its infimum over `𝓘` is its infimum over `𝒦`. By TR2,
`g(p) = KL(p̂‖p)` is the supremum of the `f_𝒫`, so it is τ-lower semicontinuous and attains a minimum `m` on the compact
`𝒦`. For every `𝒫`, `inf_𝒦 f_𝒫 ≤ inf_𝒦 g = m`, so `M(p̂) ≤ m`. Conversely, let `c < m`. Each `p ∈ 𝒦` has `g(p) > c`, so
some `𝒫_p ∈ 𝔇` has `f_{𝒫_p}(p) > c`, and `{f_{𝒫_p} > c}` is a τ-open set containing `p`. Finitely many of these sets
cover `𝒦`; let `𝒫*` in `𝔇` refine their descriptions (TR2). Merging cells never increases a divergence ([[P4 — What KL measures|P4]](iv)), so
`f_{𝒫*} > c` on all of `𝒦`, and its minimum there, attained since `f_{𝒫*}` is continuous and `𝒦` compact, exceeds `c`.
So `M(p̂) ≥ inf_𝓘 f_{𝒫*} > c` for every `c < m`.

### TR4 — Compact families, and the pursuit ray
**Statement.** (i) Let `Θ` be a compact metric space and `𝓘 = {p_θ : θ ∈ Θ}` with each `p_θ` absolutely continuous with
respect to `q`, of ratio `r_θ`, such that `θ ↦ r_θ(x)` is continuous for `q`-almost every `x`. Then `𝓘` is τ-compact,
and `M(p̂) = min_θ KL(p̂‖p_θ)`. (ii) Let `F` be an objective. If `T_F = [0, t_max]` with `t_max < ∞`, the pursuit ray is
τ-compact. If `F ≤ m` with probability one under `q` for a number `m`, and `A = {F = m}` has `q(A) > 0`, the closure of
the ray is the ray with `q(·|A)` added, and it is τ-compact. In both cases `M(p̂)` is the least divergence from `p̂` to
that compact set.

**In plain terms.** A family of acceptable behaviours that varies continuously over a bounded, closed range of
parameters is compact, and misalignment is the divergence to its nearest member. Pursuit of an objective qualifies when
it stops at a finite intensity that it still reaches, or when its best outcomes have positive probability by default:
then the limit of ever stronger pursuit, the default restricted to the best outcomes, is the one behaviour added, as in
the third case of [[P5 — Misalignment is attained, and zero exactly on the intended behaviours and their limits|P5]](iv).

**Proof.** (i) If `θ_n → θ`, then `r_{θ_n} → r_θ` almost everywhere, and since all integrate to `1` under `q`,
`E_q|r_{θ_n} − r_θ| = 2·E_q[(r_θ − r_{θ_n})⁺] → 0` by dominated convergence (`0 ≤ (r_θ − r_{θ_n})⁺ ≤ r_θ`), Scheffé's
argument. So `θ ↦ p_θ` is continuous into τ, and `𝓘`, the image of a compact set, is compact, hence τ-closed; TR3
applies with `𝒦 = 𝓘`. (ii) In the first case, `t ↦ e^{t·F}` is continuous and `e^{t·F} ≤ 1 + e^{t_max·F}`, integrable,
so `t ↦ E_q[e^{t·F}]` is continuous on `[0, t_max]` and (i) applies with `Θ = [0, t_max]`. In the second, on `[0, ∞]`
let the ratio be `e^{t·(F − m)}/E_q[e^{t·(F − m)}]` for finite `t`, and `1_A/q(A)` at `∞`; as `t → ∞`,
`e^{t·(F − m)} → 1_A` pointwise, bounded by `1`, so the normalizer tends to `q(A) > 0`, and the ratios converge almost
everywhere. (i) applies with `Θ = [0, ∞]`, a compact metric space. The image is closed and contains the ray, and its one
added point is a τ-limit of the ray, so it is the ray's closure.

### TR5 — "Misaligned" is verifiable in chance, under compactness
**Statement.** Let `𝒦`, the τ-closure of `𝓘`, be τ-compact. There are finite descriptions `𝒫_1, 𝒫_2, …`, each refining
the one before, and a sequence `j(n) → ∞`, such that the test that applies [[P55 — What a record of counts certifies, at every size|P55]](ii) at level `α` to the counts of the
cells of `𝒫_{j(n)}` in a sample of size `n` declares misaligned a sample from a behaviour in `𝒦` with probability at
most `α`, at every `n`, and a sample from any `p̂` with `M(p̂) > 0` with probability tending to `1`.

**In plain terms.** When the acceptable behaviours, with their limits, form a compact set, one test, fixed before any
data and asking finer questions as the record grows, catches every misaligned actor that decides independently, and
accuses an acceptable one no more often than the rate chosen, at every size.

**Proof.** `𝔅` is generated by a countable base of the Polish topology of GB1, so by a countable algebra `𝒜_0`, whose
finite partitions are countably many; let `𝒫_j` be the common refinement of the first `j` of them. Every partition of
`𝒜_0` is refined by some `𝒫_j`, and refining never lowers a divergence ([[P4 — What KL measures|P4]](iv)), so by TR3 with `𝒜_0`,
`M(p̂) = lim_j M_{𝒫_j}(p̂)`. *Level.* For `p ∈ 𝒦`, `p_{𝒫}` is a limit of the cell probabilities of intended behaviours,
since `p ↦ p_𝒫` is τ-continuous, and the proof of [[P55 — What a record of counts certifies, at every size|P55]](ii) uses only that, on the cells: with the method of types of
[[P55 — What a record of counts certifies, at every size|P55]](i), it bounds the chance of accusing a sample from `p` by `α`. *Power.* If `M(p̂) > 0`, some `j_0` has
`M_{𝒫_{j_0}}(p̂) > 0`. For `j ≥ j_0` and every empirical behaviour `s`, `M_{𝒫_j}(s) ≥ M_{𝒫_{j_0}}(s)`, by [[P4 — What KL measures|P4]](iv) for
each intended behaviour. By the argument of [[P55 — What a record of counts certifies, at every size|P55]](iii) on the cells of `𝒫_{j_0}`, where `p̂_{𝒫_{j_0}}` is outside the
closure of the intended cell probabilities, some `η > 0` has `M_{𝒫_{j_0}}(p̂_n) ≥ η` with probability tending to `1`.
The threshold is `log(k/α)` with `k ≤ (n + 1)^{|𝒫_{j(n)}| − 1}`; choosing `j(n)` so that `|𝒫_{j(n)}|·log(n + 1)/n → 0`,
it falls below `n·η` for every large `n`.

**Notes.** Under compactness, misalignment does not depend on the nearness (TR3), so the same test serves under any
nearness. Without compactness the nearness can decide a verdict, and a description fixed in advance can then accuse an
actor whose misalignment is `0`: under the usual nearness of the line, the on-target controller of GD3, tested at the
cells `(−∞, 0]` and `(0, ∞)`, puts all its decisions in one and every pursuit splits evenly, though its misalignment is
`0`. As on finite outcomes, an actor whose decisions depend on each other can be accused for that alone ([[P55 — What a record of counts certifies, at every size|P55]], Notes).
"Aligned within `ε`" stays unverifiable from samples even under compactness: mixing an intended behaviour with a little
probability on a value the default never produces gives a behaviour as close as one likes in total variation and
infinitely misaligned (GD11).

### TR6 — The dimension law
**Statement.** Let `X = [0, 1]^D`, let `𝒫_w`, for `w = 1/k` with `k` a whole number, be the grid of half-open cubes of
side `w`, and let every intended behaviour have a density, against volume, between numbers `a > 0` and `A < ∞` on `X`.
Then for every `p̂`, `M_{𝒫_w}(p̂) = D·log(1/w) − H(p̂_{𝒫_w}) + θ_w`, with `H` the entropy of the cell probabilities and
`log(1/A) ≤ θ_w ≤ log(1/a)`. So if `p̂` has information dimension `d` in Rényi's sense, `M_{𝒫_w}(p̂)/log(1/w) → D − d`
as `w → 0`. On the line, a mixture that gives weight `α` to a behaviour with a density and the rest to finitely or
countably many points, of finite entropy, has `d = α`, so `D − d = 1 − α`.

**In plain terms.** Against acceptable behaviours that spread over the space with no gaps and no spikes, each finer
digit of the record adds, per decision, the logarithm of the number of new cells it splits into, less what the actor's
own spread uses: an actor pinned to points pays all of it, one spread like the default pays nothing, and one that piles
a share of its decisions on single values pays that share.

**Proof.** Every cell `C` of `𝒫_w` has volume `w^D`, so `p(C)` lies between `a·w^D` and `A·w^D` for every intended `p`.
Then `KL(p̂_{𝒫_w}‖p_{𝒫_w}) = −H(p̂_{𝒫_w}) − Σ_C p̂(C)·log p(C)`, and the sum lies between `D·log(1/w) − log A` and
`D·log(1/w) − log a`, for every intended `p`; so does the infimum over them, after adding `−H(p̂_{𝒫_w})`. Rényi's
information dimension of `p̂` is the limit of `H(p̂_{𝒫_w})/log(1/w)`, the grid of the definition being these cubes, and
he showed that it is `D` for a behaviour with a density on `[0, 1]^D`, and, on the line, the weight of the part with a
density for the mixture above (both as stated in [[References|@haghighatshoar2017]], section II, which cites [[References|@renyi1959]]). Dividing
by `log(1/w)` gives the limit.

**Notes.** This is the grid that GA5 asks to be declared before the data: on another grid the leading term is the same,
while `θ_w` can differ. Probed in T1 (`probes/general/`), with slopes `0.0998`, `1.0000`, `0.9997` and `0.3691` against
`0.10`, `1`, `1` and `log 2/log 3`; the last, the Cantor measure, has no density and no atoms, and its information
dimension is not given by the mixture theorem.

### TR7 — What a view allows, on standard Borel spaces
**Statement.** Let conditions, signals and outcomes form standard Borel spaces, and let the response depend on the
condition only through a view `(Z, V)` (GD8). Then for conditions `c` and `c'`: (i) if `V_c = V_{c'}`, `p_c = p_{c'}`;
(ii) `KL(p_c‖p_{c'}) ≤ KL(V_c‖V_{c'})`; (iii) if the view depends on the condition only through an input,
`V_c = ∫ K_w W_c(dw)` for a kernel `w ↦ K_w` from a standard Borel space of inputs, then
`KL(V_c‖V_{c'}) ≤ KL(W_c‖W_{c'})`.

**In plain terms.** [[P16 — An actor cannot behave more differently than it can tell conditions apart|P16]], on any outcome space met in practice: an actor cannot act more differently in two situations
than it can tell them apart, however finely situations, signals and outcomes are described.

**Proof.** `p_c` is the kernel `z ↦ π_z` applied to `V_c`, and `p_{c'}` the same kernel applied to `V_{c'}`. (i) is
immediate, and (ii) and (iii) are the data-processing inequality for a kernel applied to two behaviours
([[References|@polyanskiy2025]], Theorem 2.17, stated for standard Borel spaces, as everywhere in that book).

### TR8 — Dependence and drift only add evidence, on standard Borel spaces
**Statement.** Let `P` be a behaviour on `Xⁿ`, `X` standard Borel, with marginals `p̂_1, …, p̂_n`, average `p̄`, drift
`δ = (1/n)·Σ_i KL(p̂_i‖p̄)` and dependence `κ = (1/n)·KL(P‖p̂_1 ⊗ … ⊗ p̂_n)`. (i) For every `p ∈ Δ`,
`(1/n)·KL(P‖p^{⊗n}) = KL(p̄‖p) + δ + κ`, both sides possibly `+∞`. (ii) Over a set `𝓘` of behaviours, the least of the
left side is `inf_{p∈𝓘} KL(p̄‖p) + δ + κ`; it is `M(p̄) + δ + κ` when `𝓘` is τ-closed with a compact closure (TR3), and
otherwise `M(p̄)` may be smaller than that infimum. (iii) Every event's share in the record has expectation its
probability under `p̄`.

**In plain terms.** [[P54 — Dependence and drift only add evidence|P54]] on any outcome space met in practice, with one change: on a continuum the expected evidence
is measured against the divergence to the nearest intended behaviour, which is the misalignment of the average behaviour
exactly when the intended behaviours are closed and compact.

**Proof.** (i) The chain rule for a product reference ([[References|@polyanskiy2025]], Theorem 2.16(c), (2.27)) gives
`KL(P‖p^{⊗n}) = n·κ + Σ_i KL(p̂_i‖p)`. If some `p̂_i` is not absolutely continuous with respect to `p`, neither is `p̄`,
and both sides are `+∞`. Otherwise `p̂_i ≤ n·p̄`, so `p̂_i` has a ratio to `p̄` bounded by `n`, and
`log(dp̂_i/dp) = log(dp̂_i/dp̄) + log(dp̄/dp)` almost surely under `p̂_i`. The negative part of `log(dp̄/dp)` has
`p̂_i`-average at most `n` times its `p̄`-average, which is at most `1/e`, since `r·log r ≥ −1/e`; so each average below
is defined, and `KL(p̂_i‖p) = KL(p̂_i‖p̄) + E_{p̂_i}[log(dp̄/dp)]`. Summing over `i`, the last terms add to
`n·E_{p̄}[log(dp̄/dp)] = n·KL(p̄‖p)`. (ii) `δ` and `κ` do not depend on `p`; the rest is TR3. (iii) The expected share
of an event `C` is `(1/n)·Σ_i p̂_i(C) = p̄(C)`.
