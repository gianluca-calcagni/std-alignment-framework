---
id: "Prop 32"
type: "proposition"
title: "the ordinal measure; R7-7"
section: "Core 07 Identification, gauge, and the intent ray"
order: 42.6
layer: "measurement"
tier: ["1"]
assumes: []
status: "proved"
depends_on: ["Def 10", "Def 17", "Lemma 5.1"]
mentions: ["R7-7 preregistration", "R7-7 results", "src Barlow 1972", "src Robertson 1988"]
checks: ["V35"]
sources: []
aliases: ["Proposition 32", "Prop. 32"]
updated: "2026-09-26"
---
# Prop 32 — the ordinal measure; R7-7
<!-- gen:header -->
> [!abstract] Proposition · tier 1 · proved · in [[Core 07 Identification, gauge, and the intent ray]]
<!-- /gen:header -->

## Statement

**Proposition 32 (the ordinal measure; R7-7; tier 1).** Let `F` be non-constant, with values `v_1 < … < v_m` on
the level sets `L_1, …, L_m`. Let `p̂` have full support, and `y = p̂/q`. Let `r°` be the `q`-weighted isotonic
(non-decreasing) regression of the level means `p̂(L_j)/q(L_j)`, with weights `q(L_j)`, read as a function of `F`
on `X`. Its **pooled blocks** `B_1, …, B_s` are the unions of consecutive levels on which it is constant. Let
`p° = q·r°`, and `⟨g, h⟩_q = Σ_x q(x)g(x)h(x)`. The measures `M_free` and `M_budget` are those of Def. [[Def 10|10]].

(a) `I_free([F]_ord) = C_F` (Def. [[Def 17|17]]).

(b) `p°` is the unique minimizer of `KL(p̂‖p)` over `C_F`, and

```
M_ord = KL(p̂‖p°) = Σ_i p̂(B_i)·KL( p̂(·|B_i) ‖ q(·|B_i) ).
```

(c) For every `p ∈ C_F`:

```
KL(p̂‖p) = KL(p̂‖p°) + KL(p°‖p) + ⟨r° − y, log(p/q)⟩_q,   the last term ≥ 0.
```

In particular, at `p = q`: `KL(p̂‖q) = M_ord + KL(p°‖q)`.

(d) `M_free ≥ M_ord + M_free(p°)`. Where `M_budget` is defined, at the budget-matched exchange rate `λ`,
`M_budget ≥ M_ord + KL(p°‖p_{F,λ})`.

(e) `C_F`, `p°` and `M_ord` depend on `F` only through the ordered partition `(L_1, …, L_m)`: they are unchanged
by `F ↦ φ∘F` for every strictly increasing `φ`.

(f) `M_budget([F]_ord)` is defined iff `M_budget` is, i.e. iff `KL(p̂‖q) < log 1/q(argmax F)`. Then
`M_ord ≤ M_budget([F]_ord) ≤ M_budget`, and `M_budget([F]_ord) = 0` iff `M_ord = 0`.

## Proof

*Proof.* (a) For `φ` strictly increasing, `p_{φ∘F,t}/q = e^{tφ(F)}/Z` is a non-decreasing function of `F`, so every
half-ray of `[F]_ord` lies in `C_F`, which is closed in `Δ°`. Conversely, let `p ∈ C_F` have level ratios
`r_1 ≤ … ≤ r_m`. If they increase strictly, take a strictly increasing `φ` with `φ(v_j) = log r_j`: then
`p = p_{φ∘F,1}`, because `Σ_x q·e^{φ(F)} = Σ_x q·r = 1`. Otherwise, with `j(x)` the level index of `x`,
`p` is the limit as `ε ↓ 0` of `q·(r + ε·j)/(1 + ε·Σ_x q·j)`, whose level ratios increase strictly.

(c) Let `K` be the convex cone of non-decreasing functions of `F` on `X`; it contains the constants of both
signs. The level means are the `L²(q)` projection of `y` onto the functions of `F`, and `K` lies in that
subspace, so `r°` is the `L²(q)` projection of `y` onto `K`. Hence `⟨y − r°, g⟩_q ≤ 0` for every `g ∈ K`, since `K`
is a cone containing `r°`. Also `⟨y − r°, h⟩_q = 0` for every `h` constant on each pooled block, since
pool-adjacent-violators sets `r°` on a block to the `q`-mean of `y` there. With `h = 1`, `Σ_x q·r° = 1`; and `r° > 0`,
as a mean of positive values. So `p° ∈ C_F`. For `p = q·r ∈ C_F`:
`KL(p̂‖p) − KL(p̂‖p°) − KL(p°‖p) = Σ_x q·(y − r°)·log(r°/r) = ⟨y − r°, log r°⟩_q − ⟨y − r°, log r⟩_q`. The first
term is 0, because `log r°` is constant on each block. The second is `≤ 0`, because `log r ∈ K`. So the remainder
is `−⟨y − r°, log r⟩_q = ⟨r° − y, log(p/q)⟩_q ≥ 0`. At `p = q` it is 0.

(b) By (c), `KL(p̂‖p) ≥ KL(p̂‖p°) + KL(p°‖p)`, and `KL(p°‖p) > 0` unless `p = p°`. On a block `B`,
`p°(B) = q(B)·(the q-mean of y on B) = p̂(B)` and `p°(·|B) = q(·|B)`. The chain rule for KL over the partition into
blocks gives the sum.

(d) Every `p_{F,t}` with `t ≥ 0` lies in `C_F`. Apply (c) to `p = p_{F,t}` and take the infimum over `t ≥ 0`; or apply
it to `p = p_{F,λ}`.

(e) `C_F` is defined by the ordered partition, and so are the level means, their weights and the regression.

(f) For `p = q·r ∈ C_F`, `r` is largest on the top level, so `q(argmax F)·max r ≤ Σ_x q·r = 1`. Hence
`KL(p‖q) = Σ_x p·log r ≤ log max r ≤ log 1/q(argmax F)`, with equality only for a distribution supported on
`argmax F`, which is not in `Δ°`. So `I_budget([F]_ord)` is empty when `KL(p̂‖q) ≥ log 1/q(argmax F)`. Below that
value, `p_{F,λ}` lies on the budget sphere (Lemma [[Lemma 5.1|5.1]]) and in `C_F`. Since
`{p_{F,λ}} ⊆ I_budget([F]_ord) ⊆ C_F`, (b) gives the two inequalities. The infimum defining `M_budget([F]_ord)` is
attained: `KL(p̂‖p) → ∞` as `p` approaches the boundary of the simplex, so its sublevel sets in the closed set
`I_budget([F]_ord)` are compact. Hence `M_budget([F]_ord) = 0` iff `p̂ ∈ I_budget([F]_ord)`. As `p̂` lies on its own
budget sphere, this holds iff `p̂ ∈ C_F`, that is, by (b), iff `M_ord = 0`. ∎

## Notes and checks

*Check.* [[V35]] (1,200 instances, 610 with tied levels; pre-registered, [[R7-7 preregistration]]):
- (b): a generic constrained optimizer never beats the isotonic value by more than `3.3·10⁻¹⁵`; the block
  formula holds to `7·10⁻¹⁶`.
- (c): the cross term is never below `−1.1·10⁻¹⁵` over 20 random members of `C_F` per instance; the split
  `KL(p̂‖q) = M_ord + KL(p°‖q)` holds to `9·10⁻¹⁶`.
- (d): the smallest slack is `−7·10⁻¹⁵` (free) and `−3·10⁻¹⁶` (budget).
- (e): `M_ord` is unchanged, to the last bit, under a random strictly increasing map.
- (f): `M_ord ≤ M_budget([F]_ord) ≤ M_budget` holds on the 1,123 instances where the budget measure is defined,
  within the solver's tolerance.

*Failed as registered (P8).* The pre-registration also claimed that the first inequality of (f) is strict when
`M_ord > 0`, tested as a gap above `10⁻¹²` whenever `M_ord > 10⁻⁹`. Four instances failed, all with `M_ord` below
`3·10⁻⁷`. Under the registered rule D2 the strict claim is withdrawn from the statement. The diagnosis is in
[[R7-7 results]]: the gap is second order in `M_ord` (the median of `gap/M_ord²` is 0.9–1.8 wherever the gap can be
resolved), so it falls below double-precision noise when `M_ord` is small. Stating strictness again needs a
check designed from that scaling.

*Reading.* **The ordinal measure charges only what no reading of the target's order can justify.** On each
pooled block, the ordinal intent is indifferent, so the intended behaviour follows the declared reference there.
`M_ord` is the divergence from the reference inside the blocks. The budget split in (c) says that the
information `p̂` spends divides exactly into the ordinal misalignment and what its ordinal projection spends.
(d) says that the cardinal measures charge the ordinal misalignment plus a **shape** term: how far the ordinal
projection lies from the target's own half-ray. Shape counts as misalignment only under a cardinal declaration.

*Prior art.* Order-restricted inference: the isotonic regression and the KL projection onto a monotone cone
([[src Barlow 1972]], [[src Robertson 1988]]). What is new here is its use as a misalignment measure against the contract.

<!-- gen:links -->
## Depends on (logical: statement and proof)
- [[Def 10]] — intent ray and misalignment measures; v6.4, R7-0
- [[Def 17]] — target sets; R7-7
- [[Lemma 5.1]] — form of the capacity actor

## Used by
- [[Prop 34]] — the core as a declared intended set; R7-9

## Mentions
- [[R7-7 preregistration]]
- [[R7-7 results]]
- [[src Barlow 1972]]
- [[src Robertson 1988]]

## Mentioned in
- [[Def 8]] — conventions, misalignment, ε-alignment; revised in R7-0
- [[Def 17]] — target sets; R7-7
- [[Prop 31]] — target sets against the contract; R7-7

## Checks
- [[V35]]

## Sources
- none

## Retractions touching this note
- none
<!-- /gen:links -->
