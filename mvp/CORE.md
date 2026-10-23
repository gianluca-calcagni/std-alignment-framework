# The core of the MVP: definitions and results

> **Status: the MVP's core (Q80), drawn from the v14 draft and written as checked items; not approved, not reviewed
> outside the executor's model family.** Every result has a proof here and checks in `mvp/checks/` that run in CI. The
> library that computes these quantities is `stdalign/spec.py`.

The framework judges what an actor does against what a principal declared, from records of the actor's decisions. This
file holds what the MVP needs to do that: ten definitions, each with what its object is in the world, and eighteen
results, each with a proof and the checks that test it. Nothing here models how the actor decides: a frozen model, a
person and an institution are judged alike, by what they do.

## Conventions

Outcomes are finite. `Δ` is the set of distributions on a finite set `X`, a **behaviour** being one of them. For `p, a ∈
Δ`, `KL(p‖a) = Σ_{x : p(x)>0} p(x)·log(p(x)/a(x))`, natural logarithms, with `log(·/0) = +∞`; `kl(u‖v)` is `KL` between
`(u, 1 − u)` and `(v, 1 − v)`. `E_a[g] = Σ_x a(x)·g(x)`. Every choice below that an equally reasonable principal could
make otherwise is named here, with what it changes.

| Convention | Why | What changes otherwise |
|---|---|---|
| evidence on a logarithmic scale, per decision | evidence of independent decisions must add; only logarithms turn products into sums | nothing a verdict depends on |
| a bet must be fair under acceptance | otherwise a large wealth is no evidence; it is the definition of an e-variable [@grunwald2023] | the level of every test |
| wealth valued by its long-run growth (Kelly) | the choice under which evidence adds and the number is Sanov's rate (R5) | expected wealth would give another divergence, Rényi's of order `∞` |
| `KL(p‖a)`, the actor first | the rate at which acceptance makes the actor's record improbable (R5) | the other order answers how fast a misaligned actor stops escaping |
| a per-decision requirement is convex and closed | a test valid whatever the dependence holds an actor only to the hull of what is acceptable (R3); closing changes no misalignment and no bet | a set that is not convex is enforced as its hull; declare it pooled instead (D4) |

## Definitions

### D1 — Outcomes and the world's part
**Statement.** A finite set `X` of **outcomes**, and a partition `ℰ` of `X` whose cells, the **conditions**, are the
part of an outcome the world chooses. When the world chooses nothing, `ℰ = {X}`.

**Interpretation.** An outcome is everything a record notes of one decision, the situation it arose in included, such as
the prompt and the answer. The principal declares which part the actor does not choose: the question asked, the
customer who called, the patient who came in. The actor is then never judged on how often the world posed each
situation. Finiteness is what a record at finite precision decides.

**Lineage.** v14's one distribution (`v14/README.md`; Q74, Q76); v13's [D1], [B2].

### D2 — Behaviour
**Statement.** A **behaviour** is `p ∈ Δ`. Its law on the conditions is `p_ℰ`, and for a condition `E` with `p(E) > 0`,
`p(·|E)` is what the actor does in it.

**Interpretation.** How often each outcome happens over many decisions. Two actors that behave alike are the same actor
for the framework: goals, beliefs and intentions are not part of a behaviour, and enter only as hypotheses about it.

**Lineage.** v13's [A1], [D1].

### D3 — Record
**Statement.** A **record** is a sequence of decisions `1, 2, …, n`, each an outcome `x_i ∈ X`, noted at a declared
partition `ℛ` of `X`, the **record's resolution**: the record shows the cell of `ℛ` that contains `x_i`, which tells
the condition (`ℛ` refines `ℰ`). Given everything before it, decision `i` has a law `p_i ∈ Δ`, its **conditional
behaviour**. Decisions are not assumed independent. A **sample** is a record whose decisions are independent draws from
one behaviour.

**Interpretation.** What a log, a grader or an instrument shows of what the actor did. `ℛ` is what that instrument can
tell apart: a grader that marks answers only "acceptable" or "harmful" sees two cells, whatever the answers say.

**Lineage.** v14's resolution (`v14/resolution.md`); v13's [D11].

### D4 — Specification
**Statement.** A **specification** is a finite list of **requirements**, declared before the record it judges, each of
one of two kinds:
- **per decision**: a set `A_E ⊆ Δ(E)`, convex and closed, for each condition `E`, asking that in every condition the
  conditional behaviour lie in `A_E`; or a convex closed `A ⊆ Δ` with the world's law fixed (R10). The **acceptable
  set** is the set of behaviours that meet every per-decision requirement;
- **pooled**: a closed set `Q ⊆ Δ` and a horizon `N`, asking that the average `p̄_N = (1/N)·Σ_{i≤N} p_i` of the
  conditional behaviours lie in `Q`.

A specification whose per-decision requirements have no behaviour in common is **inconsistent**; that is found from the
declarations alone. Common requirements: a **forbidden set** `C`, `a(C) = 0`; a **rate limit** `(C, ε)`, `a(C) ≤ ε`; a
**budget** `(g, b)`, `E_a[g] ≤ b`, with `min g < b`; and "no worse than a reference `r` on criteria `G_1, …, G_m`",
`E_a[G_j] ≥ E_r[G_j]` (R9).

**Interpretation.** What the principal asks, in a form a record can be held to. **Declared** means fixed, dated and
published before the record it judges is read: a standard fitted to the data it judges cannot fail. A per-decision
requirement protects each decision, as a patient or a user is owed; a pooled one bounds a total, as an emissions budget
does, and a risky decision may be offset by safe ones. Which kind a requirement is, its horizon and its tolerances are
the principal's to declare; the framework supplies none.

**Lineage.** v14's specification and two kinds of requirement (Q70, Q74, `v14/constraints.md`).

### D5 — Misalignment
**Statement.** For a set `A ⊆ Δ` and `p ∈ Δ`, the **misalignment** of `p` against `A` is
`M_A(p) = inf {KL(p‖a) : a ∈ A, a_ℰ = p_ℰ}`, in nats per decision, `+∞` when no such `a` exists. A behaviour
**breaches** a requirement when it lies outside it.

**Interpretation.** The rate at which evidence accumulates, per decision, that the actor is not acceptable: the growth
rate of the best fair bet against acceptance (R2), and the rate at which acceptance makes the record's counts
improbable, at the record's shares (R5). It compares the actor only with acceptable behaviours that faced the same
situations (R1). It measures evidence, not harm: a catastrophe tolerated at one in a million and occurring at two has
misalignment `3.9·10⁻⁷`, a rude answer tolerated at one in ten and occurring at two in ten, `0.044`
(`mvp/checks/test_core.py::test_d5_severity_example`). How bad an outcome is comes from a declared severity (D10).

**Lineage.** v14's misalignment (`v14/evidence.md`); v13's [A4], [D3].

### D6 — Bet, wealth and conviction
**Statement.** A **bet** against `A` is `h : X → [0, ∞)` with `E_a[h] ≤ 1` for every `a ∈ A`. Along a record, a bet
`h_i` chosen before decision `i` from what came before gives the **wealth** `W_n = Π_{i≤n} h_i(x_i)`, `W_0 = 1`. At a
declared level `α`, the record **convicts** when `W_n ≥ 1/α` for some `n`. A bet used by a record at resolution `ℛ` is
constant on its cells.

**Interpretation.** A ticket that no acceptable behaviour expects to pay more than its price. If the actor is acceptable
at every decision, wealth rarely grows (R4); if it is not, the best bets grow, on average over a sample, at its
misalignment (R2). A conviction is evidence that the actor breached, with an error rate fixed in advance, and needs no
model of how the actor's decisions depend on each other.

**Lineage.** v14's bets (`v14/evidence.md`); e-values [@grunwald2023].

### D7 — Certification
**Statement.** At a declared level `α` and margin, the record **certifies** a pooled requirement on a rate or a budget
when the confidence bound of R16 for the average conditional behaviour, read at the declared horizon `N`, lies inside
it. For a sample, the average is the behaviour itself, and a certificate is about every decision.

**Interpretation.** Evidence that a requirement is met, within a margin, at an error rate fixed in advance. It is about
an average: no record certifies that every decision of an actor that may change was acceptable (R17).

**Lineage.** Q74, Q76 (`v14/LIMITS.md`).

### D8 — What a record can see
**Statement.** For a partition `𝒢` of `X` refining `ℰ`, `p_𝒢` is the behaviour on cells, and the **misalignment at
resolution `𝒢`** is `M_A^𝒢(p) = inf {KL(p_𝒢‖a_𝒢) : a ∈ A, a_ℰ = p_ℰ}`. The misalignment **hidden** from `𝒢` is
`H_𝒢(p) = M_A(p) − M_A^𝒢(p)` when `M_A(p)` is finite, and `∞` when `M_A(p) = ∞ > M_A^𝒢(p)`.

**Interpretation.** What a record at that resolution can detect, and what lies inside its cells, out of its sight.

**Lineage.** `v14/resolution.md`.

### D9 — Interface, unavoidable misalignment and culpability
**Statement.** An **interface** declares a convex closed set `𝓕 ⊆ Δ` of **feasible** behaviours, those the actor could
produce, all with the world's law `p_ℰ`. For a set `A`:
- the **unavoidable misalignment** is `m(𝓕) = inf_{f∈𝓕} M_A(f)`;
- the **avoidable excess** of `p ∈ 𝓕` is `E(p) = M_A(p) − m(𝓕)`, when `m(𝓕)` is finite;
- for a declared **care margin** `δ ≥ 0`, the **best feasible behaviours within `δ`** are
  `𝓕*_δ = {f ∈ 𝓕 : M_A(f) ≤ m(𝓕) + δ}`;
- the actor is **culpable at margin `δ`** when `p ∉ 𝓕*_δ`, with **evidence of culpability**
  `K_δ(p) = inf_{f∈𝓕*_δ} KL(p‖f)`.

**Interpretation.** What the actor could have done: the actions it has, what it sees, how the world turns its actions
into outcomes, declared by the principal, best from capabilities shown in elicitation. Unavoidable misalignment is what
no feasible behaviour avoids; the avoidable excess, the size of what this actor could have avoided; culpability, the
verdict that it did not do as well as it could, within a declared standard of care. `K_δ` is evidence, not size: it is
infinite when the actor produces an outcome that every best feasible behaviour avoids, which is common when `δ = 0`.

**Lineage.** v14's interface and culpability (`v14/interface.md`; Q74).

### D10 — Severity
**Statement.** A **severity** is a function `sev : X → [0, ∞)` in the principal's units, declared with a budget
`E_a[sev] ≤ b` (D4). A report gives, beside the misalignment against it, the actor's expected severity `E_p[sev]` and
the overrun `E_p[sev] − b`, in those units.

**Interpretation.** How bad each outcome is for the principal: money, hours, injuries. It is never in nats and never
added to misalignment: evidence and harm rank breaches differently (D5).

**Lineage.** `v14/severity.md` (Q69).

## Results

### R1 — The world's choices carry no evidence
**Statement.** Let `p, a ∈ Δ` with `a_ℰ = p_ℰ`.
(i) `KL(p‖a) = Σ_{E∈ℰ, p(E)>0} p(E)·KL(p(·|E)‖a(·|E))`.
(ii) If the requirement is per decision, sets `A_E`, then `M_A(p) = Σ_{E : p(E)>0} p(E)·inf_{a_E∈A_E} KL(p(·|E)‖a_E)`.
(iii) `inf_{a∈A} KL(p‖a) ≤ M_A(p)`: dropping the world's part can only lower the number, and does when an acceptable
behaviour with another law on `ℰ` is nearer.

**In plain terms.** Comparing the actor with acceptable behaviours that faced the same situations removes the evidence
about how often the world posed each one, which says nothing of the actor. A requirement stated condition by condition
is then judged condition by condition, and the parts add up. Forgetting which part the world chooses lets the actor be
credited with situations it never faced.

**Proof.** (i) For `x` in a condition `E` with `p(E) > 0`, `p(x) = p(E)·p(x|E)` and `a(x) = p(E)·a(x|E)`, so
`log(p(x)/a(x)) = log(p(x|E)/a(x|E))`; sum over `x`. (ii) The behaviours `a` with `a_ℰ = p_ℰ` and `a(·|E) ∈ A_E` are
those that choose each conditional independently in `A_E`; by (i) the divergence is a sum of terms each depending on one
conditional, so its infimum is the sum of the infima. (iii) The left side is an infimum over a larger set. ∎

**Checks.** `mvp/checks/test_core.py::test_r1_chain_rule`, `::test_r1_per_condition_sum`, `::test_r1_world_part_raises`.

**Lineage.** v14's one distribution (Q74, Q76); VK6's lesson (`v14/constraints.md`).

### R2 — Misalignment against a convex set is the growth rate of the best bet
**Statement.** Let `A' = {a ∈ A : a_ℰ = p_ℰ}` be convex and closed, and `p ∈ Δ`.
(i) For every bet `h` against `A'`, `E_p[log h] ≤ M_A(p)`.
(ii) If `M_A(p) < ∞`, the minimum is attained at some `a* ∈ A'`, and `h* = p/a*` on the support of `p`, `0` elsewhere,
is a bet against `A'` with `E_p[log h*] = M_A(p)`.
(iii) If `M_A(p) = ∞`, some bets against `A'` grow under `p` faster than any given number.
(iv) If `A` is given by per-condition sets `A_E` (D4), or every member of `A` has the law `p_ℰ`, then `h*` is a bet
against `A` itself, so R4 applies to it.

**In plain terms.** Bet against the principal's standard with tickets the standard itself calls fair. If the actor is
acceptable, no such bet grows on average. If it is not, the fastest any of them grows is exactly its misalignment, and
the best ticket pays the ratio of what the actor does to the nearest acceptable behaviour.

**Proof.** (i) Let `a ∈ A'` with `KL(p‖a) < ∞`, so `a > 0` on the support `S` of `p`. If `h = 0` somewhere on `S`,
`E_p[log h] = −∞`. Otherwise, by Jensen's inequality for the logarithm,
`E_p[log h] − KL(p‖a) = E_p[log(h·a/p)] ≤ log Σ_{x∈S} h(x)·a(x) ≤ log E_a[h] ≤ 0`. Take the infimum over `a`.
(ii) `KL(p‖·)` is a sum of terms `p(x)·log(p(x)/a(x))`, each continuous from `a` into `(−∞, +∞]`, so it is lower
semicontinuous, and its minimum over the compact `A'` is attained at some `a*`, positive on `S`. For `a ∈ A'` and
`s ∈ [0, 1)`, `a_s = a* + s·(a − a*) ∈ A'` and `a_s ≥ (1 − s)·a* > 0` on `S`, so `φ(s) = KL(p‖a_s)` is finite,
differentiable, and least at `0`: `0 ≤ φ'(0+) = −Σ_{x∈S} p(x)·(a(x) − a*(x))/a*(x) = 1 − E_a[h*]`. So `h*` is a bet, and
`E_p[log h*] = KL(p‖a*) = M_A(p)`.
(iii) If every `x ∈ S` had some `a_x ∈ A'` with `a_x(x) > 0`, their average would lie in `A'` and be positive on `S`,
making `M_A(p)` finite. So some `x₀ ∈ S` has `a(x₀) = 0` for all `a ∈ A'`. For `H > 1`, `h = H` at `x₀` and `1`
elsewhere is a bet, `E_a[h] = 1`, and `E_p[log h] = p(x₀)·log H`.
(iv) If every member of `A` has the law `p_ℰ`, `A = A'`. For per-condition sets, (ii) applied in each condition gives
`E_{a_E}[p(·|E)/a*(·|E)] ≤ 1` for every `a_E ∈ A_E`, since `a*` minimizes each condition's term (R1(ii)); and `h*` is
`p(·|E)/a*(·|E)` on condition `E`, so for every `a ∈ A`, `E_a[h*] = Σ_E a(E)·E_{a(·|E)}[h*] ≤ Σ_E a(E) = 1`. ∎

**Checks.** `mvp/checks/test_core.py::test_r2_best_bet_fair_and_attains`, `::test_r2_any_bet_below`,
`::test_r2_infinite_case`, `::test_r2_bet_against_whole_set`.

**Lineage.** v14's VE1; [@grunwald2023], Theorem 1, a general form, read.

### R3 — Records hold an actor to the convex hull
**Statement.** For a closed `A ⊆ Δ`, the bets against `A` are exactly the bets against its convex hull `conv A`, so the
best growth rate of a bet against `A` is `inf_{a∈conv A} KL(p‖a)`. With `ℰ = {X}` this is `M_{conv A}(p) ≤ M_A(p)`.

**In plain terms.** If acting one acceptable way at some decisions and another way at others is fine, no bet can tell
the actor from a mixture of acceptable behaviours, so a requirement that is not convex is enforced only as its hull.
That is why per-decision requirements are convex, and why a limit on, say, a tail risk is declared pooled.

**Proof.** `a ↦ E_a[h]` is affine, so `E_a[h] ≤ 1` on `A` implies it on every mixture of points of `A`; the converse
holds since `A ⊆ conv A`. `conv A` is compact, as the convex hull of a compact set in finite dimension (Carathéodory's
theorem), and convex, so R2 with `ℰ = {X}` applies to it. ∎

**Checks.** `mvp/checks/test_core.py::test_r3_hull_bets`, `::test_r3_cvar_not_convex`.

**Lineage.** v14's VE2(i); the CVaR example of `NOTES.md` §32.

### R4 — A test from bets keeps its level whatever the dependence
**Statement.** (i) Let `ℱ_0 ⊆ ℱ_1 ⊆ …` be what is known after each decision, `ℱ_k` including the first `k` decisions,
and `W_0 = 1, W_1, …, W_N` non-negative, each `W_k` known at `ℱ_k`, with `E[W_k | ℱ_{k−1}] ≤ W_{k−1}`. Then for every
`α ∈ (0, 1]`, the probability that `W_k ≥ 1/α` for some `k ≤ N` is at most `α`; letting `N → ∞`, the same holds for
some `k` at all, by continuity of probability.
(ii) In particular, if each decision, given the past, is drawn from an acceptable behaviour, and each bet `h_k` is
chosen before decision `k` from what came before, the wealth of D6 convicts with probability at most `α`.

**In plain terms.** Keep betting against the standard, one decision at a time, changing the bet as you learn. If the
actor acts acceptably at every step, given what came before, the chance that your wealth ever reaches `20` is at most
`1/20`, however its decisions depend on each other and however you chose your bets.

**Proof.** (i) Let `τ` be the first `k ≤ N` with `W_k ≥ 1/α`, or `N` if there is none. Whether `τ ≥ k` is known at
`ℱ_{k−1}`, so `E[W_{min(τ,k)} − W_{min(τ,k−1)}] = E[1{τ ≥ k}·(W_k − W_{k−1})] ≤ 0`, and `E[W_τ] ≤ 1`. Some `W_k ≥ 1/α`
exactly when `W_τ ≥ 1/α`, which has probability at most `α·E[W_τ] ≤ α` by Markov's inequality; non-negativity makes
every expectation defined. (ii) Given the past, decision `k` is drawn from some acceptable `a`, so
`E[W_k | past] = W_{k−1}·E_a[h_k] ≤ W_{k−1}`; apply (i). ∎

**Checks.** `mvp/checks/test_core.py::test_r4_level_under_dependence`, `::test_r4_level_iid`.

**Lineage.** v14's VE3; Ville's inequality on a finite horizon, as [@grunwald2023], Corollary 1, states it for bets.

### R5 — Sanov's rate: how improbable acceptance makes the record
**Statement.** Let `A ⊆ Δ` be non-empty, `n ≥ 1`, and `k_n = (n + |X| − 1)!/(n!·(|X| − 1)!)`, the number of possible
shares of `n` decisions. For the shares `s` of `n` decisions and `P_a(s)` the probability that `n` independent draws
from `a` have shares `s`, `e^{−n·M_A(s)}/k_n ≤ sup_{a∈A} P_a(s) ≤ e^{−n·M_A(s)}`, with `ℰ = {X}`. For a general `ℰ` the
same bounds hold with the supremum over `a ∈ A` with `a_ℰ = s_ℰ`; the proof is unchanged.

**In plain terms.** The chance that some acceptable behaviour would have produced the record's counts falls
exponentially with the number of decisions, at a rate per decision equal to the misalignment of the counts, up to a
polynomial factor. Misalignment is how fast acceptance becomes implausible.

**Proof.** For `a ∈ Δ`, the probability of one sequence with shares `s` is
`Π_x a(x)^{n·s(x)} = e^{−n·(H(s) + KL(s‖a))}`, `H` the entropy, and the number `T` of such sequences is the same for
every `a`; so `P_a(s) = T·e^{−n·(H(s)+KL(s‖a))}`. With `a = s`, `P_s(s) = T·e^{−n·H(s)} ≤ 1`, so
`P_a(s) ≤ e^{−n·KL(s‖a)}`. Conversely, `s` is the most probable set of shares under `s`: for another `s'` with
`P_s(s') > 0`, so that `s'` vanishes where `s` does,
`P_s(s)/P_s(s') = Π_x ((n·s'(x))!/(n·s(x))!)· s(x)^{n·(s(x) − s'(x))} ≥ Π_x (n·s(x))^{n·(s'(x)−s(x))}·s(x)^{n·(s(x)−s'(x))} = n^{n·Σ_x (s'(x) − s(x))} = 1`,
with the products over `x` where `s(x) > 0`, using `m!/l! ≥ l^{m−l}`; the `k_n` sets of shares have probabilities adding
to `1`, so `P_s(s) ≥ 1/k_n`, and `P_a(s) ≥ e^{−n·KL(s‖a)}/k_n`. Take the supremum over `a ∈ A`. ∎

**Checks.** `mvp/checks/test_core.py::test_r5_type_bounds`.

**Lineage.** v14's SN1(i); the method of types.

### R6 — Every convex requirement is a list of budgets
**Statement.** Let `S ⊆ Δ` be non-empty, convex and closed. For every `x ∈ Δ ∖ S` there is a budget `(g, b)`, with
`min g < b`, that every member of `S` keeps and `x` breaks.

**In plain terms.** Whatever a principal requires, as long as mixing two acceptable behaviours stays acceptable and the
requirement is closed, the requirement says no more than a list of limits on averages, "on average, at most this much of
that", possibly infinite.

**Proof.** Let `c ∈ S` be nearest to `x` in Euclidean distance (`S` is compact), so `c ≠ x`. For `y ∈ S`,
`c + t·(y − c) ∈ S` for `t ∈ [0, 1]`, and minimality gives `⟨x − c, y − c⟩ ≤ 0`. Let `g = x − c` and
`b = ⟨g, c⟩ + ‖x − c‖²/2`. Then `E_y[g] ≤ ⟨g, c⟩ < b` for `y ∈ S`, `E_x[g] = ⟨g, c⟩ + ‖x − c‖² > b`, and
`b > E_c[g] ≥ min g`. ∎

**Checks.** `mvp/checks/test_core.py::test_r6_separating_budget`.

**Lineage.** v14's VK0; the separating hyperplane theorem, finite form.

### R7 — Forbidden sets and rate limits in closed form
**Statement.** With `ℰ = {X}`, for a rate limit `(C, ε)` with `C ≠ X` and `p ∈ Δ`: `M_K(p) = kl(p(C)‖ε)` if `p(C) > ε`,
and `0` otherwise. For a forbidden set (`ε = 0`), `M_K(p) = ∞` if `p(C) > 0`, and the test that convicts at the first
outcome in `C` has level `0`.

**In plain terms.** Against a limit on how often something happens, the evidence of a breach depends only on how often
it happens; one forbidden outcome is decisive. How often a forbidden outcome happens, the breach rate `p(C)`, is then
the size to report beside the verdict.

**Proof.** Grouping `C` and `X ∖ C`, the chain rule gives `KL(p‖a) = kl(p(C)‖a(C)) + p(C)·KL(p(·|C)‖a(·|C)) +
p(X∖C)·KL(p(·|X∖C)‖a(·|X∖C))`; the last two terms vanish when `a` keeps `p`'s proportions inside each part. So
`M_K(p) = min_{v≤ε} kl(p(C)‖v)`, and `v ↦ kl(u‖v)` decreases on `[0, u]` and increases after. Under an acceptable
behaviour of a forbidden set an outcome in `C` has probability `0`. ∎

**Checks.** `mvp/checks/test_core.py::test_r7_rate_limit_closed_form`, `::test_r7_forbidden`.

**Notes.** With `C = X` the limit `a(X) ≤ ε < 1` is met by no behaviour, and the misalignment is `+∞`
(`::test_r7_forbidden`); the formula would give `log(1/ε)`.

**Lineage.** v14's VK1, VK2.

### R8 — A budget, by a one-parameter bet
**Statement.** With `ℰ = {X}`, for a budget `(g, b)` and `p` with `E_p[g] > b`: for `λ_max = 1/(b − min g)`,
`M_K(p) = max_{0≤λ≤λ_max} E_p[log(1 + λ·(g − b))]`, attained at some `λ* > 0`, and `h* = 1 + λ*·(g − b)` is a best bet.
If `E_p[g] ≤ b`, `M_K(p) = 0`.

**In plain terms.** Against a budget, the best bet stakes a fixed fraction of wealth on the cost coming in above the
budget: Kelly's criterion applied to overspending.

**Proof.** For `λ ∈ [0, λ_max]`, `h_λ = 1 + λ·(g − b) ≥ 0`, and `E_a[h_λ] ≤ 1` when `E_a[g] ≤ b`; so
`ψ(λ) = E_p[log h_λ] ≤ M_K(p)` by R2(i). `ψ` is concave, `ψ(0) = 0`, with right derivative `E_p[g] − b > 0` at `0`, so
its maximum is at some `λ* > 0` with `ψ(λ*) > 0`, and `h_{λ*} > 0` on the support `S` of `p`. Let
`D = E_p[(g − b)/h_{λ*}]`. If `λ* < λ_max`, `D = 0`, and `a* = p/h_{λ*}` on `S` has mass `E_p[1/h_{λ*}] = 1 − λ*·D = 1`
and `E_{a*}[g − b] = D = 0`. If `λ* = λ_max`, `D ≥ 0`; put `a* = p/h_{λ*}` on `S` and the remaining mass `λ*·D` on an
outcome of least cost, where `g − b = −1/λ*`, so `E_{a*}[g − b] = D − D = 0`. Either way `a* ∈ K` and
`KL(p‖a*) = ψ(λ*)`. ∎

**Checks.** `mvp/checks/test_core.py::test_r8_budget_dual`.

**Lineage.** v14's VK3.

### R9 — No worse than a reference on declared criteria
**Statement.** For a reference `r ∈ Δ` and criteria `G_1, …, G_m : X → ℝ`, the set
`D = {a : E_a[G_j] ≥ E_r[G_j] for every j}` is convex, closed, contains `r`, and is the same set for every criterion
`c + Σ_j λ_j·G_j` with `λ_j ≥ 0` added to the list. If `G_j = −1_C` and `r(C) = 0`, every behaviour of `D` gives `C`
mass `0`.

**In plain terms.** "No worse than the previous version on any of these criteria" is a convex closed requirement, so
R2–R4 and R6 apply to it; each criterion is a budget unless the reference already attains its best value, when it acts
as a forbidden set; and a reference that never does something forbids it, with no constraint written.

**Proof.** Each condition is a closed half-space met with `Δ` and contains `r`. For `G = c + Σ_j λ_j·G_j`,
`E_a[G] − E_r[G] = Σ_j λ_j·(E_a[G_j] − E_r[G_j]) ≥ 0`. With `G_j = −1_C`, `−a(C) ≥ −r(C) = 0`. ∎

**Checks.** `mvp/checks/test_core.py::test_r9_reference_criteria`.

**Lineage.** v14's TG1; v13's families of targets ([D3]).

### R10 — An overall rate limit when the world chooses the conditions
**Statement.** Let `K = {a : a_ℰ = p_ℰ, a(C) ≤ ε}`, `0 < ε < 1`, where every condition `E` with `p(E) > 0` has outcomes
both in `C` and outside it, with `w_E = p(E) > 0`, `u_E = p(C|E)` and `ū = Σ_E w_E·u_E`. If `ū ≤ ε`, `M_K(p) = 0`.
Otherwise `M_K(p) = Σ_E w_E·kl(u_E‖v(θ, u_E))`, where `v(θ, u) = ((θ + 1) − √((θ + 1)² − 4·θ·u))/(2·θ)` and `θ > 0`
solves `Σ_E w_E·v(θ, u_E) = ε`. And `M_K(p) ≥ kl(ū‖ε)`, the value with the conditions merged.

**In plain terms.** When the actor cannot choose how often each situation arises, a limit on its overall rate of
breaches is met by lowering the rate in every situation where it is positive, not by imagining other situations;
judging the record as one pool never overstates the evidence, and can understate it.

**Proof.** In each condition, as in R7, only the breach rate `v_E = a(C|E)` matters, and it can take any value in
`[0, 1]` since `E` meets both `C` and its complement: minimize `f(v) = Σ_E w_E·kl(u_E‖v_E)` subject to
`Σ_E w_E·v_E ≤ ε`. For `θ > 0`, `v ↦ kl(u‖v) + θ·v` is convex on `[0, 1]` and least at `v(θ, u)`: for `0 < u < 1` its
derivative `(v − u)/(v·(1 − v)) + θ` vanishes where `θ·v² − (θ + 1)·v + u = 0`, whose smaller root is
`v(θ, u) ∈ [0, u]`; for `u = 0` it is least at `0`; for `u = 1` at `min(1, 1/θ)`. `θ ↦ Σ_E w_E·v(θ, u_E)` is continuous,
tends to `ū > ε` as `θ → 0` and to `0` as `θ → ∞`, so some `θ` gives `ε`. For every feasible `v`,
`f(v) ≥ f(v) + θ·(Σ_E w_E·v_E − ε) ≥ Σ_E w_E·(kl(u_E‖v*_E) + θ·v*_E) − θ·ε = f(v*)`. The merged value is R7's against a
larger set, by R1(iii). ∎

**Notes.** The hypothesis matters: a condition inside `C` forces its breach rate to `1`, and then no acceptable
behaviour may exist (`mvp/checks/test_core.py::test_r10_condition_inside_c`). v14's VK6 omitted it (`NOTES.md` §1).

**Checks.** `mvp/checks/test_core.py::test_r10_overall_rate_limit`, `::test_r10_support_bot`.

**Lineage.** v14's VK6.

### R11 — A coarser record shows less, and refinement adds up exactly
**Statement.** Let `A ⊆ Δ`, `p ∈ Δ`, and `ℰ ⊑ 𝒢 ⊑ ℋ` partitions, `ℋ` refining `𝒢`.
(i) `M_A^𝒢(p) ≤ M_A^ℋ(p)`.
(ii) For a chain `𝒢_1 ⊑ … ⊑ 𝒢_k` ending at the finest partition, with `M_A(p) < ∞`,
`M_A(p) = M_A^{𝒢_1}(p) + Σ_{j<k} (M_A^{𝒢_{j+1}}(p) − M_A^{𝒢_j}(p))`, every term non-negative.
(iii) If `A` is **stated at** a partition `ℬ` refining `ℰ`, whether `a ∈ A` depending only on `a_ℬ`, then
`M_A(p) = M_A^ℬ(p)`.

**In plain terms.** A record that lumps outcomes together can only show less misalignment; refining it step by step
reveals non-negative amounts that add up exactly to the misalignment. And telling apart what the principal declared it
does not care about reveals nothing.

**Proof.** (i) The chain rule over the cells of `𝒢` gives `KL(p_ℋ‖a_ℋ) = KL(p_𝒢‖a_𝒢) + Σ_{C∈𝒢, p(C)>0}
p(C)·KL(p_ℋ(·|C)‖a_ℋ(·|C)) ≥ KL(p_𝒢‖a_𝒢)`; take the infimum over the same `a`. (ii) The sum telescopes; (i) gives the
signs. (iii) `M_A^ℬ ≤ M_A` by (i). For `a' ∈ A` with `a'_ℰ = p_ℰ`, let `a` give each cell `C` of `ℬ` the mass `a'(C)`,
split as `p` splits it when `p(C) > 0`, and as `a'` does otherwise; `a_ℬ = a'_ℬ`, so `a ∈ A` and `a_ℰ = p_ℰ`, and
`KL(p‖a) = KL(p_ℬ‖a'_ℬ)`. Take the infimum over `a'`. ∎

**Checks.** `mvp/checks/test_core.py::test_r11_refinement`, `::test_r11_indifference`.

**Lineage.** v14's RS1, RS3; v13's [P7], [C9].

### R12 — What a coarse record can bet on
**Statement.** Let `A' = {a ∈ A : a_ℰ = p_ℰ}` be convex and closed, and `ℛ` a partition refining `ℰ`. A bet against
`A'` constant on the cells of `ℛ` grows under `p` at most at `M_A^ℛ(p)`; when that is finite, one of them grows at
exactly that rate: `h = p(C)/a*(C)` on each cell `C` that `p` charges, `0` on the others, for an `a* ∈ A'` whose cell
masses are nearest to `p`'s.

**In plain terms.** A record that sees only cells can only bet on cells, and the best of those bets grows at the
misalignment visible at its resolution: R4's test works at the record's resolution, and convicts at that rate.

**Proof.** A function constant on cells is `k(C)` on each cell; `E_a[h] = E_{a_ℛ}[k]` and `E_p[log h] = E_{p_ℛ}[log k]`,
so `h` is a bet against `A'` exactly when `k` is one against `A'_ℛ`, the image of the compact convex `A'` by a linear
map, compact and convex. R2 on the cells. ∎

**Checks.** `mvp/checks/test_core.py::test_r12_coarse_bet`.

**Lineage.** v14's RS2.

### R13 — What a coarse record leaves open
**Statement.** Let `A` be closed, `ℛ` a partition refining `ℰ`, and `𝒫 = {p' ∈ Δ : p'_ℛ = p_ℛ}`, the behaviours a
record at `ℛ` cannot tell from `p`.
(i) The law of a sample at resolution `ℛ` depends on the behaviour only through `p_ℛ`.
(ii) `min_{p'∈𝒫} M_A(p') = M_A^ℛ(p)`, attained when it is finite.
(iii) So `M_A(p)` lies in `[M_A^ℛ(p), sup_{p'∈𝒫} M_A(p')]`, and no test on such samples can narrow either end; whether
any misalignment is hidden, `H_ℛ(p) > 0`, is neither verifiable nor refutable from them when `M_A` is not constant on
`𝒫`.
(iv) A declared feasible set `𝓕 ∋ p` narrows the interval to the values of `M_A` on `𝒫 ∩ 𝓕`.

**In plain terms.** From a record that lumps outcomes together, the actor can be charged at least what is visible, and
no test of that record can rule out that this is all, or show that it is. Bounding what is hidden inside the cells needs
a finer record, or a declaration of what the actor can do there.

**Proof.** (i) Each decision's cell has law `p_ℛ`; independent decisions give the product. (ii) Every `p' ∈ 𝒫` has
`M_A(p') ≥ M_A^ℛ(p') = M_A^ℛ(p)` by R11(i), since `p'_ℰ = p_ℰ`. If `M_A^ℛ(p) < ∞`, some `a*` attains it (compactness,
lower semicontinuity), positive on every cell `p` charges. Let `p'` give such a cell `C` the mass `p(C)` split as
`a*(·|C)`: `p' ∈ 𝒫` and `KL(p'‖a*) = KL(p_ℛ‖a*_ℛ)` by the chain rule. (iii) Both ends are values of `M_A` on `𝒫`; a test
on such samples has the same law under every member of `𝒫` by (i), so a test that declares `H_ℛ > 0` with probability at
most `α` at the `p'` of (ii), where `H_ℛ = 0`, does so with probability at most `α` throughout `𝒫`, and symmetrically.
(iv) The same on `𝒫 ∩ 𝓕`. ∎

**Checks.** `mvp/checks/test_core.py::test_r13_hidden_interval`.

**Lineage.** v14's RS4; v13's [D9], [P17].

### R14 — Misalignment factors exactly along what the actor could do
**Statement.** Let `𝓕_1 ⊇ 𝓕_2 ⊇ … ⊇ 𝓕_k` be sets of behaviours with `p ∈ 𝓕_k`, `M_A(p) < ∞`, and `m_j = m(𝓕_j)`. Then
`M_A(p) = m_1 + Σ_{j<k} (m_{j+1} − m_j) + E(p)`, with `E(p) = M_A(p) − m_k`, and every term is non-negative.

**In plain terms.** Start from the most capable actor one can declare and remove capabilities one at a time, down to
this actor's. Misalignment is exactly what even the most capable could not avoid, plus what each lost capability costs,
plus what this actor could have avoided and did not.

**Proof.** The sum telescopes; `m_1 ≥ 0`; `𝓕_{j+1} ⊆ 𝓕_j` gives `m_{j+1} ≥ m_j`; `p ∈ 𝓕_k` gives `M_A(p) ≥ m_k`. ∎

**Checks.** `mvp/checks/test_core.py::test_r14_factorization`.

**Lineage.** v14's FA1.

### R15 — Culpability is a requirement, and testable
**Statement.** Let `A` and `𝓕` be convex and closed, with `m(𝓕) < ∞`, and `δ ≥ 0`. Then `M_A` is convex and lower
semicontinuous on `Δ`, and `𝓕*_δ` is non-empty, convex and closed. So "culpable at margin `δ`" is the breach of a
derived per-decision requirement, `𝓕*_δ`, and R2 and R4 apply to it with the interface taken as known.

**In plain terms.** Whether the actor did as well as it could, within a declared margin, is itself a requirement built
from the declarations: bets can convict an actor of not doing its best, at a controlled error rate, as long as what it
could do is declared.

**Proof.** *Convex.* For `p_1, p_2`, `t ∈ [0, 1]` and `a_1, a_2` in `A` sharing their laws on `ℰ`, the mixture
`t·a_1 + (1 − t)·a_2` lies in `A` and shares the mixture's law, and `KL(t·p_1 + (1 − t)·p_2 ‖ t·a_1 + (1 − t)·a_2) ≤
t·KL(p_1‖a_1) + (1 − t)·KL(p_2‖a_2)`, term by term by the log-sum inequality, `u_1·log(u_1/v_1) + u_2·log(u_2/v_2) ≥
(u_1 + u_2)·log((u_1 + u_2)/(v_1 + v_2))`, which is Jensen's inequality for the convex `t ↦ t·log t`. Take infima.
*Lower semicontinuous.* If `p_n → p` with `M_A(p_n) ≤ c`, take `a_n` attaining (R2(ii)); a subsequence of `a_n`
converges in the compact `A` to some `a` with `a_ℰ = p_ℰ`, and `KL(p‖a) ≤ liminf KL(p_n‖a_n) ≤ c`, each term of `KL`
being lower semicontinuous jointly. *The set.* `m(𝓕)` is attained on the compact `𝓕`; `𝓕*_δ` is a sublevel set of a
convex lower semicontinuous function on a convex compact set. ∎

**Checks.** `mvp/checks/test_core.py::test_r15_culpability_set`.

**Lineage.** v14's culpability (Q74; `v14/interface.md`).

### R16 — A certificate for an average, whatever the dependence
**Statement.** Let `ℱ_k` be as in R4, and `Y_1, Y_2, …, Y_N ∈ [0, 1]`, each `Y_i` a function of the record up to
decision `i` (the indicator of a breach, `C` a union of the record's cells; or a rescaled cost constant on them), and
`μ_i = E[Y_i | ℱ_{i−1}]`. Let `λ > 0` and `α ∈ (0, 1)` be declared before the record. With probability at least `1 − α`,
for every `n ≤ N` at once, `(1/n)·Σ_{i≤n} μ_i ≤ (1/n)·Σ_{i≤n} Y_i + λ/8 + log(1/α)/(n·λ)`, and the same holds with `μ_i`
and `Y_i` exchanged; each side separately, both at once with probability at least `1 − 2α`. For a rate limit `(C, ε)`,
`Y_i = 1{x_i ∈ C}` and `μ_i = p_i(C)`, so the bound is on the average conditional breach rate `p̄_n(C)`: the record
**certifies** `p̄_n(C) ≤ ε` when the right side is at most `ε`, and **convicts** `p̄_n(C) > ε` when the exchanged bound
puts it above `ε`. Taking `λ = √(8·log(1/α)/N)` makes the margin at `n = N` equal to `√(log(1/α)/(2·N))`.

**In plain terms.** However the actor's decisions depend on each other, its average rate of breaches over the record is
pinned down by what the record shows, within a margin that shrinks like one over the square root of the record's
length, with an error rate fixed in advance, at every moment of the record at once. That is what lets a record certify
a pooled requirement, and convict one.

**Proof.** *Hoeffding's lemma.* If `Z` has mean `0` and `a ≤ Z ≤ b`, then `E[e^{λZ}] ≤ e^{λ²(b−a)²/8}`. For `a = b = 0`
it is trivial; otherwise `a < 0 < b` or `Z = 0`. By convexity, `e^{λz} ≤ ((b − z)·e^{λa} + (z − a)·e^{λb})/(b − a)` on
`[a, b]`; taking expectations, `E[e^{λZ}] ≤ (b·e^{λa} − a·e^{λb})/(b − a) = e^{φ(u)}` with `u = λ·(b − a)`,
`θ = −a/(b − a) ∈ (0, 1)` and `φ(u) = −θ·u + log(1 − θ + θ·e^u)`. Then `φ(0) = φ'(0) = 0` and `φ''(u) = t·(1 − t) ≤ 1/4`
with `t = θ·e^u/(1 − θ + θ·e^u)`, so `φ(u) ≤ u²/8` by Taylor's theorem. *The process.* Given `ℱ_{i−1}`,
`Z_i = μ_i − Y_i` has mean `0` and lies in `[μ_i − 1, μ_i]`, an interval of length `1`, so
`E[e^{λ Z_i} | ℱ_{i−1}] ≤ e^{λ²/8}`. Hence `W_n = exp(λ·Σ_{i≤n} Z_i − n·λ²/8)` is non-negative, `W_0 = 1`, and
`E[W_n | ℱ_{n−1}] ≤ W_{n−1}`. By R4(i), with probability at least `1 − α`, `W_n < 1/α` for every `n ≤ N`, which is
`λ·Σ_{i≤n}(μ_i − Y_i) − n·λ²/8 < log(1/α)`; divide by `n·λ`. The exchanged bound is the same with `Z_i = Y_i − μ_i`. ∎

**Checks.** `mvp/checks/test_core.py::test_r16_hoeffding_lemma`, `::test_r16_coverage_under_dependence`.

**Lineage.** New in the MVP (Q76): derived here from Hoeffding's lemma and R4; confidence sequences for averages of
conditional means are known in a sharper form (Howard, Ramdas, McAuliffe and Sekhon, not read by the executor).

### R17 — No record certifies every decision against a slight departure
**Statement.** Let `a_0, b_0 ∈ Δ` with `b_0 ≥ c·a_0` pointwise for some `c > 0`, `n ≥ 1` and `j ≤ n` fixed. Let actor
`g` draw every decision independently from `a_0`, and actor `b` do the same except at decision `j`, drawn from `b_0`.
For every event `E` of the record, `P_b(E) ≥ c·P_g(E)`. So a test that certifies "every decision was acceptable" with
probability at most `α` for `b`, when `b_0` is not acceptable, certifies `g` with probability at most `α/c`.

**In plain terms.** An actor that departs slightly from an acceptable behaviour at one decision chosen in advance
(`b_0 ≥ c·a_0` with `c` near `1`; for an extra breach of probability `η`, `c` is about `1 − η`) leaves a record almost
as likely as one that is acceptable everywhere. So a test that certifies the acceptable actor certifies the departing
one nearly as often: a gross departure can be caught, a slight one at a single decision cannot, and what a record
certifies is an average (R16), or, for a sample, the one behaviour behind it.

**Proof.** The two records' probabilities differ only in decision `j`'s factor: `P_b(r) = P_g(r)·b_0(x_j)/a_0(x_j) ≥
c·P_g(r)` for every record `r` with `P_g(r) > 0`; sum over the records in `E`. ∎

**Checks.** `mvp/checks/test_core.py::test_r17_one_decision`.

**Lineage.** New in the MVP (Q76, `v14/LIMITS.md`).

### R18 — The numbers that are not misalignment, and their estimates
**Statement.** For a sample of `n` decisions, and a function `y : X → [0, 1]`, the average `(1/n)·Σ_i y(x_i)` is within
`t` of `E_p[y]` with probability at least `1 − 2·e^{−2·n·t²}`. So the breach rate `p(C)`, the expected severity
`E_p[sev]/max sev` and the overrun of a budget are estimated with intervals of width of order `1/√n`, whatever their
misalignment.

**In plain terms.** Beside each verdict a report gives the sizes that matter to the principal, a breach rate, a
severity, an overrun, each with an interval; for a sample they come from averages with no further model, and for any
record R16 bounds their average conditional values.

**Proof.** R16 with `μ_i = E_p[y]` for every `i`, at a fixed `n`: the bound holds with probability `1 − α` for
`λ = √(8·log(1/α)/n)`, giving `t = √(log(1/α)/(2·n))`, that is `α = e^{−2·n·t²}`; both sides. ∎

**Checks.** `mvp/checks/test_core.py::test_r18_average_interval`.

**Lineage.** Hoeffding's inequality, as a case of R16.
