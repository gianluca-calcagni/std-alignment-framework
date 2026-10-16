# Evidence as a bet

> **Status: draft of v14 (Q59); proved here, not yet checked in CI.** The numbers come from `probes/v14/v14_probe.py`.

v13's [A4] defines misalignment as the rate at which a record's counts become improbable under every accepted
behaviour, and [D3] computes it as the least divergence from the actual behaviour to an accepted one. This file gives
the same number a second reading, which needs no counts, no independence and no bins: the best long-run growth rate of
a bet against acceptability. It then draws three consequences: what a record can hold an actor to, a test that keeps
its level whatever the dependence between decisions, and how a bet's average is estimated.

Throughout, `X` is a finite set of outcomes, `Δ` the behaviours on it, `KL` the divergence of [D1], with `log 0 = −∞`,
and `A ⊆ Δ` a non-empty set of acceptable behaviours. `M_A(p) = inf_{a∈A} KL(p‖a)`. A **bet against `A`** is a function
`h : X → [0, ∞)` with `E_a[h] ≤ 1` for every `a ∈ A`: a ticket that pays `h(x)` for each unit staked, and that no
acceptable behaviour expects to pay more than its price. Its **growth rate** under `p` is `E_p[log h]`.

### VE1 — Misalignment against a convex set is the growth rate of the best bet
**Statement.** Let `A` be convex and closed, and `p ∈ Δ`.
(i) For every bet `h` against `A`, `E_p[log h] ≤ M_A(p)`.
(ii) If `M_A(p) < ∞`, the minimum is attained at some `a* ∈ A`, and `h* = p/a*` on the support of `p`, `0` elsewhere,
is a bet against `A` with `E_p[log h*] = M_A(p)`.
(iii) If `M_A(p) = ∞`, there are bets whose growth rate under `p` exceeds any number.
(iv) If `A` is convex but not closed, `M_A(p) = M_{cl A}(p)`, and the bets against `A` are those against its closure
`cl A`, which is convex; so (i) and (iii) hold for `A`, and the maximum of (ii) is attained in `cl A`, possibly outside
`A`. So `M_A(p) = sup_h E_p[log h]` over the bets against `A`, a maximum when it is finite.

**In plain terms.** Bet against the principal's standard, with tickets that the standard itself says are fair or worse.
If the actor really is acceptable, no such bet grows on average. If it is not, the fastest any of them can grow is
exactly its misalignment, and the best ticket pays the ratio of what the actor does to the nearest acceptable behaviour.

**Proof.** (i) Let `a ∈ A` and `S` the support of `p`. If `KL(p‖a) = ∞` there is nothing to prove; otherwise `a > 0` on
`S`. If `h = 0` somewhere on `S`, `E_p[log h] = −∞`. Otherwise, by Jensen's inequality for the concave logarithm,
`E_p[log h] − KL(p‖a) = E_p[log(h·a/p)] ≤ log E_p[h·a/p] = log Σ_{x∈S} h(x)·a(x) ≤ log E_a[h] ≤ 0`. Take the infimum
over `a`.
(ii) `KL(p‖·)` is lower semicontinuous on the compact set `A` (`general/transfer.md`, fact (b)), so its minimum is
attained, at some `a*` with `a* > 0` on `S`. For `a ∈ A` and `s ∈ [0, 1)`, `a_s = a* + s·(a − a*)` lies in `A`, by
convexity, and `a_s ≥ (1 − s)·a* > 0` on `S`, so `φ(s) = KL(p‖a_s) = Σ_{x∈S} p(x)·log(p(x)/a_s(x))` is finite and
differentiable on `[0, 1)`, with `φ(s) ≥ φ(0)`. Hence
`0 ≤ φ'(0+) = −Σ_{x∈S} p(x)·(a(x) − a*(x))/a*(x) = 1 − Σ_{x∈S} a(x)·p(x)/a*(x) = 1 − E_a[h*]`. So `h*` is a bet, and
`E_p[log h*] = Σ_{x∈S} p(x)·log(p(x)/a*(x)) = KL(p‖a*) = M_A(p)`.
(iii) If every `x ∈ S` had some `a_x ∈ A` with `a_x(x) > 0`, their average would lie in `A`, by convexity, and be
positive on `S`, so `M_A(p)` would be finite. So some `x₀ ∈ S` has `a(x₀) = 0` for every `a ∈ A`. For `H > 1`, the
function `h = 1` off `x₀` and `h(x₀) = H` is a bet, since `E_a[h] = 1 − a(x₀) = 1`, and `E_p[log h] = p(x₀)·log H`.
(iv) `a ↦ E_a[h]` is continuous, so a bet against `A` is one against `cl A`, and conversely since `A ⊆ cl A`.
`M_{cl A}(p) ≤ M_A(p)` since `A ⊆ cl A`. Conversely, let `a ∈ cl A` with `KL(p‖a) < ∞`, so `a > 0` on the support of
`p`, and `a_n ∈ A` with `a_n → a`; `KL(p‖·)` is a finite sum of continuous terms near `a`, so `KL(p‖a_n) → KL(p‖a)`, and
`M_A(p) ≤ KL(p‖a)`. The closure of a convex set is convex. ∎

**Notes.** Read in an open text: Grünwald, de Heide and Koolen ([@grunwald2023], Theorem 1) prove a general form, on any
sample space, for a null hypothesis given as all mixtures of a family, when the actor's behaviour has full support and
its misalignment is finite; the optimal bet is there "the growth-rate-optimal e-variable", the nearest behaviour "the
reverse information projection", and a bet an "e-variable". The proof above is the finite case, self-contained. By (iv),
VE1 covers v13's convex specifications, which are closed in `Δ°` but not always in `Δ`, such as the ordinal one: there
v14's number is v13's. A forbidden set (`constraints.md`) has no counterpart in v13, which asked intended behaviours to
have full support. Checked on 300 random instances of v13's ordinal specification, 104 of them with outcomes the actor
never uses: `h*` costs at most `1` under each extreme point of the specification, to within `5e-16`, which by (i) is
what makes it the best bet (`probes/v14/RESULTS.md`, VE1); its growth rate equals `KL(p‖a*)` by definition.

### VE2 — Records hold an actor to the convex hull
**Statement.** Let `A` be closed, not necessarily convex, and `conv A` its convex hull.
(i) The bets against `A` are exactly the bets against `conv A`, so the best growth rate against `A` is `M_{conv A}(p)`,
which may be smaller than `M_A(p)`.
(ii) If decisions are independent and decision `i` is drawn from some `a_i ∈ A`, the shares of `n` decisions are within
`ε` of the average `ā_n = (1/n)·Σ a_i`, outcome by outcome, with probability at least `1 − |X|/(4·n·ε²)`; and
`ā_n ∈ conv A`.

**In plain terms.** If acting one acceptable way at some decisions and another at others is fine, the shares a record
shows are those of a mixture of acceptable behaviours. Judged by its shares, or by bets against what is acceptable, such
an actor cannot be held to anything stricter than the mixtures. The order of the decisions may still reveal a fixed
schedule, but nothing acceptable is breached by one.

**Proof.** (i) `a ↦ E_a[h]` is affine, so `E_a[h] ≤ 1` on `A` implies it on every mixture of points of `A`; the
converse holds since `A ⊆ conv A`. `conv A` is compact, as the convex hull of a compact set in finite dimension, so VE1
applies to it. (ii) The count of `x` is a sum of independent indicators with averages `a_i(x)` and variances at most
`1/4`; by Chebyshev's inequality ([M2]'s argument) its share is within `ε` of `ā_n(x)` except with probability at most
`1/(4·n·ε²)`; add over `x`. ∎

**Notes.** v13's standard specification, the pursuit ray, is not convex. An actor that at each decision pursues `F` at
intensity `0` or `3`, each with probability ½, on four outcomes with a uniform default and `F = (0, 1, 2, 3)`, acts
acceptably at every decision; v13 charges it `0.0546` nats per decision, and [P55]'s count test against the ray accuses
it in 68.9% of 2,000 records of 400 decisions at level 5%, while a test against the ordinal specification, which is
convex and contains the ray's hull, accuses it in none from counts, and in 1.9% from bets (`probes/v14/RESULTS.md`,
VE2). The lesson for v14: acceptable sets are convex, by a principle stated as such (`README.md`).

### VE3 — A test from bets keeps its level whatever the dependence
**Statement.** Decisions `1, 2, …, n` are made in turn, each in one of finitely many contexts. Before decision `i`, an
acceptable set `A_i` is fixed by the context, and a bet `h_i` against `A_i` is chosen; both may depend on everything
before decision `i`. The **wealth** after `k` decisions is `W_k = Π_{i≤k} h_i(x_i)`, with `W_0 = 1`. If, given
everything before it, each decision is drawn from some behaviour in `A_i`, then for every `α ∈ (0, 1]`, the probability
that `W_k ≥ 1/α` for some `k ≤ n` is at most `α`.

**In plain terms.** Keep betting against the standard, one decision at a time, changing the bet as you learn. If the
actor acts acceptably at every step, given what came before, the chance that your wealth ever reaches `20` is at most
`1/20`, however the actor's decisions depend on each other and however you chose your bets. A large wealth is evidence
of misalignment that needs no assumption of independence.

**Proof.** With finitely many outcomes, contexts and decisions, every expectation below is a finite sum. Given the
past, decision `k` is drawn from some `a ∈ A_k`, so the conditional expectation of `W_k` is `W_{k−1}·E_a[h_k] ≤
W_{k−1}`. Let `τ` be the first `k ≤ n` with `W_k ≥ 1/α`, or `n` if there is none. Whether `τ ≥ k` is decided before
decision `k`, so `E[W_{min(τ,k)} − W_{min(τ,k−1)}] = E[1{τ ≥ k}·(W_k − W_{k−1})] ≤ 0`, and `E[W_τ] ≤ W_0 = 1`. The
event that some `W_k ≥ 1/α` is the event `W_τ ≥ 1/α`, whose probability is at most `α·E[W_τ] ≤ α` by Markov's
inequality. ∎

**Notes.** This is Ville's inequality on a finite horizon, proved here from finite sums; [@grunwald2023], Corollary 1,
states it for bets and cites Ville (1939), not read here. What changes from v13. [P55]'s exact test assumes that
accepted behaviours decide independently, a convention of v13's table, and an actor whose decisions depend on each other
may be accused for that alone ([P55], Notes). Here the hypothesis is stated instead of assumed: the level holds for
every actor that is acceptable at every step given its past, and an actor that is not, such as one that copies its first
decision when the principal accepts only independent fair coins, is accused because it is not, which is what the
declaration asked. In the probe, an actor that pursues `F` at intensity `8` right after the best outcome and at `0`
otherwise, so that its decisions depend on each other while each is acceptable under the ordinal specification, is
accused by the bet against that specification in 1.2% of 2,000 records at level 5%, as VE3 guarantees, and by [P55]'s
count test against it in none; this instance does not show the count test failing under dependence, and its 15.7%
against the ray is the ray's lack of convexity (VE2), not dependence (`probes/v14/RESULTS.md`, VE2).

### VE4 — A bet's growth is estimated by an average
**Statement.** If decisions are independent draws from `p`, and `h` is a bet fixed in advance with `h > 0` on the
support of `p`, then `(1/n)·log W_n`, the average of `log h(x_i)`, is within `ε` of `E_p[log h]` with probability at
least `1 − Var_p(log h)/(n·ε²)`.

**In plain terms.** How fast a fixed bet grows is read off the record as an average, with no binning and no estimate of
the actor's behaviour.

**Proof.** `log h(x_i)` are independent with average `E_p[log h]` and variance `Var_p(log h)`, finite on a finite
support; Chebyshev's inequality. ∎

**Notes.** Why this matters on a continuum (`NOTES.md` §22). The divergence from an empirical behaviour to any
continuous one is infinite, so v13's measure cannot be computed by plugging the record in. A bet is a function: its
average is estimated by an average, and by VE1(i) every bet gives a lower bound on misalignment, so a bet fixed in
advance, or chosen before each decision from the earlier ones as in VE3, accuses soundly with no bins. What a fixed bet
cannot do is reach the best one; how close bets chosen from the record come, and how fast, is open on a continuum, and
is where H43's `√n` blind spot reappears.

## Why this measure, among all the others

A reader may ask why misalignment is this number, and not a distance between behaviours chosen otherwise: total
variation, a Wasserstein distance, a Rényi or `χ²` divergence. The number is not chosen as a distance; it is the rate
at which evidence against acceptability accumulates. Each step from that to the formula is forced by a stated
requirement, or is a choice, named as one and listed in `v14/README.md`.
- *Evidence of independent decisions must add*, so it is counted on a logarithmic scale: the only continuous functions
  that turn products of probabilities into sums are multiples of the logarithm (Cauchy's functional equation). Forced.
- *A bet must be fair under acceptance*, `E_a[h] ≤ 1` for every acceptable `a`, or a large wealth would be no evidence
  against acceptability, and VE3's level would fail. Forced; it is the definition of an e-variable ([@grunwald2023]).
- *Wealth is valued by its long-run growth, the expected logarithm* (Kelly's criterion). A choice: a bettor who
  maximized expected wealth would be led to the Rényi divergence of order `∞`, and power utilities to other orders. It
  is the choice under which the evidence of independent decisions adds, and under which the number is v13's: the rate,
  per decision, at which acceptance makes the actor's record improbable ([A4], Sanov's rate).
- *The question is how improbable acceptance makes the actor's record*, the exponent of false accusation while the actor
  is reliably convicted, which is `KL(p̂‖a)`. The other order, `KL(a‖p̂)`, answers another question, how fast a
  misaligned actor stops escaping at a fixed level of false accusation (Stein's exponent); both are about how fast a
  record convicts. The order is forced only given this question, which is [A4]'s.
- *The best bet is taken*, so that misalignment charges only what no acceptable behaviour explains: the generalized
  likelihood ratio's benefit of the doubt, as in v13's table. A convention from the literature.
- *Under the mixture principle, the acceptable set is its convex hull* (VE2), so the number is the least divergence to
  the hull, `min_{a ∈ conv A} KL(p̂‖a)`; for a convex requirement, the requirement itself.
Given these, VE1 leaves no further freedom. One thing it does not settle: the best bet `p̂/a*` needs the actor's
behaviour, which a record only estimates. That bets chosen before each decision from the earlier ones reach the best
growth rate is not proved here (H46); a bet fixed in advance gives a lower bound, which is what a sound accusation
needs. Another divergence measures something else: total variation and Wasserstein distances measure how far
probability must move, in a geometry of outcomes the principal would have to declare, and say nothing of how fast a
record convicts. A principal who cares about such a distance declares it as a requirement (`constraints.md`, VK0), and
misalignment then counts the evidence against that requirement.
