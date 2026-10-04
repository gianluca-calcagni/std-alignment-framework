---
kind: proposition
id: P48
aliases: ["P48"]
source: "derived/diagnostics.md"
---
# P48 — Misalignment when the target is uncertain
> [!info] Generated from [derived/diagnostics.md](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/derived/diagnostics.md#p48--misalignment-when-the-target-is-uncertain). Edit the source, not this note.

## Statement
Let `F_1, …, F_k` be functions on `X`, write `Φ = (F_1, …, F_k)`, and let `𝒮` be the set of non-constant
combinations `c·Φ`, the objectives a principal may hold when its target is known only to lie in their span. For
`F' ∈ 𝒮`, let `M_{F'}` be misalignment under the standard specification of `F'` from the default `q`. Let `p̂ ∈ Δ°`, and
let `p̃` be the behaviour nearest to `q` among those with `p̂`'s averages of `Φ` ([[P15 — Misalignment splits into what the actor could avoid and what it could not|P15]](i)).
(i) **The most charitable principal.** `p̃ = tilt(q, c̃·Φ)` for some `c̃`, and `M_{F'}(p̂) ≥ KL(p̂‖p̃)` for every
`F' ∈ 𝒮`. If `p̃ ≠ q`, equality holds for `F' = c̃·Φ`, the **most charitable principal**; if `p̃ = q`, every
`M_{F'}(p̂)` equals `KL(p̂‖q)`.
(ii) **The least charitable.** `M_{F'}(p̂) ≤ KL(p̂‖q)` for every `F' ∈ 𝒮`, with equality whenever
`E_{p̂}[F'] ≤ E_q[F']`, which holds for `F'` or for `−F'`.
(iii) So, for every principal whose objective lies in `𝒮`, misalignment lies in `[KL(p̂‖p̃), KL(p̂‖q)]`, and both ends
are attained. With `Φ = (F, G_1, …, G_k)`, `p̃` is the named pursuit of [[P44 — What named objectives explain|P44]], and the lower end is its unexplained
misalignment.

## In plain terms
When the principal's goal is not known exactly, but is known to be some mix of given objectives,
misalignment is not one number but an interval. Its lower end is what even the most charitable principal of that kind
would find, the one whose goal the actor's change comes closest to pursuing; its upper end is the whole change, which a
principal wanting the opposite would find. An actor shown to be far from the lower end is far from every goal of that
kind.

## Proof
(i) `𝓛 = {p ∈ Δ : E_p[Φ] = E_{p̂}[Φ]}` is linear and contains `p̂ ∈ Δ°`, so [[P15 — Misalignment splits into what the actor could avoid and what it could not|P15]](i) and (iii), with `q` in
the role of `r`, give `p̃ = tilt(q, c̃·Φ)` for some `c̃`. For every `c`, `log(p̃/tilt(q, c·Φ))` is `(c̃ − c)·Φ` plus a
constant, whose average is the same under `p̂` and `p̃`, so
`KL(p̂‖tilt(q, c·Φ)) − KL(p̂‖p̃) = E_{p̂}[log(p̃/tilt(q, c·Φ))] = KL(p̃‖tilt(q, c·Φ)) ≥ 0`. Every pursuit `p_{F',t}`
with `F' ∈ 𝒮` and `t ≥ 0` is such a tilt, with `c` a multiple of `F'`'s coefficients, so `M_{F'}(p̂) ≥ KL(p̂‖p̃)`. If
`p̃ ≠ q`, `F' = c̃·Φ` is not constant, and the mean of `F'` under `tilt(q, F')` exceeds its mean under `q`, because
tilting by a non-constant function raises its mean (the derivative of `t ↦ E_{p_{F',t}}[F']` is a positive variance); as
`E_{p̂}[F'] = E_{p̃}[F']` and `E_{p̂}[F'] < max F'` for `p̂ ∈ Δ°`, the second case of [[P5 — Misalignment is attained, and zero exactly on the intended behaviours and their limits|P5]](iv) applies with `t* = 1`,
and `M_{F'}(p̂) = KL(p̂‖p̃)`. If `p̃ = q`, every `F' ∈ 𝒮` has `E_{p̂}[F'] = E_q[F']`, so the first case of [[P5 — Misalignment is attained, and zero exactly on the intended behaviours and their limits|P5]](iv)
gives `M_{F'}(p̂) = KL(p̂‖q)`.
(ii) The bound is [[P6 — The departure from the default splits into pursuit and misalignment|P6]], and the equality is the first case of [[P5 — Misalignment is attained, and zero exactly on the intended behaviours and their limits|P5]](iv). `E_{p̂}[F'] − E_q[F']` changes sign with `F'`,
and `−F' ∈ 𝒮`.
(iii) follows from (i) and (ii). For `Φ = (F, G_1, …, G_k)`, [[P44 — What named objectives explain|P44]](i) makes the named pursuit a tilt of `q` by a
combination of `Φ` with `p̂`'s averages of `Φ`; the identity in (i), applied to it and to `p̃` both ways, gives
`KL(p̃‖p_*) + KL(p_*‖p̃) = 0` for such a tilt `p_*`, so it is `p̃`.

## Notes
With no restriction on the target, the lower end is `0`: if the span contains `log(p̂/q)`, then `p̃ = p̂`,
which is [[P1 — Every behaviour is a tilt of any other|P1]]: every behaviour pursues its own revealed objective. So a test without a declared target can say nothing
about alignment, and a test with a declared family can bound it, as an unobserved condition is bounded by [[P17 — What an unobserved condition can hide|P17]]. The
interval depends only on the span of `Φ`, not on which function is called the target. In case W4
(`cases/w4-two-runs/RESULTS.md`), for every principal whose objective combines the run's reward, `log R`, the other
run's reward and the other run's revealed objective, run A is between `9.46` and `12.28` nats misaligned. A family with
signs, such as a non-negative weight on a reward, is a subset of the span, so its interval lies inside this one; its
ends then need a constrained minimization, not stated here.

## Lineage
New, from the PI's question whether W3 and W4 had a proper target (`NOTES.md` §7). It reads [[P44 — What named objectives explain|P44]]'s
unexplained misalignment as the least misalignment over a family of principals; inverse reinforcement learning meets the
same ambiguity as the set of rewards consistent with behaviour (`RELATED.md`).

## Checks
- [`checks/test_diagnostics.py::test_an_uncertain_target_gives_an_interval`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_diagnostics.py)

## Depends on
- [[P5 — Misalignment is attained, and zero exactly on the intended behaviours and their limits|P5]] — Misalignment is attained, and zero exactly on the intended behaviours and their limits
- [[P6 — The departure from the default splits into pursuit and misalignment|P6]] — The departure from the default splits into pursuit and misalignment
- [[P15 — Misalignment splits into what the actor could avoid and what it could not|P15]] — Misalignment splits into what the actor could avoid and what it could not
- [[P44 — What named objectives explain|P44]] — What named objectives explain

## Used by
- [[P49 — Outer and inner misalignment|P49]] — Outer and inner misalignment
