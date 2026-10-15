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
and the magnitude moves to the rate and the stakes, which are reported beside it (`README.md`, verdicts). v13 asked
intended behaviours to have full support ([D3], the table of conventions), which a forbidden set cannot meet; v14 drops
that convention. Verifying the breach needs the occurrence to be recognized without error: a record that confuses `C`
with its neighbours, as a measurement on a continuum may, verifies it only when `C` is open in the record's topology
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
Farkas's lemma, read in an open text first. Joining constraints to the order part of a request is the same intersection;
`README.md` lists it among the open questions.

### VK5 — The constrained optimizer, by the Karush–Kuhn–Tucker conditions
*This result belongs to the derived module, "actors that optimize": it is a fact about one model of an actor, not part
of what the principal asks.*

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
largest value in `b` equals `ν` within `2e-8` (`probes/v14/RESULTS.md`, VK5). Two consequences, recorded here for the
derived module.
- *Obeying and valuing look alike.* An actor that keeps a budget because it must, and one that values the cost at `ν`,
  behave identically; by [A1], the core cannot and need not tell them apart.
- *v13 charged obedience.* Under v13's standard specification of `F`, the constrained optimizer is charged, since it
  lies on the ray of `F − ν·g`, not of `F`: the principal's own budget made its actor "misaligned". Under v14 the budget
  is part of the request, and the optimizer that keeps it breaches nothing.
