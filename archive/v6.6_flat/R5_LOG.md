# R5 log — the independent review, v6.2 → v6.3

> The independent reviewer's files are in `reviews/R5_independent/`. The review has no prose summary; its
> content is two pieces of work.
> - **A blind re-routing of all 221 census items.** The routing file was frozen with a sha256 hash before the
>   v6.2 routing was opened. It comes with agreement statistics and a check of my "generous 44" snapshot
>   judgements.
> - **Six pre-registered tests** of whether tier-4 (Gibbs-actor) predictions transfer to best-of-n and to
>   vanilla policy gradient.
>
> This log gives my assessment of that work, and says what was applied, where, and why — or why not.

---

## 1. Assessment of the review

**It was done well, and it moved the package.** The strengths:

- **Genuinely blind.** The frozen, hashed routing file was opened only after freezing. The whole census was
  routed, not the 40-item sample T1b asked for.
- **Better on method than my routing.** The `Pt` code — a snapshot that reduces to a generic proxy error,
  without using specific core structure — is a sharper category than my P. It explains why my pessimistic
  bound was mis-targeted while landing on nearly the same total.
- **Pre-registered with mechanisms,** failures reported as failures. Four of the six tests changed the
  package.
- **Pushbacks based on the framework's own objects**, not on taste (C8, D2/L4, J16, J4).

**Flaws and gaps.** None of them change a conclusion.

1. **T-A crossing location:** the script failed with a `NameError` (`q` undefined in `t2b.py`), so where the
   crossing falls is not reported. The crossing itself is.
2. **T-B for best-of-n:** pre-registered ("fails on a constructed instance") but not reported. Only the
   vanilla policy gradient part ran.
3. **The natural-policy-gradient sanity check:** pre-registered, not reported.
4. **"Category" is used more liberally** (20 items against my 13). Some of it I dispute. D10 (performative
   scheming) is a behavioural non-identification statement — Prop. 12: behaviour identifies only the tilt —
   not a mechanism-level question. M5–M7 are about behaviour across contexts.
5. **J16 (resistance evolution) routed F/static** via anti-alignment of the pathogen population's tilt with
   the designer's target. It is formally admissible — the core needs no principal — but it stretches "alignment"
   to a pair with no delegation between them. I keep my reading (strategic) and record the disagreement.
6. **No prose summary.** A short findings document would have made the review easier to absorb. The data
   were enough to reconstruct everything below.

---

## 2. What was applied

| # | Finding | Where it came from | What changed | Check |
|---|---|---|---|---|
| 1 | **Rescaling is harmless under the default convention.** Under the budget and free conventions, `F̂ = sF` costs nothing, because the actual actor lies on the intent ray. Best-of-n is invariant to monotone transforms. Only the price convention charges the axial error. The v6.1 sentence "rescaling of a reward is not harmless" was wrong under the package's own default | T-E | A Remark 13.5 replaces the box; A §11 item 4 qualified; D row 61 | V26 |
| 2 | **The detection link runs one way, and only in nats.** A misalignment with zero value regret can be readily detectable — the reviewer built one for best-of-n. The v6.2 plain sentence "if a misalignment is cheap, it is also hard to detect" dropped both "in nats" and "for the entropic actor" | T-C | A plain abstract; A §9 box restructured ("the bound runs one way only"); D row 62 | — |
| 3 | **The sign criterion is actor-specific.** A vanilla gradient's initial effect is a `q²`-weighted covariance, and can have the opposite sign | T-B | **New Prop. 22** (tier 1): the first-order effect of any smooth optimizer is the covariance in its own geometry; A §11 item 5, B §5 and C6 qualified; D row 66 | V25: opposite signs in 80 of 2,000 random instances |
| 4 | **No overoptimization transfers.** Vanilla policy gradient on a Gaussian joint has a constant gold-to-proxy ratio | T-D, with the reviewer's mechanism | **New Prop. 21** (tier 1): under an affine regression of target on evaluator, every optimizer whose weights depend only on `F̂` has gold gain = slope × proxy gain; B §4 updated | V24 |
| 5 | **Tail exposure is optimizer-dependent.** At matched proxy gain, best-of-n puts far less mass on a single spike, because its weight is `≤ n·q(x)` | T-F | Prop. 20's discrimination note (it does discriminate, 1.1–21×); B §2 (catastrophic Goodhart is a property of KL-regularized optima) | V26 (the `n·q(x)` bound) |
| 6 | **The crossing transfers.** It holds for best-of-n and vanilla policy gradient | T-A | C8 marked tested; C7 rewritten as a transfer table; NOTES H1 confirmed | reviewer's output |
| 7 | **The gauge is actor-specific.** Best-of-n identifies only the evaluator's ordering | T-E | A §12 scope note | V26 |
| 8 | **C8 (auto-induced distributional shift) is inside.** With a fixed target and shared dynamics, it lives on trajectory space; only preference change (G4) is (X) | routing pushback | C §3 table split; D row 63 | — |
| 9 | **Turner-style power-seeking needs a prior over intents, not frame endogeneity.** Only acquiring capacity is (X) | routing pushback (D2, L4) | B §9 corrected; C §3 table split; D row 64 | — |
| 10 | **My routing was generous on learning phenomena.** Twelve F items name a learning mechanism: goal misgeneralization, context-dependent training, learned evaluators, composition | blind re-routing | Accepted. Reported in `T1_census_routing.md` §9; the "fully expresses" claim becomes a two-rater band (25–35 %) in A, README and D; D row 65 | agreement recomputed by `t1/make_report.py`, matching the reviewer to three decimals |
| 11 | **The two-rater result** | blind re-routing | `T1_census_routing.md` §9 (computed from both routing files); the A header, README, D §4 and ROADMAP now carry the band; T1b marked done | — |
| 12 | **Lessons** | — | F_method items 37–39 | — |

**The robust answer to the PI's question after R5.** The core fully expresses about **a quarter to a third** of
221 alignment phenomena, and gives at least a snapshot of **half to two-thirds**. Justified exceptions number
about **20** items. **Strategic interaction and frame endogeneity are the largest missing layers in both
independent routings** (about 72 items).

---

## 3. What was not applied, and why

| Suggestion or implication | Why not |
|---|---|
| Adopt the reviewer's routing as the result | Two raters are reported side by side, with agreement statistics and a consensus column. Replacing one rater's judgements with the other's would hide the disagreement, which is itself information |
| Adjudicate the roughly 60 disagreements myself | I am one of the two raters. Adjudication should be done by a third rater, against the categories as written (`ROADMAP.md`) |
| Re-route my own routing after seeing the reviewer's | It would contaminate the blind comparison. The registered v6.2 routing stays as it was; accepted pushbacks are listed in §9 of the report |
| Run the missing T2 pieces (crossing location, best-of-n on T-B, natural policy gradient, KL-penalized policy gradient) | These are tests, not fixes, and they belong to the reviewer's pre-registration. Listed in `ROADMAP.md` T2 |
| Generalize "harm in nats" beyond the entropic actor | There is no candidate that is a regret for every actor. Tier 1 keeps `C ≤ KL(p̂‖p*)`; claiming more would repeat row 62 |
| Move J16, J19, D10 and M5–M7 to the reviewer's codes | Disagreements recorded, not resolved (§1, points 4–5) |
| Build the strategic/frame layer | Still a PI decision (T6). Both routings now support making it first |
