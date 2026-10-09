---
kind: proposition
id: P1
aliases: ["P1"]
source: "derived/tilts-and-paths.md"
---
# P1 — Every behaviour is a tilt of any other
> [!info] Generated from [derived/tilts-and-paths.md](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/derived/tilts-and-paths.md#p1--every-behaviour-is-a-tilt-of-any-other). Edit the source, not this note.

## Statement
Let `r ∈ Δ°`.
(i) For every `p ∈ Δ°`, `p = tilt(r, log(p/r))`.
(ii) `tilt(r, F) = tilt(r, G)` if and only if `F − G` is constant.
(iii) `tilt(tilt(r, F), G) = tilt(r, F + G)`, and `tilt(r, 0) = r`.

## In plain terms
Any full-support behaviour can be written as any other full-support behaviour reweighted by some
function, and that function is fixed except for adding a constant. Reweightings add up. So describing a behaviour as
"the default, reweighted toward an objective" is always possible, and loses nothing.

## Proof
(i) `r·e^{log(p/r)} = p`, which already sums to 1. (ii) If `F − G = c`, the factor `e^c` cancels in the
normalization. Conversely, if the tilts are equal, then `F − log E_r[e^F] = G − log E_r[e^G]` at every outcome, so
`F − G` is constant. (iii) `tilt(tilt(r, F), G)` is proportional to `r·e^F·e^G`, and both sides are normalized;
`e^0 = 1`.

## Notes
`log(p/r)` is the log-likelihood ratio of `p` to `r`. Recovering an objective from behaviour is the problem
of inverse reinforcement learning, which is known to be ill-posed [[References|@ng2000]]; (ii) is the form the ambiguity takes here:
given the default, a behaviour reveals its objective up to a constant. Written with an intensity, `tilt(r, t·F)`, it
reveals only the product `t·F`.

## Lineage
New as a statement. v7.10 used the tilt as the form of intended behaviour (Def 1), and recorded "everything
is a tilt" as an insight (NOTES §2.1) without stating it. The freedom in (ii) is v7.10's Prop 16 (g2), and the product
`t·F` is v7.10's Prop 12.

## Checks
- [`checks/test_tilts.py::test_every_behaviour_is_a_tilt`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_tilts.py)
- [`checks/test_tilts.py::test_tilt_objective_unique_up_to_constant`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_tilts.py)
- [`checks/test_tilts.py::test_tilts_compose`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_tilts.py)

## Depends on
- nothing

## Used by
- [[D2 — Pursuit of an objective|D2]] — Pursuit of an objective
- [[D6 — Intervention and pass-through|D6]] — Intervention and pass-through
- [[D10 — Evaluator, regression and residual|D10]] — Evaluator, regression and residual
- [[P4 — What KL measures|P4]] — What KL measures
- [[P14 — The cost of departing from the default is forced|P14]] — The cost of departing from the default is forced
- [[P8 — An actor that cannot tell outcomes apart|P8]] — An actor that cannot tell outcomes apart
- [[P9 — What is at stake|P9]] — What is at stake
- [[P10 — Sensitivity to the specification|P10]] — Sensitivity to the specification
- [[P33 — Error bounds for a known evaluator|P33]] — Error bounds for a known evaluator
- [[P49 — Outer and inner misalignment|P49]] — Outer and inner misalignment
- [[P50 — Tampering: a change of the measurement, not of the world|P50]] — Tampering: a change of the measurement, not of the world
- [[C3 — An error confined to one region costs bounded nats|C3]] — An error confined to one region costs bounded nats
