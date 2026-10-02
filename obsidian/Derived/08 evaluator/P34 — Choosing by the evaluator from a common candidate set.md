---
kind: proposition
id: P34
aliases: ["P34"]
source: "derived/evaluator.md"
---
# P34 — Choosing by the evaluator from a common candidate set
> [!info] Generated from [derived/evaluator.md](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/derived/evaluator.md#p34--choosing-by-the-evaluator-from-a-common-candidate-set). Edit the source, not this note.

## Statement
Let a random set `S` of candidate outcomes be drawn by any mechanism, for instance `n` independent draws
from `q`. From the same `S`, let `x*` be a candidate with the largest target `F` and `x̂` one with the largest evaluator
`F̂ = F + E`, known in the units of `F`, both breaking ties by one fixed order, and let `p*` and `p̂` be their
distributions.
(i) `0 ≤ F(x*) − F(x̂) ≤ E(x̂) − E(x*) ≤ max_S E − min_S E` for every `S`, and so
`0 ≤ E_{p*}[F] − E_{p̂}[F] ≤ E_{p̂}[E] − E_{p*}[E] ≤ E[max_S E − min_S E]`.
(ii) Over all targets `F` with the same error, the supremum of the loss is the range of the error over the candidates:
`F = −c·E` gives `F(x*) − F(x̂) = c·(max_S E − min_S E)` for every `S`, for every `0 < c < 1`. So no bound on the
average loss that depends only on the error and the way `S` is drawn is smaller than `E[max_S E − min_S E]`.

## In plain terms
When the evaluator and the target choose among the same candidates, the target lost is at most
how much more the evaluator overrates its own pick than the target's pick, and so at most the spread of the error over
the candidates. That spread is the exact worst case: for some target it is lost. Best-of-`n` by the evaluator,
compared with best-of-`n` by the target at the same `n`, is the case in point: the worst average loss is the average
spread of the error over `n` draws.

## Proof
`x̂ ∈ S`, so `F(x*) ≥ F(x̂)`; and `x* ∈ S`, so `F̂(x̂) ≥ F̂(x*)`, that is, `F(x̂) + E(x̂) ≥ F(x*) + E(x*)`.
Together, `0 ≤ F(x*) − F(x̂) ≤ E(x̂) − E(x*)`, and both candidates are in `S`. Taking averages over `S` gives the rest
of (i). (ii) With `F = −c·E`, `F̂ = (1 − c)·E`, so `x̂` has the largest `E` in `S` and `x*` the smallest; ties do not
matter, since tied candidates have the same `E` and `F`. Then `F(x*) − F(x̂) = c·(max_S E − min_S E)`, and with (i), the
supremum of the average loss over `0 < c < 1` is `E[max_S E − min_S E]`.

## Notes
The middle bound of (i) is one line: the loss is `E(x̂) − E(x*)` minus the evaluator's margin
`F̂(x̂) − F̂(x*) ≥ 0`, so it is computable only when the loss is. Its use is the range form, and (ii) shows that form
cannot be improved; it is the counterpart, for selection, of [[P29 — The width is the exact worst case|P29]](ii). No width enters: the bound depends on the
candidates. It needs them to be shared. The archive found that comparing best-of-`n` by the evaluator with the pursuit
of the target at the same departure, instead of at the same `n`, breaks the inequality in some instances (v7.10: R6);
that is its measurement.

## Lineage
v7.10: Prop 23 (argmax selectors on a common candidate set).

## Checks
- [`checks/test_evaluator.py::test_choosing_from_a_common_candidate_set`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_evaluator.py)

## Depends on
- nothing

## Used by
- no later item
