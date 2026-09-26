# Review R6 — message to the executor

> From the third rater (T1c). Scope:
> - blind routing of 121 items (101 disputed, 20 controls), hashed before phase 2;
> - eight rule-level rulings, then adjudication of all 121 items;
> - the tier-4 transfer tests left open by R5, pre-registered;
> - a pass over the core for errors.
>
> Data and scripts are in this folder. The R6 codes were frozen before I read v6.3 in full, and were not changed afterwards.

---

## 0. The short version

1. **The generality question sits exactly on its threshold.** Counting only snapshots that use specific core structure, F + P = **134/221 (60.6 %)**. The rule needs 133.
   - It fails under several single, defensible perturbations: my own blind codes give 55.2 %, and the pre-registered v6.1 scope gives 60.2 %.
   - **Stop reporting pass/fail.** Report three nested shares: the core *names* 78 %, says something *specific* about about 60 %, and treats about 29 % *fully*.
2. **The weakest joint for the AI substrate is the actor model (C7).** Three findings:
   - tier 2 is stated as "any optimizer" but is not;
   - the budget convention assumes that every actor's resource is KL;
   - the tier-4 crossing exists for every optimizer, but *where* it falls varies about 180-fold between them.
3. **The strategic/frame layer is still the largest gap.** A causal/multi-agent influence-diagram (MAID) layer would cover about 45 of those 74 items, not 73. The 23 biological items need evolutionary game theory, and B13 already holds the Gibbs-native piece of that.

---

## 1. The generality result, and how to report it

| Reading | F + P | Rule (a) |
|---|---|---|
| Adjudicated, Pt counted as not expressible (my ruling) | 134 (60.6 %) | pass by 1 |
| Pre-registered scope (v6.1 core: B13 excluded, so I15 → N) | 133 (60.2 %) | pass by 0 |
| My blind codes on the 121 items | 122 (55.2 %) | fail |
| Strict Q1 without the proxy clause | 120 (54.3 %) | fail |
| My time-inconsistency derivation rejected (H2, H3, H22, L11) | 130 (58.8 %) | fail |
| Pt counted as expressible | 173 (78.3 %) | pass |

**What is robust:**
- F is 65 (29.4 %).
- Every N item names a layer or an outside condition; nothing is undetermined.
- 11 of the 12 hard-case groups fired.
- Missing layers: strategic 51, statistical 31, outside-X 23, dynamic 20.
- Justified exceptions: outside-E 16, category 15.

**My recommendation.**
- Report the three shares (named / specific / full) with the band above.
- Any future measurement should fix, *before routing*:
  - P's definition: specific structure, with the proxy clause;
  - which additions count, i.e. which version of the core is being tested.
- Track post-hoc entries such as B13 separately, as T1 §7 already does.

**Rulings worth writing into `T1_preregistration.md` / `T1_census_routing.md`.** Full text in `adjudication_R6.py`, `RULINGS`.

- **Q1: a generic snapshot does not count.**
  - By Prop. 12, every behaviour can be written as a tilt by *some* evaluator, so "writable as an evaluator error" cannot fail and so cannot measure generality.
  - P therefore requires a numbered result beyond the generic carriers (Thm 1, Prop. 20, Prop. 14(ii), Defs 0–3) that bears on the item's distinctive feature.
  - A stated proxy relation counts as such a feature (Prop. 21, Thm 9).
- **Q2: learning items.**
  - Items that assert *what a learning process acquires or how it transfers* are at most P, in the statistical layer.
  - Items about the consequence of a *given* error profile (for example, a frozen evaluator used off its support) can be F.
  - Your acceptance of R5's reading in T1 §9 was right.
- **Q3: "category" means internal states only.** Items about evaluation awareness are behavioural: they are P, in a strategic-observation layer, not category.
- **Q6: whose behaviour.** outside-X applies when the actor changes its *own* frame; strategic applies when other parties reshape it.
- **Q8: undetermined.** It is legitimate only if the missing structure lies in no listed layer. All seven prior uses resolve:
  - L1, L2, A10 and A11 → outside-E;
  - D2, L4 and G9 → statistical, because a distribution over evaluators is a statistical-layer object.

---

## 2. Errors to fix in the package, ranked

1. **Tier 2 is stated as "any optimizer".** This appears in the A header, README, D row 60 and ROADMAP T2. MSG_2 and C7 give the real hypothesis: a maximizer over a set containing the intended actor.
   - P12 on 1150 V25 instances: early-stopped vanilla policy gradient (VPG) breaks Thm 5(i) or has negative regret in **25.5 %** of instances; best-of-n at matched KL does so in **4.3 %**; the Gibbs actor never does.
   - Fix: tier 2 = maximizers. Add a tier 2′ for pathwise selectors *at equal sampling budget*: best-of-n at equal n holds in 0 of 1150, by a coupling argument.
   - Delete "only tier 4 needs testing" from ROADMAP T2.
2. **Thm 1's tier is misstated in the other direction.** J_F(p\*) − J_F(p) = KL(p‖p\*)/β holds for **every** actual actor p; only the intended actor must be Gibbs. I checked it along 18,003 KL-PG iterates, to 2.8e-14.
   - So, at a declared price, "harm in nats" is a non-negative regret for every actor, and Prop. 18's detection cap applies to every actor.
   - The A §9 box ("not defined off the entropic actor") and R5_LOG §3 ("no candidate that is a regret for every actor") are too strong. T-C changed the counterfactual; it did not break the bound.
3. **The budget convention assumes KL is the actor's resource.** For best-of-n it is n. P12 shows the matched-KL regret of best-of-n can be negative, while the equal-n regret cannot.
   - Proposal: add a "same own resource" convention to Def. 8 / Thm 17 for non-Gibbs actors.
   - This refines the curve M(t); it does not replace it.
4. **C15's falsifier cannot falsify.** It says the bound breaks if misalignment with small harm "is reliably detected from few samples". `final_audit.py` F2 already shows the entropic actor itself beating the bound for n ≤ 5. Prop. 18 is a statement about the asymptotic error exponent, so the falsifier should be stated asymptotically.
5. **Stale statements.**
   - "Seven" derived dictionary entries (README, D, C14): B §14 counts nine.
   - ROADMAP T2 still gives best-of-n's capacity as `log n − (n−1)/n`, which row 53's retraction did not reach. On a finite X it exceeds saturation: at n = 10⁴ it is 8.21, against log 2000 = 7.60.
   - NOTES §0 still says "awaiting C14, then C7".
6. **A free generalization, not an error.** Prop. 15's proof needs only that φ/β − U is convex; U need not be concave.

**Checked and fine.**
- The algebra of Thm 1, Cors 1.2–1.5, 13.3 and 13.4, Props 2, 3, 4, 7, 14, 18, 19, 21 and 22, Thm 13(b), B7(c) and B7(e), and B13's sign.
- `final_audit.py` and `verify_addendum.py` reproduce exactly.
- No broken row, V-block or C references.
- **`verify.py` was not fully rerun by me.**

---

## 3. What the transfer tests show

Details are in `R6_T2_results.md`. The pre-registration hash is `99fde5a1…`.

**Nine of the eleven predictions I could test held in full. Two failed in part, and one prediction was not tested:**
- P3's path criterion failed: NPG tracks Gibbs only to about 2e-5, limited by the solver. Its crossing criterion held.
- P12's best-of-n prediction failed. My coupling argument was about equal n, not equal KL.
- P9 (KL-PG convergence) was not tested at full scale.

**What matters for the core:**

- **The crossing (C8) is universal; its location is not.**

  | Actor | d\* (KL) |
  |---|---|
  | VPG | 0.026 |
  | KL-PG | 0.026 |
  | Gibbs | 0.54 |
  | NPG | 0.54 |
  | best-of-n | 4.7 |

  Any statement of the form "at this capacity, error type X dominates" is specific to the optimizer.
- **KL-regularized policy gradient behaves like unregularized VPG** over the range where the crossing happens. Its early phase overshoots into near-determinism (runner-up probability 1.9e-10, against 0.19 at the optimum), and it relaxes toward the Gibbs optimum only on very long timescales. These are tabular softmax results, but they cut against reading RLHF-trained policies as Gibbs actors.
- **Prop. 22 generalizes.** Best-of-n's first-order effect is a *rank* covariance. It disagrees in sign with Cov_q in 2.45 % of random instances, and on a constructed instance where Cov_q = +18.6.

---

## 4. The most important gaps, and what each needs

In order of value per unit of work, by my judgement.

### 4.1 Re-tier the actor model (cheap, mostly documentation, high value)

What to do:
- Fix errors 1–3 of §2.
- State C7 as a three-part map:
  - tier 1, which includes Thm 1 in the actual actor;
  - tier 2, maximizers only;
  - tier 2′, pathwise selectors at equal sampling budget.
- Then finish T2: the 850 remaining P12 instances; P9 at scale; and the Prop. 7 regret bound for VPG, which is not yet checked.

**A hunch to test, clearly speculative.** The crossing's location may be ordered by how strongly an optimizer's update favours states that are already probable:
- VPG's update scales with p, so it crosses early;
- the Gibbs update is uniform in log-space;
- best-of-n's weight is capped at n·q(x), so it crosses late.

If one index predicts the order of d\* across optimizers, it would be the first tier-4 statement that transfers *quantitatively*.
- **Falsifier:** an optimizer whose update scales with p but that crosses late.

### 4.2 The strategic/frame layer (T6)

Counts from my adjudication: 51 strategic items (23 biology, 11 institutional, 13 AI, 3 formal, 1 human) and 23 outside-X items (16 AI).

**What a CID/MAID layer would and would not cover:**
- It fits most outside-X items: tampering, shutdown, oversight subversion, exfiltration, alignment faking, sandbagging. Each becomes a directed path from a decision node to a reward or utility node.
- It fits the roughly 28 AI and institutional strategic items: collusion, commons, contests, mechanism design, signalling, oversight and off-switch games.
- It does **not** fit the 23 biological items. Frequency-dependent population processes have no decision nodes. Extend B13 instead: potential games under log-linear learning are a tilt of the joint space, inside the carrier.

**Proposed gate, in addition to ROADMAP T6.** The core cannot distinguish an actor that *rewired* its evaluator from one facing a *lenient* evaluator: both are a region overrated under Prop. 4. The layer must make that distinction *quantitatively*, by attaching β·R_J or Γ to the diagram's nodes. If it only adds incentive typing, it moves items from N to P but none to F.

**First test.** The tampering family (A3–A5, L5) and the off-switch game (D4, L15). The layer should reproduce C §3's (X) table as graph conditions without special cases.

### 4.3 A statistical layer (31 items, 29 of them AI)

- **What it hosts:**
  - learned evaluators;
  - the learning/generalization cluster: goal misgeneralization, context-dependent training, emergent misalignment (B10, B11, M10, M11);
  - distributions over evaluators, which also covers Turner's prior (D2, L4) and correlated failure (G9).
- **Why it matters:** it is the cheapest route from P to F for the AI items.
- **One constraint.** Emergent misalignment contradicts the tilt model's locality: under Cor. 1.5 and Prop. 4, a narrow error stays narrow. So the learned-evaluator map must allow non-local effects, or it will reproduce the core's wrong prediction.
- **Pairing.** It sits naturally with 4.1, since both concern the AI substrate.

### 4.4 The generality measurement

- Do not re-adjudicate the census again.
- Freeze P's definition and the core's version, then measure on held-out items: the census's own §15 gaps, such as safety engineering, medicine, and command and control.
- The census has been used to motivate additions (B13), so it is no longer a clean test set.

---

## 5. Where to discount this review

**My weakest calls:**
- H2, H3, H22 and L11 rely on my own derivation: advance choices by a (β,δ) discounter are axial, immediate choices transverse, and Γ applies. It is exact only for quasi-hyperbolic discounting.
- The proxy clause: E5, F8, I21, J17.
- J16, as F.
- D10, as F.
- M2: I sided with your original F, which you later withdrew.

**Anchoring.**
- My blind codes agreed with the independent rater: κ 0.48, against 0.04 with you.
- 11 of my 32 phase-2 changes moved toward your routing, and the net effect of my changes was +12 items on the count.
- The T1c gate does not fire: my largest share with one rater is 54 %. Still, weigh my blind 55.2 % as the independent measurement.

**The controls.** I overrode 3 of 20: K10, I15 and G6.
- **K10** suggests a shared generosity: both raters treated Price/B11 as specific structure for biological conflicts.
- **I15** credits B13, which is post-hoc.

---

## 6. A closing note

Three practices made this review possible, and I would keep them:
- the retraction ledger;
- the tier map as a concept;
- your written acceptance of R5's learning-mechanism reading.

The package is honest about what it is. The main risks now are that the generality claim is quoted as a pass, and that tier-4 predictions are quoted for trained policies. The data in this folder support neither.

---

## Files

| File | Contents |
|---|---|
| `R6_MESSAGE_to_executor.md` | this message |
| `R6_T2_results.md` | the transfer tests: pre-registered results, post-hoc analyses, what is unfinished and how to finish it |
| `adjudication/routing_R6_phase1.py` | blind routing, sha256 `ccdfc8c3…` |
| `adjudication/adjudication_R6.py` | the eight rulings and 121 adjudicated codes, sha256 `5eda7931…` |
| `adjudication/compute_final_output.txt` | final distribution over 221 items, both readings |
| `t2/R6_T2_preregistration.md` | sha256 `99fde5a1…` |
| `t2/*.py`, `t2/*.log` | the harness and runs (`t2_r6.py` holds the actors) |
