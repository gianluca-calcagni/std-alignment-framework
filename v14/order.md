# Order against a reference

> **Status: draft of v14 (Q59); proved here, not yet checked in CI.** The numbers come from `probes/v14/v14_probe.py`.

The order part of a request is a ranking of outcomes, which the principal may give only up to increasing transformations
([B3] becomes this), and a **reference** `r ∈ Δ`, a behaviour against which it is judged: a base model, the previous
version, a population of answers, the status quo. The ranking is a **preorder** `≽` on `X`: reflexive and transitive,
possibly partial, as when outcomes are ranked on two scales at once. An **upper set** is a set `U ⊆ X` that contains
every outcome ranked at least as high as one of its members; a **reading** of the ranking is a function `u : X → ℝ` that
is non-decreasing (`x ≽ y` implies `u(x) ≥ u(y)`), the scores of a principal who holds this ranking and no other
commitment.

### VO1 — Better for every reading is dominance on upper sets
**Statement.** For behaviours `a` and `r`, these are equivalent: (a) `E_a[u] ≥ E_r[u]` for every reading `u`; (b) `a(U)
≥ r(U)` for every upper set `U`. When the ranking is total, given by a function `F`, the upper sets are the sets `{F ≥
f}`, and (b) is first-order stochastic dominance of `F` under `a` over `F` under `r`.

**In plain terms.** An actor is better than the reference for everyone who holds the principal's ranking exactly when,
for every standard "at least this good", it meets the standard at least as often as the reference does.

**Proof.** (a) ⇒ (b): the indicator of an upper set is a reading. (b) ⇒ (a): let `u` be a reading with values
`c_1 < … < c_k`. Then `u = c_1 + Σ_{j≥2} (c_j − c_{j−1})·1{u ≥ c_j}`, each set `{u ≥ c_j}` is an upper set because `u`
is non-decreasing, and the coefficients are positive; so
`E_a[u] − E_r[u] = Σ_{j≥2} (c_j − c_{j−1})·(a(u ≥ c_j) − r(u ≥ c_j)) ≥ 0`. For a total ranking by `F`, an upper set
containing an outcome of value `f` contains every outcome with `F ≥ f`, so it is `{F ≥ f}` for its least value `f`, or
empty. ∎

**Notes.** For a total ranking this is the classical characterization of first-order stochastic dominance, proved here
in a few lines rather than cited. The sets `B(r) = {a : a(U) ≥ r(U) for every upper set U}`, "better or equal for every
reading", and `W(r) = {a : a(U) ≤ r(U) for every upper set U}`, "worse or equal for every reading", are convex and
closed, being cut out by finitely many linear inequalities, and both contain `r`.

### VO2 — v13's ordinal specification lies inside "better for every reading"
**Statement.** For a total ranking by `F` and `r ∈ Δ°`, every behaviour `a` whose ratio `a/r` is a non-decreasing
function of `F` lies in `B(r)`. The inclusion is strict when `F` takes at least three values.

**In plain terms.** v13's ordinal specification, which asks the actor to favour better outcomes at every level relative
to the reference, is a stronger demand than being better for everyone who holds the ranking.

**Proof.** Let `ρ = a/r`, non-decreasing in `F`, with `E_r[ρ] = 1`, and `U = {F ≥ f}`. `ρ` and `1_U` are both
non-decreasing functions of `F`, so `Cov_r(ρ, 1_U) ≥ 0` (for two non-decreasing functions of one variable,
`Σ_{x,y} r(x)·r(y)·(ρ(x) − ρ(y))·(1_U(x) − 1_U(y)) ≥ 0`, each term being a product of two numbers of the same sign; the
sum is twice the covariance). So `a(U) = E_r[ρ·1_U] ≥ E_r[ρ]·r(U) = r(U)`. Strictness: with three levels of equal
reference mass, `a = (0, 2/3, 1/3)` on the levels in increasing order dominates `r` (its upper-set masses are
`1, 1, 1/3` against `1, 2/3, 1/3`), and its ratio `(0, 2, 1)` is not non-decreasing. ∎

**Notes.** Which of the two the order's requirement should be is an open question for the PI (`README.md`). `B(r)` asks
only what every holder of the ranking would agree on; v13's cone asks, besides, a shape, which best-of-`n` and every
pursuit of an increasing transformation of `F` meet, and which a greedy decoder does not.

### VO3 — Three verdicts, and which of them a record verifies
**Statement.** Against a reference `r` and a ranking, a behaviour `a` is **better** when `a ∈ B(r)`, **worse** when `a
∈ W(r)`, both when `a(U) = r(U)` for every upper set, and **neither** otherwise. With records of independent decisions:
(i) "not better", `a ∉ B(r)`, and "not worse", `a ∉ W(r)`, are verifiable in the statistical sense, by the bets of VE1
against the convex sets `B(r)` and `W(r)`;
(ii) "worse", and "better", are not verifiable: each is refutable only;
(iii) for a total ranking, "worse by a margin `m > 0` on a declared range of upper sets", `a(U) ≤ r(U) − m` for every
upper set `U` in a declared finite list, is verifiable.

**In plain terms.** A record can show that an actor is not an improvement for everyone who holds the ranking, and that
it is not a regression for everyone. It can never show that the actor is a regression for everyone, since a behaviour
that equals the reference is a regression for no one and lies arbitrarily close to one that is; it can show a
regression by a stated margin at stated standards.

**Proof.** (i) The complement of a closed set is open in the behaviours, and the open sets are those verifiable in the
statistical sense ([@genin2017], as cited in [D3]); the tests are VE3's, against `B(r)` or `W(r)`. (ii) `W(r)` and
`B(r)` are closed and contain `r`. Every neighbourhood of `r` contains behaviours outside `W(r)`, unless every
behaviour near `r` is in `W(r)`, which fails as soon as some upper set `U` has `0 < r(U) < 1`, by moving a little mass
into `U`; likewise for `B(r)`. A set with a boundary point in it that is not interior is not open, so not verifiable.
(iii) The set is cut out by finitely many strict inequalities, so it is open. ∎

**Notes.** The greedy decoder of `NOTES.md` §22: ten levels, a uniform reference, and an actor that always answers at
level `8`. It meets the standard "level `9`" less often than the reference (`0` against `0.1`) and every standard up to
level `8` more often, so it is neither better nor worse (`probes/v14/RESULTS.md`, VO3), while its average rank is
`0.889` against `0.5`. v13's ordinal specification calls it misaligned. Common sense would not; what the decoder lacks
is the principal's value scale, under which its average rank would count, or a declared standard ("at least level 8"),
which it meets every time. The verdicts of v14 say this instead of one number: neither better nor worse for every
reading, and better under the declared scale or standard, if one is declared. "Misaligned" is kept for a breach of a
constraint, and for "worse", which the principal may declare by margins (iii). Whether these are the right words is for
L2 to test before anyone adopts them.
