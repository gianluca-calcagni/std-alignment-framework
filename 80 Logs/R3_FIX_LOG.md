---
id: "R3_FIX_LOG"
type: "log"
source_file: "R3_FIX_LOG.md"
updated: "2026-09-26"
---
# R3 fix log — v6 → v6.1

> What was done with each recommendation of review R3. Sources for the recommendations are
> [[MESSAGE_to_previous_executor]] (written against v6) and the R3 feedback to the PI.
>
> Every applied mathematical change is proved in the file where it lands and checked by a named `verify.py`
> block. `verify_output.txt` is a full rerun of [[V01|V1]]–[[V17]] after all edits.
>
> Status: **Applied**, **Partially applied**, **Not applied**. Each item that is not fully applied says why,
> and where it is tracked.

---

## 1. Applied

### Prior art and bibliography

| # | Recommendation | What was done | Where | Check |
|---|---|---|---|---|
| A1 | Cite prior art at the point of use | Cited where each result is used: Korbak et al. and Zhao et al. (Thm [[Thm 1\|1]]); Mroueh / Mroueh & Nitsure (Prop. [[Prop 7\|7]], B §§2, 4); Huang et al. (A §6, B §2); El-Mhamdi & Hoang (A §11 item 6, B §§3–4); STARC (Thm [[Thm 13\|13]](b)); Wang & Huang (B §5); Gottwald & Braun (A §10); Ben-Tal et al. and Namkoong & Duchi (Prop. [[Prop 6\|6]]) | A, B | — |
| A2 | Correct "Manhart & Morozov" | Manhart, Haldane & Morozov (2012) | A §10, D, [[Sources index\|References]], `.bib` | — |
| A3 | Fix the best-of-n KL hedge | "Exact without ties" → an upper bound (Beirami et al. 2024); the conditions under which it is attained are not claimed | B §4; D row [[R053\|53]] | — |
| A4 | Lead with the index verdict | A header and README state the C14 answer; C14 marked answered; D §4 rewritten | A, README, C, D | — |

### Scope and definitions

| # | Recommendation | What was done | Where | Check |
|---|---|---|---|---|
| A5 | Narrow the scope claim | "A formalization of alignment" → "a verified calculus for one module, not yet a general theory", with the missing layers named | README, A header, D row [[R052\|52]] | — |
| A6 | Define "alignment instance" and "aligned" | Def. 0 (instance tuple); Def. [[Def 8\|8]] (ε-alignment under a declared convention) | A §§1, 7 | V14 |
| A7 | Add a units table | Table in A §1, covering all quantities including the new ones | A §1 | by hand |
| A8 | Treat full support as a normalization | `X := supp q` stated | A §1 | — |
| A9 | Drop the principal | Def. 0: the target is any designated functional, normative or teleonomic; no principal assumed. See P3 for why "intent" was not renamed | A §1 | — |
| A10 | Update the scope conditions | Actor, target, observation, static bullets rewritten | A §12 | — |

### New and revised results

| # | Recommendation | What was done | Where | Check |
|---|---|---|---|---|
| A11 | Make the gauge explicit and add a reporting rule | Prop. [[Prop 16\|16]] (gauge group; lists of identified and non-identified quantities); Def. [[Def 7\|7]] (reporting rule) | A §7 | V14 |
| A12 | Make the counterfactual explicit | Thm [[Thm 17\|17]]: all regret notions are points on the convex curve `M(t)`, with the same-price and same-budget points and `D_⊥` as the minimum; Def. [[Def 8\|8]] conventions; 11.4 % disagreement measured | A §7; D row [[R056\|56]] | V14 |
| A13 | Restrict the intent ray to `t ≥ 0` (following STARC) | Thm [[Thm 13\|13]](b): `β·R_J = D_⊥ + D_∥ + X_anti` on the half-ray, canonical from v6.1; Cors [[Cor 13.1\|13.1]]–[[Cor 13.2\|13.2]] restated; the full-ray identity kept as Thm [[Thm 13\|13]](a) | A §7; D row [[R054\|54]] | V14 (3·10⁻¹³, 1,052 anti-aligned cases) |
| A14 | Generalize Theorem [[Thm 1\|1]] beyond the entropic actor | Prop. [[Prop 15\|15]]: for any convex regularizer and concave target, regret is a Bregman divergence (equality at interior optima, `≥` at the boundary). Examples: χ²; a non-linear target | A §2 | V12 |
| A15 | The exchange rate is derived, not primitive | Cor. [[Cor 5.2\|5.2]]: `λ_δ = 1/V'(δ)`; `g(δ)` is the value-of-information curve | A §4 | V13 |
| A16 | Composition of stages | Cor. [[Cor 1.5\|1.5]]: stacked entropic stages equal one stage; second-order covariance cross term (outer/inner) | A §2 | V15 |
| A17 | Reference misspecification as a locus | Remark [[Rem 16.1\|16.1]] | A §7 | — |
| A18 | Observation channel and detection | New A §9: Prop. [[Prop 18\|18]] (no behavioural test beats the regret exponent); Def. [[Def 9\|9]] (contexts); Prop. [[Prop 19\|19]] (evaluation gap `Γ`) | A §9; new C15 | V16 |
| A19 | Import quantitative genetics | New B §11: Price's selection term (exact, any actor), Robertson's secondary theorem (= Prop. [[Prop 14\|14]](ii)), correlated response (= [[B04\|B4]]). The multilevel Price route is stated, not derived | B §11 | V17, V8, V9 |
| A20 | Institutional obstacle is the reference | A §10 states it, via Prop. [[Prop 16\|16]] (was NOTES H4) | A §10 | — |
| A21 | Connect the width to DRO | Prior-art note at Prop. [[Prop 6\|6]] | A §4 | — |

### Package housekeeping

| # | Recommendation | What was done | Where | Check |
|---|---|---|---|---|
| A22 | Update the attack surface | C1, C5, C7, C14 updated; C15 added; §5.4 records the Layer-0 proposal; ranking adds generality as target 0 | C | — |
| A23 | Put the generality test first | ROADMAP T1 = route the census through loci L1–L7 (pre-registered); T6 = Layer-0 decision; carrier rule updated | ROADMAP | — |
| A24 | Record the lessons | F_method items 33–34; D rows [[R052\|52]]–[[R056\|56]]; ledger, open questions and hygiene log updated | F, D | — |
| A25 | Every number has a check | `verify.py` V12–V17 added; full rerun into `verify_output.txt`; every number quoted in A and B cross-checked against the output | `verify.py` | mechanical grep |
| A26 | Cross-references | A §§9–11 renumbered to §§10–12 for the new §9; every cross-file reference updated. [[MESSAGE_to_previous_executor]] kept as written, with a header note | all | grep |
| A27 | Found during the fix pass: broken tables | Pipe characters inside table cells (`q(·\|argmax G)`, `\|E_pE − E_qE\|`, `E_q\|E\|`) broke six table rows. The bug has been present since v6. Escaped; a scan confirms every table in every file has consistent columns | A §§1, 6; B §2; MESSAGE | table scan |
| A28 | Found during the fix pass: an overstatement in R3 itself | "Harm and detectability are one number" → "harm in nats caps the detection exponent" (the ratio is 17–54 % on [[V16]]). Corrected in A §9, with a note in the message header | A §9; MESSAGE | V16 |
| A29 | Found during the fix pass: an understated scope note | Prop. [[Prop 15\|15]]'s scope note now also lists Thm [[Thm 17\|17]], Props [[Prop 18\|18]]–[[Prop 19\|19]] and Cor. [[Cor 1.5\|1.5]] as entropic-specific | A §2 | — |

---

## 2. Partially applied

| # | Recommendation | Applied part | Not applied, and why |
|---|---|---|---|
| P1 | Restate the core over general regularizers | The identity (Prop. [[Prop 15\|15]]), and the scope statement of which results remain entropic | Thms [[Thm 13\|13]] and [[Thm 17\|17]] and Props [[Prop 2\|2]]–[[Prop 4\|4]], [[Prop 14\|14]] and [[Prop 18\|18]] rely on the exponential-family form. The Pythagorean identity needs the intent ray to be an exponential family, and fails for other regularizers, whose "rays" are curves without that structure. Generalizing them is **new research, not a fix**; doing it inside a fix pass risks unproved claims. Tracked: A §12, C7. |
| P2 | Allow non-linear (concave) targets | The identity, in Prop. [[Prop 15\|15]], with a checked example | Widths, the conjugate pairings (Props [[Prop 10\|10]]–[[Prop 11\|11]]), Prop. [[Prop 14\|14]] and the Gaussian slope all use linearity in `p`. Extending them needs new results — e.g. linearizing `U` at `p*` and bounding the remainder — which should be derived and checked, not asserted. Tracked: A §12. |
| P3 | Drop the principal ("intent" → "target") | A definitional clarification in Def. 0 | Renaming "intent" across 13 files risks exactly the inconsistency F_method R12 forbids: a rename is done everywhere or not at all. Terminology is better reset once, in the Layer-0 rewrite (N3). |

---

## 3. Not applied

| # | Recommendation | Why not | Tracked in |
|---|---|---|---|
| N1 | Measurable spaces instead of finite `X` throughout | Re-proving every result under integrability conditions is substantial and a source of new errors. The only results needing infinite `X` (Prop. [[Prop 11\|11]], [[B04\|B4]]) are already stated on general spaces. The extension is routine under exponential integrability, and says so. Best done once, in the Layer-0 rewrite | A §12 |
| N2 | Sets of targets (aggregation, disagreement, multiple selves) | Requires choosing between worst case, Bewley-style dominance, or a social-choice rule. Arrow's theorem makes that choice substantive, so it belongs to the PI. A definition without results would be decoration | A §12; D §3 |
| N3 | Causal influence diagrams as the Layer-0 ontology | Changes the carrier. Anti-drift rule 1 requires a gate and a PI decision, and the candidate must first be tested on the 12 pre-registered hard cases | C §5.4; ROADMAP T6 |
| N4 | Frame conditions (E), (X) as graph conditions | Depends on N3 | C §3; ROADMAP T6 |
| N5 | Dynamic layer: correction loop, resource growth, target drift | A research programme, not a fix. The control-theoretic restatement stays a stated extension | C §5.1; ROADMAP T5 |
| N6 | Data layer: evaluator learned from `D ≠ q` | Needs a statistical model of evaluator estimation. The concentrability / coverage imports (Fluri, Huang) mark where it would attach | A §12; B §2 |
| N7 | Strategic, multi-agent layer | The equilibrium fork is deferred by design; reopening it is a PI decision | C §4 |
| N8 | Chains beyond entropic stacking | Only the entropic composition law is proved (Cor. [[Cor 1.5\|1.5]]). Heterogeneous links and delegation hierarchies are unexamined | C §5.3; NOTES H6 |
| N9 | Run the census routing | It is a **test** with a pre-registered prediction. Running it inside a fix pass would mix fixing with testing, and invites defining loci to fit the data. It is now ROADMAP T1, with the loci fixed before routing starts | ROADMAP T1 |
| N10 | Actor-robustness experiment | An experiment, not a fix | ROADMAP T2; C7, C8 |
| N11 | Verify the census sources (128 named, 57 generic) | Out of scope for a fix pass. They are listed item by item and flagged | [[Sources index\|References]] Part C |
| N12 | Re-verify the biology constants (substitution-model factor in `ν ∝ N_e`) | Requires primary-source reading not done in this pass. Still marked imported and not re-verified | A §10; D §1.3 |
| N13 | Re-derive Bode's integral for the delayed loop | Same reason; Freudenberg & Looze is the reference to check | C §5.1 |
| N14 | Confirm when the best-of-n KL expression is attained | Could not check the paper's statement in this pass, so the claim was **weakened** (A3) rather than confirmed | B §4 |
| N15 | Replace the old regret names with the single curve | Result numbers and names are kept stable so cross-references and the retraction history stay valid. Thm [[Thm 17\|17]] reads the old quantities as named points on `M(t)` | A §7 |
| N16 | Target uncertainty (CIRL), corrigibility as a target over the frame | Both need the dynamic layer or the Layer-0 frame (N3, N5) | MESSAGE §5.2 |

---

## 4. Net effect

**The module is now:**
- defined (Defs 0, [[Def 8|8]]);
- typed (units table);
- gauge-aware (Prop. [[Prop 16|16]], Def. [[Def 7|7]]);
- explicit about its counterfactual (Thm [[Thm 17|17]]);
- independent of the entropic regularizer for its central identity (Prop. [[Prop 15|15]]);
- connected to observation (Props [[Prop 18|18]]–[[Prop 19|19]]);
- honest about its prior art.

**It is still one module.** Everything in §3 is what separates it from the general framework the PI is
aiming at. The first test of that aim is ROADMAP T1: routing the census.

---

## 5. Final audit (after the fix pass)

An independent audit, `final_audit.py`, with its output in `final_audit_output.txt`. It does not reuse the
closed forms that `verify.py` relies on.

### What was checked

| Check | Result |
|---|---|
| **F1** Every closed-form actor (Gibbs, capacity actor at finite and infinite `β`, width, χ² actor, concave-target actor) against a generic constrained optimizer | The generic optimizer never beats a closed form (max gain `2·10⁻¹¹`). **This removes the circularity** of checking Lemma [[Lemma 5.1\|5.1]] with its own formula |
| **F2** Exact finite-`n` Bayes error, by enumeration of types | Converges toward the Chernoff information. It **exceeds `β·R_J` for `n ≤ 5`**, so Prop. [[Prop 18\|18]] is an asymptotic statement and is now worded as one |
| **F3** Scale covariance — a programmatic unit check of all quantity classes | Deviations ≤ `9·10⁻⁹` |
| **F4** Edge cases: `n = 2`, `q` masses `10⁻¹²`, `β` from `10⁻³` to 60, errors up to ~100, ties, strongly anti-aligned actors | All identities hold to ≤ `1.8·10⁻¹¹` relative |
| **F5** The Def. [[Def 8\|8]] budget fallback | **Defect found:** it gave `+∞` for an essentially aligned actor |
| **F6** Every numbered result and every V-block cited in any file | All exist (0 unresolved) |
| **F7** Capacity actor versus budget convention | They coincide (Cor. [[Cor 17.1\|17.1]]) |

### Fixes applied

| # | Fix | Where |
|---|---|---|
| X1 | Def. [[Def 8\|8]]: the budget convention is undefined past saturation; report `M_free` and the raw regret there. The behaviour of `M(λ) → ∞` near saturation is explained | A §7; D row [[R057\|57]] |
| X2 | New Cor. [[Cor 17.1\|17.1]]: the capacity actor's regret equals the budget convention, which links Thm [[Thm 5\|5]] and Thm [[Thm 17\|17]] | A §7; `verify.py` V18, V19 |
| X3 | Def. 0: resource wording; the target proper is `[F]₊`, and a representative is fixed only when value-unit quantities are reported | A §1 |
| X4 | Prop. [[Prop 18\|18]]'s box states that the claim is asymptotic, citing F2 | A §9 |
| X5 | Def. [[Def 9\|9]] linked to the closed-loop lift of [[B07\|B7]]: one structure, not two | A §9 |
| X6 | Thm [[Thm 13\|13]](b) proof: its use of Thm [[Thm 17\|17]](i) is shown to depend only on (a), so there is no circularity | A §7 |
| X7 | Stale B §1 anchor (two-term decomposition) updated; D ledger row relabelled as Thm [[Thm 13\|13]](a) | B, D |

### Not fixed, and why

The audit found nothing else that is a defect *within* the module. What remains is scope — sections 2 and 3
above — and PI decisions.
