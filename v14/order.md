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
closed, being cut out by finitely many linear inequalities, and both contain `r`. `B(r)` is `targets.md`'s TG1 for the
family of a ranking's readings: "no worse than the reference on any target", with the readings as the targets.

### VO2 — v13's ordinal specification lies inside "better for every reading"
**Statement.** For a total ranking by `F` and `r ∈ Δ°`, every behaviour `a` whose ratio `a/r` is a non-decreasing
function of `F` lies in `B(r)`. The inclusion is strict when `F` takes at least three values, or when two outcomes tie
in `F`.

**In plain terms.** v13's ordinal specification, which asks the actor to favour better outcomes at every level relative
to the reference, is a stronger demand than being better for everyone who holds the ranking.

**Proof.** Let `ρ = a/r`, non-decreasing in `F`, with `E_r[ρ] = 1`, and `U = {F ≥ f}`. `ρ` and `1_U` are both
non-decreasing functions of `F`, so `Cov_r(ρ, 1_U) ≥ 0` (for two non-decreasing functions of one variable,
`Σ_{x,y} r(x)·r(y)·(ρ(x) − ρ(y))·(1_U(x) − 1_U(y)) ≥ 0`, each term being a product of two numbers of the same sign; the
sum is twice the covariance). So `a(U) = E_r[ρ·1_U] ≥ E_r[ρ]·r(U) = r(U)`. Strictness. With three levels
`f_1 < f_2 < f_3` of `F`, move a mass `s`, with `0 < s ≤ r(F = f_1)`, from the outcomes at the lowest level to those at
the middle one, in proportion to `r` within each. The mass of `{F ≥ f}` rises by `s` for `f_1 < f ≤ f_2` and is
unchanged otherwise, so the result is in `B(r)`; its ratio is above `1` at the middle level and `1` at the top, so it is
not non-decreasing. With two outcomes tied in `F`, moving a little mass from one to the other changes no upper set's
mass, and makes `a/r` differ between two outcomes at the same level, which v13's ordinal specification, asking `a/r` to
be a function of `F`, excludes. ∎

**Notes.** Which requirement an order gives, `B(r)`, the ordinal cone or margins, is the PI's to decide (`ROADMAP.md`,
recommendation 2). `B(r)` asks only what every holder of the ranking would agree on; v13's cone asks, besides, a shape,
which best-of-`n` and every pursuit of an increasing transformation of `F` meet, and which a greedy decoder does not.

### VO3 — Three verdicts, and which of them a record verifies
**Statement.** Against a reference `r` and a ranking, a behaviour `a` is **better** when `a ∈ B(r)`, **worse** when `a
∈ W(r)`, both when `a(U) = r(U)` for every upper set, and **neither** otherwise. With records of independent decisions:
(i) "not better", `a ∉ B(r)`, and "not worse", `a ∉ W(r)`, are verifiable in the statistical sense, by the bets of VE1
against the convex sets `B(r)` and `W(r)`;
(ii) if some upper set `U` has `0 < r(U) < 1`, as it does when `r` has full support and the ranking has at least two
classes, "worse or equal", `a ∈ W(r)`, and "better or equal", `a ∈ B(r)`, are not verifiable: each is refutable only;
(iii) for a margin `m > 0` and a finite list `𝒰` of upper sets declared in advance, **worse by `m` at `𝒰`**,
`a(U) < r(U) − m` for every `U ∈ 𝒰`, is verifiable. It is a verdict of its own: it does not imply `a ∈ W(r)`, since it
says nothing of the upper sets outside `𝒰`.

**In plain terms.** A record can show that an actor is not an improvement for everyone who holds the ranking, and that
it is not a regression for everyone. It can never show that the actor is worse or equal for everyone: the reference
itself is worse or equal, and behaviours arbitrarily close to it are not, so no finite record separates the two. It can
show a shortfall by a stated margin at standards stated in advance, which is a different verdict.

**Proof.** (i) The complement of a closed set is open in the behaviours, and the open sets are those verifiable in the
statistical sense ([@genin2017], as cited in [D3]); the tests are VE3's, against `B(r)` or `W(r)`. (ii) `W(r)` and
`B(r)` are closed and contain `r`. Every neighbourhood of `r` contains behaviours outside `W(r)`, unless every
behaviour near `r` is in `W(r)`, which fails as soon as some upper set `U` has `0 < r(U) < 1`, by moving a little mass
into `U`; likewise for `B(r)`. A set with a boundary point in it that is not interior is not open, so not verifiable.
(iii) `a ↦ a(U)` is continuous, so the set is cut out by finitely many strict inequalities between continuous functions,
and it is open. ∎

**Notes.** The greedy decoder of `NOTES.md` §22: ten levels, a uniform reference, and an actor that always answers at
level `8`. It meets the standard "level `9`" less often than the reference (`0` against `0.1`), the standards from level
`1` to level `8` more often, and level `0` as often, so it is neither better nor worse (`probes/v14/RESULTS.md`, VO3),
while its average rank is `0.889` against `0.5`. v13's ordinal specification calls it misaligned, and so does the
requirement `B(r)`. Common sense would not; what the decoder lacks is the principal's value scale, under which its
average rank would count, or a declared standard ("at least level 8"), which it meets every time. The verdicts of v14
say this instead of one number: neither better nor worse for every reading, and better under the declared scale or
standard, if one is declared. The executor's proposal is to build the order's requirement from margins: no shortfall
beyond `m` at any declared standard, `a(U) ≥ r(U) − m` for every `U ∈ 𝒰`, a convex closed set whose breach is a
shortfall at some declared standard, verifiable by VF1; (iii)'s "worse by `m` at `𝒰`", short at every one, is a stronger
verdict, not a requirement, since what it leaves acceptable is not convex. So "misaligned" is kept for a breach of a
constraint and for a declared shortfall; under `B(r)` the decoder would be misaligned (the section below). Whether these
are the right words is for L2 to test before anyone adopts them.

## Why dominance is the canonical reading of a ranking

A ranking, read only up to increasing transformations, is all the principal declares; "better" must then mean better for
every principal who holds that ranking, or it adds a commitment the principal did not make. VO1 shows that this is
exactly dominance on upper sets, so dominance is not one order among several but the content of the ranking itself, once
"better" is read as unanimity over the ranking's readings, which is itself a choice. What a ranking does not fix is the
requirement built from it. The verdicts of VO3 are comparisons with the reference, reported as such; to judge
misalignment the principal declares a requirement, and each choice changes verdicts: `B(r)`, "better than the reference
for every reading", which the greedy decoder breaches, so that it is misaligned under that requirement; v13's ordinal
specification, which adds a shape (VO2); or shortfalls by margins at declared standards (VO3(iii)), which it does not
breach. Choosing among them is the PI's (`ROADMAP.md`, recommendation 2). A reference known only from a sample, such as
a base model's answers, is not a set fixed in advance, as [A5] asks, until it is declared as such; how its uncertainty
enters the requirement is open (`LIMITS.md`).
