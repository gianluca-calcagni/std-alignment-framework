# B — Dictionary

> **Status: v6.3.** Changes in R5: §2 (optimizer-dependent tail exposure), §4 (B4 generalized by Core
> Prop. 21), §9 (power-seeking corrected). v6.2: rebuilt after review R2. Prior art found in review R3 is cited at each entry. Added:
> §11 quantitative genetics (v6.1); B7(e), rational inattention, and §12 human choice (v6.2). Entries are organized by what the core can *derive*, not by
> field: each asks for a derivation from Core, or says there is none.

## Abstract, in plain terms

Results from other literatures, written in the core's terms. v5 used three slots — error, capacity,
exchange rate — and a product between the first two. v6 replaces the product with a pairing: **the
divergence used to limit the actor determines which measure of the error must be controlled**
(Core §6). Several entries that v5 kept separate (error–regret mismatch, concentrability,
catastrophic Goodhart, the χ²-regularization proposal) turn out to be points on one scale.

Every theorem cited here belongs to someone else. What the dictionary adds is the demonstration that the
core derives them, or the statement of exactly where it cannot.

---

## 0. How to read an entry

| Slot | Meaning |
|---|---|
| **capacity** | the divergence that limits how far the actor may move from the reference |
| **error functional** | the functional of the error that the capacity makes relevant (its conjugate) |
| **unit** | whether the entry needs an external unit for value (Core Prop. 12) |
| **actor** | the actor model the entry assumes: Gibbs tilt, capacity maximizer, or other |
| **verdict** | **derived** (follows from a stated result in A), **stated** (fits the slots, not derived), or **does not translate** |

And **what moves**: what the entry exports to the others, or imports.

---

## 1. Anchor

| | |
|---|---|
| **Result** | `β·R_J = KL(p̂‖p*)` (Thm 1); worst-case regret under capacity `δ` is the width `w_δ(E)` (Thm 5); `β·R_J = D_⊥ + D_∥ + X_anti` on the half-ray (Thm 13(b)); every regret notion lies on `M(t)` (Thm 17) |
| **Capacity** | KL to the reference |
| **Error functional** | the CGF of `E` under `p*` (soft); the support function of `C_δ` at `E` (capacity) |
| **Unit** | `R_J` needs one; `β·R_J`, `D_⊥`, `sign(t̂)` do not |
| **Actor** | Gibbs / capacity maximizer |

**What moves:** the replacement of a product bound by an identity and a support function. Everything below
reads that object at a particular capacity, divergence, or order of approximation.

---

## 2. The conjugacy scale *(merges four v5 entries)*

Core Prop. 10: each capacity divergence pairs with a norm of the error. Four literatures sit at four
points of this one scale.

| Capacity | Error functional | Literature | What the core derives |
|---|---|---|---|
| TV | `osc(E)` (`L^∞`) | v5 anchor | Remark 7.1; dominated by Props 2 and 7 |
| KL | CGF of `E` under `q` | Kwa, Thomas & Garriga-Alonso (NeurIPS 2024), *catastrophic Goodhart* | Prop. 11(i): if `log 1/q(E>m) = o(m)`, KL-limited exposure is infinite at every budget |
| χ² | `Var_q(E)` (`L²`) | Laidlaw, Singhal & Dragan (ICLR 2025): χ² occupancy-measure regularization | Prop. 11(ii): χ²-limited exposure `≤ √(δ·Var_q E)` |
| `D_∞` | `E_q\|E\|` (`L¹`) | concentrability in offline RL; Fluri, Lang, Abate, Forré, Krueger & Skalse (ICML 2025), *error–regret mismatch* | Prop. 10(d): `E_p\|E\| ≤ e^{D_∞(p‖q)}·E_q\|E\| ≤ E_q\|E\|/min q` |

**Verdict: derived**, for the exposure statements. What is **not** derived:

- **Kwa et al.** Their result that such policies obtain *no more utility than the base model* is not derived
  here; Prop. 11 gives only the exposure half.
- **Laidlaw et al.** Their guarantee is for occupancy measures in MDPs; the core is static.
- **Fluri et al.** The exact thresholds are not re-derived. The `D_∞` row reproduces the qualitative shape of
  their result — sufficiently low expected error suffices, but "sufficient" depends on how thin the data
  distribution is — without checking that their constants are `1/min q`.

**v5 read Fluri et al. as "training error cannot fill the epistemic slot". That is wrong.** Training error
fills the slot in the norm conjugate to the capacity. `L¹` error under the data pairs only with a
density-ratio (`D_∞`) capacity; KL capacity needs exponential moments of the error; χ² needs its variance.

**Prior art for this entry as a whole.**
- **Huang, Zhan, Xie, Lee, Sun, Krishnamurthy & Foster** (ICLR 2025, χPO) argue that KL regularization is
  too weak to prevent overoptimization, and that χ² regularization is preferable, via coverage and
  single-policy concentrability. That is the statistical counterpart of the KL/χ² rows.
- **Mroueh (2024); Mroueh & Nitsure (TMLR 2025)** give the KL transportation bound (sub-Gaussian tails)
  and Rényi-divergence refinements for reward improvement. That is the KL row, and the `D_α` family of
  Core Prop. 10(d), applied to reward rather than error.

What was not found stated elsewhere is the organization of the four rows as one conjugate pairing.

**The exposure bounds are worst cases over the capacity set (tiers 1–2). Actual optimizers can sit far
inside them (R5, T-F).**
- At matched proxy gain, best-of-n moves much less mass onto a single overrated state than the Gibbs actor,
  because its weight on any state is at most `n·q(x)` (`verify.py` V26).
- The Gibbs actor's weight on that state grows like `e^{βM}`.
- So Kwa et al.'s catastrophic-Goodhart mechanism is a property of **KL-regularized optima**, not of every
  optimizer inside a KL budget.

**What moves:** **choosing a regularizer is choosing which norm of reward-model error must be measured.**
This is the concrete form of v5's open question about the divergence order (v5 A6). The answer is that the
order is structural: at order 1 (KL), heavy-tailed-but-finite-variance errors are uncontrolled at any
budget; at order 2 (χ²) they are controlled.

---

## 3. Goodhart variants — Manheim & Garrabrant (2018)

| Variant | Core reading | Verdict |
|---|---|---|
| regressional | small-capacity asymptote: `w_δ(E) = 2√(2δ·Var_q E) + O(δ)` (Prop. 6(ii)); first-order gain `β·Cov_q(F̂,F)` (Prop. 14) | **derived** |
| extremal | large-capacity asymptote: `w_δ(E) = osc(E)` (Prop. 6(iii)); terminal regret set by argmax agreement (Prop. 14(iii)) | **derived** |
| causal | the proxy–target relation changes under intervention — needs interventional structure the core lacks | does not translate |
| adversarial | another agent optimizes against the proxy — needs equilibrium (Boundary §4) | does not translate |

**What moves:** Theorem 9 — the two derived variants are the two ends of one support function, and **no
capacity-free ranking of errors exists** because the regime switches between them. Karwowski et al.
(ICLR 2024; imported in v5, not re-examined) give the polytopal, MDP-occupancy counterpart with early
stopping; the Gibbs setting here is smooth, and v5 already noted that the sharp turn is weaker there.

**Prior art: El-Mhamdi & Hoang (2024).** In a selection (top-quantile) model they show that the strength of
Goodhart's law is decided by the tail of the discrepancy. Gaussian discrepancies give only a *weak*
Goodhart effect; power-law discrepancies heavier than the goal give a *strong* one, where optimizing hurts
the goal. A follow-up (arXiv:2505.23445) drops their independence assumption. Their weak/strong
distinction and this entry's regressional/extremal asymptotes are the same phenomenon, read in a selection
model and in a KL-tilt model respectively.

---

## 4. Reward-model overoptimization — Gao, Schulman & Hilton (ICML 2023)

Their empirical forms, with `d = √KL(π‖π_init)` (a **realized** travel from the reference):
`R_bon(d) = d(α_bon − β_bon·d)` and `R_RL(d) = d(α_RL − β_RL·log d)`.

**Proposition B4 (Gaussian Gibbs path).** *[Assumes (E) along the path.]* Let `X = ℝ^k`, `q = N(0, I)`, `F = u·x`, `F̂ = w·x`, and
`ρ = u·w/(|u||w|)`. Along the Gibbs path `p_{F̂,λ}`, with `d = √KL(p‖q)`:

```
E_p F − E_q F = √2 · ρ · sd_q(F) · d     exactly, for every d ≥ 0.
```

*Proof.* `p_{F̂,λ} = N(λw, I)`, `KL = λ²|w|²/2`, so `λ = √2·d/|w|`, and `E_pF = λ·u·w`. ∎
*Check.* `verify.py V9`: gold gain / `d` = 0.8485 = `√2·0.6` at `d` = 0.14, 0.71, 1.41, 2.12.

Consequences:

- **Generalized in v6.3 (Core Prop. 21):** under any affine regression of target on evaluator, *every*
  optimizer whose weights depend on behaviour only through the evaluator has gold gain exactly proportional
  to proxy gain. Covered: Gibbs, threshold selection, best-of-n and vanilla policy gradient from a uniform
  reference. The independent review confirmed it for vanilla policy gradient (R5, T-D).
- **For jointly Gaussian intent and evaluator under the reference, the KL-optimal path never
  overoptimizes.** Gao et al.'s downturn therefore requires non-Gaussian joint structure — tails
  (Core §11, item 6).
- **Prediction, untested.** The leading coefficient should satisfy `α ≈ √2·ρ_q(F, F̂)·sd_q(F)` for the Gibbs
  path. For best-of-n, in the Gaussian case, the gold gain is `ρ·sd·E[max of n normals] ≈ ρ·sd·√(2 log n)`,
  and the standard BoN expression `log n − (n−1)/n` is an **upper bound** on `KL(π_BoN‖π_ref)` (Beirami et
  al. 2024; the conditions under which it is attained were not checked here). With it, the same slope is
  approached as `n → ∞` (slowly), up to that bound. RL training paths are not Gibbs paths. That is consistent with their finding that RL is less
  KL-efficient than BoN, but it is not derived.
- **Prior art.** Mroueh (2024; Mroueh & Nitsure 2025) proves that the `√KL` law is an upper bound on reward
  improvement when the reward has sub-Gaussian tails under the reference, for both the Gibbs policy and
  best-of-n. The Gaussian identity above is the case in which that bound is attained. The "Gaussian ⇒ no
  downturn" statement is the tilt counterpart of El-Mhamdi & Hoang's weak Goodhart law.

**Verdict: derived for the leading coefficient under Gaussian structure; curvature terms not derived.**
**What moves:** a concrete check of the core against published coefficients (C9). It also
shows that the v5 prohibition on realized distances in the capacity slot was wrong: the best-established
empirical law in the area is written in one.

---

## 5. When does optimizing a proxy help at all? — Laidlaw et al.; Holmström & Milgrom (1991)

Core Prop. 14(ii): `T'(0) = −Cov_q(F̂, F)`. **For the entropic actor**, a small amount of optimization
helps iff evaluator and intent are **positively correlated under the reference**. For other smooth
optimizers the criterion is the covariance in the optimizer's own geometry: for a vanilla policy gradient,
`q²`-weighted (Core Prop. 22). The two can disagree in sign (R5, T-B).

- **Laidlaw, Singhal & Dragan** define a proxy by positive correlation with the true reward under a
  reference policy. In this model their definition is exactly the condition that small optimization helps.
  **Derived** (first order).
- **Holmström & Milgrom, multitasking.** Take a measured component `F_m`, an unmeasured one `F_u`,
  `F = F_m + F_u`, and evaluator `F̂ = F_m` (so `E = −F_u`). Then
  `T'(0) = −(Var_q F_m + Cov_q(F_m, F_u))`, and optimization initially **hurts** iff
  `Cov_q(F_m, F_u) < −Var_q F_m`. Their zero-incentive corner corresponds to this condition. In their model
  the substitution between tasks comes from the effort cost; **here it must be carried by the reference**, as
  a negative covariance between the measured and unmeasured components. Their risk-sharing structure (noise,
  risk aversion) has no counterpart. **Derived at first order; the full contract result is not.**
  **Prior art.** Wang & Huang (2026, arXiv:2603.28063) instantiate the Holmström–Milgrom multitask model
  for AI alignment in full, with a computable distortion index. This entry is its first-order special case
  in the tilt model.

**What moves:** a one-line criterion — the sign of `Cov_q(F̂, F)` — shared by an ML definition and a
contract-theory result, plus the terminal criterion (argmax agreement) that neither states.

---

## 6. Holmström (1979) — the informativeness principle

**v5 claimed:** conditioning the evaluator on a feature uninformative about the intent strictly increases
regret. **False.** Counterexample (`verify.py V9`): behaviours are (content, length); the intent depends
on content only (`corr_q(F, N) = 0`); the error is length bias, `E = 0.8N + noise`. Then
`R_J(E) = 0.2586` and `R_J(E − 0.8N) = 0.1506` at `β = 4`. Length penalties in RLHF are the practical case.

**Proposition B6.** *[Assumes (E): `R_J(·)` is read as a function of the error.]*
(i) **Exact negative half.** Let `X = X₁ × X₂`, `q = q₁ ⊗ q₂`, with `F`, `E` functions of `x₁` and `N` a
function of `x₂`. Then `β·[R_J(E + N) − R_J(E)] = KL(p_{N,β}^{(2)} ‖ q₂) > 0` for non-constant `N`.
(ii) **Positive half, second order.** For fixed `E`, `N` (non-constant), the minimizer `c(β)` of `R_J(E + cN)`
satisfies `c(β) = c*(β) + O(β)` as `β → 0`, where `c*(β) = −Cov_{p*}(E, N)/Var_{p*}(N)`. So a signal enters
the evaluator iff it is (linearly) informative about the **error**.

*Proof.* (i) The tilt factorizes: `p_{F+E+N,β} = p^{(1)}_{F+E,β} ⊗ p^{(2)}_{N,β}` and `p* = p*^{(1)} ⊗ q₂`, and KL
is additive over products. (ii) By Core Cor. 1.3,
`β·R_J(E + cN) = (β²/2)·Var_{p*}(E + cN) + O(β³)`, uniformly for `c` in compacts. The quadratic has
curvature `β²·Var_{p*}(N)`, so a uniform `O(β³)` perturbation moves its minimizer by `O(β)`. ∎
*Check.* V9: (i) the added regret 0.28656971 equals the KL term to 8 digits. (ii) numerical argmin vs `c*`
at `β = 4, 1, 0.25, 0.05`: (−0.954, −0.871), (−0.855, −0.853), (−0.833, −0.833), (−0.827, −0.827).

**Verdict: derived, with a changed condition.** The condition is informativeness about the error, not
about the intent.
**The mechanism is not Holmström's.** His cost of an uninformative signal is a risk premium paid to a
risk-averse agent; here there is no risk, and the cost is behavioural distortion. The correspondence is
structural (both are sufficiency/regression conditions), not mechanistic.

---

## 7. Ashby (requisite variety); Conant & Ashby (good regulator)

**v5 claimed** that requisite variety "is the boundedness term of the same decomposition", resolving a sign
conflict and explaining an interior optimum. **As stated, verbal**:

- The open-loop core has no disturbance variable; requisite variety is a statement about a regulator
  counteracting one.
- The only property used was that `g` decreases with capacity, which is monotonicity of the value of
  information (Stratonovich) and needs no Ashby.
- The explained "interior optimum when the error is large" had already failed the v5 check.
- The "dangerous" side is not monotone (Core Prop. 14).

**The closed-loop lift, in which the translation is a theorem.** Let a disturbance `D ~ ρ` on finite `𝒟`,
a regulator policy `π(r|d)` with reference `q` on actions, and an outcome `Z = φ(D, R)`, with `φ(·, r)`
injective for each `r` (Ashby's regulation-table condition).

**Proposition B7.**
(a) `E_d KL(π(·|d) ‖ q) = I(D;R) + KL(π̄ ‖ q) ≥ I(D;R)`, where `π̄` is the action marginal.
(b) **(Conant)** `H(Z) ≥ H(D) − I(D;R)`.
(c) If the intent is target-hitting, `F = 1{Z = z₀}`, and `g = P(Z ≠ z₀)`, then under closed-loop capacity
`E_d KL(π(·|d)‖q) ≤ δ`:  `h(g) + g·log(|𝒵| − 1) ≥ H(D) − δ`, for every such policy, in particular the
intended one. Since the left side increases in `g` on `[0, 1 − 1/|𝒵|]`, this is a floor on the boundedness
cost that decreases with capacity.
(d) Theorem 1 holds per disturbance: for `π*(·|d) ∝ q·e^{βF(d,·)}`,
`J(π*) − J(π) = (1/β)·E_d KL(π(·|d) ‖ π*(·|d))`.
(e) **(Rational inattention: an endogenous reference; added in v6.2.)** Let the information cost be the
mutual information, `J(π) = E[F(D,R)] − (1/β)·I(D;R)`. Equivalently, the reference is the actor's own
action marginal, optimized jointly with the policy (Sims 2003; Matějka & McKay 2015). Let `π*` maximize
`J` with a full-support marginal `π̄*`. Then for every `π` with `π(·|d) ≪ π*(·|d)`:

```
J(π*) − J(π) = (1/β)·[ E_d KL(π(·|d) ‖ π*(·|d)) − KL(π̄ ‖ π̄*) ],
```

and the correction satisfies `0 ≤ KL(π̄‖π̄*) ≤ E_d KL(π(·|d)‖π*(·|d))` (data processing).

*Proof.*
(a) Standard decomposition of expected conditional KL.
(b) `H(Z) ≥ H(Z|R) = H(D|R)` (injectivity) `= H(D) − I(D;R)`.
(c) (a), (b), and `H(Z) ≤ h(g) + g·log(|𝒵|−1)` (grouping).
(d) Theorem 1 applied for each `d`.
(e) By (a), for every `q`, `I(π) = E_d KL(π_d‖q) − KL(π̄‖q)`. So `J(π) = J_{q}(π) + (1/β)KL(π̄‖q)`, where
`J_q` is the fixed-reference objective of (d). Take `q = π̄*`. The optimality conditions of the joint
problem give `π*_d ∝ π̄*·e^{βF(d,·)}`, and `J(π*) = J_{π̄*}(π*)`. Apply (d) with reference `π̄*`, then
subtract. ∎
*Check.* V9: (b) 0 violations / 5,000; slack 0.045 / 0.446 / 0.87. V21, for (e): to `2·10⁻¹⁵` on
exactly constructed optima; the correction is a median 42 % of the conditional term.

*Tier (R7-2).* (e) holds for every actual policy `π` with `π(·|d) ≪ π*(·|d)`: only the **intended** actor is the
rational-inattention optimum. So it is tier 1 in the actual actor, like Thm 1, not a separate actor tier.
*(Filed as "tier 4′" from v6.2 to v7.0; row 77.)* The intended reference `π̄*` is determined by the
target, the price and the law of `D`, so it is a declared counterfactual — not the actor's own reference.

*Consequence for the frame condition (X).* An endogenous reference does **not** by itself put a case
outside the calculus. When the reference is optimized as part of the capacity, the regret identity
survives, with a marginal correction. What remains outside is endogeneity the calculus cannot absorb:
tampering with the evaluator, manipulating the correction loop, or changing the target (Boundary §3).

*Caveat.* Rational-inattention optima often leave some actions unused ("consideration sets"; Caplin, Dean &
Leahy 2019). Then (e) needs `π(·|d) ≪ π*(·|d)`. For a `π` that uses an action the intended actor ignores,
both KL terms are infinite, and only the fixed-reference identity (d) applies.

**Verdict: translates only in the closed-loop extension, which is not the core.** In that extension one
capacity functional appears in both a floor on `g` (b, c) and the regret identity (d). The v5 phrase
"opposite signs" survives only for `g`. **Capacity is necessary (a floor on `g`); it is not in general
dangerous** (Prop. 14 applies per disturbance).
**What moves:** a candidate for the core's next carrier (ROADMAP T4). It adds the observation channel
that the dynamic form (Boundary §5.1) also needs.

---

## 8. Zahavi, Grafen — the handicap principle

**v5 claimed:** every mitigation of reward hacking that works by raising a cost is an instance of a
handicap, and the conditions for honesty are known. **Contradicted by the current signalling
literature.** Penn & Számadó (Biol. Rev. 2020) argue that Grafen's models do not support the handicap
hypothesis. Számadó, Zachar, Czégel & Penn (BMC Biol. 2023) argue that honesty is maintained by
*trade-offs rather than costs*. What separates types is a **differential** marginal trade-off (a
single-crossing condition), and equilibrium signals can be cheap.

In the core, the cost of behaviour is `KL(p‖q)`, the same functional for every actor type, so it cannot
separate types. Separation would need type-dependent references `q_θ`, and an equilibrium.

**Verdict: does not translate.** The lever "raise the cost of producing the signature without the cause" is
restated as **"make the trade-off of producing the signature differ by type"**, and its conditions need
the equilibrium import (Boundary §4).

---

## 9. Turner et al. — power as attainable utility

| | |
|---|---|
| **Exact part** | `Ψ_β(F) = (1/β)·log E_q e^{βF} = max_p J_F(p)`: attainable utility under the Gibbs actor |
| **Missing primitive** | a distribution over intents `F ~ 𝒟`, to form `E_𝒟 Ψ_β(F; q)` |
| **Where power-seeking lives (corrected in v6.3)** | Turner's theorem is about optimal behaviour in a **fixed** environment: for most intents drawn from `𝒟`, optimal trajectories pass through states that keep options open. With `X` a set of trajectories under shared dynamics, the reference `q(·\|s)` and the capacity are unchanged along the way, so **no frame endogeneity is involved** — what is missing is the prior `𝒟`. Frame endogeneity enters only when the actor acquires capacity or resources that change the environment or its own budget (census D1) |

**Verdict: stated, not derived.**
- Within a fixed environment, power-seeking is inside the core on trajectory space, **given a prior over
  intents**, which the core does not supply.
- Acquiring capacity is outside, by (X).

v6.2 placed all power-seeking at the boundary, and v5 placed it inside. The independent review (R5)
separated the two cases (row 64).

---

## 10. Immune tolerance — the biological anchor

Core Prop. 4: an error confined to a region `A` costs exactly `kl(p̂(A)‖p*(A))` nats, bounded by
`max{log 1/p*(A), log 1/(1−p*(A))}` whatever its magnitude.

- **Autoimmunity** (evaluator overrates self-antigens) is an overrating of a region the intended actor
  avoids; its cost scales as `log 1/p*(A)`.
- **Silent infection** (evaluator underrates evasive pathogens) is an underrating of a region the intended
  actor should occupy; its cost scales as `log 1/(1−p*(A))`.

v5's "same error functional with opposite sign" is right, and the core says more: **which branch is costly
is set by the intended actor's occupancy of the region, not by the sign.**

**Verdict: derived (structure).** The immunological operating curve itself is not derived.
**What moves:** the architecture (pre-deployment filtering vs runtime suppression as an operating curve,
carried from v5), and the rule that filtering should target the error's upper tail on regions the intended
actor avoids.

---

## 11. Quantitative genetics — selection on a proxy trait *(new in v6.1)*

Artificial and natural selection on one trait, with a response in another, is the oldest quantitative
theory of optimizing a proxy.

**Proposition B11.**
(i) **(Price's selection term.)** For any actor `p ≪ q` and any target `F`,
`E_pF − E_qF = Cov_q(w, F)` with `w = dp/dq`. The likelihood ratio plays the role of relative fitness.
This holds for every optimizer, not only tilts.
(ii) **(Robertson's secondary theorem.)** For the entropic actor, `w = 1 + β(F̂ − E_qF̂) + O(β²)`. So the
first-order response of the target is `β·Cov_q(F̂, F)`; this is Core Prop. 14(ii).
(iii) **(Correlated response.)** B §4, Prop. B4, is the response of a trait `F` to
directional exponential selection on a correlated trait `F̂`, with Gaussian phenotypes and heritability 1
(the tilt acts directly on the transmitted distribution). This is the setting of Lande's (1979)
multivariate response and of Falconer's correlated response.

*Proof.* (i) `Cov_q(w, F) = E_q[wF] − E_q[w]·E_qF = E_pF − E_qF`, since `E_q w = 1`. (ii) Expand
`w = e^{βF̂}/E_q e^{βF̂}`. (iii) Prop. B4 (§4) with `q = N(0, I)`: the tilt shifts the mean by `λw`. ∎
*Check.* `verify.py V17`: (i) to `4·10⁻¹⁶`; (ii) is V8; (iii) is V9.

**Verdict: derived.**
**What moves:**
- A century of results imports directly: selection gradients and differentials (Lande & Arnold 1983),
  the breeder's equation, and the limits of correlated response.
- The **multilevel Price decomposition** (between-group plus within-group covariance) is the natural
  formal route to multi-level alignment — census §11, intragenomic conflict. That route is **stated, not
  derived**.
- Heritability below 1 corresponds to an actor whose behaviour is transmitted imperfectly to the next
  round, a dynamic element the static core lacks.

---

## 12. Human choice — logit, defaults, rational inattention, present bias *(new in v6.2)*

Individual human choice was requested explicitly by the PI and absent from v5 and v6 (row 58).
Three questions, each answered against the core.

### (a) The actor

The conditional logit, `p(x) ∝ exp(V(x)/μ)` (McFadden 1974), is the Gibbs actor with `β = 1/μ`. A logit with
default-dependent weights, `p(x) ∝ q(x)·exp(βV(x))`, with `q` the choice probabilities under the default, is
exactly the entropic actor of Core Definition 2, from the chooser's own reference: hypothesis **(E_A)**
(Def. 13; R7-2).

Rational inattention (Sims 2003; Matějka & McKay 2015) derives the same generalized logit from an
information cost. There, `q` is the endogenously optimized action marginal. **That is not outside the
calculus.** Its regret identity is B7(e): the conditional divergence minus a marginal correction. It holds for
**any** actual behaviour, measured against the rational-inattention optimum as the intended actor: tier 1 in
the actual actor. *(Filed as "tier 4′" until R7-2; row 77.)*

The human actor therefore sits in the core in both forms. Fixed defaults (habits) are the entropic model
from the chooser's own reference, (E_A). Rational inattention is an actor model whose reference is
optimized, and the regret against its optimum is B7(e), with the consideration-set caveat stated there.

### (b) The reference is partly measurable for humans

**Proposition B12 (defaults identify the reference, under exclusion).** *[Assumes (E_A) in each environment, with `q_A = q_d`.]* Two choice environments differ only
in their default `d ∈ {d₀, d₁}`. The references are `q_{d}`, from a known parametric family — for example
`q_d = (1−α)·u + α·1_d`. Assume the evaluator is the same in both (**exclusion**: the default does not change
what the chooser values). Then:
- `log(p_{d₀}/p_{d₁}) − log(q_{d₀}/q_{d₁})` is constant in `x`;
- the family parameter `α` is identified;
- hence `q_d` is identified, and so is `βF̂ = log(p_d/q_d)` up to a constant.

If the default also moves the evaluator — defaults read as implicit recommendations (McKenzie, Liersch &
Finkelstein 2006) — the identification is biased.

*Proof.* `p_d ∝ q_d·e^{βF̂}` with `F̂` independent of `d`. Take the ratio. For the example family, one option
outside `{d₀, d₁}` pins the constant, and either default option then solves for `α`. ∎
*Check.* V22: exact recovery (`9·10⁻¹⁶`) under exclusion. With an endorsement effect of size `γ` on the
default option, the median error in `α` is 0.16 at `γ = 0.3` and 0.39 at `γ = 1`.

**Consequence.** Default experiments — retirement-plan enrolment (Madrian & Shea 2001), organ-donation
consent (Johnson & Goldstein 2003) — are a handle on `q` that institutions lack (Core §10), valid
insofar as exclusion holds. So humans sit **above** institutions in the identification table, conditionally.

*Note (R7-2).* What B12 identifies is the chooser's **own** reference `q_A = q_d`: an explanation-layer object
(Def. 13). Measuring misalignment needs only a declared reference (Def. 1). The value of B12 is attribution:
under exclusion, it separates a departure caused by the default from one caused by the evaluator. By
Prop. 26(b), behaviour in a single environment cannot do that.

### (c) Present bias lands on the framework's existing boundary

- **Naive quasi-hyperbolic agent** (Laibson 1997; O'Donoghue & Rabin 1999). At each date the agent
  optimizes a present-biased evaluator `F̂_t` while the target is long-run utility, and it believes its
  future selves will follow its current plan. No self acts *against* another. Each decision is a static
  instance with an evaluator error, contexts indexed by date (Core Def. 9), and the time
  inconsistency lives in the **sequence** of evaluators. Minimal layer: **dynamic**.
- **Sophisticated agent.** Anticipates and responds to its future selves. That is an intrapersonal game,
  which is **the equilibrium fork** (Boundary §4). Minimal layer: **strategic**.
- **Planner–doer and dual-self models** (Thaler & Shefrin 1981; Fudenberg & Levine 2006). A two-link
  chain: planner target, doer evaluator, with a self-control cost in the role of capacity. For entropic
  links this is Core Cor. 1.5, but the self-control cost in those models is not a KL. **Stated, not
  derived.**

The naive/sophisticated line falls exactly on the line between a dynamic layer without strategic
interaction and the equilibrium fork. That adds a fourth name — **intrapersonal games** — to Core §10's "one boundary", independently of the other three substrates.

**Verdict:**
- (a) derived ((E_A); B7(e) is tier 1);
- (b) derived, conditional on exclusion;
- (c) routed to existing boundaries, not derived.

**What moves:**
- the human actor needs no new carrier;
- default experiments are the one identification handle on `q` found in any substrate other than
  biology;
- the rational-inattention case refines condition (X) (B7(e)).

---

## 13. Potential games — collective behaviour is a tilt (Blume 1993) *(new in v6.2)*

The census routing (T1_census_routing) found strategic interaction to be the largest missing layer.
This entry is the first piece of that layer that needs no new carrier. It rests on a known theorem.

**Proposition B13.** Take a finite game with an exact potential `Φ`: for every player `i`,
`u_i(a, x_{−i}) − u_i(a', x_{−i}) = Φ(a, x_{−i}) − Φ(a', x_{−i})` (Monderer & Shapley 1996). Play proceeds by
**log-linear learning**: at each step a uniformly chosen player `i` revises, choosing `a` with probability
`∝ q_i(a)·e^{β u_i(a, x_{−i})}`. Then the joint play is a reversible Markov chain with stationary law

```
p̂(x) ∝ (∏_i q_i(x_i)) · e^{β Φ(x)},
```

the **entropic actor on the joint behaviour space**, with reference `⊗_i q_i` and evaluator `Φ`. *(R7-2: this reads
the players' own base measures as the declared reference, `q = q_A = ⊗_i q_i`, so hypothesis (E) holds at the
group level. A different declared reference turns their gap into measured misalignment, by Prop. 26.)*

*Proof.* Detailed balance between profiles that differ only in player `i`'s action. The ratio of transition
probabilities is `q_i(x'_i)e^{βu_i(x')}/(q_i(x_i)e^{βu_i(x)})`, which equals the ratio of the proposed
stationary weights, because `u_i` differences are `Φ` differences. ∎ (Blume 1993, uniform reference.)
*Check.* `verify.py V23`: 200 random 2–3-player potential games; the exact stationary law matches the tilt to
`6·10⁻¹³`.

**Consequence.** Let the principal's target on joint behaviour be a welfare `W`. The collective's
misalignment is then the core's, with evaluator `F̂ = Φ` and target `F = W`. All tier-4 results apply to the
group as one actor. The error `E = Φ − W` is what the players jointly optimize minus welfare — the tilt-form
counterpart of the price of anarchy (Koutsoupias & Papadimitriou 1999).

Two worked cases:

- **Linear public goods (free riding).** Private cost `c` per unit contributed, pooled contributions
  multiplied by `m` and shared among `n` players, with `m/n < c < m` (a social dilemma). Up to constants,
  `Φ = (m/n − c)·Σx_i` and `W = (m − c)·Σx_i`. So `F̂ = a·W` with `a < 0`.
  **Free riding is anti-alignment along the target.** The evaluator is a negative multiple of welfare, so
  `t̂ < 0`. On the full ray (Core Thm 13(a)) this is pure axial error (`D_⊥ = 0`). On the canonical
  half-ray (Thm 13(b)) it registers as `X_anti > 0`, with `D_⊥ = KL(p̂‖q)`.
- **Cournot commons.** The potential differs from joint profit by the externality term, a transverse error
  (`D_⊥ > 0`).

**Scope.**
- *Covered:* exact potential games under log-linear learning, at stationarity. This includes congestion
  games (Rosenthal 1973), public goods, Cournot commons, and every symmetric 2×2 game — among them the
  prisoner's dilemma.
- *Not covered:* non-potential games (zero-sum, most asymmetric conflicts), repeated-game collusion,
  transients, and equilibrium selection away from stationarity.
- *A second candidate:* logit quantal-response equilibrium (McKelvey & Palfrey 1995) is also Gibbs-native.
  It gives a product-form fixed point, not a joint tilt, and its alignment calculus is unexamined.

**Verdict: derived** (for potential games).
**What moves:** part of the strategic layer enters without a carrier change. The census items this plausibly
affects are listed as a **post-hoc** note in T1_census_routing §7. They were **not** re-routed: the
registered result stands.

---

## 14. Gate

| Entry | Verdict |
|---|---|
| §2 conjugacy scale (four literatures) | derived (exposure statements) |
| §3 Goodhart variants | 2 of 4 derived |
| §4 Gao et al. | derived (leading coefficient, Gaussian); curvature not |
| §5 Laidlaw; Holmström–Milgrom | derived (first order) |
| §6 Holmström | derived (second order), condition changed |
| §7 Ashby / Conant | closed-loop extension only |
| §8 handicap | does not translate |
| §9 Turner | stated |
| §10 immune tolerance | derived (structure) |
| §11 quantitative genetics | derived (Price term, Robertson, correlated response) |
| §12 human choice | derived (actor, both forms; reference identification under exclusion); present bias routed |
| §13 potential games | derived (collective play as a joint tilt; price-of-anarchy error) |

**Nine entries derive something from the core; v5 had zero derivations and one claimed derivation (§6),
which was wrong as stated.** Most of these derivations are known in their home literatures (see each
entry's prior-art note). This is the change that matters. A dictionary that derives its entries is evidence
that the slots carry content (C14). A dictionary that only fills them is not.

## 15. What this dictionary is not

- **Not a claim of priority.** Every result belongs to its authors; several of v6's "derivations" are
  one-line consequences of standard inequalities that those authors surely know.
- **Not a licence to move constants between fields.** Slots correspond; exchange rates and units differ by
  substrate and by link (Core Prop. 12, §10).
- **Not complete.** ELK and mechanistic interpretability still have no slot (Boundary §2.3).
