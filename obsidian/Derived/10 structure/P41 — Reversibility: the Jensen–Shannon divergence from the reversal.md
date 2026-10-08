---
kind: proposition
id: P41
aliases: ["P41"]
source: "derived/structure.md"
---
# P41 — Reversibility: the Jensen–Shannon divergence from the reversal
> [!info] Generated from [derived/structure.md](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/derived/structure.md#p41--reversibility-the-jensenshannon-divergence-from-the-reversal). Edit the source, not this note.

## Statement
Let `S` be a finite set of states, and take as outcomes the transitions, the ordered pairs
`(x, y) ∈ S × S`. The **reversal** of a behaviour `F` on transitions is `F^T(x, y) = F(y, x)`, and `F` is
**reversible** if `F = F^T`. Take a reversible default in `Δ°(S × S)`, and as intended behaviours the reversible ones in
`Δ°(S × S)`. For `F ∈ Δ(S × S)` let `m = (F + F^T)/2`, and let its **entropy production** be `e(F) = KL(F‖F^T)`.
(i) `M(F) = KL(F‖m) = ½·KL(F‖m) + ½·KL(F^T‖m)`, the Jensen–Shannon divergence between `F` and its reversal. The infimum
is attained at `m` when `m` has full support, and approached otherwise.
(ii) `M(F) ≤ e(F)/2`.
(iii) If `F_s = m + s·A`, with `m ∈ Δ°(S × S)` reversible and `A ≠ 0` with `A^T = −A`, then `M(F_s)/e(F_s) → 1/4` as
`s → 0`.
(iv) Let `P` be the transition matrix of a Markov chain on `S` with a stationary distribution `π` of full support, and
`F(x, y) = π(x)·P(x, y)`. Among the transition matrices `R` that are reversible with respect to some distribution and
positive wherever `P` is, the smallest value of `Σ_x π(x)·KL(P(x,·)‖R(x,·))` is `M(F)`, attained at
`R(x, y) = m(x, y)/π(x)` alone.

## In plain terms
Record transitions and compare the film run forward with the film run backward. If they look alike,
the process is reversible. Measured against reversibility, misalignment is the Jensen–Shannon divergence between the two
films: at most half of the entropy production, the plain divergence from the backward film, and a quarter of it when the
asymmetry is small. For a Markov chain, the nearest reversible chain runs each transition as often as the two films do
on average.

## Proof
(i) For a reversible `W`, `Σ F·log W = Σ F^T·log W = Σ m·log W`, so `KL(F‖W) = Σ F·log F − Σ m·log W`. This
holds for `W = m`, which is reversible, so `KL(F‖W) − KL(F‖m) = Σ m·log(m/W) = KL(m‖W) ≥ 0`, with equality exactly at
`W = m`. If `m` has zeros, the reversible behaviours `(1 − ε)·m + ε·u`, with `u` uniform, have full support, and
`KL(F‖·)` at them tends to `KL(F‖m)` as `ε → 0`, because `m > 0` wherever `F > 0`. And
`KL(F^T‖m) = KL(F‖m^T) = KL(F‖m)`. The reversible behaviours of full support form a closed set in `Δ°(S × S)`, so this
is a specification ([[D3 — Specification, declaration and misalignment|D3]]).
(ii) KL is convex in its second argument, so `KL(F‖m) ≤ ½·KL(F‖F) + ½·KL(F‖F^T) = e(F)/2`.
(iii) `F_s^T = m − s·A`. Second-order expansions give `KL(F_s‖m) = (s²/2)·Σ A²/m + O(s³)` and
`KL(F_s‖F_s^T) = (s²/2)·Σ (2A)²/m + O(s³)`, and `Σ A²/m > 0`, so the ratio tends to `1/4`.
(iv) An `R` reversible with respect to some distribution and positive wherever `P` is has the form
`R(x, y) = W(x, y)/W_1(x)`, with `W` symmetric and non-negative and `W_1(x) = Σ_y W(x, y)`. Since the rows of `F` sum to
`π`, `Σ_x π(x)·KL(P(x,·)‖R(x,·)) = Σ F·log P − Σ F·log W + Σ_x π(x)·log W_1(x)`. As in (i), `Σ F·log W = Σ m·log W`,
and the rows of `m` also sum to `π`, because `π` is stationary. With `Q(x, y) = m(x, y)/π(x)`, a transition matrix, the
value is therefore `Σ F·log P − Σ_x π(x)·Σ_y Q(x, y)·log R(x, y)`
`= Σ F·log P − Σ_x π(x)·Σ_y Q(x, y)·log Q(x, y) + Σ_x π(x)·KL(Q(x,·)‖R(x,·))`, smallest exactly at `R = Q`, which is
reversible with respect to `π`. Its value is `Σ F·log F − Σ m·log m = KL(F‖m)`, the two terms in `log π` cancelling.

## Notes
Log-linear learning in a potential game, in which players revise one at a time by a logit rule, has the Gibbs
law of the potential as its long-run behaviour [[References|@blume1993]] and is reversible; in other games it need not be. What
drives the circulation is the game's harmonic part [[References|@candogan2011]]. On a single cycle the entropy production is the
cycle's flux times its affinity [[References|@schnakenberg1976]], and for log-linear learning in a two-by-two game the affinity is
`t·C`, with `C` the payoff gained around the cycle of single-player deviations (`probes/general/`, B2;
`general/derived-spaces.md`). (iii) is the quarter law that probe T4 found before it was derived (B1).

## Lineage
New. `NOTES.md` §5.4, H12; probes T4, B1 and B2.

## Checks
- [`checks/test_structure.py::test_reversibility_misalignment_is_jensen_shannon`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_structure.py)
- [`checks/test_structure.py::test_entropy_production_bounds_and_the_quarter_law`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_structure.py)
- [`checks/test_structure.py::test_the_nearest_reversible_chain`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_structure.py)

## Depends on
- [[D3 — Specification, declaration and misalignment|D3]] — Specification, declaration and misalignment

## Used by
- no later item
