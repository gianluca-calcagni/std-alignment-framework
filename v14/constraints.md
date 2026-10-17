# Constraints

> **Status: draft of v14 (Q59); proved here, not yet checked in CI, except VK4's equality, which is supported by the
> probe and not proved.** The numbers come from `probes/v14/v14_probe.py`.

A **constraint** is a statement that every acceptable behaviour satisfies, whatever else the principal asks: it needs
no reference and no ranking. The PI asked for constraints as a concept of the core, since breaking one is plainly a
form of misalignment (Q59). Three forms cover what a principal states in practice, and each is a convex closed set of
behaviours, so VE1 applies to it:
- a **forbidden set** `C ⊆ X`, `C ≠ X`: `K = {a : a(C) = 0}`; "never give this answer";
- a **rate limit** `(C, ε)`, `C ≠ X`, `0 ≤ ε < 1`: `K = {a : a(C) ≤ ε}`; "at most one harmful answer in a thousand";
- a **budget** `(g, b)`, a cost `g : X → ℝ` and a number `b` with `min g < b`: `K = {a : E_a[g] ≤ b}`; "on average at
  most five seconds", or "at most this much spent".

A forbidden set is a rate limit with `ε = 0`, and a rate limit is a budget with `g = 1_C` and `b = ε`, except that a
budget with `b = min g` is excluded, since it is a forbidden set in disguise and has no bet of the form below. A
behaviour **breaches** a constraint when it lies outside it. Notation as in `evidence.md`; `kl(u‖v)` is the divergence
between the two-outcome behaviours `(u, 1 − u)` and `(v, 1 − v)`.

### VK0 — Every convex requirement is a set of budgets
**Statement.** Let `S ⊆ Δ` be non-empty, convex and closed. For every behaviour `x ∉ S` there is a budget `(g, b)`,
with `min g < b` as the definition above asks, that every member of `S` keeps and `x` breaks. So `S` is the
intersection of the budgets its members all keep.

**In plain terms.** Whatever a principal requires of a behaviour, as long as mixing two acceptable behaviours stays
acceptable, the requirement says no more than a list of limits on averages, "on average, at most this much of that",
though the list may be infinite. A budget is not one kind of constraint among others; it is the general form of every
convex requirement. A rate limit is one budget, of an indicator; a forbidden set is the rate limits at every rate above
zero.

**Proof.** Read behaviours as vectors in `ℝ^X`. `S` is compact, so some `c ∈ S` minimizes the Euclidean distance
`‖x − y‖` over `y ∈ S`, and `c ≠ x`. For `y ∈ S` and `s ∈ [0, 1]`, `c + s·(y − c) ∈ S` by convexity, so
`‖x − c − s·(y − c)‖² ≥ ‖x − c‖²`; the derivative in `s` at `0` is `−2·⟨x − c, y − c⟩ ≥ 0`. Let `g = x − c`, read as a
function on `X`, and `b = ⟨g, c⟩ + ‖x − c‖²/2`. Every `y ∈ S` has `E_y[g] = ⟨g, y⟩ ≤ ⟨g, c⟩ < b`;
`E_x[g] = ⟨g, c⟩ + ‖x − c‖² > b`; and `b > ⟨g, c⟩ = E_c[g] ≥ min g`. So the budgets that `S` keeps exclude every
`x ∉ S`, and contain `S`. ∎

**Notes.** This is the separating hyperplane theorem in its finite form, proved here from the nearest point. With VK3's
bets it is a **bipolar correspondence**: a convex closed requirement is exactly the set of behaviours under which every
bet against it is fair, since for `x ∉ S` the bet `1 + λ·(g − b)`, with `0 < λ ≤ 1/(b − min g)`, is fair under `S` and
has expected payoff above `1` under `x`; a small enough `λ` also makes it grow under `x`. A principal could therefore
declare a requirement by the bets it accepts as fair. How many budgets a requirement needs: a rate limit with `ε > 0`,
one; v13's ordinal specification, with a default of full support, and dominance (`order.md`), when every proper upper
set has reference mass strictly between `0` and `1`, finitely many; a forbidden set, infinitely many, `a(C) ≤ ε` for
every `ε > 0`, or one limit `E_a[1_C] ≤ 0` if limits with `b = min g` are admitted, which VK3's dual does not cover;
balls in total variation, and in a Wasserstein distance on finitely many outcomes, finitely many, since both are
polyhedral; balls in KL, Euclidean or Hellinger distance whose boundary meets the interior of `Δ`, on three or more
outcomes, infinitely many. It is why the PI's choice to declare constraints explicitly, as a general concept (Q60),
loses nothing: CORE's requirement, a convex closed set, and the PI's constraint are the same object. For finitely many
budgets, VK4 gives every bet of the affine form as a lower bound on misalignment; for any convex requirement, VE1 gives
the equality when all bets are allowed.

### VK1 — A forbidden set: one occurrence decides
**Statement.** For a forbidden set `C`: `M_K(p) = ∞` if `p(C) > 0`, and `0` otherwise. For every `H > 1`, the function
`h = H` on `C` and `1` off `C` is a bet against `K`. A test that rejects at the first outcome in `C` has level `0`.

**In plain terms.** A forbidden answer is never acceptable, so a single one shows a breach with certainty: no amount of
good behaviour elsewhere makes it acceptable. How often the actor breaches is a different number, its rate `p(C)`, and
it is that rate, with the stakes it carries, that says how bad the breach is.

**Proof.** If `p(C) > 0`, every `a ∈ K` gives `C` mass `0`, so `KL(p‖a) = ∞`; if `p(C) = 0`, `p ∈ K`. For `a ∈ K`,
`E_a[h] = a(X ∖ C) = 1`. Under any `a ∈ K` an outcome in `C` has probability `0`, at every decision, whatever the past.
∎

**Notes.** This is where misalignment, read as evidence, is infinite and still informative: the evidence is decisive,
and the magnitude moves to the rate and the stakes, which are reported beside it (`v14/README.md`, the design, 3). v13
asked intended behaviours to have full support ([D3], the table of conventions), which a forbidden set cannot meet; v14
drops that convention. Verifying the breach needs the occurrence to be recognized without error: a record that confuses
`C` with its neighbours, as a measurement on a continuum may, verifies it only when `C` is open in the record's topology
(`CORE-GENERAL.md`).

### VK2 — A rate limit, in closed form
**Statement.** For a rate limit `(C, ε)` and `p ∈ Δ`: `M_K(p) = kl(p(C)‖ε)` if `p(C) > ε`, and `0` otherwise. When
`p(C) > ε > 0`, a nearest acceptable behaviour keeps the actor's proportions inside `C` and outside it, and scales their
masses to `ε` and `1 − ε`; it is unique when `p(C) < 1`.

**In plain terms.** Against a limit on how often something happens, the evidence of breach depends only on how often it
does happen: it is the evidence against a coin that lands on "breach" at the permitted rate. What the actor does inside
and outside the forbidden region does not matter to it.

**Proof.** For `a` with `0 < a(C) < 1`, grouping the outcomes into `C` and `X ∖ C` gives, by the chain rule on finite
sums, `KL(p‖a) = kl(p(C)‖a(C)) + p(C)·KL(p(·|C)‖a(·|C)) + p(X∖C)·KL(p(·|X∖C)‖a(·|X∖C))`, a term with zero mass being
`0`. The last two terms are non-negative and vanish when `a` keeps `p`'s proportions inside each part. So `M_K(p) =
min_{v≤ε} kl(p(C)‖v)`, and `v ↦ kl(u‖v)` decreases on `[0, u]` and increases after; when `u = p(C) > ε` the minimum is
at `v = ε`, and when `u ≤ ε` it is `0` at `v = u`. The boundary `a(C) ∈ {0, 1}` gives `∞` unless `p` agrees, and is
covered by the same formula. ∎

**Notes.** With `ε = 0` it is VK1, since `kl(u‖0) = ∞` for `u > 0`. Checked against a numerical minimization on 35
random instances, within `3e-12` (`probes/v14/RESULTS.md`, VK2). The exact test of [P55] on two outcomes, breach and no
breach, applies unchanged to a record of independent decisions, and VE3 to any record.

### VK3 — A budget, by a Lagrange dual
**Statement.** For a budget `(g, b)` and `p ∈ Δ`: if `E_p[g] ≤ b`, `M_K(p) = 0`. Otherwise, with
`λ_max = 1/(b − min g)`, `M_K(p) = max_{0 ≤ λ ≤ λ_max} E_p[log(1 + λ·(g − b))]`, attained at some `λ* > 0`. The bet
`h* = 1 + λ*·(g − b)` is a best bet against `K`, and the nearest acceptable behaviour is `a* = p/h*` on the support of
`p`, with any remaining mass on outcomes of least cost.

**In plain terms.** Against a budget, the best bet is simple: stake a fixed fraction `λ` of your wealth on the cost
coming in above the budget, winning in proportion to the overrun and losing in proportion to the saving. A budget that
the actor keeps on average makes every such bet lose; one it overruns makes the best fraction grow at exactly its
misalignment. This is the Kelly criterion, applied to the evidence of overspending.

**Proof.** *Bets.* For `0 ≤ λ ≤ λ_max`, `h_λ = 1 + λ·(g − b) ≥ 1 − λ·(b − min g) ≥ 0`, and for `a ∈ K`,
`E_a[h_λ] = 1 + λ·(E_a[g] − b) ≤ 1`. So each `h_λ` is a bet, and `E_p[log h_λ] ≤ M_K(p)` by VE1(i).
*Equality.* Let `S` be the support of `p` and `ψ(λ) = E_p[log h_λ]`, concave and continuous on `[0, λ_max]` with values
in `[−∞, ∞)`, `ψ(0) = 0`, so its maximum is attained at some `λ*`. Its right derivative at `0` is `E_p[g] − b > 0`, so
`λ* > 0` and `ψ(λ*) > 0`, hence `h_{λ*} > 0` on `S`. Let `D = E_p[(g − b)/h_{λ*}]`. Since `1/h = 1 − λ·(g − b)/h`,
`E_p[1/h_{λ*}] = 1 − λ*·D`.
- If `λ* < λ_max`, `ψ'(λ*) = D = 0`. Then `a* = p/h_{λ*}` on `S`, `0` elsewhere, has total mass `1` and `E_{a*}[g − b] =
  D = 0`, so `a* ∈ K`.
- If `λ* = λ_max`, the left derivative gives `D ≥ 0`, and `h_{λ*}` vanishes exactly on the outcomes of least cost, none
  of them in `S`. Put `a* = p/h_{λ*}` on `S`, and the remaining mass `λ*·D ≥ 0` on one outcome `x₀` of least cost, where
  `g(x₀) − b = −1/λ*`. Then `E_{a*}[g − b] = D − λ*·D/λ* = 0`, so `a* ∈ K`.
In both cases `KL(p‖a*) = E_p[log h_{λ*}] = ψ(λ*)`, so `M_K(p) ≤ ψ(λ*) ≤ M_K(p)`. ∎

**Notes.** Checked against a numerical minimization on 80 random instances, within `2e-8`, with the constructed nearest
behaviour attaining it within `4e-8`; in 37 of them the maximum is at `λ_max` and the nearest acceptable behaviour moves
mass to a cheap outcome the actor never uses (`probes/v14/RESULTS.md`, VK3). The dual is the empirical-likelihood form
of a moment constraint in statistics (Owen; not read here). Two readings for v14: the misalignment of a budget is an
average of a function of the outcome, so it is estimated from a record on a continuum with no bins (VE4); and its bet is
a fair game under any behaviour that keeps the budget, given the past, so VE3 tests it under any dependence.

### VK4 — Several constraints
**Statement.** Let `K = K_1 ∩ … ∩ K_m`, non-empty, each `K_j` a rate limit or a budget `(g_j, b_j)`.
(i) `M_K(p) ≥ max_j M_{K_j}(p)`, and a breach of any `K_j` is a breach of `K`.
(ii) For `λ ∈ [0, ∞)^m` with `h_λ = 1 + Σ_j λ_j·(g_j − b_j) ≥ 0` on `X`, `h_λ` is a bet against `K`, so `M_K(p) ≥
E_p[log h_λ]`.
(iii) *Not proved:* the supremum of (ii) over `λ` equals `M_K(p)`.

**In plain terms.** Breaking one rule is enough to break the rules; the evidence against all of them together is at
least that against the worst one, and a combined bet on the overruns is always a valid lower bound.

**Proof.** (i) `K ⊆ K_j`. (ii) For `a ∈ K`, `E_a[h_λ] = 1 + Σ_j λ_j·(E_a[g_j] − b_j) ≤ 1`; VE1(i). ∎

**Notes.** (iii) holds on the 22 of 30 random instances with two budgets in which some behaviour keeps both, within
`5e-13` (`probes/v14/RESULTS.md`, VK4); a proof needs the Karush–Kuhn–Tucker conditions for linear constraints, or
Farkas's lemma, read in an open text first. *Requirements do not add.* In the support bot of `slides/framework.md`, the
misalignment against the rate limit on wrong answers alone is `0.0496`, against the order alone `0.0730`, and against
both `0.0730` (`probes/slides/RESULTS.md`): the joint is at least the largest, as (i) says, and can be smaller than the
sum, as here, or larger: for the uniform behaviour on three outcomes and the limits `a_1 ≤ 0.05` and `a_2 ≤ 0.05`, each
alone gives `0.396`, the sum `0.793`, and both `0.934`. An exact split exists only along a chosen order of the
requirements, `M_{A_1∩A_2} = M_{A_1} + (M_{A_1∩A_2} − M_{A_1})`, the same telescoping as FA1, and it depends on the
order. A report gives a verdict and a misalignment per requirement, and the joint. Joining constraints to an order is
the same intersection; how the reference should meet the constraints is H45, and the requirement built from an order is
the PI's choice (`ROADMAP.md`, recommendation 2).

### VK5 — The constrained optimizer, by the Karush–Kuhn–Tucker conditions
*This result belongs to OPTIMIZERS: it is a fact about one model of an actor, not part of what the principal asks.*

**Statement.** Let `q ∈ Δ°`, `F : X → ℝ`, `t > 0`, and a budget `(g, b)`. Among behaviours `a` with `E_a[g] ≤ b`, the
value `E_a[F] − KL(a‖q)/t` is largest at `a_ν = tilt(q, t·(F − ν·g))`, where `ν = 0` if `E_{a_0}[g] ≤ b`, and otherwise
`ν > 0` is the unique number with `E_{a_ν}[g] = b`. For a forbidden set `C`, the largest value is at
`tilt(q(·|X∖C), t·F)`, the limit of `a_ν` for `g = 1_C` as `ν → ∞`.

**In plain terms.** An actor that optimizes under a budget acts exactly as one that optimizes with no budget an
objective from which the cost has been subtracted at a price `ν`, the budget's shadow price; the price is zero when the
budget does not bind. An actor that must avoid some outcomes optimizes as if they did not exist.

**Proof.** `ν ↦ E_{a_ν}[g]` is continuous and non-increasing, its derivative being `−t·Var_{a_ν}(g)`, and tends to
`min g < b` as `ν → ∞`, since `q` has full support; so `ν` exists, and it is unique where the variance is positive. For
any `a` with `E_a[g] ≤ b`:
`E_a[F] − KL(a‖q)/t = (E_a[F − ν·g] − KL(a‖q)/t) + ν·E_a[g] ≤ (E_{a_ν}[F − ν·g] − KL(a_ν‖q)/t) + ν·b`, by [P4](i) for
the objective `F − ν·g` at intensity `t`, and since `ν ≥ 0`. The right side equals `E_{a_ν}[F] − KL(a_ν‖q)/t`, because
`ν·(E_{a_ν}[g] − b) = 0`: either `ν = 0` or the budget binds. These are the Karush–Kuhn–Tucker conditions, verified
directly. For a forbidden set, an `a` with `a(C) = 0` has `KL(a‖q) = KL(a‖q(·|X∖C)) − log q(X∖C)`, so the problem is
[P4](i) on the outcomes `X ∖ C`, where `q(·|X∖C)` has full support, or trivial if `X ∖ C` has one outcome. ∎

**Notes.** Checked against a numerical maximization on 29 random instances, within `3e-9`, and the derivative of the
largest value in `b` equals `ν` within `2e-8` (`probes/v14/RESULTS.md`, VK5). Two consequences, recorded here for
OPTIMIZERS.
- *Obeying and valuing look alike.* An actor that keeps a budget because it must, and one that values the cost at `ν`,
  behave identically; by [A1], the core cannot and need not tell them apart.
- *v13 charged obedience.* Under v13's standard specification of `F`, the constrained optimizer is charged, since it
  lies on the ray of `F − ν·g`, not of `F`: the principal's own budget made its actor "misaligned". Under v14 the budget
  is part of the request, and the optimizer that keeps it breaches nothing.

### VK6 — A pooled rate limit when the conditions are not chosen
**Statement.** Let the conditions `c` have frequencies `w_c > 0` that the actor does not choose, so that behaviours are
tuples `(a_c)_c` judged on pairs ([B2]), and let the rate limit be pooled over them: `K = {(a_c)_c : Σ_c w_c·a_c(C) ≤
ε}`, `0 < ε < 1`. Let `u_c = p_c(C)` and `ū = Σ_c w_c·u_c`. If `ū ≤ ε`, `M_K(p) = 0`. Otherwise
`M_K(p) = Σ_c w_c·kl(u_c‖v_c(θ))`, where, for `θ > 0` and `u ∈ [0, 1]`,
`v(θ, u) = ((θ + 1) − √((θ + 1)² − 4·θ·u))/(2·θ)`, and `θ > 0` is a number with `Σ_c w_c·v(θ, u_c) = ε`. A nearest
acceptable behaviour keeps, in each condition, the actor's proportions inside `C` and outside it. And `M_K(p) ≥
kl(ū‖ε)`, VK2's pooled formula, which is therefore a lower bound.

**In plain terms.** When the actor cannot choose how often each situation arises, a limit on the overall rate of
breaches is judged condition by condition: the nearest acceptable actor lowers its breach rate in every condition, by
`θ·v·(1 − v)` at the new rate `v`, until the overall rate meets the limit. Treating the record as one pool, as VK2 does,
understates the evidence.

**Proof.** In each condition, as in VK2, the chain rule on `C` and `X ∖ C` reduces the problem to choosing the breach
rates `v_c`, with the proportions inside and outside `C` kept: minimize `f(v) = Σ_c w_c·kl(u_c‖v_c)` over `v ∈ [0, 1]^𝒞`
with `Σ_c w_c·v_c ≤ ε`. For `θ > 0`, the function `v ↦ kl(u‖v) + θ·v` is convex on `[0, 1]` and least at `v(θ, u)`: for
`0 < u < 1`, its derivative `(v − u)/(v·(1 − v)) + θ` vanishes where `θ·v² − (θ + 1)·v + u = 0`, whose smaller root is
`v(θ, u)`, in `[0, u]` since the quadratic is `u ≥ 0` at `0` and `θ·u·(u − 1) ≤ 0` at `u`; for `u = 0`, the function is
`−log(1 − v) + θ·v`, increasing, least at `0 = v(θ, 0)`; for `u = 1`, it is `−log v + θ·v`, least at
`min(1, 1/θ) = v(θ, 1)`. The map `θ ↦ Σ_c w_c·v(θ, u_c)` is continuous, tends to `ū > ε` as `θ → 0` and to `0` as
`θ → ∞`, so some `θ` gives `ε`. Let `v* = v(θ, u)`. For every feasible `v`,
`f(v) ≥ f(v) + θ·(Σ_c w_c·v_c − ε) ≥ Σ_c w_c·(kl(u_c‖v*_c) + θ·v*_c) − θ·ε = f(v*)`, since each term is least at `v*_c`
and `Σ_c w_c·v*_c = ε`. The lower bound: without the frequencies fixed, the pooled limit is VK2's on the pairs, whose
acceptable set contains `K`. ∎

**Notes.** Against a numerical minimization on 40 random instances, within `1e-10`; the pooled formula falls short of it
by up to `0.19`. For the support bot of `slides/framework.md`, wrong answers in `2.91%` of open questions and `35.34%`
of account questions give `0.04956`, the number its probe found by minimization, where VK2's pooled formula gives
`0.0440` (`probes/v14/RESULTS-resolution.md`). This was the first lesson of the slides' example (`NOTES.md` §31): the
closed forms of this file hold for behaviours on outcomes alone, and on pairs whose frequencies are fixed they become
one-parameter forms like this one.

### VK7 — How misalignment moves with the budget
**Statement.** Let `(g, b)` be a budget with `E_p[g] > b > min g`, `M(b)` the misalignment against it, and `λ*(b)` the
best fraction of VK3. For every `b' > min g`, `M(b') ≥ M(b) − log(1 + λ*(b)·(b' − b)) ≥ M(b) − λ*(b)·(b' − b)`. So
`b ↦ M(b)` is convex and non-increasing, `−λ*(b)` is a subgradient of it, and wherever `λ*` is continuous,
`M'(b) = −λ*(b)`.

**In plain terms.** For an actor held fixed, the best bet's stake is also the price of the budget: loosening the budget
by one unit of cost removes about `λ*` nats per decision of evidence. The price depends on the actor's behaviour and on
the budget, and rescales with the units of the cost, so no constant converts units of cost into nats of evidence.

**Proof.** Let `h* = 1 + λ*·(g − b)` and `a*` the nearest acceptable behaviour of VK3, equal to `p/h*` on the support
`S` of `p`. Take `a` with `E_a[g] ≤ b'` and `KL(p‖a) < ∞`, so `a > 0` on `S`. By Jensen's inequality,
`KL(p‖a) − M(b) = E_p[log(a*/a)] ≥ −log E_p[a/a*] = −log Σ_{x∈S} a(x)·h*(x) ≥ −log E_a[h*]`, as `h* ≥ 0`, and
`E_a[h*] = 1 + λ*·(E_a[g] − b) ≤ 1 + λ*·(b' − b)`, which is positive since `λ* ≤ 1/(b − min g)` and `b' > min g`. Take
the infimum over `a`; `log(1 + y) ≤ y` gives the second inequality. Convexity: if `a_0`, `a_1` are nearest for `b_0`,
`b_1`, their mixture with weight `s` keeps the budget `(1 − s)·b_0 + s·b_1`, and `KL(p‖·)` is convex. A convex function
with the subgradients `−λ*(b)` satisfies `−λ*(b) ≤ (M(b') − M(b))/(b' − b) ≤ −λ*(b')` for `b < b'`, so it is
differentiable where `λ*` is continuous. ∎

**Notes.** On 30 random budgets, the derivative of `M`, by finite differences, equals `−λ*` within `1e-7`, and the first
inequality holds on a grid of 25 values of `b'` each (`probes/v14/RESULTS-resolution.md`). An independent reviewer found
`M` differentiable with `M' = −λ*` also where `λ* = λ_max`, on 166 instances, and `λ*` continuous across the switch, so
`M` is probably continuously differentiable on `(min g, ∞)`; the continuity of `λ*` is not proved here. This answers a
gap the slides' example showed (`NOTES.md` §31): v13 had a sensitivity of verdicts to the specification ([P10]) and v14
had none; the sensitivity of misalignment to a budget is the budget's best bet. It is also where severity, a cost scale
the principal declares, meets evidence (`v14/severity.md`).

## Declaring a specification: what is implicit, what must be explicit

The PI asked when a constraint is part of the other definitions and when it must be declared explicitly, because there
would be no other way to account for it, and how the interface enters (Q69). Every requirement is a convex closed set,
and by VK0 a list of budgets; the question is only which of them a declaration states by itself.

**What each declared object already constrains.**

| Declared | The requirements it makes, with no constraint written | Where |
|---|---|---|
| the outcomes `X` | none; but nothing outside them can be required: an effect no record holds is out of reach | `LIMITS.md` |
| conditions and their frequencies | `a(c) = w_c` for every condition: the actor does not choose its situations | [B2]; VK6 |
| the principal's σ-algebra `ℬ` | no requirement inside its cells: indifference | `resolution.md`, RS3 |
| a family of targets and a reference `r` | `E_a[G_i] ≥ E_r[G_i]` for each generating target; a forbidden set when `−1_C` is a target and `r(C) = 0` | `targets.md`, TG1 |
| a ranking and a reference | dominance at every standard, `B(r)`, or the requirement the principal builds from it | `order.md` |

**When a constraint must be explicit.** When nothing else in the declaration implies it:
- *there is no reference*: absolute standards, such as a legal limit or "never";
- *the quantity is one no target of the family scores*: side effects, cost, latency, privacy, about which a family of
  targets says nothing;
- *the tolerance is not the reference's*: stricter, because the reference itself breaks it (H45), or looser;
- *the reference produces a forbidden outcome*, `r(C) > 0`, so TG1(iv) does not forbid it;
- *the requirement ties conditions together*, such as acting alike in every condition ([P40]), which no per-condition
  average states.

**The interface is not part of the specification.** The specification says what the actor *may* do; the interface what
it *can* do.
- A capability the actor lacks needs no requirement: no record can show it, and declaring it as one would make an
  inability look like obedience.
- A requirement that no feasible behaviour meets is not an error of the specification: it shows as unavoidable
  misalignment, `m_1 > 0` in FA1, and culpability is measured against the best feasible behaviours, not against it.
- A requirement that the interface makes automatic, `𝓕 ⊆ A_j`, still belongs in the specification: a new version, a
  shaped actor or a wider deployment can have a larger feasible set.
- For an actor that optimizes, a binding constraint acts as a shadow price (VK5), and VK7 gives what it costs in
  evidence.

**In five questions.** Before any record is read: (1) what are the outcomes, and the conditions with their frequencies?
(2) Which distinctions between outcomes does the principal not care about? (3) Is there a reference, and which targets
must it not be beaten on? (4) What is required absolutely: forbidden outcomes, rates, averages? (5) What can the actor
see and do, declared apart, as its interface? The first four make the specification; the fifth only explains it.
`slides/specification.md` walks through them.
