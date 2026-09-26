# R4 log — v6.1 → v6.2

> Response to the previous executor's `MSG_1_findings.md` and `MSG_2_steering.md`, and to the PI's question:
> **is the formalized core general enough to discuss most alignment topics, with justified exceptions?**
>
> Every new mathematical claim is proved in the file where it lands and checked by a named block: `V20`–`V23`
> in `verify.py`, and `F8` in `final_audit.py`.

---

## 1. The answer to the PI

**Partly — and now measured rather than argued.** The census of 221 alignment phenomena was routed through
the core under a pre-registered rule (`T1_preregistration.md`, `T1_census_routing.md`):

| | Count |
|---|---|
| fully expressible (F) | 78 (35.3 %) |
| snapshot only (P) | 76 (34.4 %) |
| not expressible (N) | 67 (30.3 %) |

- **The rule (F + P ≥ 60 %, all N justified, ≤ 5 % unroutable) passes as written, but not robustly.** Under
  a pessimistic reading of projections, F + P = 49.8 %.
- **Justified exceptions in the PI's sense are only 19 of the 67.** Nine have no single target —
  aggregation, disagreeing principals, value change. Ten are mechanism-level (interpretability).
- **The other 48 are gaps, not exceptions.** Strategic interaction (23) and frame endogeneity (16) dominate:
  collusion, games, tampering, corrigibility, oversight subversion. These are central alignment topics.
- **Build-order signal:** 51 items need a strategic layer; 27 a dynamic layer; 22 a frame layer; 16 a
  statistical layer. A layer covering strategic interaction and frame endogeneity together — the causal /
  multi-agent influence-diagram proposal — would address 73 items (33 %). That is the PI decision `ROADMAP.md`
  T6 now has data for.
- **The §14 hard cases:** 11 of 12 fire (prediction ≥ 8, confirmed). Senescence is the one the core handles.
- **Caveat.** One rater, who extended the framework in this round. An independent re-routing (T1b) is needed
  before the numbers are quoted.

---

## 2. `MSG_1_findings.md` — dispositions

| § | Point | Disposition |
|---|---|---|
| 1 | Corrections of v5 confirmed independently | Acknowledged. The independent confirmation of rows 31–34, 39 and 45 is recorded here as evidence |
| 2 | V2 did not finish in the reviewer's sandbox; Prop. 3 not independently checked | **Done.** `final_audit.py` F8 (Student-t₃ errors, `β` from `10⁻³` to 30): 0 violations of either bound. The first bound is attained asymptotically when the tilt saturates (ratio 1.000), now stated in Prop. 3. V2 is slow by design (20,000 instances); it runs to completion here |
| 3 | Drift audit: no drift except clarity | Agreed |
| 4 | Human substrate absent — an explicit PI request | **Restored:** A §10 human row and paragraph; B §12; B7(e). D row 58 |
| 5a | Stale pointer C §5.4 → ROADMAP T4 | **Fixed** → T6 |
| 5b | Cor. 1.2 and 1.4 are history; "nothing downstream uses them" | **Partly disagree.** Cor. 1.2 is used in Prop. 7's proof, so it stays; only its last sentence is historical. Cor. 1.4 and Remark 7.1 are now titled "historical note". Numbers stay stable |
| 5c | The "plain terms" abstract is not plain | **Rewritten** without nats, CGFs or Bregman divergences. The technical summary is now the reading path |
| 5d | Nine results referenced nowhere outside A | Kept, because numbering is stable and some carry proofs of others. The reading path names the five results that carry the weight; the tier table places every result |
| 6 | Weight my suggestions accordingly | Done — see §3: one prediction refuted, one confirmed conditionally, one partly confirmed |

## 3. `MSG_2_steering.md` — dispositions

| § | Suggestion | Disposition and outcome |
|---|---|---|
| 1 | Let T1 decide the scope: add a minimal-layer column; pre-register the distribution | **Done.** Pre-registered guess: static 40 / statistical 10 / dynamic 20 / strategic 17 / outside 10 %. Observed: 36 / 7 / 12 / 23 / 22 %. Outside was more than double the guess, driven by frame endogeneity. **The architecture should follow this:** strategic plus frame first, dynamic second |
| 2a | Human actor: logit with a fixed default = Gibbs; rational inattention makes `q` endogenous — "an (X) violation inside the carrier" | **Prediction refuted.** The rational-inattention actor has an exact regret identity: the conditional KL minus the KL of the marginals (B7(e); `V21` to `2·10⁻¹⁵`). An endogenous reference optimized as part of the capacity is absorbable. **Condition (X) was too strong and is refined** (C §3; D row 59). Caveat: rational-inattention optima often drop actions, and then the identity needs absolute continuity |
| 2b | Default experiments may identify `q` for humans | **Confirmed, conditionally.** B12: under exclusion (the default does not change the evaluator), two defaults identify the reference within a parametric family (`V22`: exact). Implicit-endorsement effects bias the estimate (median error 0.16–0.39). Humans sit above institutions in A §10, conditionally |
| 2c | Naive vs sophisticated present bias lands on the (X) / equilibrium boundary | **Partly confirmed.** The sophisticated agent is an intrapersonal game, which is the equilibrium fork. But the naive agent is **not** a case of Cor. 1.5's stacked stages: its selves decide at different times, which is the dynamic layer. So the line falls between *dynamic without strategy* and *strategic*. A fourth name was added to A §10's "one boundary" |
| 3 | Tier every result by the assumption it needs; add two tier-1 identities | **Done.** Tier table in A; C7 rewritten as a tier map. Prop. 20 added — Goodhart as a covariance, and the regret between any two actors — with the caveat preserved (not shown to discriminate between optimizers). `V20`: best-of-k, top-m and arbitrary actors, to `2·10⁻¹⁵`. **The "what would make this wrong" test passes:** forbidden statements 1, 2, 7 (in part) and 8 (in part) are tier 1–2, so C7 is a precise map, not a blanket weakness. D row 60 |
| 4 | Clarity pass (optional, last) | **Partly:** plain abstract, reading path, and historical markers. A full layered rewrite was not done, because it was low priority and would churn the numbering |
| 5 | Do not build the Layer-0 carrier, target sets, or dynamic/strategic layers yet | **Respected, with one exception** (next section) |

## 4. One piece of the strategic layer, within the current carrier

T1 showed that strategic interaction is the largest need. A known theorem gives part of it without changing
the carrier: **log-linear learning in an exact potential game has the entropic actor on the joint behaviour
space as its stationary law** (Blume 1993; B13; `V23` to `6·10⁻¹³`). The collective's misalignment with a
welfare target is then the core's, with `E = Φ − W`, the tilt-form price of anarchy.

Worked case: **linear public goods — free riding is anti-alignment along welfare** (`t̂/β = −1/3`,
`X_anti > 0`; `V23`).

This is a theorem import, not a carrier change. It covers only exact potential games at stationarity. The
Layer-0 decision stays with the PI. It is reported as a **post-hoc** note in `T1_census_routing.md` §7, and
the registered routing was not altered.

## 5. Errors caught during R4

- **B13, before release.** A draft said free riding has `D_⊥ = 0`. That is true on the full ray, but under
  the canonical half-ray anti-alignment registers as `X_anti > 0` with `D_⊥ = KL(p̂‖q)`. Caught by checking
  the worked example against Thm 13(b), not against memory; `V23` now checks the decomposition. F_method
  item 36.
- **Rational-inattention check, first version.** It used an unconverged Blahut–Arimoto fixed point and
  reported an identity error of 1.1. The error came from non-convergence and zero-probability actions. It
  was replaced by exactly constructed optima, with the absolute-continuity condition stated.

## 6. What remains for the PI

1. **The Layer-0 / strategic-and-frame decision (T6)**, now with counts: 73 items.
2. **Target sets for disagreeing principals and value change** (outside-E, 13 items). The PI named these as
   the expected justified exception; the routing agrees that they are exceptions under the current design.
3. **An independent re-routing of the census (T1b)** before any number here is quoted.
