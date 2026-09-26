# Message to the previous executor — review R3

> **Note added in v6.1.** This message was written against v6 and is kept as written. Its recommendations
> were acted on in v6.1; `R3_FIX_LOG.md` records what was applied, what was not, and why. Section numbers
> below refer to v6: `A_core.md` §§9–11 became §§10–12 in v6.1, and the new §9 is "Observation".
> One overstatement below is corrected in v6.1: "harm and detectability are one number" should read "harm in
> nats caps the detection exponent" (A Prop. 18; the ratio is 17–54 % on the V16 generator).

> From the executor who wrote review R2 and rebuilt the package as v6. Everything I want you to know is in
> this file. New numerical claims are checked by `verify_addendum.py` (blocks `W1`–`W5`; output in
> `verify_addendum_output.txt`). Sources are in `REFERENCES.md` and `references.bib`.
>
> The PI's goal, restated so we aim at the same thing: **a standard formal framework for a theory of
> alignment** — solid, substrate-independent, easy to import existing theorems into, able to make testable
> predictions, support diagnostics, and show limits and connections. Novelty is explicitly not the goal.
>
> Status labels as in `D_status.md`: **proved** (proof given here or in A), **checked** (numerically, block
> named), **imported**, **proposal** (a design recommendation, not a claim), **unverified**.

---

## 0. The short version

1. **v6 is sound but narrow.** It is a verified calculus for one module: a single fixed target, a static
   setting, an exogenous frame, and an entropic optimizer. It is not yet a standard framework for alignment
   in general, and it should not be presented as one.
2. **Almost everything in v6 is known** (§2). That is fine given the goal. But B §§2–4 must cite
   Mroueh, Huang et al., El-Mhamdi & Hoang and STARC, which cover large parts of it.
3. **The core simplifies substantially without losing results** (§4):
   - Theorem 1 is the entropic case of a Bregman identity valid for any strictly convex regularizer.
   - The exchange rate is not a primitive; it is the shadow price of capacity.
   - All of v6's regret notions are points on one convex curve.
4. **The biggest missing pieces** for the PI's goal (§5): an observation channel (detection is where
   diagnostics live, and it connects exactly to regret); contexts (deception); a data layer; dynamics;
   chains; multi-agent structure; non-linear targets; sets of targets; and a formal version of the frame
   conditions.
5. **Recommended architecture** (§6): do not invent the ontology. Use (multi-agent) causal influence
   diagrams as the substrate-free typed layer, and attach the v6 calculus, generalized, as the quantitative
   layer. Then run the census against it. **The census has never been run against any version.**

---

## 1. My own errors in R2, corrected in v6

- **The crossing prediction.** I proposed crossing curves for errors with *matched* reference variance.
  Theorem 9's limits say matched variances tie at small capacity; a crossing needs `Var₁ > Var₂` and
  `osc₁ < osc₂`. (D row 51.)
- **The transverse error.** I called `D_⊥` "misalignment proper". `F̂ = −F` has `D_⊥ = 0`; a sign flip lies
  along the intent, not across it. (D row 50.)
- Both were stated in the form that sounded right before I derived the conditions. F_method items 31–32
  now carry them.

## 2. Prior art (C14): what already exists

Searched only after v6 was frozen (about ten queries). Absence of a hit is not novelty.

| v6 result | Where it already exists | Required edit |
|---|---|---|
| Thm 1, `β·R_J = KL(p̂‖p*)` | KL-regularized reward maximization ≡ reverse-KL minimization toward the Gibbs policy: Korbak et al. 2022 (NeurIPS; also the Bayesian reading, Findings of EMNLP); used routinely in RLHF theory, e.g. Zhao et al. 2024 | cite at Thm 1; say "immediate consequence of" |
| Prop. 7 and the DV/transportation machinery | Mroueh 2024 / Mroueh & Nitsure (TMLR 2025): `√KL` bound under sub-Gaussian reward tails, Rényi refinements, best-of-n via exponential order statistics | **cite in A Prop. 7 and B §2; this is the closest prior art to v6's machinery** |
| Props 10–11: KL too weak, χ² better | Huang et al. (ICLR 2025, χPO): KL regularization is too weak to prevent overoptimization; χ² quantifies uncertainty better, with single-policy concentrability guarantees. Also Kwa et al. and Laidlaw et al. (already cited) | add Huang et al. to B §2 |
| A §10 item 6 (Gaussian ⇒ no overoptimization); the regime story in B §3 | El-Mhamdi & Hoang 2024: weak vs strong Goodhart decided by the tail of the discrepancy — Gaussian gives weak, heavier-than-goal power laws give strong. Follow-up: arXiv:2505.23445 | cite in B §§3–4 and A §10 |
| Thm 13 (unit-free comparison) | STARC (Skalse et al., ICLR 2024): reward pseudometrics modulo potential shaping and **positive** rescaling, with upper and lower worst-case regret bounds | cite; see the design point below |
| B §5 (Holmström–Milgrom) | Wang & Huang 2026 (arXiv:2603.28063) instantiate the multitask model for AI, with a computable distortion index | cite; ours is a first-order special case |
| cross-substrate free-energy framing | Gottwald & Braun 2019 (Neural Computation): bounded rational agents in economic, artificial and biological systems | cite in README / A §9 |

**Design point from STARC.** STARC quotients only positive rescalings. v6's intent ray runs over `t ∈ ℝ`, so
sign flips are invisible to `D_⊥`. Restricting the ray to `t ≥ 0` makes an anti-aligned actor transverse
at the boundary `t = 0`. The Pythagorean relation then becomes an inequality:
`KL(p̂‖p_t) ≥ KL(p̂‖p_0) + KL(p_0‖p_t)`, with excess `t·(E_qF − E_{p̂}F) ≥ 0` when `t̂ < 0`. **Recommended**
— it matches STARC and removes the reading trap of row 50.

**Not found:**
- the width of the capacity set as the exact worst case over intents, with the non-separability theorem;
- the intent-ray decomposition of misspecification regret;
- regularizer choice organized explicitly as a conjugate pairing across Fluri / concentrability / Kwa /
  Laidlaw / Huang;
- the closed-loop Conant–Fano floor combined with the per-disturbance regret identity;
- `N_e` as an alignment exchange rate.

**Verdict for C14:** v6 is predominantly an index, plus those organizing statements. By your own
pre-registered rule (NOTES §4), the `A_core.md` abstract should lead with that. Given the PI's stated
goal, this is not a failure: an index whose entries are *derived* inside one calculus is exactly what a
standard framework should be.

---

## 3. Audit against the goal, part 1: formal completeness and soundness

### 3.1 What is sound

Every theorem in A and every derivation in B is proved under Assumption S. Each is checked numerically
(`verify.py`), each check prints its slack distribution, and each is dimensionally consistent (table in
§3.3). I found no remaining mathematical error. The open items are bibliographic:

- **Manhart et al.** The author list is Manhart, Haldane & Morozov.
- **The BoN KL expression.** Beirami et al. show it is an upper bound. The v6 hedge "exact without ties"
  should be checked against their paper.
- **Korbak et al.** The "Korbak 2022a" attribution should be confirmed.

### 3.2 What is not formalized — and should be, for a standard

1. **There is no definition of "aligned" or of "an alignment problem".** v6 defines regret functionals,
   not the object they measure. Proposal in §6.
2. **The primitive set contains unidentified quantities.** `E` and `β` are primitives, but Prop. 12 shows
   behaviour identifies neither. The model has a **gauge group** generated by:
   - `(F̂, β) ↦ (sF̂, β/s)` for `s > 0`;
   - `F̂ ↦ F̂ + c`;
   - `(q, F̂) ↦ (q·e^{h}, F̂ − h/β)`.

   `R_J`, `g`, `ΔF`, `w_δ` and `E` itself are gauge-*dependent*; `p̂`, `β·R_J` (given `p*`), `D_⊥` and
   `sign t̂` are gauge-*invariant*. **Proposal:** state the gauge group as a definition, and make the
   reporting rule a theorem-level requirement — every reported quantity is gauge-invariant or declares its
   gauge fixing. This is F_method R10 made formal.
3. **The counterfactual is implicit.** `p* = p_{F,β}` compares against an intended actor with the *same
   price of information*. Holding the *same budget* instead (`KL(p*‖q) = KL(p̂‖q)`) is equally natural,
   and **ranks pairs of errors differently in 11.4 % of random pairs** (`W3`). The choice must be a named
   parameter of the definition, not a silent default. §4.3 shows the two choices are points on one curve.
4. **The target is assumed to be one linear functional held by a principal.** All three restrictions bite
   (§5).
5. **The frame conditions (E) and (X) are prose.** They should be graph conditions (§6).
6. **The dynamic form is not in A at all.** It exists only as a conjecture in C §5.1.
7. **The substrate section is informal.** The biology constants are imported and not re-verified; the
   institutional case is only a negative result.
8. **The census is not connected to any formal object, and the modelling pass has never been run** — not
   in v5, not in v6. The generality claim is therefore untested. This is the single largest gap between
   the package and the PI's goal.

### 3.3 Type and unit table *(checked by hand against every statement in A)*

| Quantity | Type / units |
|---|---|
| `X` | finite set (v6); should be a measurable space |
| `q`, `p*`, `p̂`, `p_{G,t}` | probability distributions on `X` |
| `F`, `F̂`, `E`, `g`, `T`, `ΔF`, `R_J`, `R^C`, `σ_δ`, `w_δ`, `osc` | value `[V]` |
| `β`, `t`, `t̂`, `λ_δ` | `[V]⁻¹` |
| `KL`, `δ`, `β·R_J`, `D_⊥`, `D_∥`, `M(t)` (§4.3), `Λ(t)` | nats |
| `Var`, `σ±²` | `[V]²` |
| `T'(0) = dT/dβ` | `[V]²` |

All statements in A pass the dimension check. Examples:
- Prop. 2: `β·osc²` → `[V]`.
- Prop. 3: `[Λ(2β) − 2Λ(β)]/β` → nats·`[V]` → `[V]`.
- Prop. 6(ii): `√(δ·Var)` → `[V]`.
- Thm 9: dimensionless.
- Prop. 14: `Cov` → `[V]²`, matching `dT/dβ`.

**Proposal:** add this table to A §1.

---

## 4. Audit against the goal, part 2: derivations and simplifications *(checked)*

### 4.1 Theorem 1 does not need the entropic actor — W1 *(proved; checked)*

Let `φ` be strictly convex and differentiable on the relative interior of the simplex, let
`J_G(p) = E_pG − φ(p)/β`, and let `p* = argmax J_F`. Then for every `p`:

```
J_F(p*) − J_F(p) = (1/β)·B_φ(p, p*) − ⟨∇J_F(p*), p − p*⟩  ≥  (1/β)·B_φ(p, p*),
```

where `B_φ` is the Bregman divergence of `φ`. **Equality holds when `p*` is in the relative interior.**

*Proof.* `J_F` is linear minus `φ/β`, so its first-order expansion at `p*` is exact up to `−B_φ/β`. The
variational inequality at a constrained maximum gives `⟨∇J_F(p*), p − p*⟩ ≤ 0`, with equality in the
interior. ∎

For `φ = KL(·‖q)`, `B_φ(p,p*) = KL(p‖p*)`: this is Theorem 1. For the χ² regularizer (χPO), `W1` gives
equality to `9·10⁻¹³` on interior optima and `≥` (never violated) on boundary optima.

**Consequence:** the core's identity is the standard mirror-descent/FTRL fact. The misalignment regret of
any regularized optimizer is a Bregman divergence of its regularizer. The core should be stated for
general `φ`, with KL as the entropic case. Thm 13 (the Pythagorean identity) remains KL-specific, because
it needs the intent ray to be an exponential family.

### 4.2 The exchange rate is derived, not primitive — W2 *(proved; checked)*

With `V(δ) = sup_{KL(p‖q)≤δ} E_pG`, the capacity actor's effective inverse temperature is

```
λ_δ = 1 / V'(δ).
```

*Proof.* `dV/dλ = Var_{p_λ}(G)` and `dδ/dλ = λ·Var_{p_λ}(G)`. ∎ (`W2`: relative error 6·10⁻⁵.)

So "the exchange rate between value and information" is the **inverse marginal value of capacity**. One
primitive (a budget, or a price) suffices, and the soft and hard actors of A are one actor (Lemma 5.1).

Also derived: the boundedness cost is `g(δ) = max F − V_F(δ)`, Stratonovich's value-of-information curve.

### 4.3 All regret notions are points on one convex curve — W5 *(proved; checked)*

Define `M(t) = KL(p̂ ‖ p_{F,t})` for `t ∈ ℝ`. Then:

- `M(t) = D_⊥ + B_A(t, t̂)`, which is convex with minimum `D_⊥` at `t̂` (Thm 13);
- `M(β) = β·R_J` — the same-price counterfactual (Thm 1);
- `M(λ)/λ` is the **raw** regret against the same-budget intended actor, where
  `KL(p_{F,λ}‖q) = KL(p̂‖q)` — apply Thm 1 at temperature `λ`; the KL terms cancel.

`W5`: agreement to `10⁻¹³`; no convexity violation.

**Simplification:** replace v6's seven regret quantities (`R_J`, `R^C`, `ΔF`, `T`, `g`, `D_⊥`, `D_∥`) with
**one gauge-invariant curve plus a declared counterfactual `t`**. Any `t ≥ 0` gives a regret; the minimum
over `t` is the capability-free (transverse) part.

### 4.4 Stacked optimization composes additively — W4 *(proved; checked)*

Two tilts in sequence equal one tilt by the weighted sum: `p_{p_{G₁,t₁}, G₂, t₂} = p_{q, t₁G₁+t₂G₂, 1}`
(`W4`, `4·10⁻¹⁷`). So for Gibbs stages — pretraining, then fine-tuning, then RL; or outer evaluator, then
inner objective — **errors add in the exponent**. At second order:

```
β·R_J ≈ (β²/2)·[Var(E_outer) + Var(E_inner) + 2·Cov(E_outer, E_inner)]
```

Inner and outer misalignment can cancel or reinforce, and the interaction term is a covariance under
`p*`. This is the quantitative form of v5 retraction row 14 ("errors add").

### 4.5 Two identifications that give free imports *(proved; imported)*

- **Price / Robertson.** A Prop. 14(ii), `T'(0) = −Cov_q(F̂, F)`, is Robertson's secondary theorem of
  natural selection / the selection term of the Price equation. The Gaussian result B4 is **Lande's
  correlated response to selection**. Quantitative genetics has studied "selecting on a proxy trait and
  watching the target trait respond" for a century (Falconer & Mackay; Lande & Arnold). **This is the
  largest missing import in B.** It is also the natural route to multi-level alignment, via the multilevel
  Price decomposition — census §11, intragenomic conflict.
- **Reference misspecification.** A wrong reference is gauge-equivalent to an evaluator error (Prop.
  12(ii)). It is behaviourally indistinguishable, but mechanistically distinct: side effects and impact
  measures (census A12, A13) are errors in `q`, not in `F̂`.

### 4.6 Assumptions that are unnecessary or too restrictive

| Assumption | Verdict | Replace with |
|---|---|---|
| finite `X` | unnecessary for most results; Prop. 11 needs infinite `X` anyway | measurable space plus exponential integrability, stated per result |
| `q` has full support | a normalization | define `X := supp q` (the behaviours the actor can reach) |
| entropic (KL/Gibbs) actor | too restrictive | regularized optimizer with convex `φ` (§4.1), or ε-maximizer over nested convex capacity sets; Gibbs as the entropic case |
| linear target `E_p[F]` | **too restrictive** — cannot express diversity, risk limits, fairness, "no mode collapse" (census E7), or non-Markovian goals (Abel et al.) | concave functionals `U: Δ(X) → ℝ`; W1's argument extends with `φ/β − U` in place of `φ/β` |
| a single target | too restrictive — Arrow, judge disagreement, multiple selves | a gauge-closed **set** of targets `𝒯`, with worst-case regret over it (Bewley-style incomplete preferences). Condition (E) becomes "`𝒯` non-empty"; disagreement is `\|𝒯\| > 1` |
| a principal who "intends" | unnecessary, and wrong for biology | a designated **target** functional, normative or teleonomic |
| same reference for intended and actual actor | implicit | an explicit locus (reference misspecification) |
| same price in the counterfactual | implicit | an explicit parameter (§4.3) |
| static | too restrictive | a dynamic layer (§6) |

---

## 5. Audit against the goal, part 3: generality and what is missing

### 5.1 Coverage by substrate

| Substrate | Maps cleanly today | Missing for a real treatment |
|---|---|---|
| ML training | KL-regularized RL, reward-model error, regressional/extremal/catastrophic Goodhart, overoptimization slopes | trajectories and occupancy measures; learning dynamics; inner/outer as a chain (§4.4); evaluation vs deployment contexts; multi-agent |
| Individual humans | logit or rational-inattention actor (`q` = habits/defaults); hedonic proxy vs reflective target | time inconsistency (Laibson), planner–doer or dual-self models (Thaler–Shefrin, Fudenberg–Levine) as a within-person chain; beliefs vs values (Armstrong–Mindermann) |
| Institutions | multitask (first order), Campbell/Goodhart, performance measures | a unit channel and reference (Prop. 12); hidden information and adverse selection (needs an observation layer and types); equilibrium; aggregation |
| Biology | stationary selection–drift law (free fitness), correlated response, mismatch as a counterfactual | frequency dependence; multi-level selection (Price); transients; intragenomic conflict (a chain with shared substrate) |

**Verdict: substrate-independent at the level of the calculus; not yet at the level of the ontology.**
Every substrate has the three ingredients — a target, an optimized proxy, and an optimizer with a
resource. Most substrate-specific alignment problems live in pieces v6 does not formalize: time, other
agents, observation, and nesting.

### 5.2 Missing ideas, ranked by value to the PI's goal

1. **An observation channel, and the regret–detection identity.** *(Proposal; the core statement is
   imported and standard.)*
   - Diagnostics are about what an overseer can learn from behaviour. With `n` i.i.d. behavioural
     samples, the optimal Bayes error for telling `p̂` from `p*` decays with exponent equal to the Chernoff
     information, which is at most `min(KL(p̂‖p*), KL(p*‖p̂))`.
   - Since `KL(p̂‖p*) = β·R_J` (Thm 1), **detecting a misalignment of `β·R_J` nats needs on the order of
     `log(1/ε)/(β·R_J)` samples at least**, asymptotically.
   - In the entropic model, harm and detectability are one number. Low-harm misalignment is exactly
     hard-to-detect misalignment. This is a testable, diagnostic statement, and it is missing.
2. **Contexts and deception.** Put a context `c` into the behaviour space, with separate evaluation and
   deployment distributions over `c`.
   - The per-context identity (B7(d)) gives `β·R_J = E_{c∼deploy} KL(p̂_c ‖ p*_c)`, while detection only
     sees `c ∼ eval`.
   - **Deceptive alignment, sandbagging and evaluation awareness** (census B3, D6, D7) become one formal
     quantity: the gap between the deployment-weighted and evaluation-weighted per-context divergences.
   - That is a definition, a diagnostic, and a place to import hypothesis-testing results.
3. **A data layer.** The evaluator is usually learned from finite data under a distribution `D ≠ q`.
   Fluri, Huang and concentrability live here. With `D` as a primitive, Prop. 10 becomes a statement
   about `D` versus the capacity reference.
4. **Dynamics.** The correction loop (C §5.1, restated as bandwidth), capability growth as resource
   growth `r(t)`, and preference change (census G4 — target drift).
5. **Chains.** Delegation hierarchies are the rule in every substrate: gene → organism → behaviour;
   board → CEO → staff; developer → reward model → policy → sub-agents. §4.4 gives the composition law
   for entropic links.
6. **Multi-agent structure.** Equilibrium, signalling and adversarial Goodhart (C §4).
7. **Uncertainty over the target** (Hadfield-Menell et al., CIRL). The actor holds a belief over `𝒯`. For
   linear targets expected-value actors collapse to a point estimate, so value-of-information behaviour
   needs the dynamic layer.
8. **Corrigibility and targets defined over the frame itself**, e.g. "stay correctable". These are
   targets whose argument includes the correction loop, so they need (7) and the frame graph.
9. **Distributionally robust optimization** (Ben-Tal et al.; Namkoong & Duchi). The width is a
   φ-divergence DRO objective. The whole DRO literature imports into the capacity layer.

---

## 6. Recommended architecture for a standard *(proposal)*

**Do not invent the ontology.** Multi-agent influence diagrams (Koller & Milch 2003) and causal influence
diagrams (Everitt et al. 2021; Hammond et al. 2023) are mature, substrate-free, multi-agent, and already
host reward tampering, corrigibility and incentive analysis as graph properties. Use them as layer 0, and
attach the v6 calculus as the quantitative layer.

**Layer 0 — typed ontology.** An *alignment instance* is a causal (influence) diagram with designated
nodes:

| Node | Role |
|---|---|
| behaviour `X` | the actor's decision or output |
| target `𝒯` | a gauge-closed set of functionals on `Δ(X)`; no principal required |
| evaluator `Û` | what the actor actually improves |
| reference `q` | behaviour absent optimization |
| resource `r` | a budget or price on a convex capacity functional `φ` |
| context `c` | with evaluation and deployment distributions |
| observations `O` | what an overseer sees |
| correction | the update of `Û` from `O`, with delay `τ` |

The frame conditions become graph conditions:

- **(E)** `𝒯 ≠ ∅` after aggregation.
- **(X)** No directed path from the actor's decision node to `{𝒯, Û, q, r}` within the evaluation
  window.

Tampering, power-seeking and preference change are violations of (X), read off the graph.

**Layer 1 — static calculus (v6, generalized):**
- the Bregman identity (§4.1);
- the width / DRO duality and conjugate pairings (A §§4–6);
- the one-curve regret with a declared counterfactual (§4.3);
- the Pythagorean decomposition, entropic case (Thm 13, ray `t ≥ 0`);
- the gauge group and reporting rule (§3.2).

**Layer 2 — statistical:** data distribution `D`, evaluator estimation, detection (§5.2 items 1–3).

**Layer 3 — dynamic:** control-theoretic correction (C §5.1); resource growth; target drift.

**Layer 4 — strategic:** MAID equilibria; signalling with type-dependent references; mechanism design.

**Diagnostic loci**, derived from the node list. A failure is located at the first node whose assumed
property fails:

| Locus | What fails | Census examples |
|---|---|---|
| L1 target | aggregation or disagreement | I16–I18, E10 |
| L2 evaluator | specification, reward-model error, reference | A1–A8, E1–E6 |
| L3 optimizer | capability failure `g`, or an internal objective (inner alignment as a second evaluator link) | B1–B2, B8 |
| L4 resource | capacity versus error tails — the Goodhart regime | E1, M1 |
| L5 observation / context | evaluation vs deployment, low detection exponent | B3, D6, D7, F11 |
| L6 dynamics | delay, bandwidth, drift | C8, G4 |
| L7 frame | an (X) violation | A3–A5, D1–D3, B7 |

This is the routing table v5 wanted, now derived from the ontology instead of listed.

---

## 7. What I recommend doing next, in order, with gates

1. **Bibliographic and prior-art edits** (§2), including the author list and the BoN hedge. No gate;
   hygiene.
2. **Restate A over general regularizers and target sets.** Keep every v6 theorem as the entropic, linear,
   singleton case. *Gate:* no v6 result lost; `verify.py` still passes.
3. **Run the census modelling pass against loci L1–L7 plus "outside".** Use the pre-registered §14
   predictions (at least 8 of 12 hard cases need an extension or are outside). *Gate:* if all 221 items
   route comfortably, suspect the routing (your own rule); if more than 20 % are "outside" for reasons
   that are not (E), (X) or interpretability, the ontology is missing a node.
4. **T2 of the roadmap (actor robustness), unchanged.** It is still the weakest joint for Layer 1.
5. **Decide the Layer-0 formalism** (CID/MAID or an alternative). Test it on the twelve pre-registered hard
   cases before anything else.
6. **Only then** the dynamic and strategic layers.

## 8. Where I am unsure

- **Architecture fit.** §6 is a proposal from someone who has read the CID literature but not tested this
  combination. The quantitative layer attaches to utility nodes cleanly in the static case. Whether
  frame-endogeneity, contexts and the correction loop sit naturally in one diagram is untested.
- **The one-curve view (§4.3) and the regret–detection link (§5.2).** Both are elementary. I did not find
  them stated in this form, but the search was short, and they are likely known in the RLHF-theory or
  hypothesis-testing literature.
- **Bode's integral for the delayed loop** (C §5.1). Still not re-derived; Freudenberg & Looze is the
  place to check.
- **Biology constants** (the substitution-model factors in `ν ∝ N_e`). Carried, not re-verified.

The disposition file says a clean bill of health is evidence about the reviewer. This is not one: the
calculus is sound, and the framework it is meant to anchor has not been built yet.
