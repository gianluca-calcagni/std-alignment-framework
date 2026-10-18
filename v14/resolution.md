# What each side can tell apart: σ-algebras

> **Status: draft of v14 (Q69); proved here, not yet checked in CI.** The numbers come from `probes/v14/resolution.py`,
> as run once (`probes/v14/RESULTS-resolution.md`), and the example's from `probes/slides/qa_model.py`.

Three parties tell outcomes apart, each in its own way: the principal, who may not care how some outcomes differ; the
record, which shows only what its instrument, a grader or a log, distinguishes; and the actor, which may not see what
situation it is in or may not control which of several outcomes occurs. Each of them is a σ-algebra. On finitely many
outcomes a σ-algebra is the same thing as a partition into **cells** ([D4]), so this file works with partitions.

The PI asked that the role of σ-algebras be explained, and their effect on misalignment factored properly (Q69). v13
used one object, the resolution, in two positions, the principal's and the actor's ([D4], [P7], [P8]). v14 adds the
third, the record's, and gives each position its own exact factorization. In short:
- *the principal's* σ-algebra says what matters: a requirement stated on it is judged entirely there (RS3);
- *the record's* says what is seen: misalignment splits exactly into what a record at that σ-algebra can detect and what
  it hides, and the hidden part is neither verifiable nor refutable from that record (RS1, RS2, RS4);
- *the actor's*, on conditions (its view) and on outcomes (its resolution), says what it can do; both are linear
  interfaces, so their costs are exact terms of `factorization.md`'s FA1, Pythagorean under FA2 (RS5).

Notation as in `evidence.md`. For a partition `𝒢` of `X` and `p ∈ Δ`, `p_𝒢` is the behaviour on cells, `p_𝒢(C) =
p(C)`. `𝒢 ⊑ ℋ` says that `ℋ` **refines** `𝒢`: every cell of `ℋ` lies in a cell of `𝒢`; the finest partition, one
outcome per cell, refines every other. For a set `A ⊆ Δ`, `A_𝒢 = {a_𝒢 : a ∈ A}`, and the **misalignment at resolution
`𝒢`** is `M_A^𝒢(p) = inf_{a∈A} KL(p_𝒢‖a_𝒢)`, the misalignment of the cell masses against the cell masses of the
acceptable behaviours; at the finest partition it is `M_A(p)`. With conditions, by [B2], `X` holds the pairs of a
condition and an outcome, with the conditions' frequencies fixed, and a σ-algebra of the record that sees the
conditions has cells inside each condition.

### RS1 — A coarser record shows less, and refinement adds up exactly
**Statement.** Let `A ⊆ Δ` be non-empty and `p ∈ Δ`.
(i) If `𝒢 ⊑ ℋ`, then `KL(p_𝒢‖a_𝒢) ≤ KL(p_ℋ‖a_ℋ)` for every `a ∈ Δ`, so `M_A^𝒢(p) ≤ M_A^ℋ(p)`.
(ii) For a chain `𝒢_1 ⊑ 𝒢_2 ⊑ … ⊑ 𝒢_k`, with `𝒢_k` the finest partition and `M_A(p) < ∞`,
`M_A(p) = M_A^{𝒢_1}(p) + Σ_{j=1}^{k−1} (M_A^{𝒢_{j+1}}(p) − M_A^{𝒢_j}(p))`, and every term is non-negative.

**In plain terms.** A record that lumps outcomes together can only show less misalignment than one that tells them
apart. Refine the record one step at a time: each step reveals a non-negative amount, and the amounts add up exactly to
the misalignment.

**Proof.** (i) Group the cells of `ℋ` by the cells of `𝒢` that contain them. The chain rule on finite sums ([P4](iii))
gives `KL(p_ℋ‖a_ℋ) = KL(p_𝒢‖a_𝒢) + Σ_{C∈𝒢, p(C)>0} p(C)·KL(p_ℋ(·|C)‖a_ℋ(·|C))`, where `p_ℋ(·|C)` is the behaviour of
`p` on the cells of `ℋ` inside `C`, and a term with `a(C) = 0 < p(C)` makes both sides infinite. The sum is
non-negative. Take the infimum over `a ∈ A` on both sides. (ii) The sum telescopes, the last term being `M_A^{𝒢_k} =
M_A`; each term is non-negative by (i). ∎

**Notes.** This is the data-processing inequality for KL, here for a deterministic grouping, and v13's [C9], "grouping
never shows more", carried to any acceptable set. It is the record's counterpart of FA1: FA1 telescopes along a chain
of feasible sets, RS1 along a chain of σ-algebras. On 40 random instances (six outcomes, two budgets, three nested
partitions) the least increment is `0` within `2e-15` (`RESULTS-resolution.md`).

### RS2 — What a coarse record can bet on
**Statement.** Let `A` be convex and closed, `ℛ` a partition, and `p ∈ Δ`. A bet against `A` that is constant on the
cells of `ℛ`, a bet that a record at resolution `ℛ` can settle, grows under `p` at most at `M_A^ℛ(p)`; when `M_A^ℛ(p)`
is finite, one of them grows at exactly that rate: `h = k` on each cell, with `k = p_ℛ/a*_ℛ` for an acceptable `a*`
whose cell masses are nearest to `p_ℛ`; and when it is infinite, such bets grow at any rate.

**In plain terms.** A record that sees only cells can only bet on cells. The fastest its bets can grow is exactly the
misalignment at its resolution, so VE3's test from bets works at the record's resolution, with no model of what happens
inside the cells, and convicts at that rate and no faster.

**Proof.** A function `h` constant on cells is `k(C)` on each cell `C`, and for every `a ∈ Δ`, `E_a[h] = E_{a_ℛ}[k]`
and `E_p[log h] = E_{p_ℛ}[log k]`. So `h` is a bet against `A` exactly when `k` is a bet against `A_ℛ`, on the cells.
`A_ℛ` is the image of the compact convex set `A` by the linear map `a ↦ a_ℛ`, so it is compact and convex, and
`M_{A_ℛ}(p_ℛ) = M_A^ℛ(p)`. VE1 on the cells gives the rest. ∎

**Notes.** On the 40 instances of RS1, the bet built from the coarse nearest behaviour costs at most `1` under every
acceptable behaviour, to within `1e-6` (a linear program over `A`), and grows at the coarse misalignment to machine
precision (`RESULTS-resolution.md`).

### RS3 — Indifference: a requirement stated on the principal's σ-algebra is judged there
**Statement.** A set `A ⊆ Δ` is **stated at** a partition `ℬ` if whether `a ∈ A` depends only on `a_ℬ`. Then for every
`p ∈ Δ` and every `ℋ` that refines `ℬ`, `M_A^ℋ(p) = M_A^ℬ(p)`; in particular `M_A(p) = M_A^ℬ(p)`. A nearest acceptable
behaviour, when one exists, can be chosen to split each cell of `ℬ` as `p` does.

**In plain terms.** When the principal declares that it does not care how outcomes inside a cell differ, misalignment
depends only on how often each cell occurs: telling apart what the principal does not care about reveals nothing.

**Proof.** `M_A^ℬ ≤ M_A^ℋ ≤ M_A` by RS1(i), so it suffices that `M_A(p) ≤ M_A^ℬ(p)`. For `a' ∈ A`, let `a` give each
cell `C` of `ℬ` the mass `a'(C)`, split as `p` splits it when `p(C) > 0` and as `a'` does otherwise. Then `a_ℬ = a'_ℬ`,
so `a ∈ A`, and the chain rule gives `KL(p‖a) = KL(p_ℬ‖a'_ℬ)`, every within-cell term being `0`. Take the infimum over
`a'`; the construction applied to a minimizer gives the last sentence. ∎

**Notes.** This is v13's [P7](i), now with no default and no requirement of full support. On 40 random instances with
budgets whose costs are constant on the cells of a partition, the misalignment and the misalignment at that partition
agree within `1e-13` (`RESULTS-resolution.md`). Indifference is declared, never assumed ([D4]): a principal who declared
a coarse σ-algebra to hide a distinction it cares about has misspecified its specification, which no record can show
(`LIMITS.md`).

### RS4 — What a coarse record leaves open: hidden misalignment
**Statement.** Let `A ⊆ Δ` be closed and non-empty, `ℛ` a partition, `p ∈ Δ`, and `𝒫 = {p' ∈ Δ : p'_ℛ = p_ℛ}`, the
behaviours a record at resolution `ℛ` cannot tell from `p`. Call `H_ℛ(p) = M_A(p) − M_A^ℛ(p) ≥ 0` the misalignment
**hidden** from `ℛ`.
(i) A sample at resolution `ℛ`, independent decisions of which the record shows only the cell, has a law that depends
on the actor's behaviour only through `p_ℛ`.
(ii) `min_{p'∈𝒫} M_A(p') = M_A^ℛ(p)`, attained, when it is finite, by the behaviour that gives each cell `p`'s mass and
splits it as a nearest acceptable `a*` of the cell masses does.
(iii) So `M_A(p)` lies in `[M_A^ℛ(p), sup_{p'∈𝒫} M_A(p')]`, the lower end attained in `𝒫`, and neither end can be
narrowed by samples at resolution `ℛ`. The statement "`H_ℛ > 0`", as a set of behaviours, is neither verifiable nor
refutable from such samples whenever it splits some fibre `𝒫`, that is, whenever `M_A` is not constant on it. When `A`
is convex, the supremum is a maximum over the vertices of `𝒫`, the behaviours that put each cell's mass on one outcome
of the cell.
(iv) A declared feasible set `𝓕 ∋ p` narrows the interval to `[min_{𝒫∩𝓕} M_A, sup_{𝒫∩𝓕} M_A]`, by what the interface
says the actor can do inside cells.

**In plain terms.** From a record that lumps outcomes together, the least the actor can be charged is the misalignment
visible at that grouping, and the record cannot rule out that this is all; whatever more there is, hidden inside the
cells, no test of that record can detect, and no test of it can clear. Bounding it needs a declaration of what the
actor can do inside cells, or a finer record.

**Proof.** (i) Each decision's cell has law `p_ℛ`, and independent decisions give the product. (ii) Every `p' ∈ 𝒫` has
`M_A(p') ≥ M_A^ℛ(p') = M_A^ℛ(p)` by RS1(i). If `M_A^ℛ(p) < ∞`, `A_ℛ` is compact and `KL(p_ℛ‖·)` lower semicontinuous, so
some `a* ∈ A` attains it, with `a*(C) > 0` wherever `p(C) > 0`. Let `p'` give such a cell `C` the mass `p(C)`, split as
`a*(·|C)`, and the other cells nothing. Then `p' ∈ 𝒫`, and by the chain rule `KL(p'‖a*) = KL(p_ℛ‖a*_ℛ) = M_A^ℛ(p)`.
(iii) Both ends are values of `M_A` on `𝒫`. A test that is a function of a sample at resolution `ℛ` has, by (i), the
same law under every `p' ∈ 𝒫`; under the `p'` of (ii), `H_ℛ(p') = 0`, so a test that declares "`H_ℛ > 0`" with
probability at most `α` there declares it with probability at most `α` everywhere in `𝒫`, and symmetrically for any
`p''` with `H_ℛ(p'') > 0`. When `A` is convex, `M_A` is convex, as an infimum over `a ∈ A` of the jointly convex `KL`,
and `𝒫` is a polytope, the product over cells of the behaviours with given cell masses, so a supremum is approached at
its vertices; it is a maximum, `M_A` being lower semicontinuous and `𝒫` having finitely many vertices.
(iv) The same argument on `𝒫 ∩ 𝓕`. ∎

**Notes.** On the 40 instances of RS1, the split of (ii) has misalignment equal to the coarse one within `1e-13`, while
random splits of the same coarse masses hide up to `0.29` nats per decision more, `0.03` at the median
(`RESULTS-resolution.md`). In the example of `slides/mathematicians.md`, a grader that cannot tell a wrong answer from a
harmful one sees none of a requirement on harmful answers. This is v13's hidden misalignment ([D9], [P17]) across
outcomes instead of across conditions, and the reason a report states the σ-algebra of its record.

### RS5 — The actor's σ-algebras are linear interfaces
**Statement.** (i) *A view.* Let `𝒱` be a partition of the conditions, and an actor whose decision depends on the
condition only through its cell of `𝒱`, with the outcome its own choice. Its feasible behaviours, on pairs with the
conditions' frequencies `w` fixed, are `{p : p(·|c) = p(·|c')` whenever `c` and `c'` share a cell of `𝒱}`, a linear set
([D7]) that contains a full-support behaviour.
(ii) *A resolution.* Let `𝒜` be a partition of the outcomes and `e(·|A)`, for each cell `A`, a full-support split of the
cell fixed by the environment. An actor that chooses only how often each cell occurs has the feasible behaviours
`{p : p(x) = p(A)·e(x|A)` for `x ∈ A}`, a linear set that contains a full-support behaviour.
(iii) Coarsening a view shrinks the feasible set. Coarsening a resolution does too when the environment's splits are
consistent, `e(x|A) = e(A_i|A)·e(x|A_i)` for `x` in a cell `A_i` of the finer partition inside `A`, as when every split
is the restriction of one full-support `e` on `X`; without consistency the coarse set need not lie in the fine one. So a
chain of views, or of resolutions with consistent splits, is a chain of linear feasible sets: the cost of each
coarsening is a term of FA1, and FA2 and FA3 give their Pythagorean forms under their hypotheses.

**In plain terms.** An actor that cannot tell some situations apart must act alike in them; one that cannot tell some
outcomes apart can only choose how often each group happens. Both are limits of the form "these averages are fixed", so
what each costs is an exact term of the factorization of misalignment, and, toward a fixed target, a divergence between
named behaviours.

**Proof.** (i) `p(x|c) = p(x|c')` is `p(c, x)/w_c − p(c', x)/w_{c'} = 0`, a linear equality, for every `x` and every
pair in one cell; the uniform choice in every condition is feasible and has full support. (ii)
`p(x)·e(y|A) − p(y)·e(x|A) = 0` for `x, y ∈ A`, linear equalities; the cell masses are free, so taking them positive
gives full support. (iii) A coarser view adds equalities. For resolutions, `p(x) = p(A)·e(x|A) = p(A)·e(A_i|A)·e(x|A_i)`
with consistent splits, so `p(A_i) = p(A)·e(A_i|A)` and `p(x) = p(A_i)·e(x|A_i)`: `p` is feasible for the finer
resolution. Without consistency, four outcomes with fine cells `{0, 1}`, `{2, 3}` split evenly and one coarse cell split
`(0.7, 0.1, 0.1, 0.1)` give a coarse behaviour, that split itself, which the fine resolution cannot produce. FA1 needs
nothing more; FA2 and FA3 need linear sets with a full-support member. ∎

**Notes.** (i) assumes the actor chooses the outcome, the environment being the identity; with an environment kernel,
the feasible set is the image of the policies, a polytope in general, so FA1 applies and FA2 does not
(`factorization.md`). The actor's resolution is v13's [D4] in its second position, with the default's split replaced by
the environment's, and [P8] its best effort. On three conditions with the actor choosing among three outcomes and a
budget whose cheapest outcome differs by condition, the least misalignment is `0` with a full view, `0.190` with a view
that merges two conditions, and `0.990` with no view; an actor that sees nothing has
`7.149 = 0 + 0.190 + 0.800 + 6.159`, the last term avoidable (`RESULTS-resolution.md`). The example's is in
`slides/mathematicians.md`.

### RS6 — An actor at least as fine as the principal loses nothing to resolution
**Statement.** Let `A` be stated at a partition `ℬ` (RS3), and let an actor have the resolution `𝒜` with full-support
splits `e(·|A)` (RS5(ii)), feasible set `𝓕_𝒜`. If `𝒜` refines `ℬ`, then `M_A(𝓕_𝒜) = M_A(Δ)`: its resolution costs
nothing. If `𝒜` does not refine `ℬ`, the cost `M_A(𝓕_𝒜) − M_A(Δ)` can be positive: it is the misalignment due to
**missing resolution**, a term of FA1 when the splits are consistent.

**In plain terms.** An actor that can tell apart everything the principal cares about can meet any specification that
an actor seeing everything could meet. Only when it cannot tell apart two outcomes the principal treats differently
does its resolution cost misalignment, and that cost is a factor of its own.

**Proof.** For any `f ∈ Δ`, let `p` give each cell `A` of `𝒜` the mass `f(A)`, split by `e(·|A)`; then `p ∈ 𝓕_𝒜`. Each
cell of `ℬ` is a union of cells of `𝒜`, so `p_ℬ = f_ℬ`, and RS3 gives `M_A(p) = M_A^ℬ(p) = M_A^ℬ(f) = M_A(f)`. So
`M_A(𝓕_𝒜) ≤ M_A(Δ)`, and the converse holds since `𝓕_𝒜 ⊆ Δ`. For the second sentence: two outcomes in one cell of `𝒜`,
split evenly, and a principal who forbids one of them and accepts the other: every feasible behaviour that uses the
cell breaks the requirement, while the actor that sees both need not. ∎

### RS7 — Latitude: what the actor does where the specification is silent (a proposal)
**Definition, proposed.** Let `ℬ` be the principal's partition and `r ∈ Δ°` a declared reference. The **latitude taken**
by a behaviour `p̂` is `L_r(p̂) = Σ_{C∈ℬ, p̂(C)>0} p̂(C)·KL(p̂(·|C)‖r(·|C))`, the divergence of its splits inside the
principal's cells from the reference's.

**Statement.** (i) `L_r(p̂) = KL(p̂‖r) − KL(p̂_ℬ‖r_ℬ) ≥ 0`, with equality exactly when `p̂` splits every cell of `ℬ` it
charges as `r` does. (ii) For a specification stated at `ℬ`, behaviours with the same cell masses have the same
misalignment and may have any latitude: latitude never changes a verdict. (iii) `L_r` is continuous on `Δ`, so
"`L_r > l`" is verifiable from records at any partition that refines `ℬ` and resolves the outcomes inside its cells,
and, like hidden misalignment, untestable from records at a partition no finer than `ℬ`. (iv) For an actor of resolution
`𝒜` with splits `e`, and a reference that splits each cell of `𝒜` as `e` does, `L_r(p̂) = KL(p̂_𝒜‖r_𝒜) − KL(p̂_ℬ‖r_ℬ)`
for every feasible `p̂`; it is `0` for every feasible behaviour when `ℬ` refines `𝒜`. Only distinctions finer than the
principal's give latitude.

**In plain terms.** Where the principal has said it does not care, an actor that can tell more apart may still choose:
answer long or short, use one tool or another. Those choices break nothing declared, but the principal did not foresee
them, and a large latitude says the specification may be silent where the principal would not be. It is a signal to
revise the specification for the next record, never a verdict on this one.

**Proof.** (i) The chain rule on the cells of `ℬ`; a KL divergence is `0` exactly when its arguments agree, and `r(C) >
0` makes every conditional defined. (ii) RS3. (iii) `r ∈ Δ°` makes `KL(·‖r)` and `KL(·_ℬ‖r_ℬ)` continuous, so the set
`{L_r > l}` is open (VF1); two behaviours with the same cell masses of a partition no finer than `ℬ`, one split as `r`
and one not, have the same law of such records. (iv) Inside each cell of `𝒜` both `p̂` and `r` split as `e`, so
`KL(p̂‖r) = KL(p̂_𝒜‖r_𝒜)` by the chain rule; when `ℬ` refines `𝒜`, `p̂_ℬ` and `r_ℬ` split the cells of `𝒜` as `e` too,
so `KL(p̂_ℬ‖r_ℬ) = KL(p̂_𝒜‖r_𝒜)`. ∎

**Notes.** This is v13's within-cell departure ([P7](ii)) with a reference in place of the default, and v7.10's
underdetermination (G1, [D4]'s reasons) given a number. The PI suggested "deviance" or "miscalibration"; the executor
proposes **latitude** because both have fixed meanings in statistics, deviance being twice a log-likelihood ratio
against a saturated model and miscalibration a forecast whose probabilities disagree with frequencies. Its interplay
with declarations: it needs a declared reference and the principal's partition; found on a record, it is exploratory
for that record ([A5]) and can only motivate a specification declared before the next one (`NOTES.md` §33). No probe:
the proofs leave nothing to compute.

## The three positions together

The two factorizations below are of the same number, `M_A(p̂)`, by different chains.
- *What is seen*, along σ-algebras of the record (RS1): `M_A(p̂) = M_A^ℛ(p̂) + H_ℛ(p̂)`, the misalignment a record at
  `ℛ` can detect plus the hidden part; when the record's partition is coarser than the principal's, `ℛ ⊑ ℬ`, as for a
  grader whose classes merge the
principal's, `M_A^ℛ + (M_A^ℬ − M_A^ℛ) + 0` (RS3); in general the two partitions need not be ordered.
- *What could be done*, along interfaces (FA1, RS5): `M_A(p̂) = m_full + Σ_j (m_{j+1} − m_j) + E(p̂)`, with a term for
  each coarsening of the actor's view or resolution.

**Verification status of the labels** (VF1, VF2), for an acceptable set `A` that is convex, closed and has a
full-support member, as rate limits with `ε > 0`, budgets with `b > min g` and dominance sets do. Then every `M_A^𝒢` is
continuous: it is finite, being at most the divergence to that member; lower semicontinuous, as `evidence.md`'s VE1
uses; and convex, so for `x_n → x`, writing `x_n = (1 − t_n)·x + t_n·y_n` with `t_n = ‖x_n − x‖_∞/min_{x(i)>0} x(i) →
0` and `y_n` a behaviour, `M(x_n) ≤ (1 − t_n)·M(x) + t_n·max_Δ M`, the maximum of a convex function on the simplex being
at a vertex and finite; so it is upper semicontinuous too. The same holds on pairs with the conditions' frequencies
fixed.

| Label | Statement | Status |
|---|---|---|
| misaligned, as far as a record at `ℛ` shows | `M_A^ℛ(p̂) > 0` | verifiable from records at `ℛ` (RS2, VE3) |
| refining from `𝒢_j` to `𝒢_{j+1}` reveals misalignment | `M_A^{𝒢_{j+1}}(p̂) > M_A^{𝒢_j}(p̂)` | verifiable from records at `𝒢_{j+1}`: the set is open, both sides continuous |
| misalignment hidden from `ℛ` | `H_ℛ(p̂) > 0` | neither verifiable nor refutable from records at `ℛ` (RS4) |
| the principal does not care inside the cells of `ℬ` | `A` stated at `ℬ` | declared; not about the record |
| the actor cannot tell `c` from `c'` | its consequence, `p̂(·|c) = p̂(·|c')`; the claim about capability needs elicitation (VF3) | the consequence refutable (VF2) |
| the cost of a coarse view or resolution | `m_{j+1} − m_j > 0` | computed from the declarations (VF2) |

With a forbidden set the functions are only lower semicontinuous, and the second row is not shown.
