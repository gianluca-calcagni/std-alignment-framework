---
id: "Status 01 Claim ledger"
type: "section"
title: "Claim ledger"
part: "status"
order: 2
updated: "2026-09-26"
---
## 1. Claim ledger

### 1.1 Proved — standard mathematics, proof in the file

| Claim | Where | Check | Attack |
|---|---|---|---|
| `β·R_J = KL(p̂‖p*)` | A Thm [[Thm 1\|1]] | V1, 10⁻¹³ | C1 |
| optimality gap `= (1/β)×` Jeffreys; CGF and integral forms; ratio is a weighted mean of `t/β` | A Cors [[Cor 1.2\|1.2]]–[[Cor 1.4\|1.4]] | V1 | C1 |
| `R_J ≤ β·osc(E)²/8`, sharp | A Prop. [[Prop 2\|2]] | V2, 0 / 20,000 | — |
| `R_J ≤ [Λ(2β) − 2Λ(β)]/β ≤ 2βσ₊²` (upper tail only) | A Prop. [[Prop 3\|3]] | V2, 0 / 20,000 | — |
| an error on one region costs exactly the binary KL; bounded whatever its size | A Prop. [[Prop 4\|4]] | V3 | — |
| form of the capacity actor | A Lemma [[Lemma 5.1\|5.1]] | V4 | C2 |
| the width is the exact worst case over intents | A Thm [[Thm 5\|5]] | V4, 0 / 3,000; attainment exact | C2 |
| Donsker–Varadhan formula for the width; `√(2δ·Var)` and `osc` asymptotes | A Prop. [[Prop 6\|6]] | V4 | C2 |
| bound with realized travel from the reference | A Prop. [[Prop 7\|7]] | V4, 0 / 3,000 | — |
| separable bounds are loose when rankings move | A Lemma [[Lemma 8\|8]] | — | C3 |
| worst-case regret is not separable | A Thm [[Thm 9\|9]] | V5 | **C3** |
| four conjugate pairings | A Prop. [[Prop 10\|10]] | V6, 0 / 20,000 each | C4 |
| KL exposure infinite under sub-exponential tails; χ² finite under finite variance | A Prop. [[Prop 11\|11]] | V6 | **C4** |
| behaviour identifies only the tilt (not `β`, not the actor's own reference `q_A`), under (E_A) | A Prop. [[Prop 12\|12]] | — | C10 |
| full-ray decomposition `β·R_J = D_⊥ + D_∥` (Thm [[Thm 13\|13]](a)); rescaling is axial | A Thm [[Thm 13\|13]](a), Cors [[Cor 13.3\|13.3]]–[[Cor 13.4\|13.4]] | V7, 10⁻¹² | C5 |
| initial sign `−Cov_q(F̂,F)`; terminal value by argmax agreement | A Prop. [[Prop 14\|14]] | V8 | C6 |
| regret is a Bregman divergence for any convex regularizer and concave target *(v6.1)* | A Prop. [[Prop 15\|15]] | V12 | C1, C7 |
| stacked entropic stages add in the exponent; second-order covariance cross term *(v6.1)* | A Cor. [[Cor 1.5\|1.5]] | V15 | C1 |
| the exchange rate is the inverse marginal value of capacity; `g(δ)` is the value-of-information curve *(v6.1)* | A Cor. [[Cor 5.2\|5.2]] | V13 | — |
| gauge group; identified quantities; reporting rule *(v6.1)* | A Prop. [[Prop 16\|16]], Def. [[Def 7\|7]] | V14 | C5, C10 |
| half-ray decomposition `β·R_J = D_⊥ + D_∥ + X_anti` *(v6.1)* | A Thm [[Thm 13\|13]](b) | V14, 10⁻¹³ | C5 |
| all regret notions are points on the convex curve `M(t)`; same-budget identity *(v6.1)* | A Thm [[Thm 17\|17]], Def. [[Def 8\|8]] | V14 | C5 |
| Chernoff information `≤ min(KL, KL_rev) ≤ β·R_J`: no test beats the regret exponent *(v6.1)* | A Prop. [[Prop 18\|18]] | V16, 0 / 5,000 | C15 |
| evaluation gap `Γ` bounds harm minus detectability *(v6.1)* | A Prop. [[Prop 19\|19]] | V16 | C15 |
| the capacity actor's regret is the budget convention; saturated case *(v6.1, final audit)* | A Cor. [[Cor 17.1\|17.1]] | V18, V19 | C5 |
| Price selection term; Robertson; correlated response *(v6.1)* | B Prop. [[B11]] | V17, V8, V9 | — |
| Goodhart as a covariance; regret between any two actors — tier 1, any optimizer *(v6.2)* | A Prop. [[Prop 20\|20]] | V20 | C7 |
| rational-inattention regret identity: an endogenous reference absorbed by a marginal correction *(v6.2)* | B [[B07\|B7(e)]] | V21 | C13 |
| defaults identify the reference under exclusion *(v6.2)* | B Prop. [[B12]] | V22 | C10 |
| potential games under log-linear learning are a joint tilt; free riding is anti-alignment *(v6.2)* | B Prop. [[B13]] | V23 | C §4 |
| assumption tiers for every result *(v6.2)* | A "Assumption tiers"; C7 | by inspection | C7 |
| no overoptimization under an affine regression, for every optimizer whose weights depend only on `F̂` — tier 1 *(v6.3)* | A Prop. [[Prop 21\|21]] | V24 | C7 |
| Thm [[Thm 1\|1]], Thm [[Thm 13\|13]](b), Thm [[Thm 17\|17]](iii) and Prop. [[Prop 18\|18]]'s cap hold for an **arbitrary** actual actor — tier 1 *(v6.4)* | A "Assumption tiers"; Thm [[Thm 1\|1]] remark | V27; R6 P11 | C7 |
| argmax selectors on a common candidate set: `0 ≤ R ≤ E_{p̂}E − E_{p*}E` — tier 2′ *(v6.4)* | A Prop. [[Prop 23\|23]] | V28; R6 P12 | C7 |
| Prop. [[Prop 15\|15]] needs only `φ/β − U` convex (`U` need not be concave) *(v6.4)* | A Prop. [[Prop 15\|15]] | V29 | — |
| actor models and the named hypotheses (E), (C); the actual behaviour is a primitive *(R7-1)* | A Def. [[Def 13\|13]], Def. [[Def 5\|5]] | tool check: 0 untagged uses | C7 |
| mechanism-relative comparison `M_own`, `R_own`: `M_own` meets M1, M2, M3 (equivariant models), M5′ (the mechanism analogue of M5), M6, M8, and caps detection, but **fails M4**; `R_own` fails M1 and M2 *(R7-1)* | A Def. [[Def 14\|14]], Prop. [[Prop 25\|25]] | V31 | C7 |
| the measurement layer uses a **declared** reference `q`; the actor's own reference `q_A` is explanation-layer, under (E_A). Absorption: `p^{q_A}_{F̂,β} = p_{F̂ + log(q_A/q)/β, β}`, so every (E) result transfers to (E_A). A right-target agent from its own default has zero misalignment iff `log(q_A/q) = aF + c` with `β + a ≥ 0`; second order `(ε²/2)Var_{p*}(h₀⊥)`; → 0 as `β → ∞` for a unique argmax (not monotone in general: an interior peak in 67/200 instances). The alternative — budget matched on `q_A` — fails M4 *(R7-2)* | Core Prop. [[Prop 26\|26]], Def. [[Def 13\|13]] | [[V32]] | [[C05]], [[C07]] |
| **two layers** *(R7-3)*: the measurement layer — 20 items: Defs 1–3, 5, 8–12, Overview 0, Lemma 5.1, Cor. 5.2, Thm 1, Prop. 15, Thm 13, Cor. 13.2, Thm 17, Props 18, 19, 24 — uses no evaluator, error, actor reference or actor model, and depends on nothing that does. Every measurement-layer result is checked | every item's `layer`; [[Core index]] | `tools/vault.py lint` (vocabulary, layering, required checks; each rule tested by a planted violation) | [[C05]], [[C07]] |
| Lemma 5.1's monotone mean, `d/dt E_{p_{G,t}}G = Var_{p_{G,t}}(G) > 0` (was Prop. 14(i)) *(checked for the first time in R7-3)* | Core Lemma [[Lemma 5.1\|5.1]] | [[V33]] | [[C06]] |
| instrumental tracking: under (E_R) the agent tilts by `G + κ_c R` with `κ_c = W_c'(E_{p̂}R)`; under persistence, `κ_c = γνm_cV*` (Dinkelbach); `m_c = 0` ⇒ own-objective behaviour *(R7-4)* | Core Prop. [[Prop 27\|27]] | [[V34]] (P1–P3) | [[C07]] |
| incentive masking: `KL` between two types' behaviour in a contingent context is `O(e^{−βκ·gap_R})`, at exactly that rate when a runner-up is informative *(R7-4)* | Core Prop. [[Prop 28\|28]] | [[V34]] (P4, window) | [[C15]] |
| selection sees only rewarded behaviour (any actor); the selection differential between types vanishes at rate `β·gap_R` *(R7-4)* | Core Prop. [[Prop 29\|29]] | [[V34]] (P8, window) | [[C07]] |
| fake-alignment gap: `Γ_free →` deployment misalignment when `argmax R = argmax F` in evaluation; reward hacking exposed, with limit `−log sup_t p_{F,t}(x_R)` *(R7-4)* | Core Prop. [[Prop 30\|30]] | [[V34]] (P6, P7) | [[C15]] |
| the misalignment contract (M1–M9); budget and free measures satisfy it; the price measure fails M5 (it charges a right-target agent at the wrong intensity); raw `ΔF` fails M1–M2 *(R7-0)* | A Def. [[Def 11\|11]], Prop. [[Prop 24\|24]] | V30 | C5 |
| first-order effect of any smooth optimizer = covariance in its geometry; vanilla gradient is `q²`-weighted — tier 1 *(v6.3)* | A Prop. [[Prop 22\|22]] | V25 | C6, C7 |
| rescaling costs nothing under the budget and free conventions and the axial error under the price convention; best-of-n is monotone-invariant *(v6.3)* | A Remark [[Rem 13.5\|13.5]] | V26 | C5 |
| Gaussian Gibbs path: gold gain exactly `√2·ρ·sd·d` | B Prop. [[B04\|B4]] | V9 | C9 |
| informativeness: exact additive cost under independence; second-order optimal weight | B Prop. [[B06\|B6]] | V9 | — |
| closed-loop lift: capacity ≥ mutual information; Conant; Fano floor on `g`; per-disturbance regret identity | B Prop. [[B07\|B7]] | V9 (Conant) | C12 |

"Proved" means proved in the file under Assumption S. None of it is new as mathematics.

### 1.2 Measured — generator-dependent

| Claim | Evidence | Scope |
|---|---|---|
| masking is not monotone: a moderate incentive reveals more about the own objective than none in 50 % of random instances (pre-registered 10–70 %) *(R7-4)* | [[V34]] | generator-dependent |
| under reward hacking, evaluation misalignment rises with the incentive (median ×4.6 from `κ = 0` to `300`) *(R7-4, not pre-registered)* | [[V34]] | generator-dependent |
| slack distributions of every bound | V1, V2, V4 | random instances; the generators are in `verify.py` |
| the v5 capacity-ball bound fails under readings (a), (b) | V4 retraction record | hard-constraint generator |
| for a fixed intent, the error ranking reverses (×103 span) | V5 | one constructed pair |
| total regret monotone decreasing in `β` in 37–86 % of instances; interior optimum 14–45 %; median optimal `β` 64 → 1.7 as error scale 0.2 → 8 | V8 | 300 instances per cell |
| proportional correction at the margin oscillates; PI removes steady error; amplification near `ω = 1/τ` | V10 | toy loop |
| an equipartition repair of H2 fails when `p*` concentrates | V11 | `n = 6`, MCMC |
| price and budget conventions rank error pairs differently in 11.4 % of pairs *(v6.1)* | V14 | 1,218 random pairs |
| Chernoff information is 17–54 % of `β·R_J` (p5–p95) *(v6.1)* | V16 | random instances |
| **census routing** *(v6.2)*: F 35.3 %, P 34.4 %, N 30.3 %; F + P 69.7 % (pessimistic 49.8 %); 11 of 12 hard cases fire | [[T1_census_routing]] | one rater, the framework's own extender |
| **adjudicated census routing** *(R6, frozen)*: named 78.3 %, specific 60.6 % (third rater blind: 55.2 %), full 29.4 %; missing layers strategic 51, statistical 31, outside-X 23, dynamic 20 | [[T1_census_routing]] §10; [[T1_RULES_FROZEN]] | three raters; **frozen format: nested shares, no pass/fail** |
| **tier 2 violations** *(R6)*: early-stopped VPG 25.5 %, best-of-n at matched KL 4.3 %, best-of-n at equal `n` 0, Gibbs 0 (1,150 instances) | `reviews/R6_independent/t2/p12_summary_output.txt` | the reviewer's pre-registered P12; 1,150 of 2,000 instances |
| **crossing locations** *(R6)*: VPG 0.026, KL-PG 0.026, Gibbs 0.54, NPG 0.54, best-of-n 4.7 (KL) | `reviews/R6_independent/R6_T2_results.md` | V5 instance only |
| **independent re-routing** *(R5)*: κ 0.54–0.57 (expressibility), 0.70 (layer), 0.76 (locus); F by both raters 24.9 %; F + P 52.9–70.1 %; strategic and frame lead in both | [[T1_census_routing]] §9 | a second rater, blind; the T1b gate passes |
| **tier-4 transfer** *(R5)*: C8 crossing and [[B04\|B4]] transfer to best-of-n and vanilla policy gradient; the sign criterion, the value reading of Prop. [[Prop 18\|18]], and the harm of rescaling do not | [[C07\|C7]]; `reviews/R5_independent/` | the reviewer's pre-registered tests; one instance each |

### 1.3 Imported — not ours, load-bearing

| Import | What it buys | Conditions |
|---|---|---|
| Gibbs variational principle; Donsker–Varadhan; Hölder; Popoviciu; Hoeffding's lemma; Pinsker | the core | finite `X` or exponential integrability |
| Csiszár's Pythagorean identity (exponential families) | Thm [[Thm 13\|13]] | — |
| Iwasa (1988); Sella & Hirsh (2005); Manhart, Haldane & Morozov (2012) | `β ∝ N_e`; the maximized functional is free fitness | weak mutation, reversibility, stationarity; constants depend on the substitution model and are carried from v5, not re-verified |
| Train (2009), scale normalization in discrete choice | the institutional identification failure | logit-type models |
| Francis & Wonham (1976); Bode's sensitivity integral | §5.1 of C | Bode not re-derived for the delayed loop |
| Conant (1969); Fano grouping bound | [[B07\|B7]] | injective regulation table |
| Kwa et al. 2024; Laidlaw et al. 2025; Fluri et al. 2025; concentrability (offline RL) | B §2 | their settings; exposure halves only |
| Gao et al. 2023 | B §4 | synthetic gold RM |
| Manheim & Garrabrant 2018; Karwowski et al. 2024 | B §3 | — |
| Holmström 1979; Holmström & Milgrom 1991 | B §§5–6 | mechanisms differ; stated |
| Penn & Számadó 2020; Számadó et al. 2023 | B §8 | — |
| Turner et al. | B §9 | a prior over intents, not supplied |
| Korbak et al. 2022 (both papers); Zhao et al. 2024 *(v6.1)* | prior art for Thm [[Thm 1\|1]] | — |
| Mroueh 2024; Mroueh & Nitsure 2025 *(v6.1)* | prior art for Prop. [[Prop 7\|7]], B §§2, 4 | reward improvement, not error |
| Huang et al. 2025 *(v6.1)* | prior art for Props [[Prop 10\|10]]–[[Prop 11\|11]] | statistical coverage framing |
| El-Mhamdi & Hoang 2024; arXiv:2505.23445 *(v6.1)* | prior art for B §§3–4, A §11 item 6 | selection model, not tilt |
| Skalse et al. 2024 (STARC) *(v6.1)* | motivates the half-ray (Thm [[Thm 13\|13]](b)) | reward-space, not behaviour-space |
| Wang & Huang 2026 *(v6.1)* | prior art for B §5 | — |
| Gottwald & Braun 2019 *(v6.1)* | related cross-substrate framework | no misspecification |
| Chernoff 1952 *(v6.1)* | Prop. [[Prop 18\|18]] | i.i.d. samples, simple hypotheses |
| Price 1970; Robertson 1966; Lande 1979; Falconer & Mackay 1996 *(v6.1)* | B §11 | heritability 1 in the static core |
| Beirami et al. 2024 *(v6.1)* | the BoN KL expression is an upper bound | — |

### 1.4 Conjectural — flagged, not promoted

| Claim | Where | Why flagged |
|---|---|---|
| the crossing (rank reversal) holds for every optimizer, and one index orders where it falls | C7, C8; [[ROADMAP]] T8 | tested on one instance (V5) for five optimizers: it held for all, and its location varied about 180-fold (R5, R6; §1.2). No general statement, and no index yet. *(Until v7.3.3 this row read "untested". Its other half, the conjugacy picture, is tier 1: Props [[Prop 10\|10]]–[[Prop 11\|11]] hold for any behaviour, and what actual optimizers expose is [[B02\|B §2]].)* |
| `α ≈ √2·ρ·sd` against published overoptimization coefficients | C9 | untested |
| delay sets a bandwidth; correction amplifies error near crossover; double protection restated | C §5.1 | simulation only; the actor acting on `τ` is outside the core |
| the closed-loop lift as the next carrier | C §5.2 | proved pieces, untested as a carrier |
| transverse errors compose along chains | C §5.3 | unexamined |
| the arrangement has content beyond an index | C14 | answered in R3: predominantly an index; the residual organizing statements are listed in C14 |
| practical relevance of the detection bound | C15 | untested |
| multi-level alignment via the multilevel Price decomposition | B §11 | stated, not derived |
| causal influence diagrams as the Layer-0 ontology | C §5.4 | a proposal; not applied ([[R3_FIX_LOG]]) |
| the framework's generality across the census | [[T1_census_routing]] | **routed twice (v6.2, R5)**: partly general; strategic and frame layers missing in both routings |

---

