# Adversarial review of the Q69 pieces of v14

> **Status: the review of `NOTES.md` §32 (Q69), by a subagent of the executor's, not independent (rule (f)). Every
> finding was fixed in the commit that pushed the Q69 work; its check scripts stayed in the session's scratchpad and are
> not kept. Kept here so that its findings outlive the session.**

Reviewer: an executor session acting as adversarial mathematical reviewer, at the PI's executor's request. No file of
the repository was edited. Scripts used are in this scratchpad: `vk6.py`, `vk6b.py`, `vk7.py`, `misc.py`, `kB.py`;
`qa_out.txt` is the output of `probes/slides/qa_model.py` as run here.

Findings are listed most severe first. Severity: **error** (a false statement), **gap** (a missing hypothesis or step),
**overclaim** (says more than is proved), **wording**.

---

## A. Errors

### A1. `v14/severity.md`, "Severity and misalignment in training", and `v14/training.md`, "Severity and training": VK7 misapplied (error)
What is wrong, three things.
1. VK7 holds the actor's behaviour `p` fixed and varies `b`. A trainer whose budget changes produces a different actor
   (VK5: `a_ν` moves with `b`). So "tightening the severity budget by one unit raises the evidence … against the
   trained actor by about `λ*`" ignores the change in `p`. VK7 gives no total derivative of `b ↦ M_b(p_b)`.
2. A trainer that *keeps* the budget (VK5) produces an actor inside `K`, so `M = 0` and `λ* = 0`. `ν > 0` needs the
   budget to bind and be kept (`E_{a_ν}[g] = b`); `λ* > 0` needs it to be broken (`E_p[g] > b`). For one actor and one
   budget the two prices are never both non-zero. So "the trainer's `ν` and the bettor's `λ*` are two prices of the same
   budget" is wrong as stated, and H50 is ill-posed unless the trainer's budget differs from the principal's: other
   conditions, another σ-algebra (the shaper's `𝒮`), or another cost.
3. "raises the evidence *needed*" has the direction wrong. Misalignment is the *rate* at which evidence piles up. The
   evidence needed to accuse at level `α` stays `log(1/α)`. A tighter budget raises `M`, so *fewer* decisions are
   needed.

Fix: say that for a fixed actor, VK7 gives the sensitivity of the evidence rate to the principal's tolerance. Say that a
budget-keeping trainer produces an actor with zero misalignment against that same budget. Restate H50 for a trainer's
budget `(g_S, b_S)` that differs from the principal's `(g, b)`. Replace "evidence needed" with "evidence per decision".

### A2. `v14/training.md`, SH1, "In plain terms" and the paragraph after it: the gloss on the middle term is false (error)
The middle term `M_A(𝓕_T ∩ A_S) − M_A(𝓕_T)` is positive exactly when `A_S` leaves out every best feasible behaviour. It
does not measure "rewarding behaviours that the principal does not accept". Counterexample: `A_S ⊇ 𝓕_T`, a feedback that
fully rewards everything, unacceptable behaviours included. Then the middle term is `0`, and the whole cost lands in the
last term. Conversely, a feedback that rewards only acceptable behaviours, but none of the best feasible ones, has a
positive middle term. The proof (FA1) is correct. Only the label is wrong.

Fix: "what the feedback costs by not fully rewarding any of the best behaviours the actor could produce". Then add that
rewarding unacceptable behaviours shows up in the last term, through what the course picks among them. Naming the middle
term "outer misalignment" is fine as a definition, but L2 should test it.

### A3. `v14/resolution.md`, RS5(iii): coarsening a resolution need not shrink the feasible set (error)
For views, a coarser partition adds equalities, so (iii) holds. For resolutions, the coarse cell `A = A_1 ∪ A_2` comes
with its own environment split `e(·|A)`. The coarse feasible set is a subset of the fine one only if the splits are
consistent: `e(x|A) = e(A_i|A)·e(x|A_i)` for `x ∈ A_i`. Counterexample (`misc.py`): four outcomes; fine cells `{0,1}`
and `{2,3}`, each split `(½, ½)`; coarse cell `{0,1,2,3}` split `(0.7, 0.1, 0.1, 0.1)`. Then `p = (0.7, 0.1, 0.1, 0.1)`
is feasible for the coarse resolution and not for the fine one. Without nesting, FA1 does not apply to the chain. The
same gap is on the slide "RS5: the actor's σ-algebras are linear" ("coarser partitions give smaller sets").

Fix: add the consistency hypothesis to RS5(ii)–(iii). It holds, for example, when every split is the restriction of one
full-support `e` on `X`.

### A4. `v14/constraints.md`, VK4 Notes, "Requirements do not add": "no exact attribution … exists, unlike the factorizations of `factorization.md`" (error)
An exact attribution does exist. The chain `A_1 ⊇ A_1 ∩ A_2` telescopes:
`M_{A_1∩A_2} = M_{A_1} + (M_{A_1∩A_2} − M_{A_1})`, and both terms are non-negative. This is the same mechanism as FA1
and RS1, which also depend on the order of the chain. What fails is an *order-free* attribution in which each term is
the requirement's own misalignment. The joint can also be *larger* than the sum (`misc.py`). Take `p` uniform on three
outcomes, `K_1 = {a_1 ≤ 0.05}` and `K_2 = {a_2 ≤ 0.05}`. Each alone gives `0.396`, the sum is `0.793`, and the joint is
`0.934`. So "do not add" holds in both directions.

Fix: "the joint is at least the largest, can be smaller or larger than the sum, and splits exactly only along a chosen
order of the requirements, like FA1". Keep the per-requirement report.

### A5. `slides/mathematicians.md`, "Every factorization, named" (error / overclaim)
- The **[P54]** row contradicts v14's mixture principle. [P54]'s drift `δ` and dependence `κ` are evidence against "an
  acceptable behaviour deciding independently". v14 accepts any schedule of acceptable behaviours (VE2), and any
  decision that is acceptable given the past (VE3). So `δ` and `κ` are not parts of `M_A`, and "always exact,
  verifiable" does not apply to v14's number. The same row in `interface.md`'s table ("drift and dependence over time:
  CORE") needs the same correction.
- **VK6** is a closed form, not a factorization. Its per-condition terms `w_c·kl(u_c‖v_c*)` are evaluated at the joint
  minimizer. They are not the misalignment each condition would have alone. "verifiable" names no statement.
- **FA1, "computed"**: the last term `M_A(p̂) − m_k` depends on `p̂`. "`M_A(p̂) > m_k`" is an open set, since `M_A` is
  lower semicontinuous, so it is verifiable, not computed.
- **RS1, "verifiable at the finer σ-algebra"**: this needs the continuity hypothesis (B1 below).
- **"Every"** is false. The table leaves out [B2], [P45], [P46], [P39], [P50], [P8], [P6], [P44] and [P49], which are in
  `factorization.md`'s own table.

Fix: drop the [P54] and VK6 rows, or move them under "other decompositions"; give FA1's last term the status
"verifiable"; retitle the slide "The factorizations of v14".

---

## B. Gaps

### B1. `v14/resolution.md`, the verification-status table: the hypothesis "requirements whose members have full support" excludes every rate limit, budget and dominance set, and the slide's R1 and R2 (gap)
These sets all contain behaviours without full support, so the table, as stated, does not cover the example it is used
for. The hypothesis is sufficient, but it is much stronger than needed. A weaker sufficient one, derived here: **`A`
convex and closed, with one full-support member.** Then `M_A^𝒢` is finite, convex and lower semicontinuous on the
simplex. It is also upper semicontinuous, by this argument. For `x_n → x`, write `x_n = (1 − t_n)·x + t_n·y_n`, with
`t_n = ‖x_n − x‖_∞ / min_{x(i)>0} x(i) → 0`, which puts `y_n` in `Δ`. Convexity gives
`M(x_n) ≤ (1 − t_n)·M(x) + t_n·max_{vertices} M`. So `M_A^𝒢` is continuous. The same argument works on a product of
simplices, which covers conditions with fixed frequencies. This covers rate limits with `ε > 0`, budgets with
`b > min g`, and R1 ∩ R2.

Also, "with the principal's `ℬ` between them" ("The three positions together") assumes `ℛ ⊑ ℬ`. Say so: in general the
record's partition and the principal's need not be ordered.

### B2. `v14/interface.md` and the slide "Factoring by capabilities": `K = ∞` is generic, and the slide's reason is incomplete (gap)
interface.md's claim is correct, and it can be sharpened. `𝓕*` is convex, so the union of the supports of its members is
the support of one member. Hence `K = ∞` *exactly when* `p̂` charges an outcome that no best behaviour charges.
1. The slide gives only one reason, short benign answers. The new model also refuses 5% of benign questions, which the
   best behaviour never does. Read at the principal's `ℬ`, where S and L are merged, culpability still diverges. I
   computed it with the probe's machinery (`kB.py`): `0.341` at a tolerance of `1e-6` on the best misalignment, and
   `0.418` at `1e-8`. It grows as the tolerance shrinks. So `K = ∞` is not an artefact of the S/L distinction.
2. Best feasible behaviours of a convex programme over a polytope typically sit on its boundary, often with a
   deterministic policy. So `K ∈ {0, ∞}` for most actors. This is a property of the definition, not a finding of the
   example. It should be stated in interface.md next to the definition.
3. When `M_A(𝓕) < ∞`, `K > 0 ⇔ E > 0 ⇔ p̂ ∉ 𝓕*`. "K for the verdict" therefore adds a growth-rate reading (VE1, VE3) but
   not a different verdict. Say so.

### B3. Slide "FA2: the Pythagorean form": missing hypotheses (gap)
`K = E + min R_f ≥ E` needs every `f ∈ 𝓕*` to have a nearest acceptable `a_f ∈ Δ°`, and `M_A(𝓕) < ∞`
(`factorization.md`, FA2). The slide states only `a° ∈ Δ°`.

### B4. `v14/training.md`, SH1: `𝓕_T ∩ A_S` has no common space (gap)
`A_S` is a set on pairs over the shaping conditions `𝒞_S` (frequencies `w^S`), stated at `𝒮`. `A` is on `𝒞_D`
(frequencies `w^D`). The intersection, and `M_A` of it, need behaviours as tuples over `𝒞_S ∪ 𝒞_D`, with `A_S` a
cylinder set, and need a statement of the frequencies that `M_A` uses. Without that, SH1's terms are undefined whenever
`𝒞_S ≠ 𝒞_D`, which is exactly the misgeneralization case the file wants to cover.

### B5. `v14/severity.md`, iso-risk tolerances (gap)
- With `ε_k = R/s_k`, each class carries expected harm at most `R`, so `m` classes together allow up to `m·R`, not `R`.
  This intersection of rate limits is not the budget `E_a[s] ≤ R`, and it is not the same shape of set.
- A class with `s_k ≤ R` gets `ε_k ≥ 1`, which is not a rate limit (`constraints.md` asks for `ε < 1`). The class is
  then unconstrained, and the text should say so.
- `s_k` needs severity to be constant on a class, or a rule such as the class maximum.
- `s : X → [0, ∞]` with value `∞` is not a budget cost (`g : X → ℝ`). The budget form must be split into a forbidden
  set on `{s = ∞}` plus a budget on the finite part, and only then do VK3 and VK7 apply.

### B6. `v14/severity.md`, report table: "price `λ*` … computed (VK7)" (gap)
`λ*` depends on `p̂`. It is estimated from the record, not computed from the declarations. It is defined only for a
single budget with `E_p̂[s] > b`, so the rate-limit-per-class form has no single `λ*`.

### B7. `v14/resolution.md`, RS4(iii) (gap, minor)
- "Both ends belong to behaviours in `𝒫`": the upper end is attained when `A` is convex, as the proof shows. For `A`
  that is only closed, `M_A` is only lower semicontinuous, and a supremum over `𝒫` need not be attained. Restrict the
  claim to convex `A`, or write "sup".
- "neither verifiable nor refutable … unless `M_A` is constant on `𝒫`" mixes a pointwise condition with a property of a
  statement. State it as: the set `{p : H_ℛ(p) > 0}` is not a union of fibres `𝒫` whenever some fibre carries a
  non-constant `M_A`, and a statement that is not a union of fibres is neither verifiable nor refutable from samples at
  `ℛ`. RS4 is proved for samples; the slide drops "samples", although the setting slide says records are not assumed
  independent.

---

## C. Overclaims and wording

- **C1. VK7, plain terms, and `severity.md`, "There is no fixed exchange rate".** VK7 shows that `M` is convex and not
  affine in `b`, with a slope that depends on `p`. It does not show that no exchange rate could be *declared*: the file
  itself allows one for log-wealth. "meet only through this price" also overclaims. `λ*` has units of 1/cost and
  rescales with `g`. Fix: "VK7 shows that the marginal rate varies with the actor and the budget, so no constant
  converts units of cost into nats of evidence".
- **C2. VK6, plain terms, "more where it breaches more".** Stationarity gives `u − v* = θ·v*(1 − v*)`. The absolute
  reduction increases with `u` only while `v* ≤ ½`. `v(θ, ·)` is convex with `v(θ, 0) = 0`, so the *relative* reduction
  `1 − v*/u` never increases with `u`. Counterexample (`vk6b.py`): `w = (½, ½)`, `u = (0.50, 0.95)`, `ε = 0.6` give
  reductions `0.164` and `0.086`. Fix: "lowers each condition's rate, by `θ·v(1 − v)`; more where it breaches more while
  the rates stay below ½". The formula itself is correct (C-list below).
- **C3. VK0 Notes, the bipolar remark.** "wins under `x`" holds in expectation, `E_x[h] > 1`, for every admissible `λ`.
  Positive growth needs small `λ`. At `λ = 1/(b − min g)`, `h = 0` on `argmin g`, and the growth is `−∞` if `x` charges
  it. Fix: "has expected payoff above 1 under `x`". The correspondence itself is correct.
- **C4. Slide "A family of targets".** "one budget per generator" needs a finitely generated cone. A generator with
  `E_r[G_i] = max G_i` gives a forbidden set, not a budget (TG1's Notes say so; the slide does not). "first-order
  stochastic dominance" applies to a total ranking; for a preorder it is dominance on upper sets.
- **C5. Slide "Doing no worse is not pursuing": "v13's own measure is a case of TG1".** It is not `M_{D(p̂)}(p̂)`, which
  is `0` since `p̂ ∈ D(p̂)`. It is a difference of departures from `q`, with the requirement fitted to the actor, which
  [A5] forbids for a standard. Fix: "has the form of a comparison with TG1's set, with the actor as reference". The
  slide also drops TG2(iv)'s `p̂ ∈ Δ°`.
- **C6. Slide VF1: "Every label below gets one of three statuses".** RS4's "neither" and RS3's "declared" are two more.
- **C7. Slide "Why requirements are convex": "So requirements are convex".** What the premises force is that a valid
  test enforces only the hull. A principal can still declare a set that is not convex (`LIMITS.md`). "closing changes no
  number" is true of `M_A`, but closing changes verification status: membership of an open set is verifiable.
- **C8. Slide "What is open": "shifts of `1/√(n·I)` escape every test".** Such shifts are detected with power bounded
  away from both `α` and `1`; they do not escape. H43 is also a hypothesis, not a result.
- **C9. Slide "What a record shows", Sanov.** No record of 400 decisions has exactly the new model's shares
  (`240·0.423 = 101.52`). State the bound for types near `p̂`.
- **C10. Slide "Verdicts and evidence": R1 `0.0456`** is a double rounding. VK6 gives `0.045545` (checked independently
  here: `θ = 4.232`, `v* = (0, 0.00383, 0.0603)`), which is `0.0455` to four places.
- **C11. Slide "The best bet".** The maximum is attained only when `M_A(p) < ∞` (VE1(ii)–(iii)).
- **C12. SN1(ii).** "the one most likely": the maximum-likelihood member need not be unique, for example VK3's `λ_max`
  case, where mass may be split among the least-cost outcomes. `s/a*` is a bet fitted in sample, not one fixed in
  advance.
- **C13. resolution.md table, "the actor cannot tell `c` from `c'`".** The status "refutable" belongs to its consequence
  `p̂(·|c) = p̂(·|c')`, not to the claim about capability (VF3). Say so in the row.
- **C14. interface.md.** "whenever the actor produces an outcome no best feasible behaviour produces" should read
  "exactly when" (B2).
- **C15. VK7, an understatement, not an error.** `ψ` is strictly concave, because some `x ∈ S` has `g(x) ≠ b`, so `λ*`
  is unique. `λ*` is also continuous in `b` across the switch to `λ_max`. In that regime the envelope computation gives
  `−λ*·E_p[1/h*] − D·λ*² = −λ*·(1 − λ*D) − λ*²D = −λ*`, so `M` is in fact `C¹` on `(min g, ∞)`. Numerically (`vk7.py`),
  on 166 instances at `λ_max`, `|M′ + λ*| ≤ 1.0e-7`, and a sweep of `b` shows `λ*` continuous across the switch.
  "wherever `λ*` is continuous" is true but weaker than the truth. Strengthening it needs a proof of continuity, by
  Berge's theorem read in an open text or directly.
- **C16. VK6 Notes.** "one- parameter" has a stray space.

---

## D. Checked and correct (one line each)

- **RS1** (i)–(ii): chain rule and telescoping; correct.
- **RS2**: reduction to cell bets plus VE1 on `A_ℛ`, which is compact and convex; correct.
- **RS3**: the construction keeps cell masses and makes the within-cell terms zero; correct, including without full
  support.
- **RS4** (i)–(ii), and (iii) for convex `A`: correct, including the vertex maximum by convexity.
- **RS5** (i)–(ii): correct as linear sets with a full-support member. The gap in (iii) is A3.
- **TG1** (i)–(iv): correct.
- **TG2** (i)–(iii): correct by the variance and covariance derivatives. (iv) agrees with [P53](iv), whose hypotheses,
  `p̂, q ∈ Δ°`, are stated.
- **SN1** (i): the method of types with `P_s(T(s)) ≥ 1/k_n` and `k_n ≤ (n + 1)^{|X|−1}`; correct. (ii) and (iii):
  correct, subject to C12.
- **VK6**: the quadratic `θv² − (θ + 1)v + u` is correct. Its smaller root lies in `[0, u]`. The edge cases are correct:
  `u = 0` gives `0`, and `u = 1` gives `min(1, 1/θ)`. `θ` exists by continuity, with the limits `ū` as `θ → 0` and `0`
  as `θ → ∞`; it is also unique, since `v` decreases strictly in `θ` when `u > 0`. The Lagrangian sufficiency argument
  is valid. The pooled bound `M_K ≥ kl(ū‖ε)` holds. The closed form matches SLSQP within `2.3e-11` on 300 random
  instances, including `u_c ∈ {0, 1}` (`vk6.py`).
- **VK7**: the inequality, convexity, the subgradient and the derivative are correct. The `λ* = λ_max` case raises no
  problem: the proof uses `a*` only on `S`, where `a* = p/h*` in both cases of VK3, and the step
  `Σ_{x∈S} a·h* ≤ E_a[h*]` needs only `h* ≥ 0`. The first inequality fails by at most `5e-13` on a grid of 25 values of
  `b'` over 400 instances.
- **interface.md, derived requirement**: `M_A` is convex, as a partial minimization of the jointly convex `KL` over
  convex `A`, and lower semicontinuous, since `A` is compact and `KL` jointly lower semicontinuous. So `𝓕*`, a sublevel
  set on convex closed `𝓕`, is convex and closed. `K = M_{𝓕*}(p̂)` holds by definition. Correct. When `M_A(𝓕) = ∞`,
  `𝓕* = 𝓕` and `K = 0`; consistent.
- **VK0** proof and **"Declaring a specification"**: no mathematical error. The table's TG1 row inherits TG1(ii)'s
  finitely-generated hypothesis.
- **SH1**: the proof (FA1) is correct; the problems are A2 and B4.
- **severity.md** numbers: `kl(2e-6‖1e-6) = 3.86e-7` and `kl(0.2‖0.1) = 0.0444`; both correct.
- **The slides' example numbers** reproduce in `probes/slides/qa_model.py`, re-run here (`qa_out.txt`): `0.04744` and
  `0.02274`, the interval `[0.02274, 0.14830]`, the FA1 split `0 + 0.00369 + 0.04376`, and `e^{−400·0.04744} = 5.7e-9`.
- **CVaR counterexample** (`v14/README.md`, `v14/LIMITS.md`, the slides): verified directly and by the
  Rockafellar–Uryasev form `min_t {t + E[(L − t)_+]/α}`. Loss 1 with probability 0.06 has CVaR `0.6`; loss 0.6 for sure
  has CVaR `0.6`; their even mixture `(0.47, 0.5, 0.03)` has CVaR `0.72`. The conclusion is right, and stronger than
  stated. The Rockafellar–Uryasev form is a minimum over `t` of functions affine in the distribution, so CVaR is
  *concave* under mixtures of behaviours, and mixing never lowers it below the average of the parts. Its sublevel sets
  are therefore not convex in general. The words "under mixtures of behaviours" are essential: CVaR *is* convex in the
  random variable on a fixed probability space, which is the usual sense in which it is called a coherent risk measure.
  On the outcomes `{0, 0.6, 1}`, the hull that is enforced is the single budget `a(1) + 0.06·a(0.6) ≤ 0.06`, with
  extreme points `δ_0`, `δ_{0.6}` and `(0.94, 0, 0.06)`. The text could state it, to show what the principal actually
  gets.
