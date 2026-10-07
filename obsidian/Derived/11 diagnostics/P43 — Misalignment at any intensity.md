---
kind: proposition
id: P43
aliases: ["P43"]
source: "derived/diagnostics.md"
---
# P43 — Misalignment at any intensity
> [!info] Generated from [derived/diagnostics.md](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/derived/diagnostics.md#p43--misalignment-at-any-intensity). Edit the source, not this note.

## Statement
Under the standard specification of a non-constant `F`, let `p̂ ∈ Δ`, with revealed intensity `t*` and
nearest intended behaviour `p°` (or its limit `q(·|A)`) ([[P5 — Misalignment is attained, and zero exactly on the intended behaviours and their limits|P5]](iv)).
(i) For every `t ≥ 0`, `KL(p̂‖p_{F,t}) = M(p̂) + KL(p°‖p_{F,t}) + t·[E_q[F] − E_{p̂}[F]]⁺`. The middle term, the
**intensity mismatch** at `t`, is `0` exactly when `t = t*`. At the matched intensity, `t = λ`, this is [[P9 — What is at stake|P9]](ii).
(ii) **One intensity for several conditions.** Let conditions `c` have frequencies `ρ(c) > 0`; in each, let `q_c ∈ Δ°`
be the default, `F_c` a non-constant objective, and `p_c ∈ Δ` a behaviour with misalignment `M_c`, finite revealed
intensity `t*_c` and nearest intended behaviour `p°_c`. With `a_c = [E_{q_c}[F_c] − E_{p_c}[F_c]]⁺`, the misalignment at
one shared intensity ([[P24 — The evaluation gap|P24]], Notes) is
`min_{t≥0} Σ_c ρ(c)·KL(p_c‖p_{c,F_c,t}) = Σ_c ρ(c)·M_c + min_{t≥0} Σ_c ρ(c)·[KL(p°_c‖p_{c,F_c,t}) + t·a_c]`,
and both minima are attained. The excess over `Σ_c ρ(c)·M_c` depends on each condition only through `q_c`, `F_c`, `t*_c`
and `a_c`, and it is `0` exactly when all the `t*_c` are equal.

## In plain terms
Judged against a pursuit at some other strength than its own, a behaviour carries two costs beyond
its misalignment: how far its nearest pursuit is from the pursuit at that strength, and, if it did worse than the
default, that loss times the strength. So when several situations must all be pursued at one strength, the extra
misalignment depends only on how strongly each situation was pursued, never on what else the actor did there.

## Proof
(i) Write `Λ(t) = log E_q[e^{t·F}]`, so `KL(p‖p_{F,t}) = KL(p‖q) − t·E_p[F] + Λ(t)` for every `p ∈ Δ`. In the
first case of [[P5 — Misalignment is attained, and zero exactly on the intended behaviours and their limits|P5]](iv), `p° = q`, `M(p̂) = KL(p̂‖q)` and `E_{p̂}[F] ≤ E_q[F]`; since `KL(q‖p_{F,t}) = −t·E_q[F] + Λ(t)`,
`KL(p̂‖p_{F,t}) = M(p̂) + KL(q‖p_{F,t}) + t·(E_q[F] − E_{p̂}[F])`. In the second, `p° = p_{F,t*}` with
`E_{p°}[F] = E_{p̂}[F] > E_q[F]`, and
`KL(p̂‖p_{F,t}) − KL(p̂‖p°) = E_{p̂}[log(p°/p_{F,t})] = (t* − t)·E_{p̂}[F] − Λ(t*) + Λ(t)`, which equals
`E_{p°}[log(p°/p_{F,t})] = KL(p°‖p_{F,t})` because the two averages of `F` agree. In the third, `p̂` puts all its mass
on `A`, `E_{p̂}[F] = max F`, and `M(p̂) = KL(p̂‖q) + log q(A)`; also `KL(q(·|A)‖p_{F,t}) = −log q(A) − t·max F + Λ(t)`,
and the two add up to `KL(p̂‖q) − t·max F + Λ(t) = KL(p̂‖p_{F,t})`. In the last two cases the last term is `0`. The
mismatch is `0` exactly when `p° = p_{F,t}`: the map `t ↦ p_{F,t}` is one to one, because `t ↦ E_{p_{F,t}}[F]` increases
strictly (proof of [[P9 — What is at stake|P9]](i)), and `q(·|A)` is not a pursuit at a finite intensity, since `A ≠ X`.
(ii) Apply (i) in each condition, weight by `ρ(c)`, and minimize over `t`. Each `KL(p°_c‖p_{c,F_c,t})` is continuous and
convex in `t`, being `Λ_c(t) − t·E_{p°_c}[F_c]` plus a constant, and it tends to infinity as `t → ∞`, because `p°_c` has
full support while the mass of `p_{c,F_c,t}` outside the outcomes where `F_c` is largest tends to `0`. So the minimum is
attained. If all the `t*_c` equal some `τ`, then at `t = τ` every mismatch is `0`, and `τ·a_c = 0`: either `τ = 0`, or
every `t*_c > 0`, so every `a_c = 0`. Conversely, if the excess is `0` at its minimizer `t`, every mismatch is `0`
there, so every `t*_c = t` by (i).

## Notes
W1's report judged best-of-`n` in 1,000 prompts at one shared intensity and found misalignment higher by
`0.138` nats at `n = 16` than with each prompt at its own (`cases/w1-best-of-n-slope/REPORT.md`). By (ii), that excess
is set entirely by how the revealed intensities differ across prompts, and by the prompts where best-of-`n` lowered the
gold: a fixed `n` is not a fixed intensity. A principal who asks for one intensity, as KL-regularized training with one
coefficient does, should report the excess apart from the misalignment of each condition.

## Lineage
v7.10: Thm 13(b), the three-term decomposition of the half-ray (transverse, axial and anti-alignment),
which [[P9 — What is at stake|P9]](ii) reads at the matched intensity only. New: the reading at any intensity, and across conditions at one
intensity.

## Checks
- [`checks/test_diagnostics.py::test_misalignment_at_any_intensity`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_diagnostics.py)
- [`checks/test_diagnostics.py::test_one_intensity_for_several_conditions`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_diagnostics.py)

## Depends on
- [[P5 — Misalignment is attained, and zero exactly on the intended behaviours and their limits|P5]] — Misalignment is attained, and zero exactly on the intended behaviours and their limits
- [[P9 — What is at stake|P9]] — What is at stake
- [[P24 — The evaluation gap|P24]] — The evaluation gap

## Used by
- no later item
