---
kind: proposition
id: P23
aliases: ["P23"]
source: "derived/estimation.md"
---
# P23 — The estimated misalignment of an actor that pursues the objective
> [!info] Generated from [derived/estimation.md](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/derived/estimation.md#p23--the-estimated-misalignment-of-an-actor-that-pursues-the-objective). Edit the source, not this note.

## Statement
Let `F` be non-constant, `|X| ≥ 3`, and let the actor pursue `F` from `q` at an intensity `t > 0`, so
that its behaviour is `p_{F,t}`. Let `p̂_n` be the empirical behaviour of a sample of size `n` from it, and `M` the
misalignment under the standard specification of `F`. Then, as `n → ∞`, `2n·M(p̂_n)` converges in distribution to a χ²
distribution with `|X| − 2` degrees of freedom.

## In plain terms
Even an actor that pursues the objective exactly shows some misalignment in a finite record, by
chance. How much is known: twice the number of decisions times the estimated misalignment follows, approximately, a
chi-squared law with two fewer degrees of freedom than there are outcomes. An estimate well above that law's range is
evidence of real misalignment.

## Proof
`n·M(p̂_n) = n·min_{s≥0} KL(p̂_n‖p_{F,s})` is the logarithm of the ratio between the largest likelihood of
the sample over all behaviours, reached at `p̂_n`, and over the pursuit ray. The ray is a smooth one-parameter family
inside the `(|X| − 1)`-parameter family of all full-support behaviours, and the true intensity `t > 0` is an interior
point of the half-line `s ≥ 0`. Wilks's theorem then gives the χ² limit with `(|X| − 1) − 1 = |X| − 2` degrees of
freedom [[References|@wilks1938]].

## Notes
At `t = 0`, the true intensity is on the boundary of the half-line and the limit is a mixture of χ²
distributions (chi-bar-square), not covered here. The check is a light simulation (300 samples of size 2000, for three
and five outcomes), which compares the mean with `|X| − 2`.

## Lineage
v8: the deviance of [[P5 — Misalignment is attained, and zero exactly on the intended behaviours and their limits|P5]]'s Notes. New as a result (`NOTES.md` E1).

## Checks
- [`checks/test_estimation.py::test_estimated_misalignment_is_chi_squared`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_estimation.py)

## Depends on
- nothing

## Used by
- no later item
