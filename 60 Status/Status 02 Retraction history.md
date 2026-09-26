---
id: "Status 02 Retraction history"
type: "section"
title: "Retraction history"
part: "status"
order: 3
updated: "2026-09-26"
---
## 2. Retraction history

Every line was believed, and stated in bold, in some version of this corpus. Rows 1–30 are carried
verbatim from v5, even where their "replaced by" column has itself since been retracted — see rows 32, 35,
37 and 40. v5 said "twenty-nine"; the table had thirty rows (hygiene, §5).

| # | Retracted | Replaced by | Found by |
|---|---|---|---|
<!-- gen:retractions -->
| # | Retracted | Replaced by | Found by |
|---|---|---|---|
| [[R001\|1]] | "Alignment holds iff all five gaps close" | circular; replaced by an explicit definiendum | external review |
| [[R002\|2]] | verification is a fifth alignment gap | assurance — a different type | external review |
| [[R003\|3]] | three of five gaps un-closable in principle | one impossibility; the rest are prices. The verdicts were artifacts of measurability conditions with no threshold | external review |
| [[R004\|4]] | grounding as measurability w.r.t. a self-reachable σ-algebra | vacuous — generically satisfied | external review |
| [[R005\|5]] | value learning is harder than world learning *by requirement* | a bandwidth ratio; the channel-modularity premise is false | external review |
| [[R006\|6]] | "you cannot specify values, only in terms of concepts already acquired" | true instantaneously, false dynamically | external review |
| [[R007\|7]] | an irreducible floor on total failure | **not established** | self |
| [[R008\|8]] | "the unconstrained residual is the one object underlying every failure" | wrong for two of five loci | self |
| [[R009\|9]] | correlation-induced underdetermination is the mechanism | correlation inflates estimator *variance*, not underdetermination | pre-run check |
| [[R010\|10]] | exact and inexact confounding need different mechanisms | one inequality, opposite factors — I read one factor of a product | derivation |
| [[R011\|11]] | the regret bound is tight by Bauer's principle | **false**; median tightness 0.000 | arithmetic check |
| [[R012\|12]] | thresholding vanishes as extreme points grow | **false**; 40× more vertices moved it 0.77 → 0.63 | scope check |
| [[R013\|13]] | concentration under optimization requires convexity | it does not | scope check |
| [[R014\|14]] | "widths multiply through a chain" | errors **add**; multiplication only across different reaches | derivation |
| [[R015\|15]] | non-linear intents break the core | linearity is needed only for the product form | derivation |
| [[R016\|16]] | lever "re-specify" attacks the reach | it attacks the **error** | audit |
| [[R017\|17]] | enlarging the probe space is a sixth lever | a different type; it **gates** three others | audit |
| [[R018\|18]] | the error decomposition holds in general | needs an inner product — linear case only | audit |
| [[R019\|19]] | the evaluator is the functional behaviour maximizes | **wrong twice**: execution failure inexpressible, and it collides with reward non-identifiability | census evaluation |
| [[R020\|20]] | the observable/unobservable split is structural | a continuum of attribution difficulty, which gives the sharper `e*(τ) ∝ τ` | revision |
| [[R021\|21]] | grounding is about the instrument | one row of seven | brainstorm |
| [[R022\|22]] | multi-agent failures are gaps in the framework | several are **legitimately out of scope** — in the commons every agent tracks its principal | re-reading |
| [[R023\|23]] | stability of the error is the dynamic condition | regret is a product; flat error with growing reach gives growing regret | a bug in my own verdict line |
| [[R024\|24]] | the frame table unifies previously unrelated failure modes | **subsumed** by reward tampering + corrigibility + instrumental convergence. Conceded, and left as attack **A11** in case the concession is itself wrong | preregistered kill test |
| [[R025\|25]] | the frame table is complete over how an actor acts on its setup | wrong in one direction — it had no cell for the actor **maintaining** the frame | the reverse-direction check |
| [[R026\|26]] | cross-substrate breadth is a contribution | **0 of 21** sampled items beat the native literature | preregistered breadth test |
| [[R027\|27]] | transfer between substrates is bidirectional | **directional** — all clear transfers run *into* AI | same |
| [[R028\|28]] | early stopping falls out as an interior optimum in `β` | **13–40 % of instances.** What survives is the comparative static | T1 check |
| [[R029\|29]] | `osc(E)` unqualified | `osc_δ(E)`, over the **capacity ball** | Fluri et al., via the dictionary |
| [[R030\|30]] | `β` will have no principled meaning without a designer | **wrong** — it is the effective population size, and biology is the strongest of the three cases | T2 search |
| [[R031\|31]] | the optimality gap is "tight to within about 2×" | it is `(1/β)×` the Jeffreys divergence; the ratio is a weighted mean of `t/β`, which tends to 1/2 for small errors (A Cor. [[Cor 1.4\|1.4]]) | review R2 |
| [[R032\|32]] | `R_J ≤ osc_δ(E)·√(2δ)`, oscillation over the capacity ball (row 29's replacement) | ill-typed. Two readings are false (up to 100 % violations at small `δ`); the third is plain `osc`. Replaced by the width (A Thm [[Thm 5\|5]]) | review R2 |
| [[R033\|33]] | separability holds iff the kinematic term is a capacity | the evidence was a correlation with a constant (s.d. 0.000). Separability is a property of the relaxation; worst-case regret is non-separable (A Thm [[Thm 9\|9]]) | review R2 |
| [[R034\|34]] | the capacity slot must never hold a realized distance | A Prop. [[Prop 7\|7]] uses realized travel from the reference. The T1 "collapse" used travel from `p*`, which **is** `β·R_J` | review R2 |
| [[R035\|35]] | "regret is a product" (row 23's replacement); the normal form "epistemic × kinematic" | regret is an identity (A Thm [[Thm 1\|1]]). The product is a relaxation, forceable for every convex capacity (C14) | review R2 |
| [[R036\|36]] | Ashby's requisite variety is the boundedness term of the same decomposition | verbal in the open-loop core. A theorem only in the closed-loop lift, and there only as a floor on `g` ([[B07\|B7]]) | review R2 |
| [[R037\|37]] | `β` has an interior optimum when the error is large | row 28 had retracted this, but it still stood in v5 A §3.1, B §4 and B §9. Removed everywhere | review R2 (hygiene) |
| [[R038\|38]] | capacity amplifies the alignment term | raw alignment regret has no sign (`ΔF'(0) = −Cov_q(E,F)`) and is non-monotone in `β` in 47–99 % of instances (A Prop. [[Prop 14\|14]], V8) | review R2 |
| [[R039\|39]] | "a constant error costs nothing — uniform rescaling of a reward is harmless" | constants are free; rescaling costs exactly the axial error (A Cor. [[Cor 13.3\|13.3]]) | review R2 |
| [[R040\|40]] | `β` is principled in all three substrates (row 30's replacement) | behaviour identifies only the tilt. `β` is a system property only given an external unit channel; institutions have none (A Prop. [[Prop 12\|12]], §10 in v6.1 numbering) | review R2 |
| [[R041\|41]] | conditioning the evaluator on a feature uninformative about the intent is strictly harmful | counterexample (length bias). The condition is independence from the error, with exact additive cost ([[B06\|B6]]) | review R2 |
| [[R042\|42]] | the positive half of the informativeness principle cannot be derived here | derived at second order: the weight is the regression coefficient of the error on the signal ([[B06\|B6]]) | review R2 |
| [[R043\|43]] | the divergence order is a free parameter trading tightness | structural: KL and χ² differ in whether exposure is finite at all (A Prop. [[Prop 11\|11]]) | review R2 |
| [[R044\|44]] | training error cannot fill the epistemic slot (v5 reading of Fluri et al.) | it can, in the norm conjugate to the capacity; `L¹` pairs only with `D_∞` (A Prop. [[Prop 10\|10]]) | review R2 |
| [[R045\|45]] | `e*(τ) = (2/π)·c·τ`, and double protection as "the sharpest thing the framework says" | proportional control at the stability margin, which oscillates; PI gives zero steady error; delay limits bandwidth. An actor acting on `τ` violates (X) (C §5.1) | review R2 |
| [[R046\|46]] | every cost-raising mitigation of reward hacking is a handicap | the signalling literature says honesty comes from differential trade-offs; KL cost is type-independent (B §8) | review R2 |
| [[R047\|47]] | three of four outside items are one condition (frame exogeneity) | Arrow is non-existence under sincere reports; two conditions, (E) and (X) (C §3) | review R2 |
| [[R048\|48]] | regret is driven by the error's variance, not its level | a second-order statement; beyond it the CGF and the upper tail govern (A Props [[Prop 3\|3]], [[Prop 4\|4]], [[Prop 11\|11]]) | review R2 |
| [[R049\|49]] | H2 (notes): the drift barrier is a floor on achievable alignment | the drift barrier bounds `g`, not the error. An equipartition repair fails when `p*` concentrates (V11). Never promoted | review R2 |
| [[R050\|50]] | the transverse error `D_⊥` is "misalignment proper" — stated in review R2 itself | `F̂ = −F` has `D_⊥ = 0`: a sign flip is axial. `D_⊥` says where regret lies, not how bad it is | rebuild, checking the sign case |
| [[R051\|51]] | the crossing test uses two errors with *matched* reference variance — proposed in review R2 itself | with matched variances the worst-case curves tie to leading order at small capacity; crossing needs `Var₁ > Var₂` and `osc₁ < osc₂` (A Thm [[Thm 9\|9]]) | rebuild, fresh-eye review of C8 |
| [[R052\|52]] | README: "A formalization of alignment for bounded actors" — read as a general theory | a verified calculus for the static, single-target, exogenous-frame module; the general theory is not built | review R3 |
| [[R053\|53]] | BoN KL "exact for a continuous evaluator without ties; an upper bound otherwise" | an upper bound (Beirami et al. 2024); the conditions under which it is attained were not checked | review R3 |
| [[R054\|54]] | the full intent ray `t ∈ ℝ` as the canonical decomposition (Thm [[Thm 13\|13]]) | the half-ray `t ≥ 0`, matching STARC's positive rescaling; anti-alignment is then transverse plus `X_anti` | review R3 |
| [[R055\|55]] | "Manhart & Morozov (2012)" | Manhart, Haldane & Morozov (2012) | review R3 (bibliographic) |
| [[R056\|56]] | `β·R_J` — the same-price counterfactual — presented as *the* measure of misalignment | one point on the curve `M(t)`; the counterfactual is a declared convention (Def. [[Def 8\|8]]); price and budget disagree on 11.4 % of error pairs | review R3 |
| [[R057\|57]] | Def. [[Def 8\|8]] (first v6.1 release): when `λ` does not exist, the budget convention uses `p_{F,∞}` | that gives `+∞` even for an essentially aligned actor. The convention is undefined past saturation; report `M_free` and the raw regret `max F − E_{p̂}F` | final audit (F5) |
| [[R058\|58]] | (implicit since v5) the framework covers individual humans, as the PI requested | it had no human treatment at all; restored in v6.2 (A §10, B §12, [[B07\|B7(e)]]) | previous executor (MSG_1 §4) |
| [[R059\|59]] | condition (X): `q` must not be a function of the actor's behaviour | too strong. A reference optimized jointly with the policy (rational inattention) keeps an exact regret identity with a marginal correction ([[B07\|B7(e)]]). Only endogeneity the calculus cannot absorb is outside | review R4, testing MSG_2 §2(a) |
| [[R060\|60]] | C7: "deployed optimizers are not Gibbs actors" as a blanket weakness | a tier map: tiers 1–2 hold for any optimizer (A, "Assumption tiers"); only tier 4 needs the Gibbs actor | previous executor (MSG_2 §3) |
| [[R061\|61]] | (row 39's replacement) "uniform rescaling of a reward is harmless" is false in this model | false only under the price convention. Under the budget (default) and free conventions rescaling costs nothing, and for best-of-n it is harmless outright (A Remark [[Rem 13.5\|13.5]]) | independent review R5 (T-E) |
| [[R062\|62]] | (v6.2 plain abstract) "if a misalignment is cheap, it is also hard to detect" | holds only for the entropic actor, and only with "cheap" meaning cheap in nats — lost value plus information spent. A misalignment with zero value regret can be readily detectable (A §9) | independent review R5 (T-C) |
| [[R063\|63]] | (C §3) auto-induced distributional shift (census C8) is an (X) failure | with a fixed target and shared dynamics it is inside on trajectory space; only preference change (G4) is (X) | independent review R5 (routing) |
| [[R064\|64]] | (B §9, v6.2) power-seeking lives at the frame boundary | Turner-style power-seeking in a fixed environment is inside on trajectory space, given a prior over intents; only acquiring capacity is (X) | independent review R5 (routing) |
| [[R065\|65]] | (T1, v6.2) "the core fully expresses 35 % of the census" | 25–35 % across two raters. Twelve of my F items name a learning mechanism and are snapshots (P, statistical) | independent review R5 (blind re-routing) |
| [[R066\|66]] | (A §11 item 5, v6.1–v6.2) "the initial effect of optimization has the sign of `Cov_q(F̂,F)`" | for the entropic actor only; in general it is the covariance in the optimizer's geometry (A Prop. [[Prop 22\|22]]), and a vanilla gradient can have the opposite sign | independent review R5 (T-B) |
| [[R067\|67]] | "tiers 1–2 hold for any optimizer" (A header, README, row 60, ROADMAP T2) | tier 2 needs an exact maximizer. Early-stopped vanilla policy gradient violates it in 25.5 % of instances, best-of-n at matched KL in 4.3 %. Best-of-n compared at equal `n` is covered by the new tier 2′ (Prop. [[Prop 23\|23]]) | independent review R6 |
| [[R068\|68]] | Thm [[Thm 1\|1]] and its consequences filed as tier 4; "harm in nats is not defined off the entropic actor" (A §9 box); "no candidate that is a regret for every actor" (R5_LOG §3) | Thm [[Thm 1\|1]] is stated for every `p`: only the **intended** actor must be Gibbs. Thm [[Thm 13\|13]], Thm [[Thm 17\|17]] (i)–(iii), Prop. [[Prop 18\|18]]'s cap and Prop. [[Prop 19\|19]] are tier 1 in the actual actor as well (the extension beyond Thm [[Thm 1\|1]] was found by the executor while applying the fix) | independent review R6 |
| [[R069\|69]] | the budget convention as the default comparison for every actor | KL is the natural resource only for Gibbs and capacity actors. The own-resource convention (Def. [[Def 8\|8]]) compares best-of-n at equal `n` | independent review R6 |
| [[R070\|70]] | C15's falsifier: "reliably detected from few behavioural samples" | Prop. [[Prop 18\|18]] is asymptotic. Finite-`n` success cannot falsify it (the entropic actor already beats it for `n ≤ 5`) | independent review R6 |
| [[R071\|71]] | "seven" derived dictionary entries (README, D, C14) | nine | independent review R6 (hygiene) |
| [[R072\|72]] | the census result reported as a pass or fail against the 60 % threshold (T1 v6.2 headline, R4, v6.3 band) | three nested shares: named 78 %, specific 55–61 %, full 29 %. The specific share sits on the threshold | independent review R6 |
| [[R073\|73]] | ROADMAP T2: "only tier-4 results need testing"; best-of-n capacity given as `log n − (n−1)/n` | tier 2 also needed testing, and fails for non-maximizers. The expression is only an upper bound, and on finite `X` exceeds saturation (8.21 at `n = 10⁴` against `log 2000 = 7.60`) | independent review R6 |
| [[R074\|74]] | (Def. [[Def 8\|8]], v6.1–v6.4) ε-alignment defined under the price convention as well | the price measure charges an agent that pursues the right target at a different intensity, violating the contract's M5 (Prop. [[Prop 24\|24]](c)). ε-alignment is now defined under the budget and free conventions only; the price convention gives ε-**regret** | found internally, R7-0 contract check |
| [[R075\|75]] | (Def. [[Def 8\|8]], v6.4) the "own-resource convention" as a counterfactual convention for regret or misalignment of non-KL actors | it needs the agent's mechanism and resource, which behaviour does not identify (Prop. [[Prop 12\|12]]), so it fails M4. It is now an explanation-layer comparison (Def. [[Def 14\|14]]), and its value-unit form also fails M1 and M2 (Prop. [[Prop 25\|25]]) | found internally, R7-1 |
| [[R076\|76]] | (tier table, v6.4) Lemma [[Lemma 5.1\|5.1]], Cor. [[Cor 5.2\|5.2]], Prop. [[Prop 14\|14]](i), Cor. [[Cor 1.1\|1.1]] in full, and Thm [[Thm 5\|5]](iii) filed in tier 4 | Lemma [[Lemma 5.1\|5.1]], Cor. [[Cor 5.2\|5.2]], Prop. [[Prop 14\|14]](i) and Cor. [[Cor 1.1\|1.1]](a) assume nothing about the actual actor: they are facts about the target, the Gibbs family or the capacity problem. Thm [[Thm 5\|5]](iii) concerns capacity maximizers (tier 2). Only Cor. [[Cor 1.1\|1.1]](b) needs (E) | found internally, R7-1 dependency scan |
| [[R077\|77]] | (tier table, v6.2–v7.0) [[B07\|B7(e)]], the rational-inattention regret identity, filed as a separate actor tier "4′" | B7(e) holds for every actual policy `π` with `π(·\|d) ≪ π*(·\|d)`. Only the intended actor is the rational-inattention optimum, so it is tier 1 in the actual actor, like Thm [[Thm 1\|1]]. The same misfiling as rows [[R067\|67]]–[[R068\|68]] and [[R076\|76]], for an intended actor that is not a tilt of a fixed reference | found internally, R7-2 dependency scan |
| [[R078\|78]] | (tier table, v6.2–v7.1) Prop. [[Prop 15\|15]], the Bregman identity for any regularizer, filed as "tier 3: an exact optimum of `U − φ/β`", with a statement ending "the actual actor `p̂ = argmax [Û − φ/β]` has regret at least …" | The identity holds for every `p`; only the intended behaviour must be an exact optimum. Prop. [[Prop 15\|15]] is tier 1 in the actual actor, and tier 3 is empty. The fifth instance of filing a result by its intended actor, after rows [[R067\|67]]–[[R068\|68]], [[R076\|76]] and [[R077\|77]] | found internally, R7-3 layering scan |
<!-- /gen:retractions -->


**Seventy-eight retractions.** By source:
- external reviews: 45 (6 before v5, 19 in R2, 5 in R3, 2 from the previous executor's review of v6.1, 6 in
  the independent review R5, 7 in R6);
- found internally: 33 (24 in v5 and earlier, 2 in the v6 rebuild, 1 in the final audit of v6.1, 1 in R4, 1 in
  R7-0, 2 in R7-1, 1 in R7-2, 1 in R7-3).

> **The bias is still toward elegance, and R2 adds a second pattern: bounding what has a closed form.**
> Five versions bounded `R_J`; none asked whether it had an exact expression. Rows 31–35 are what that cost.
> The two self-found rows were a clean name for a clean decomposition (50), and a prediction stated in the
> form that sounded right rather than the form the theorem supports (51).

---

