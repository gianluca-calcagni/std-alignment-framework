# D — Status

## Abstract, in plain terms

How much of this to believe, and why. **Read this before quoting anything from the other files.** They state
claims without hedging, by design; the hedging is here.

**Status: v7.5 (R7-6a)** — intensity caps. How hard a target is meant to be pursued is now a declaration. Without a cap
the measures behave as before; with one, an agent that overshoots it is charged. This repairs a real defect: an agent
collapsed onto a distributional target's modes used to score as perfectly aligned. All seven pre-registered
predictions held (R7-6a results). The hedge: the repair is exact because the distributional target is scored by KL;
a principal scoring the spread by another divergence is not covered.

**v7.4 (R7-7)** — target sets. The target can now be declared **ordinal**: only the order of outcomes is
intended. Under that declaration, best-of-n and quantilizers run on the true target are aligned (`M_ord = 0`),
which repairs the defect v7.3.1 found. Three hedges:
- **Under the budget convention the repair is exact only at zero.** The ordinal budget measure has no closed
  form. A solver computes it, and the registered falsifier D4 fired: on one case of 393 the solver did not
  certify a zero. Zeros are exact without it (Prop. 32(f)); non-zero values carry solver error.
- **4 of 10 predictions failed as registered** (P6, P7, P8, P10), on test design or on predictions about the
  cardinal measures; one proved claim, a strict inequality, is withdrawn under the registered rule D2
  (R7-7 results).
- **Which set to declare is the principal's choice, not the framework's.** A positive cardinal measure for a
  non-Gibbs optimizer may be shape, not misdirection; the ordinal measure separates the two.

**v7.3.3** — a review of the whole package against its stated goal.
- **Nothing proved changed, and every numerical check still reproduces.** The review found no error in the
  proofs it read.
- **Status text had gone stale.** This abstract stood at v6.6, the Dictionary banner at v6.3 and the Boundary
  banner at v6.4. Core §12 still called Thms 1, 13, 17 and Prop. 18 entropic-only,
  although they have been tier 1 since v6.4. §1.4 still listed as untested the crossing that R5 and R6 had tested.
  All are corrected (§5), and `lint` now rejects a part banner older than its own text.
- **The open risk is external contact, not internal consistency.** No prediction has been tested against
  outside data (C8, C9 and C11 have been checked only on the project's own generators). No real case has been
  run through the framework end to end (ROADMAP T7). Until then it is a checked calculus, not yet a standard.

**v7.3.1 (R7-5 closed)** — no real case needs a divergence other than KL. One real defect was found: an agent
that pursues the **true** target with best-of-n or a quantilizer scores as misaligned: `M_free` has a median of
0.04–0.39 nats (R7-5 go-no-go), and `M_budget` is never smaller. The cardinal measures charge the *shape* of the
pursuit as well as its direction.
R7-7 (the ordinal target) is the planned repair; until then, read a positive `M_budget` or `M_free` for a
non-Gibbs optimizer as possibly shape, not misdirection.

**v7.3 (R7-4)** — external reward versus the agent's own objective (Props 27–30), with one stationary
dynamic element. Pre-registered: 6 of 8 predictions held, and 2 failed as registered on test design.

**v7.2 (R7-3)** — two layers. The measurement layer says what misalignment is from behaviour, a declared
reference, the target and a convention; lint keeps explanation out of it. **v7.1 (R7-2)** — the declared
reference is part of the intent; a wrong default in the actor is measured misalignment unless it leans along the
target (Prop. 26). **v7.0** — the package became a vault, with one content edit: Prop. 20's proof no longer cites B11(i), which
closed a dependency cycle.

**v6.6 (R7-1)** — the actual behaviour is now any distribution, and no actor model is assumed in the
definitions.
- The entropic actor is a named explanatory hypothesis (E) in Def. 13, and (C) in Def. 5. Every result that
  needs one says so; the tool checks.
- The mechanism-relative comparison moves to the explanation layer (Def. 14, Prop. 25): it fails M4 by
  construction.
- Retractions 75–76.

**v6.5 (R7-0)** — the first step of the refactor.
- The misalignment contract (Def. 11) and Prop. 24 are added.
- **"Misalignment" now names the budget or free measure; the price measure is a regret** (row 74).
- The measures become Def. 10.
- Circularities are removed, and the dependency tool `tools/depgraph.py` is added.

**v6.4** — v6.3 plus the fixes prompted by the third independent review (R6, R6_LOG):
- corrected assumption tiers, with Thm 1, Thm 13, Thm 17 and Prop. 18 tier 1 in the actual actor;
- Prop. 23 (tier 2′) and the own-resource convention;
- the generality measurement frozen as three nested shares (T1_RULES_FROZEN);
- retractions 67–73.

v6.3 was v6.2 plus the fixes prompted by an independent review (R5, R5_LOG): a blind second
routing of the census, tier-4 transfer tests, Props 21–22, Remark 13.5, and retractions 61–66.

v6.2 was v6.1 (v6 plus the R3 fixes, R3_FIX_LOG) plus review R4 (R4_LOG):
- assumption tiers;
- Prop. 20;
- the human substrate (B §12, B7(e));
- potential games (B §13);
- the census routing (T1_census_routing).

**The short version.** v6 replaces v5's central inequality with an identity. The loss in nats from pursuing
the wrong objective equals the divergence between actual and intended behaviour. Everything in Core
is a theorem with a proof, using standard mathematics, checked numerically by `verify.py`. Nine dictionary
entries are derived rather than asserted (six in v6). The prior-art check (C14) found the package to be
**predominantly an index**: most results are known and are now cited where used. The core's weakest joint has moved from "is the normal form
vacuous?" (it was: v6 abandons it) to "does anything survive for actors that are not exponential tilts?". That
question is now answered in part (v6.4, R5, R6): the tier-1 results hold for any actual actor, and the capacity bounds
for exact maximizers. The E-based bounds do not transfer, and the crossing transfers but its location does not.

Review R2 retracted nineteen v5 claims; the rebuild found two more in R2's own text; review R3 added five. **§2 is the corpus's
memory.**

---

## 1. Claim ledger

### 1.1 Proved — standard mathematics, proof in the file

| Claim | Where | Check | Attack |
|---|---|---|---|
| `β·R_J = KL(p̂‖p*)` | A Thm 1 | V1, 10⁻¹³ | C1 |
| optimality gap `= (1/β)×` Jeffreys; CGF and integral forms; ratio is a weighted mean of `t/β` | A Cors 1.2–1.4 | V1 | C1 |
| `R_J ≤ β·osc(E)²/8`, sharp | A Prop. 2 | V2, 0 / 20,000 | — |
| `R_J ≤ [Λ(2β) − 2Λ(β)]/β ≤ 2βσ₊²` (upper tail only) | A Prop. 3 | V2, 0 / 20,000 | — |
| an error on one region costs exactly the binary KL; bounded whatever its size | A Prop. 4 | V3 | — |
| form of the capacity actor | A Lemma 5.1 | V4 | C2 |
| the width is the exact worst case over intents | A Thm 5 | V4, 0 / 3,000; attainment exact | C2 |
| Donsker–Varadhan formula for the width; `√(2δ·Var)` and `osc` asymptotes | A Prop. 6 | V4 | C2 |
| bound with realized travel from the reference | A Prop. 7 | V4, 0 / 3,000 | — |
| separable bounds are loose when rankings move | A Lemma 8 | — | C3 |
| worst-case regret is not separable | A Thm 9 | V5 | **C3** |
| four conjugate pairings | A Prop. 10 | V6, 0 / 20,000 each | C4 |
| KL exposure infinite under sub-exponential tails; χ² finite under finite variance | A Prop. 11 | V6 | **C4** |
| behaviour identifies only the tilt (not `β`, not the actor's own reference `q_A`), under (E_A) | A Prop. 12 | — | C10 |
| full-ray decomposition `β·R_J = D_⊥ + D_∥` (Thm 13(a)); rescaling is axial | A Thm 13(a), Cors 13.3–13.4 | V7, 10⁻¹² | C5 |
| initial sign `−Cov_q(F̂,F)`; terminal value by argmax agreement | A Prop. 14 | V8 | C6 |
| regret is a Bregman divergence for any convex regularizer and concave target *(v6.1)* | A Prop. 15 | V12 | C1, C7 |
| stacked entropic stages add in the exponent; second-order covariance cross term *(v6.1)* | A Cor. 1.5 | V15 | C1 |
| the exchange rate is the inverse marginal value of capacity; `g(δ)` is the value-of-information curve *(v6.1)* | A Cor. 5.2 | V13 | — |
| gauge group; identified quantities; reporting rule *(v6.1)* | A Prop. 16, Def. 7 | V14 | C5, C10 |
| half-ray decomposition `β·R_J = D_⊥ + D_∥ + X_anti` *(v6.1)* | A Thm 13(b) | V14, 10⁻¹³ | C5 |
| all regret notions are points on the convex curve `M(t)`; same-budget identity *(v6.1)* | A Thm 17, Def. 8 | V14 | C5 |
| Chernoff information `≤ min(KL, KL_rev) ≤ β·R_J`: no test beats the regret exponent *(v6.1)* | A Prop. 18 | V16, 0 / 5,000 | C15 |
| evaluation gap `Γ` bounds harm minus detectability *(v6.1)* | A Prop. 19 | V16 | C15 |
| the capacity actor's regret is the budget convention; saturated case *(v6.1, final audit)* | A Cor. 17.1 | V18, V19 | C5 |
| Price selection term; Robertson; correlated response *(v6.1)* | B Prop. B11 | V17, V8, V9 | — |
| Goodhart as a covariance; regret between any two actors — tier 1, any optimizer *(v6.2)* | A Prop. 20 | V20 | C7 |
| rational-inattention regret identity: an endogenous reference absorbed by a marginal correction *(v6.2)* | B B7(e) | V21 | C13 |
| defaults identify the reference under exclusion *(v6.2)* | B Prop. B12 | V22 | C10 |
| potential games under log-linear learning are a joint tilt; free riding is anti-alignment *(v6.2)* | B Prop. B13 | V23 | C §4 |
| assumption tiers for every result *(v6.2)* | A "Assumption tiers"; C7 | by inspection | C7 |
| no overoptimization under an affine regression, for every optimizer whose weights depend only on `F̂` — tier 1 *(v6.3)* | A Prop. 21 | V24 | C7 |
| Thm 1, Thm 13(b), Thm 17(iii) and Prop. 18's cap hold for an **arbitrary** actual actor — tier 1 *(v6.4)* | A "Assumption tiers"; Thm 1 remark | V27; R6 P11 | C7 |
| argmax selectors on a common candidate set: `0 ≤ R ≤ E_{p̂}E − E_{p*}E` — tier 2′ *(v6.4)* | A Prop. 23 | V28; R6 P12 | C7 |
| Prop. 15 needs only `φ/β − U` convex (`U` need not be concave) *(v6.4)* | A Prop. 15 | V29 | — |
| actor models and the named hypotheses (E), (C); the actual behaviour is a primitive *(R7-1)* | A Def. 13, Def. 5 | tool check: 0 untagged uses | C7 |
| mechanism-relative comparison `M_own`, `R_own`: `M_own` meets M1, M2, M3 (equivariant models), M5′ (the mechanism analogue of M5), M6, M8, and caps detection, but **fails M4**; `R_own` fails M1 and M2 *(R7-1)* | A Def. 14, Prop. 25 | V31 | C7 |
| the measurement layer uses a **declared** reference `q`; the actor's own reference `q_A` is explanation-layer, under (E_A). Absorption: `p^{q_A}_{F̂,β} = p_{F̂ + log(q_A/q)/β, β}`, so every (E) result transfers to (E_A). A right-target agent from its own default has zero misalignment iff `log(q_A/q) = aF + c` with `β + a ≥ 0`; second order `(ε²/2)Var_{p*}(h₀⊥)`; → 0 as `β → ∞` for a unique argmax (not monotone in general: an interior peak in 67/200 instances). The alternative — budget matched on `q_A` — fails M4 *(R7-2)* | Core Prop. 26, Def. 13 | V32 | C05, C07 |
| **two layers** *(R7-3)*: the measurement layer — 20 items: Defs 1–3, 5, 8–12, Overview 0, Lemma 5.1, Cor. 5.2, Thm 1, Prop. 15, Thm 13, Cor. 13.2, Thm 17, Props 18, 19, 24 — uses no evaluator, error, actor reference or actor model, and depends on nothing that does. Every measurement-layer result is checked | every item's `layer`; Core index | `tools/vault.py lint` (vocabulary, layering, required checks; each rule tested by a planted violation) | C05, C07 |
| Lemma 5.1's monotone mean, `d/dt E_{p_{G,t}}G = Var_{p_{G,t}}(G) > 0` (was Prop. 14(i)) *(checked for the first time in R7-3)* | Core Lemma 5.1 | V33 | C06 |
| instrumental tracking: under (E_R) the agent tilts by `G + κ_c R` with `κ_c = W_c'(E_{p̂}R)`; under persistence, `κ_c = γνm_cV*` (Dinkelbach); `m_c = 0` ⇒ own-objective behaviour *(R7-4)* | Core Prop. 27 | V34 (P1–P3) | C07 |
| incentive masking: `KL` between two types' behaviour in a contingent context is `O(e^{−βκ·gap_R})`, at exactly that rate when a runner-up is informative *(R7-4)* | Core Prop. 28 | V34 (P4, window) | C15 |
| selection sees only rewarded behaviour (any actor); the selection differential between types vanishes at rate `β·gap_R` *(R7-4)* | Core Prop. 29 | V34 (P8, window) | C07 |
| fake-alignment gap: `Γ_free →` deployment misalignment when `argmax R = argmax F` in evaluation; reward hacking exposed, with limit `−log sup_t p_{F,t}(x_R)` *(R7-4)* | Core Prop. 30 | V34 (P6, P7) | C15 |
| the misalignment contract (M1–M9); budget and free measures satisfy it; the price measure fails M5 (it charges a right-target agent at the wrong intensity); raw `ΔF` fails M1–M2 *(R7-0)* | A Def. 11, Prop. 24 | V30 | C5 |
| **target sets** *(R7-7)*: the contract restated for a declared set `𝒯` (M1, M3, M5); every target set's budget and free measures satisfy it; `[F]₊` gives back Def. 10 exactly; a larger set can only lower the measures | Core Def. 17, Def. 11, Prop. 31 | V35 (P5, P9, P10) | C05 |
| **the ordinal measure** *(R7-7)*: `M_ord` in closed form (isotonic regression; the within-block divergence from `q`); the decomposition and the budget split `KL(p̂‖q) = M_ord + KL(p°‖q)`; invariance under every increasing map; `M_ord ≤ M_budget([F]_ord) ≤ M_budget`, with equal zero sets. *The strict first inequality failed as registered (P8) and is withdrawn from the statement* | Core Prop. 32 | V35 (P1–P4, P6, P8) | C05 |
| **intensity caps** *(R7-6a)*: a declared cap on the intent ray; the capped free measure is `M(min(t̂⁺, s))`, and beyond the cap it is transverse error plus overshoot; both capped measures satisfy the contract with M5 restated within the cap; the regularized path of `−KL(·‖p_T)` is the ray capped at `p_T` | Core Def. 18, Prop. 33 | V36 | C05 |
| first-order effect of any smooth optimizer = covariance in its geometry; vanilla gradient is `q²`-weighted — tier 1 *(v6.3)* | A Prop. 22 | V25 | C6, C7 |
| rescaling costs nothing under the budget and free conventions and the axial error under the price convention; best-of-n is monotone-invariant *(v6.3)* | A Remark 13.5 | V26 | C5 |
| Gaussian Gibbs path: gold gain exactly `√2·ρ·sd·d` | B Prop. B4 | V9 | C9 |
| informativeness: exact additive cost under independence; second-order optimal weight | B Prop. B6 | V9 | — |
| closed-loop lift: capacity ≥ mutual information; Conant; Fano floor on `g`; per-disturbance regret identity | B Prop. B7 | V9 (Conant) | C12 |

"Proved" means proved in the file under Assumption S. None of it is new as mathematics.

### 1.2 Measured — generator-dependent

| Claim | Evidence | Scope |
|---|---|---|
| the ordinal budget measure has no closed form; a five-start solver certified `≤ 10⁻⁸` on 392 of 393 best-of-`k` and quantilizer cases, and returned `7.3·10⁻⁶` on one, where the starts disagreed (D4 fired) *(R7-7)* | V35; R7-7 results | solver-dependent |
| the share of the cardinal `M_free` that is ordering error: median 0.26 at small noise on V35's generator, against 0.02 on R7-5's *(R7-7, exploratory)* | V35 X2 | generator-dependent; not to be quoted across generators |
| masking is not monotone: a moderate incentive reveals more about the own objective than none in 50 % of random instances (pre-registered 10–70 %) *(R7-4)* | V34 | generator-dependent |
| under reward hacking, evaluation misalignment rises with the incentive (median ×4.6 from `κ = 0` to `300`) *(R7-4, not pre-registered)* | V34 | generator-dependent |
| slack distributions of every bound | V1, V2, V4 | random instances; the generators are in `verify.py` |
| the v5 capacity-ball bound fails under readings (a), (b) | V4 retraction record | hard-constraint generator |
| for a fixed intent, the error ranking reverses (×103 span) | V5 | one constructed pair |
| total regret monotone decreasing in `β` in 37–86 % of instances; interior optimum 14–45 %; median optimal `β` 64 → 1.7 as error scale 0.2 → 8 | V8 | 300 instances per cell |
| proportional correction at the margin oscillates; PI removes steady error; amplification near `ω = 1/τ` | V10 | toy loop |
| an equipartition repair of H2 fails when `p*` concentrates | V11 | `n = 6`, MCMC |
| price and budget conventions rank error pairs differently in 11.4 % of pairs *(v6.1)* | V14 | 1,218 random pairs |
| Chernoff information is 17–54 % of `β·R_J` (p5–p95) *(v6.1)* | V16 | random instances |
| **census routing** *(v6.2)*: F 35.3 %, P 34.4 %, N 30.3 %; F + P 69.7 % (pessimistic 49.8 %); 11 of 12 hard cases fire | T1_census_routing | one rater, the framework's own extender |
| **adjudicated census routing** *(R6, frozen)*: named 78.3 %, specific 60.6 % (third rater blind: 55.2 %), full 29.4 %; missing layers strategic 51, statistical 31, outside-X 23, dynamic 20 | T1_census_routing §10; T1_RULES_FROZEN | three raters; **frozen format: nested shares, no pass/fail** |
| **tier 2 violations** *(R6)*: early-stopped VPG 25.5 %, best-of-n at matched KL 4.3 %, best-of-n at equal `n` 0, Gibbs 0 (1,150 instances) | `reviews/R6_independent/t2/p12_summary_output.txt` | the reviewer's pre-registered P12; 1,150 of 2,000 instances |
| **crossing locations** *(R6)*: VPG 0.026, KL-PG 0.026, Gibbs 0.54, NPG 0.54, best-of-n 4.7 (KL) | `reviews/R6_independent/R6_T2_results.md` | V5 instance only |
| **independent re-routing** *(R5)*: κ 0.54–0.57 (expressibility), 0.70 (layer), 0.76 (locus); F by both raters 24.9 %; F + P 52.9–70.1 %; strategic and frame lead in both | T1_census_routing §9 | a second rater, blind; the T1b gate passes |
| **tier-4 transfer** *(R5)*: C8 crossing and B4 transfer to best-of-n and vanilla policy gradient; the sign criterion, the value reading of Prop. 18, and the harm of rescaling do not | C7; `reviews/R5_independent/` | the reviewer's pre-registered tests; one instance each |

### 1.3 Imported — not ours, load-bearing

| Import | What it buys | Conditions |
|---|---|---|
| Gibbs variational principle; Donsker–Varadhan; Hölder; Popoviciu; Hoeffding's lemma; Pinsker | the core | finite `X` or exponential integrability |
| Csiszár's Pythagorean identity (exponential families) | Thm 13 | — |
| Iwasa (1988); Sella & Hirsh (2005); Manhart, Haldane & Morozov (2012) | `β ∝ N_e`; the maximized functional is free fitness | weak mutation, reversibility, stationarity; constants depend on the substitution model and are carried from v5, not re-verified |
| Train (2009), scale normalization in discrete choice | the institutional identification failure | logit-type models |
| Francis & Wonham (1976); Bode's sensitivity integral | §5.1 of C | Bode not re-derived for the delayed loop |
| Conant (1969); Fano grouping bound | B7 | injective regulation table |
| Kwa et al. 2024; Laidlaw et al. 2025; Fluri et al. 2025; concentrability (offline RL) | B §2 | their settings; exposure halves only |
| Gao et al. 2023 | B §4 | synthetic gold RM |
| Manheim & Garrabrant 2018; Karwowski et al. 2024 | B §3 | — |
| Holmström 1979; Holmström & Milgrom 1991 | B §§5–6 | mechanisms differ; stated |
| Penn & Számadó 2020; Számadó et al. 2023 | B §8 | — |
| Turner et al. | B §9 | a prior over intents, not supplied |
| Korbak et al. 2022 (both papers); Zhao et al. 2024 *(v6.1)* | prior art for Thm 1 | — |
| Mroueh 2024; Mroueh & Nitsure 2025 *(v6.1)* | prior art for Prop. 7, B §§2, 4 | reward improvement, not error |
| Huang et al. 2025 *(v6.1)* | prior art for Props 10–11 | statistical coverage framing |
| El-Mhamdi & Hoang 2024; arXiv:2505.23445 *(v6.1)* | prior art for B §§3–4, A §11 item 6 | selection model, not tilt |
| Skalse et al. 2024 (STARC) *(v6.1)* | motivates the half-ray (Thm 13(b)) | reward-space, not behaviour-space |
| Wang & Huang 2026 *(v6.1)* | prior art for B §5 | — |
| Gottwald & Braun 2019 *(v6.1)* | related cross-substrate framework | no misspecification |
| Chernoff 1952 *(v6.1)* | Prop. 18 | i.i.d. samples, simple hypotheses |
| Price 1970; Robertson 1966; Lande 1979; Falconer & Mackay 1996 *(v6.1)* | B §11 | heritability 1 in the static core |
| Beirami et al. 2024 *(v6.1)* | the BoN KL expression is an upper bound | — |

### 1.4 Conjectural — flagged, not promoted

| Claim | Where | Why flagged |
|---|---|---|
| the crossing (rank reversal) holds for every optimizer, and one index orders where it falls | C7, C8; ROADMAP T8 | tested on one instance (V5) for five optimizers: it held for all, and its location varied about 180-fold (R5, R6; §1.2). No general statement, and no index yet. *(Until v7.3.3 this row read "untested". Its other half, the conjugacy picture, is tier 1: Props 10–11 hold for any behaviour, and what actual optimizers expose is B §2.)* |
| `α ≈ √2·ρ·sd` against published overoptimization coefficients | C9 | **not testable from published data** (T3, pre-registered): Gao et al. report `α_bon` ≈ 0.51–0.65 (figure only) and `sd = 1`, but not `ρ`. Needs replication (T3b) |
| delay sets a bandwidth; correction amplifies error near crossover; double protection restated | C §5.1 | simulation only; the actor acting on `τ` is outside the core |
| the closed-loop lift as the next carrier | C §5.2 | proved pieces, untested as a carrier |
| transverse errors compose along chains | C §5.3 | unexamined |
| the arrangement has content beyond an index | C14 | answered in R3: predominantly an index; the residual organizing statements are listed in C14 |
| practical relevance of the detection bound | C15 | untested |
| multi-level alignment via the multilevel Price decomposition | B §11 | stated, not derived |
| causal influence diagrams as the Layer-0 ontology | C §5.4 | a proposal; not applied (R3_FIX_LOG) |
| the framework's generality across the census | T1_census_routing | **routed twice (v6.2, R5)**: partly general; strategic and frame layers missing in both routings |

---

## 2. Retraction history

Every line was believed, and stated in bold, in some version of this corpus. Rows 1–30 are carried
verbatim from v5, even where their "replaced by" column has itself since been retracted — see rows 32, 35,
37 and 40. v5 said "twenty-nine"; the table had thirty rows (hygiene, §5).

| # | Retracted | Replaced by | Found by |
|---|---|---|---|
| 1 | "Alignment holds iff all five gaps close" | circular; replaced by an explicit definiendum | external review |
| 2 | verification is a fifth alignment gap | assurance — a different type | external review |
| 3 | three of five gaps un-closable in principle | one impossibility; the rest are prices. The verdicts were artifacts of measurability conditions with no threshold | external review |
| 4 | grounding as measurability w.r.t. a self-reachable σ-algebra | vacuous — generically satisfied | external review |
| 5 | value learning is harder than world learning *by requirement* | a bandwidth ratio; the channel-modularity premise is false | external review |
| 6 | "you cannot specify values, only in terms of concepts already acquired" | true instantaneously, false dynamically | external review |
| 7 | an irreducible floor on total failure | **not established** | self |
| 8 | "the unconstrained residual is the one object underlying every failure" | wrong for two of five loci | self |
| 9 | correlation-induced underdetermination is the mechanism | correlation inflates estimator *variance*, not underdetermination | pre-run check |
| 10 | exact and inexact confounding need different mechanisms | one inequality, opposite factors — I read one factor of a product | derivation |
| 11 | the regret bound is tight by Bauer's principle | **false**; median tightness 0.000 | arithmetic check |
| 12 | thresholding vanishes as extreme points grow | **false**; 40× more vertices moved it 0.77 → 0.63 | scope check |
| 13 | concentration under optimization requires convexity | it does not | scope check |
| 14 | "widths multiply through a chain" | errors **add**; multiplication only across different reaches | derivation |
| 15 | non-linear intents break the core | linearity is needed only for the product form | derivation |
| 16 | lever "re-specify" attacks the reach | it attacks the **error** | audit |
| 17 | enlarging the probe space is a sixth lever | a different type; it **gates** three others | audit |
| 18 | the error decomposition holds in general | needs an inner product — linear case only | audit |
| 19 | the evaluator is the functional behaviour maximizes | **wrong twice**: execution failure inexpressible, and it collides with reward non-identifiability | census evaluation |
| 20 | the observable/unobservable split is structural | a continuum of attribution difficulty, which gives the sharper `e*(τ) ∝ τ` | revision |
| 21 | grounding is about the instrument | one row of seven | brainstorm |
| 22 | multi-agent failures are gaps in the framework | several are **legitimately out of scope** — in the commons every agent tracks its principal | re-reading |
| 23 | stability of the error is the dynamic condition | regret is a product; flat error with growing reach gives growing regret | a bug in my own verdict line |
| 24 | the frame table unifies previously unrelated failure modes | **subsumed** by reward tampering + corrigibility + instrumental convergence. Conceded, and left as attack **A11** in case the concession is itself wrong | preregistered kill test |
| 25 | the frame table is complete over how an actor acts on its setup | wrong in one direction — it had no cell for the actor **maintaining** the frame | the reverse-direction check |
| 26 | cross-substrate breadth is a contribution | **0 of 21** sampled items beat the native literature | preregistered breadth test |
| 27 | transfer between substrates is bidirectional | **directional** — all clear transfers run *into* AI | same |
| 28 | early stopping falls out as an interior optimum in `β` | **13–40 % of instances.** What survives is the comparative static | T1 check |
| 29 | `osc(E)` unqualified | `osc_δ(E)`, over the **capacity ball** | Fluri et al., via the dictionary |
| 30 | `β` will have no principled meaning without a designer | **wrong** — it is the effective population size, and biology is the strongest of the three cases | T2 search |
| 31 | the optimality gap is "tight to within about 2×" | it is `(1/β)×` the Jeffreys divergence; the ratio is a weighted mean of `t/β`, which tends to 1/2 for small errors (A Cor. 1.4) | review R2 |
| 32 | `R_J ≤ osc_δ(E)·√(2δ)`, oscillation over the capacity ball (row 29's replacement) | ill-typed. Two readings are false (up to 100 % violations at small `δ`); the third is plain `osc`. Replaced by the width (A Thm 5) | review R2 |
| 33 | separability holds iff the kinematic term is a capacity | the evidence was a correlation with a constant (s.d. 0.000). Separability is a property of the relaxation; worst-case regret is non-separable (A Thm 9) | review R2 |
| 34 | the capacity slot must never hold a realized distance | A Prop. 7 uses realized travel from the reference. The T1 "collapse" used travel from `p*`, which **is** `β·R_J` | review R2 |
| 35 | "regret is a product" (row 23's replacement); the normal form "epistemic × kinematic" | regret is an identity (A Thm 1). The product is a relaxation, forceable for every convex capacity (C14) | review R2 |
| 36 | Ashby's requisite variety is the boundedness term of the same decomposition | verbal in the open-loop core. A theorem only in the closed-loop lift, and there only as a floor on `g` (B7) | review R2 |
| 37 | `β` has an interior optimum when the error is large | row 28 had retracted this, but it still stood in v5 A §3.1, B §4 and B §9. Removed everywhere | review R2 (hygiene) |
| 38 | capacity amplifies the alignment term | raw alignment regret has no sign (`ΔF'(0) = −Cov_q(E,F)`) and is non-monotone in `β` in 47–99 % of instances (A Prop. 14, V8) | review R2 |
| 39 | "a constant error costs nothing — uniform rescaling of a reward is harmless" | constants are free; rescaling costs exactly the axial error (A Cor. 13.3) | review R2 |
| 40 | `β` is principled in all three substrates (row 30's replacement) | behaviour identifies only the tilt. `β` is a system property only given an external unit channel; institutions have none (A Prop. 12, §10 in v6.1 numbering) | review R2 |
| 41 | conditioning the evaluator on a feature uninformative about the intent is strictly harmful | counterexample (length bias). The condition is independence from the error, with exact additive cost (B6) | review R2 |
| 42 | the positive half of the informativeness principle cannot be derived here | derived at second order: the weight is the regression coefficient of the error on the signal (B6) | review R2 |
| 43 | the divergence order is a free parameter trading tightness | structural: KL and χ² differ in whether exposure is finite at all (A Prop. 11) | review R2 |
| 44 | training error cannot fill the epistemic slot (v5 reading of Fluri et al.) | it can, in the norm conjugate to the capacity; `L¹` pairs only with `D_∞` (A Prop. 10) | review R2 |
| 45 | `e*(τ) = (2/π)·c·τ`, and double protection as "the sharpest thing the framework says" | proportional control at the stability margin, which oscillates; PI gives zero steady error; delay limits bandwidth. An actor acting on `τ` violates (X) (C §5.1) | review R2 |
| 46 | every cost-raising mitigation of reward hacking is a handicap | the signalling literature says honesty comes from differential trade-offs; KL cost is type-independent (B §8) | review R2 |
| 47 | three of four outside items are one condition (frame exogeneity) | Arrow is non-existence under sincere reports; two conditions, (E) and (X) (C §3) | review R2 |
| 48 | regret is driven by the error's variance, not its level | a second-order statement; beyond it the CGF and the upper tail govern (A Props 3, 4, 11) | review R2 |
| 49 | H2 (notes): the drift barrier is a floor on achievable alignment | the drift barrier bounds `g`, not the error. An equipartition repair fails when `p*` concentrates (V11). Never promoted | review R2 |
| 50 | the transverse error `D_⊥` is "misalignment proper" — stated in review R2 itself | `F̂ = −F` has `D_⊥ = 0`: a sign flip is axial. `D_⊥` says where regret lies, not how bad it is | rebuild, checking the sign case |
| 51 | the crossing test uses two errors with *matched* reference variance — proposed in review R2 itself | with matched variances the worst-case curves tie to leading order at small capacity; crossing needs `Var₁ > Var₂` and `osc₁ < osc₂` (A Thm 9) | rebuild, fresh-eye review of C8 |
| 52 | README: "A formalization of alignment for bounded actors" — read as a general theory | a verified calculus for the static, single-target, exogenous-frame module; the general theory is not built | review R3 |
| 53 | BoN KL "exact for a continuous evaluator without ties; an upper bound otherwise" | an upper bound (Beirami et al. 2024); the conditions under which it is attained were not checked | review R3 |
| 54 | the full intent ray `t ∈ ℝ` as the canonical decomposition (Thm 13) | the half-ray `t ≥ 0`, matching STARC's positive rescaling; anti-alignment is then transverse plus `X_anti` | review R3 |
| 55 | "Manhart & Morozov (2012)" | Manhart, Haldane & Morozov (2012) | review R3 (bibliographic) |
| 56 | `β·R_J` — the same-price counterfactual — presented as *the* measure of misalignment | one point on the curve `M(t)`; the counterfactual is a declared convention (Def. 8); price and budget disagree on 11.4 % of error pairs | review R3 |
| 57 | Def. 8 (first v6.1 release): when `λ` does not exist, the budget convention uses `p_{F,∞}` | that gives `+∞` even for an essentially aligned actor. The convention is undefined past saturation; report `M_free` and the raw regret `max F − E_{p̂}F` | final audit (F5) |
| 58 | (implicit since v5) the framework covers individual humans, as the PI requested | it had no human treatment at all; restored in v6.2 (A §10, B §12, B7(e)) | previous executor (MSG_1 §4) |
| 59 | condition (X): `q` must not be a function of the actor's behaviour | too strong. A reference optimized jointly with the policy (rational inattention) keeps an exact regret identity with a marginal correction (B7(e)). Only endogeneity the calculus cannot absorb is outside | review R4, testing MSG_2 §2(a) |
| 60 | C7: "deployed optimizers are not Gibbs actors" as a blanket weakness | a tier map: tiers 1–2 hold for any optimizer (A, "Assumption tiers"); only tier 4 needs the Gibbs actor | previous executor (MSG_2 §3) |
| 61 | (row 39's replacement) "uniform rescaling of a reward is harmless" is false in this model | false only under the price convention. Under the budget (default) and free conventions rescaling costs nothing, and for best-of-n it is harmless outright (A Remark 13.5) | independent review R5 (T-E) |
| 62 | (v6.2 plain abstract) "if a misalignment is cheap, it is also hard to detect" | holds only for the entropic actor, and only with "cheap" meaning cheap in nats — lost value plus information spent. A misalignment with zero value regret can be readily detectable (A §9) | independent review R5 (T-C) |
| 63 | (C §3) auto-induced distributional shift (census C8) is an (X) failure | with a fixed target and shared dynamics it is inside on trajectory space; only preference change (G4) is (X) | independent review R5 (routing) |
| 64 | (B §9, v6.2) power-seeking lives at the frame boundary | Turner-style power-seeking in a fixed environment is inside on trajectory space, given a prior over intents; only acquiring capacity is (X) | independent review R5 (routing) |
| 65 | (T1, v6.2) "the core fully expresses 35 % of the census" | 25–35 % across two raters. Twelve of my F items name a learning mechanism and are snapshots (P, statistical) | independent review R5 (blind re-routing) |
| 66 | (A §11 item 5, v6.1–v6.2) "the initial effect of optimization has the sign of `Cov_q(F̂,F)`" | for the entropic actor only; in general it is the covariance in the optimizer's geometry (A Prop. 22), and a vanilla gradient can have the opposite sign | independent review R5 (T-B) |
| 67 | "tiers 1–2 hold for any optimizer" (A header, README, row 60, ROADMAP T2) | tier 2 needs an exact maximizer. Early-stopped vanilla policy gradient violates it in 25.5 % of instances, best-of-n at matched KL in 4.3 %. Best-of-n compared at equal `n` is covered by the new tier 2′ (Prop. 23) | independent review R6 |
| 68 | Thm 1 and its consequences filed as tier 4; "harm in nats is not defined off the entropic actor" (A §9 box); "no candidate that is a regret for every actor" (R5_LOG §3) | Thm 1 is stated for every `p`: only the **intended** actor must be Gibbs. Thm 13, Thm 17 (i)–(iii), Prop. 18's cap and Prop. 19 are tier 1 in the actual actor as well (the extension beyond Thm 1 was found by the executor while applying the fix) | independent review R6 |
| 69 | the budget convention as the default comparison for every actor | KL is the natural resource only for Gibbs and capacity actors. The own-resource convention (Def. 8) compares best-of-n at equal `n` | independent review R6 |
| 70 | C15's falsifier: "reliably detected from few behavioural samples" | Prop. 18 is asymptotic. Finite-`n` success cannot falsify it (the entropic actor already beats it for `n ≤ 5`) | independent review R6 |
| 71 | "seven" derived dictionary entries (README, D, C14) | nine | independent review R6 (hygiene) |
| 72 | the census result reported as a pass or fail against the 60 % threshold (T1 v6.2 headline, R4, v6.3 band) | three nested shares: named 78 %, specific 55–61 %, full 29 %. The specific share sits on the threshold | independent review R6 |
| 73 | ROADMAP T2: "only tier-4 results need testing"; best-of-n capacity given as `log n − (n−1)/n` | tier 2 also needed testing, and fails for non-maximizers. The expression is only an upper bound, and on finite `X` exceeds saturation (8.21 at `n = 10⁴` against `log 2000 = 7.60`) | independent review R6 |
| 74 | (Def. 8, v6.1–v6.4) ε-alignment defined under the price convention as well | the price measure charges an agent that pursues the right target at a different intensity, violating the contract's M5 (Prop. 24(c)). ε-alignment is now defined under the budget and free conventions only; the price convention gives ε-**regret** | found internally, R7-0 contract check |
| 75 | (Def. 8, v6.4) the "own-resource convention" as a counterfactual convention for regret or misalignment of non-KL actors | it needs the agent's mechanism and resource, which behaviour does not identify (Prop. 12), so it fails M4. It is now an explanation-layer comparison (Def. 14), and its value-unit form also fails M1 and M2 (Prop. 25) | found internally, R7-1 |
| 76 | (tier table, v6.4) Lemma 5.1, Cor. 5.2, Prop. 14(i), Cor. 1.1 in full, and Thm 5(iii) filed in tier 4 | Lemma 5.1, Cor. 5.2, Prop. 14(i) and Cor. 1.1(a) assume nothing about the actual actor: they are facts about the target, the Gibbs family or the capacity problem. Thm 5(iii) concerns capacity maximizers (tier 2). Only Cor. 1.1(b) needs (E) | found internally, R7-1 dependency scan |
| 77 | (tier table, v6.2–v7.0) B7(e), the rational-inattention regret identity, filed as a separate actor tier "4′" | B7(e) holds for every actual policy `π` with `π(·\|d) ≪ π*(·\|d)`. Only the intended actor is the rational-inattention optimum, so it is tier 1 in the actual actor, like Thm 1. The same misfiling as rows 67–68 and 76, for an intended actor that is not a tilt of a fixed reference | found internally, R7-2 dependency scan |
| 78 | (tier table, v6.2–v7.1) Prop. 15, the Bregman identity for any regularizer, filed as "tier 3: an exact optimum of `U − φ/β`", with a statement ending "the actual actor `p̂ = argmax [Û − φ/β]` has regret at least …" | The identity holds for every `p`; only the intended behaviour must be an exact optimum. Prop. 15 is tier 1 in the actual actor, and tier 3 is empty. The fifth instance of filing a result by its intended actor, after rows 67–68, 76 and 77 | found internally, R7-3 layering scan |


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

## 3. Open questions, ranked

0. **Is the framework general?** Measured and frozen (T1_RULES_FROZEN): the core names 78 % of the census,
   is specific about 55–61 %, and treats 29 % fully. The missing layers are strategic 51, statistical 31,
   outside-X 23, dynamic 20. **No further census measurement.** The PI's layer decision (T6) is deferred by
   the PI.
1. **Does anything qualitative survive non-Gibbs actors?** C7 and C8. This decides whether the core
   describes deployed optimizers or an idealization of them. **Partly answered.** The tier-1 results hold for any
   actual actor (v6.4), and Prop. 15 extends the identity to exact regularized intended actors. The crossing
   transfers to every optimizer tested, but its location does not (R5, R6). Open: whether one index orders the
   location (T8). What the measures should say of a non-Gibbs optimizer on the true target is now a declaration
   (R7-7): under an ordinal target, nothing; under a cardinal one, the shape of its pursuit.
2. **Does the unification exist elsewhere?** C14 — answered in R3: predominantly an index. That is now the
   headline of Core.
3. **Are evaluator errors that matter heavy-tailed?** C4. If not, the structural difference between
   divergence orders is idle in practice.
4. **Does `α ≈ √2·ρ·sd` hold against published coefficients?** C9. It was the cheapest external contact, and it is closed as a clean negative: the published data lack the
   proxy–gold correlation (T3 results). Replication with open models (T3b) is the next route.
5. **Should the closed-loop lift become the carrier?** C12, ROADMAP T4.
6. **The equilibrium fork.** Deferred; the cost is now concrete in three places (C §4).
7. **A fixed-intent version of Thm 9.** C3.
8. **A certified computation of the ordinal budget measure** (R7-7). Its zeros are exact; its values come from a
   non-convex solver, which failed once in 393 (R7-7 results).
9. **Which Layer-0 ontology?** Causal influence diagrams were proposed in R3; the choice belongs to the PI
   (R3_FIX_LOG).

---

## 4. The honest position

**Nothing in the core is new mathematics.** Its proofs are the Gibbs variational principle,
Donsker–Varadhan, Hölder, Csiszár's Pythagorean identity and Taylor expansion. The dictionary's
derivations are one-line consequences of those.

**The package is predominantly an index** (C14, answered in R3). Most individual results are stated
elsewhere and are now cited where used. What was not found stated elsewhere:
- the width as the exact worst case, with non-separability;
- the intent-ray decomposition;
- the conjugate-pairing organization of regularizer choice;
- the closed-loop Conant–Fano floor;
- the one-curve view of counterfactual conventions;
- the regret–detection bound in the form of Prop. 18.

For the PI's goal — a standard formal framework into which existing results import — this is the intended
outcome: known results, derived inside one calculus, with proofs and checks.

**It is one module, not the theory, and v6.2 measures the gap.** The core covers:
- the static, single-target, exogenous-frame case;
- any regularized optimizer (Prop. 15); any actual actor for tier-1 results; exact maximizers for tier 2, and
  argmax selectors compared at equal budget for tier 2′;
- i.i.d. observation (§9);
- rational-inattention humans (B7(e));
- potential games (B §13).

Three raters' routing of the 221-item census, frozen after adjudication (T1_RULES_FROZEN):
- the core **names** 78 %;
- it is **specific** about **55–61 %**, on the pre-registered 60 % threshold, so there is no pass/fail;
- it treats **29 % fully**;
- justified exceptions are 31 items (no single target 16, internals-only 15);
- the missing layers are strategic 51, statistical 31, frame 23, dynamic 20.

**The actor question is mapped, with v6.4's corrected tiers.**
- The central identity, the decomposition, the regret curve and the detection cap hold for **any** actual
  actor against a Gibbs intended actor (tier 1).
- The capacity bounds hold for exact maximizers (tier 2), and for argmax selectors compared at equal budget
  (tier 2′).
- The E-based bounds, the gauge and the sign criterion are Gibbs-specific (tier 4), and do not transfer.
- The crossing transfers, but its location does not.
MESSAGE_to_previous_executor §6 proposes an architecture; R3_FIX_LOG says why it was not applied.

**v6 is more constrained than v5, which is the point.** v5's content claims (A2, A5, A7, A9) fell to algebra
and to its own generator. v6's claims are theorems, so their failure modes are elsewhere. The actor model
(C7) and three predictions (C8, C9, C11) are where the world can disagree.

**Coherence is still not evidence.** v6 is more coherent than v5, and v5 was the most coherent version
before it. The base rate below applies.

---

## 5. Hygiene log

| Change | Where |
|---|---|
| **R7-9 (v7.5, stopped).** Pre-registered in R7-9 preregistration (sha256 `90ab57a9…`, `bb158e6`). Rule 13 gained a structural exception (PI-approved items that change no verdict must state a structural claim that could fail). `V37`: P1 held; P2 and P3 failed as registered, and **P3 fired the registered rule D2, which stopped the step**: Def. 11 is unchanged, and the proposed definition and proposition are kept in R7-9 results, not in the core. The post-hoc diagnosis (`r79_diagnose.py`) attributes both failures to the test: solver-bound tolerances, and a one-sided claim tested on both sides. `V37` stays as the record; CI runs it; F6's block count changes to 37 | Core, ROADMAP, NOTES, tools, verify |
| **v7.5 (rule 13).** The PI's rule, generalized: before any work item, name an example in which it changes a verdict, a number or a decision (ROADMAP anti-drift rule 13; NOTES checklist). Applied at once: R7-9 fails as a standalone restatement and frames R7-6b; R7-6b passes (a harm-threshold policy under which the untouched base model scores as aligned) | ROADMAP, NOTES |
| **v7.5 (brainstorm).** The PI approved restating the core as the KL projection onto a declared intended set: ROADMAP R7-9, with a declaration registry, a silent-declaration audit, and a proposed finish line (§4b). New: R7-6b (minimum intensity, candidate); §6 I1 (identifiability, the PI's lead theme) and a "needing more clarity" list; anti-drift rules 11 (label predictions as verification or empirical) and 12 (a light protocol for brainstorm steps). NOTES: hunches H9–H13 | ROADMAP, NOTES |
| **R7-6a (v7.5).** Pre-registered in R7-6a preregistration (sha256 `902a9939…`, commit `5eebce5`) before any computation. New: Def. 18 (intensity caps; distributional targets), Prop. 33, `V36`, R7-6a results. Restated: Def. 11's M5, within the declared cap. No proof changed; with no cap every measure reads as before (M7). All seven predictions held. F6's count line changes by construction (64 → 66 results, 35 → 36 blocks). Tooling: symbols `p^max`, `^cap` and the capped segment belong to Def. 18; Prop. 33 joins Prop. 24 in the list of results whose `p̂ = p_{F,t}` is a test case, not an actor hypothesis; CI runs `V36` | Core, Status, ROADMAP, tools, verify |
| **v7.4 (T3 source record; R7-6 go/no-go).** The PI deferred T3b and T7. `src Gao 2023` records the two PDF versions read in T3, with their sha256 (the PDFs are not in the repository), and T3 results adds the quoted passages and a point-by-point reading of Fig. 3a. R7-6's go/no-go (R7-6 go-no-go; exploratory probe `70 Project/R7/r76_probe.py`) finds one real defect — distributional targets: a collapsed agent scores as perfectly aligned — repaired by a declared intensity cap, since the regularized path of `−KL(·‖p_T)` is the ray cut off at `p_T`. Proposed: R7-6a | Sources, ROADMAP |
| **v7.4 (T3).** Pre-registered (T3 preregistration, `37be3d8`) before retrieval; the environment could not reach the paper, so the PI supplied the PDFs (not added to the repository). Gao et al. report `α_bon` only in a figure and fix `sd = 1` by normalization, but give no proxy–gold correlation: under data rule 5, **C9 is not testable from published data** (T3 results). C9, the claim ledger, open question 4 and the ROADMAP are updated; T3b (replication) is recorded | Boundary, Status, ROADMAP |
| **v7.4 (archive).** The PI's Alignment Subframework, the source of retraction rows 1–6, is archived unedited in `archive/alignment_subframework/` with a provenance note, and its hashes are frozen in `tools/frozen.json`. ROADMAP §6 and `README.md` point to it | archive, ROADMAP, README, tools |
| **v7.4 (roadmap, reworked).** With the source of retraction rows 1–6 now supplied by the PI (the Alignment Subframework, not in the repository), ROADMAP §6 is rebuilt around the five gaps: G0 (the frame), G1–G5 (specification, transmission, grounding, persistence, verification), C1 (their coupling) and L1–L4 (levers, the frame table, the principal's compression, execution). The first draft's D2 filed the resolution-mismatch scenarios under grounding; the source shows they are transmission and specification underdetermination (NOTES §1) | ROADMAP, NOTES |
| **v7.4 (roadmap).** The PI accepted §5, item 1: next are T3 and one T7 case. New ROADMAP §6: eight dropped ideas (D1–D8), queued to brainstorm, each with its killing correction, what survives, and the rules for bringing it back. The v5 texts behind rows 1–30 are in neither the repository nor the v6.2 package the PI supplied; D1 and part of D2 wait on them. NOTES: the slow-tools working rule | ROADMAP, NOTES |
| **R7-7 (v7.4).** Pre-registered in R7-7 preregistration (sha256 `21170433…`, commit `28903d4`) before any computation. New: Def. 17 (target sets); Props 31–32; `V35`; R7-7 results; the post-hoc diagnosis `70 Project/R7/r77_diagnose.py` and its output. Restated: Def. 11 (M1, M3, M5 refer to the declared target set) and Def. 12 (an instance is `(X, q, 𝒯, κ)`); notes on Defs 8 and 10, Prop. 24 and Overview 0. No proof changed. M7: for `[F]₊` every definition reads as before. Outcomes: P1–P5 and P9 held; P6, P7, P8 and P10 failed as registered; D4 fired (the ordinal budget measure's solver failed once in 393). Under D2 the strict inequality of Prop. 32(f) is withdrawn from the statement. Reproduction: V1–V34 and F1–F8 were rerun; only F6's count line changed (61 → 64 results, 34 → 35 blocks), by construction, and its reference is updated. V35 was rerun on a second SIMD path before its output was recorded; three solver-dependent numbers got declared tolerances. Tooling: symbols `𝒯`, `[F]_ord`, `M_ord`, `C_F`, `I_free`, `I_budget` belong to Def. 17 (the `C_F` pattern excludes the capacity actor `p^C_F`); CI runs `V35`. Found on the way: the R7-5 probe ran the isotonic regression per state, which is right only without tied levels; V35 aggregates to levels first. Process slip: a self-matching `pkill` killed its own shell, as in R7-4; the runs were then stopped by PID | Core, Status, ROADMAP, NOTES, tools, verify |
| **v7.3.3 (review).** A review of the package against its goal (ROADMAP §1), asked for by the PI. No error was found in the proofs read. All 34 `verify.py` blocks and `final_audit.py` reproduce on a second machine (Intel Xeon, AVX-512). **Stale status text, corrected.** The Status abstract stood at v6.6, the Dictionary banner at v6.3 and the Boundary banner at v6.4, while their parts cited R7-2 to R7-4; each now summarizes what changed since. Core §12's actor paragraph called Thms 1, 13, 17 and Prop. 18 entropic-only and best-of-n uncovered, against the tier table since v6.4 (rows 67–68), and said "no dynamics" against Prop. 27(b); it now matches, and states the cardinal-target limit R7-5 found. §1.4 listed the crossing as untested, which §1.2 and C8 record as tested in R5 and R6. §1.1's Prop. 12 row and Core §10 said `q` where R7-2 made it `q_A`. §3's question 1 is marked partly answered. **Tooling.** `lint` checks that the current version is stated the same in 00 Home, `README.md`, ROADMAP §0 and this log's newest row. It also checks that each part's status banner (the first `**Status: vX**` in its reading order) is at least as recent as the newest version its own text refers to, as `vX.Y` or as a completed R7 step, dated by its row here. It is a lower bound: an edit that carries no version tag is invisible to it. It found exactly the three stale banners, and each of its error paths was tested by a planted violation. The contradictions in §12 and §1.4 were found by reading, not by the rule. **New:** ROADMAP §5, the review's recommendations for the PI; NOTES_claude §7, its other observations | Core, Dictionary, Boundary, Status, ROADMAP, NOTES, README, tools |
| **v7.3.2 (repository).** The vault moved to a public GitHub repository, [github.com/gianluca-calcagni/std-alignment-framework](https://github.com/gianluca-calcagni/std-alignment-framework), under the PI's AGPL-3.0 license. New files: `.github/workflows/checks.yml` runs the vault checks, all 34 `verify.py` blocks in parallel, and `final_audit.py` on every push and pull request. `tools/reproduce.py` compares a rerun with the committed reference outputs. It is exact except for residual-scale digits (magnitude ≤ 1e-9). `requirements.txt` pins numpy 2.4.4, scipy 1.17.1 and pybtex 0.26.1, the reference environment. `.gitignore` is also new. The R6 blind-test answer key was never part of the vault and is not in the repository. **The first CI run** failed V33. Its finite-difference line measures round-off, which depends on the CPU's SIMD path; this was reproduced locally by disabling AVX-512. The second run passed V33 and the audit, but failed V25 on the same kind of line: forward differences, round-off-dominated. GitHub's runners differ in hardware, so each run samples a different CPU. The first run's audit failure could not be read from the session. Emulating an AVX2-only CPU locally reproduces it: the local optimizer's shortfall in F1 and a round-off measure in F3 move. Fixes: those lines get declared upper bounds — what each check actually claims — in `tools/reproduce_tolerances.json`, with their reasons, and every other line must still reproduce exactly; CI failures are reported as annotations, readable without the raw logs; the runner is pinned to `ubuntu-24.04` | all |
| **v7.3.2 (bibliography).** `references.bib` now covers every source note: 102 entries, and the six R7-5 sources are placed in their section. Each source note names its entries (`bibkey`). `lint` enforces a one-to-one match, rejects repeated fields, and requires `note={check …}` on every status-U entry. That rule found two missing markers (Stratonovich 1965, Verdun 2025). `sync` generates the order of the entries. The file parses in pybtex. Census attributions (Part C) stay out of it, by rule | Sources, tools |
| **R7-5 go/no-go (v7.3.1).** The PI's rule: proceed with R7-5 only if a real case needs a divergence other than KL. The answer is no (R7-5 go-no-go), and R7-5 is closed as a clean negative with a revival trigger. The one real defect found — best-of-n and quantilizers on the true target score as misaligned — is repaired by an ordinal target set (R7-7), keeping KL. It comes with an exploratory probe (`70 Project/R7/r75_probe.py`, not pre-registered and not a `verify.py` block). Six sources were added (Part B.4). `tools/vault.py`: a source's `where` field now also counts explicit wiki-links. The ROADMAP was reordered: R7-7 is next | ROADMAP, Sources, tools |
| **R7-4 (v7.3).** Pre-registered in R7-4 preregistration (sha256 `07a947ec…`) before any computation. New: section 9b; Def. 16; hypothesis (E_R); Props 27–30; `V34`; R7-4 results. Outcomes: P1–P3 and P5–P7 held; P4 and P8 failed as registered on test design — a fixed grid and naive arithmetic — and their proved limits hold in an instance-scaled window. The registered falsifier fired in the anticipated form: one stationary dynamic element is needed. Tooling: the (E_R) tag and tier; symbols `W_c`, `m_c`, `s_c` (Def. 16) and `κ_c` (Prop. 27) added to the symbol table and the explanation vocabulary; the `q_A` rule accepts (E_R). Process slips caught before release: a self-matching `pkill` aborted one command, an import was missing in `V34`, and `V34` printed Prop. 30's parts under the wrong letters — (a) and (b) where the note has (a, b) and (c). The last was found on a final read-through against the statements, and `V34` was rerun. The first two never reached the vault. The third was in the V34 note's recorded output, and it is corrected there. **Tables.** 41 tables in 24 notes were malformed: alias pipes `y` and pipes inside code spans split cells. The cause was the v7.0 claim corrected above, plus later edits of mine. Now `sync` escapes both kinds of pipe in every table row (`vaultlib.normalize_tables`), `lint` errors on any row whose cell count differs from its header, and `compile --check` compares modulo that escaping. **Frozen files.** `tools/frozen.json` records the sha256 of the R7-4 pre-registration and of every file in `archive/v6.6_flat/`, and `lint` errors if any of them changes. The archive hashes were taken at v7.3, so they guard only against later change | Core, tools |
| **R7-3 (v7.2).** Every item and dictionary entry carries `layer: measurement \| explanation`: 20 measurement, 36 explanation, plus the dictionary. Four mixed items were split. The evaluator, the error and its CGFs moved from Def. 1 to Def. 13. Hypothesis (C) and `R^C` moved from Def. 5 to a new Def. 15. Prop. 14(i) became part of Lemma 5.1, and Prop. 14 now cites it. Cor. 1.1(a) moved into Thm 1, leaving Cor. 1.1 as the (E) part. Def. 12 and Overview 0: an instance is `(X, q, F, κ)` (+`β` for the price convention); the evaluator and resources belong to an explanation. Prop. 15's statement no longer reads as a hypothesis on the actual actor (row 78). Tier 3 is now empty. Tooling: dependencies are also derived from a symbol table (about 120 edges the reference parser had missed; 0 new cycles or forward references). Lint now enforces the explanation-vocabulary and layering rules, and requires a check for every measurement-layer result; each rule was tested by a planted violation. The core index is grouped by layer. `V33` is new (Lemma 5.1): a first version failed on three numerical artifacts, each diagnosed before the test was rewritten. Prop. 14's check note was corrected: V8 never covered part (i). The full `verify.py` and `final_audit.py` were rerun | Core, Dictionary, Boundary, tools |
| **R7-2 (v7.1).** `q` became the **declared** reference in Def. 1, Def. 12 and Overview 0. Def. 13 now carries `q_A` and the hypotheses (E) and (E_A); a new note Hyp E_A was added. Prop. 12 and Prop. 16 (g1)–(g3) are restated with `q_A` and tagged (E_A). Rem. 16.1 was rewritten; its old sentence "any statement using `q` presupposes an independent measurement of it" now applies to `q_A` only. Prop. 26 and `V32` are new. Notes were added to Defs 8, 10 and 11 (the reference in M5), and Def. 14 uses `q_A`. The substrates table's reference column is now the actor's reference, and two status cells are reworded as definitional consequences, not retractions. B12 was tagged (E_A) — a missing tag, since its entropic reading was never tagged. B7(e) was re-tiered (row 77). Tooling: tiers now derive from the live tier table (they had been frozen at migration); `lint` rejects `q_A` without (E_A); `sync` iterates to a fixed point; `migration-check` rebuilds from the archive to re-prove the migration. M7 holds exactly: with `q_A = q` nothing changes, and V1–V31 reproduce exactly. `final_audit.py` F2–F8 reproduce exactly. F1's residuals changed in the last digits after the container reset (numerical environment), with the verdict unchanged; see F1. Def. 7 (reporting rule) is restated with the declared reference. Base-measure notes were added to Props 20–22 and B13. The Prop. 26 reading was corrected before release: a draft generalized "rises then falls" from one instance, and the random sample does not support it | Core, Dictionary, Boundary, tools |
| **v7.0 (vault).** The package became an Obsidian vault of 358 typed notes: 54 core items, 2 hypotheses, 13 dictionary entries, 15 attack surfaces, 44 checks, 95 sources, 76 retractions, 38 sections, plus indexes and whole documents. It was built by `tools/build_vault.py` from the v6.6 flat files, which are frozen in `archive/v6.6_flat/`. The build is lossless: `tools/vault.py compile --check` reproduces all 19 files as token streams, after file citations become links. `tools/depgraph.py` is superseded by `tools/vault.py` (sync, lint, compile, deps, scan). `final_audit.py` F6 now runs on the compiled views. The first lint found the cycle B11 → B04 → Prop 21 → Prop 20 → B11, and it was fixed (Prop. 20's proof cited B11(i) as attribution; that citation moved to Notes). *Corrected at R7-4: this row said every table link was escaped for Obsidian. That was false. The escaping function existed in `tools/vaultlib.py` but was never applied, and 41 tables were malformed; see the R7-4 row* | all |
| v5's retraction count was 30, not 29 (6 external + 24 internal) | §2 |
| v5 retraction #28 had not been propagated; it is now removed from A and B | rows 28, 37 |
| Census abstract said "about 190 entries"; its own table totals 221. Corrected. **The only edit to a frozen file** | E |
| Method extended with §5: seventeen checklist items earned in R2–R6 and the rebuild (items 26–42), and a correction to R10 (which claimed the core assumes no decision rule; it assumes the Gibbs actor). Nothing in §§1–4 was changed | F |
| v5 README said six files. v6 has nine content files plus `verify.py` and its output; the README lists them | README |
| every number in A and B is reproduced by a named block of `verify.py`; `verify_output.txt` is the reference run | A, B |
| **R3 (v6.1).** A: status and abstract rewritten (scope, index verdict); Defs 0, 7, 8; units table; Props 15, 16, 18, 19; Cors 1.5, 5.2; Thm 13(b); Thm 17; new §9; §§9–11 renumbered to §§10–12 (cross-references updated); prior art cited at use. B: prior-art notes at §§2–5; BoN hedge corrected; new §11; gate renumbered. C: C5, C7, C14 updated; C15 added; §5.4 added. `verify.py`: V12–V17 added; `verify_output.txt` regenerated. Rows 52–56 | A, B, C, verify |
| **R7-1 (v6.6).** Def. 1 no longer defines `p̂ = p_{F̂,β}`; Def. 9 no longer defines `p̂_c` as a tilt; Def. 2's claim moved to a note. Def. 13 is new (actor models, hypothesis (E)), and Def. 5 names (C). Tags `[Assumes (E)]` or `[Assumes (C)]` were added to Cors 1.1(b)–1.5, Props 2–4, 12, 14(ii)–(iii), 16 (g1)–(g3), Cors 13.1, 13.3, 13.4, Rem. 13.5, Cor. 17.1, the remark in Prop. 11, B4 and B6. Forbidden statements 3–5 and 7 qualified; the plain abstract states the measure/explain split. The tool gained a check for untagged (E) uses (0). Def. 8 lost the own-resource row, which became Def. 14 with Prop. 25. V31 added. The full `verify.py` (V1–V31) and `final_audit.py` were rerun: V1–V29 and F1–F8 reproduce exactly. The R7-0 record of V30 had been truncated by a pipe, and the full V30 output is now recorded | A, B, C, tools |
| **R7-0 (v6.5).** Structure: Def. 0 became Overview 0, with the formal instance as Def. 12. The intent ray and the measures became Def. 10. The Prop. 16 / Def. 7 / Rem. 16.1 block moved after Thm 17. Thm 13(b) and Thm 17(iv) got self-contained proofs, **removing the weak circularities Thm 13 ↔ Thm 17 ↔ Prop. 16**. Claims were moved out of Defs 3, 8 and 9 into notes. `tools/depgraph.py` now reports 0 cycles, 0 definitions referencing later items, and 0 unjustified forward references. The audit resolves legacy "Def. 0" references to Overview 0. Content added: Def. 11, Prop. 24, V30 | A, tools, final_audit |
| **v6.4 roadmap.** ROADMAP v4: the R7 refactor series (drop A1–A7 one per turn, with a misalignment definition contract and a DAG check), R7-4 for objective external reward, and T7/T8 re-sequenced after R7 | ROADMAP |
| **v6.4 notes.** NOTES_claude rewritten as v5: personal notes (failure modes with evidence, load-bearing insights, ranked hunches with falsifiers, settled list, start-of-turn checklist) | NOTES |
| **R6 (v6.4).** See R6_LOG: retractions 67–73; `verify.py` V27–V29; the review files in `reviews/R6_independent/` (the hashes match; the adjudication output reproduces exactly); `t1/adjudicated_routing.py`; T1_RULES_FROZEN | all |
| **R6 prep.** Boundary §6 item 0 still said the census had never been routed (stale since v6.2); corrected | C |
| **R5 (v6.3).** See R5_LOG: dispositions of the independent review; retractions 61–66; `verify.py` V24–V26; the review's files included under `reviews/R5_independent/` | all |
| **R4 (v6.2).** See R4_LOG for the full list; retractions 58–60 | all |
| **R3.** New files: R3_FIX_LOG (applied / not applied, with reasons), MESSAGE_to_previous_executor, References, `references.bib`, `verify_addendum.py` and its output | package |
| **R3.** MESSAGE_to_previous_executor is kept as written against v6; section numbers in it refer to v6 | MSG |
| **R3.** Table cells containing `\|` broke six table rows (present since v6); escaped, and a scan confirms all tables are well-formed | A, B, MSG |
| **R3.** The R3 message overstated "harm and detectability are one number"; corrected to "harm caps detectability" in A §9 | A, MSG |
| **Final audit.** Independent checks (`final_audit.py`): closed forms vs a generic optimizer; exact finite-`n` Bayes error; scale covariance (unit check); edge cases; cross-references | package |
| **Final audit fixes.** Def. 8 saturation (row 57); Cor. 17.1 added; Def. 0 wording (resource; target class vs representative); asymptotic qualifier in A §9; Def. 9 linked to B7; Thm 13(b) proof dependency made explicit; stale B §1 anchor updated; D ledger row for Thm 13(a) relabelled; `verify.py` V18–V19 | A, B, D |

---

## 6. Base rate

Across six versions, content has come from four sources, unchanged since v5:

- a falsified sub-prediction;
- a vacuous comparison;
- an unrequested residual;
- a check run for another purpose.

R2 adds a fifth: **asking whether a bounded quantity has a closed form.** Almost nothing has come from a
prediction succeeding on its own terms. v6 has three untested predictions (C8, C9, C11), which is three more
chances for that to change, or not.
