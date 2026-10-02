---
kind: proposition
id: P10
aliases: ["P10"]
source: "derived/stakes.md"
---
# P10 — Sensitivity to the specification
> [!info] Generated from [derived/stakes.md](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/derived/stakes.md#p10--sensitivity-to-the-specification). Edit the source, not this note.

## Statement
Let `F` be non-constant, `p̂ ∈ Δ`, and write `M_{q,F}` for the misalignment under the standard
specification of `F` from the default `q`. For a function `h`, `osc(h) = max h − min h`.
(i) **The default.** For all `q, q' ∈ Δ°`, `|M_{q',F}(p̂) − M_{q,F}(p̂)| ≤ osc(log(q'/q))`.
(ii) **The objective.** For every `g : X → ℝ` with `F + g` non-constant, if the revealed intensity `t*` of `p̂` under
`F` is finite, then `M_{q,F+g}(p̂) ≤ M_{q,F}(p̂) + t*·osc(g)`.

## In plain terms
If the declared default is wrong, misalignment moves by at most the spread, in nats, of the
log-ratio between the right default and the wrong one. If the objective is wrong, misalignment moves by at most the
spread of the error times the intensity the behaviour reveals: the harder the actor pursues, the more an error in the
objective matters.

## Proof
First, for every `r ∈ Δ°`, `p ∈ Δ` and `h : X → ℝ`,
`KL(p‖tilt(r, h)) − KL(p‖r) = log E_r[e^h] − E_p[h]`, and both terms lie in `[min h, max h]`, so the difference lies in
`[−osc(h), osc(h)]`.
(i) Let `h = log(q'/q)`. By [[P1 — Every behaviour is a tilt of any other|P1]](iii), `tilt(q', t·F) = tilt(tilt(q, h), t·F) = tilt(p_{F,t}, h)`, where `p_{F,t}` is
the
pursuit from `q`. By the first step, `KL(p̂‖tilt(q', t·F))` and `KL(p̂‖p_{F,t})` differ by at most `osc(h)` for every
`t ≥ 0`, and so do their infima over `t ≥ 0`, which are the two misalignments.
(ii) Let `p_{F,t*}` be the nearest intended behaviour under `F`, so `M_{q,F}(p̂) = KL(p̂‖p_{F,t*})`. The pursuit of
`F + g` at intensity `t*` is `tilt(q, t*·(F + g)) = tilt(p_{F,t*}, t*·g)`, which is on the ray of `F + g`. By the first
step, `M_{q,F+g}(p̂) ≤ KL(p̂‖tilt(p_{F,t*}, t*·g)) ≤ M_{q,F}(p̂) + t*·osc(g)`.

## Notes
Both bounds are worst cases. The first is nearly attained (a ratio above 0.9 in the check). Exchanging the
roles of `F` and `F + g` in (ii) gives the reverse bound with the revealed intensity under `F + g`. In the third case
of [[P5 — Misalignment is attained, and zero exactly on the intended behaviours and their limits|P5]](iv) the revealed intensity is infinite and (ii) says nothing: at the extreme of pursuit, a small error in the
objective can change the verdict entirely.

## Lineage
New as statements. v7.10: Prop 26 (a wrong default is measured misalignment unless it leans along the
target), and NOTES §2.3 (capacity switches the regime: errors matter more at high capacity).

## Checks
- [`checks/test_sensitivity.py::test_default_error_moves_misalignment_by_at_most_its_spread`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_sensitivity.py)
- [`checks/test_sensitivity.py::test_objective_error_matters_in_proportion_to_intensity`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_sensitivity.py)

## Depends on
- [[P1 — Every behaviour is a tilt of any other|P1]] — Every behaviour is a tilt of any other

## Used by
- no later item
