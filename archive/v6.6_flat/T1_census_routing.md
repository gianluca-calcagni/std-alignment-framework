# T1 — Census routing: is the core general enough?

> Pre-registration: `T1_preregistration.md`, written before routing. Data and scripts: `t1/routing_data.py`
> (the 221 routings), `t1/analyse.py` (all counts below), `t1/analyse_output.txt`.
>
> The routing was done by the executor who extended the framework in this round; the bias that implies is
> discussed in §6.

## 1. Answer to the PI's question

**Partly.** The pre-registered rule passes as written, but not robustly. And most of what the core cannot
discuss is missing layers, not justified exceptions. The result says exactly which layers.

- **The decision rule passes as written:** F + P = 69.7 % ≥ 60 %, every N item is justified by a named
  layer or outside condition, and 0 % are unroutable.
- **It does not pass robustly.** Under a pessimistic reading of 44 "projection" judgements, F + P falls to
  49.8 %.
- **Fully expressible items are 35.3 %.**

**The exceptions are mostly not the "justified" kind the PI anticipated.** Of the 67 items the core cannot
discuss at all (N):
- only **19** are exceptions in that sense: 9 have no single target (aggregation, disagreeing principals,
  value change), and 10 are category differences (mechanism-level interpretability);
- **the other 48 need a missing layer:** 23 strategic, 16 frame-endogeneity, 5 dynamic, 4 statistical.

Counting every item that needs something beyond the static core — the build-order signal of
`MSG_2_steering.md` §1 — gives:

| strategic | dynamic | frame (outside-X) | statistical | outside-E | category |
|---|---|---|---|---|---|
| 51 | 27 | 22 | 16 | 13 | 13 |

**What this means for the architecture.** A layer that handles strategic interaction *and* frame
endogeneity together — the causal / multi-agent influence-diagram proposal, `C_boundary.md` §5.4 — would
address **73 items (33 %)** in one move. A dynamic layer comes second (27). The statistical layer is least
urgent (16).

> **Final, frozen (v6.4; §10 and `T1_RULES_FROZEN.md`).** A third rater adjudicated the 101 disputed items.
> The result is reported as three nested shares:
> - **named** 78 %;
> - **specific** 55–61 %;
> - **full** 29 %.
>
> The routing below (§§1–8) is the first rater's, kept as registered. **On the disputed items it was the
> outlier:** the third rater's blind codes gave κ 0.04 with it, against 0.48 with the second rater.

> **Update after the independent re-routing (R5, §9).** A second rater routed all 221 items blind to this
> routing. Agreement on expressibility is moderate (κ = 0.54–0.57), on layer substantial (κ = 0.70), and on
> locus substantial (κ = 0.76).
> - **Items both raters call fully expressible: 55 (24.9 %).**
> - At least a snapshot: 52.9 % (second rater, strict) to 70.1 % (lenient).
> - The 60 % threshold of the pre-registered rule is met only under lenient readings.
> - The build-order signal is robust: strategic interaction (51 vs 49 items) and frame endogeneity (22 vs 23)
>   lead in both routings.

## 2. Totals

| Expressibility | Count |
|---|---|
| F — fully expressible in the core | 78 (35.3 %) |
| P — snapshot in the core, mechanism needs a layer | 76 (34.4 %) |
| N — not expressible | 67 (30.3 %) |

| Minimal layer | Count | Pre-registered guess |
|---|---|---|
| static | 79 (35.7 %) | 40 % |
| statistical | 16 (7.2 %) | 10 % |
| dynamic | 27 (12.2 %) | 20 % |
| strategic | 51 (23.1 %) | 17 % |
| outside-E / outside-X / category | 13 / 22 / 13 = 48 (21.7 %) | 10 % |
| undetermined | 0 (0.0 %) | 3 % |

| Locus | Count |
|---|---|
| L1 target | 23 (10.4 %) |
| L2 evaluator | 71 (32.1 %) |
| L3 optimizer | 6 (2.7 %) |
| L4 resource | 10 (4.5 %) |
| L5 observation/context | 47 (21.3 %) |
| L6 dynamics | 22 (10.0 %) |
| L7 frame | 42 (19.0 %) |

**Against the pre-registered predictions:**

- **Layer distribution: partly wrong.**
  - static: 36 % vs 40 %;
  - dynamic: 12 % vs 20 % — lower;
  - strategic: 23 % vs 17 % — higher;
  - outside (E + X + category): 22 % vs 10 % — **more than double**.

  The error is informative. Frame endogeneity (tampering, corrigibility, oversight subversion,
  self-modification) is far more common in the census than I expected.
- **F + P ≥ 60 %: met** (69.7 %), but not robust (§5).
- **Unroutable ≤ 5 %: met** (0).
- **§14 hard cases: 11 of 12 fire** (prediction ≥ 8; §4).
- **Gates.** Not every item routes comfortably, so the "suspect the routing" gate does not fire. No items are
  outside for reasons other than (E), (X) or category, so the "missing node" gate does not fire either. But
  see §6: the strategic and frame layers are missing *layers*, not missing *nodes*.

## 3. By section

| Section | n | F | P | N | static | statistical | dynamic | strategic | outside-E | outside-X | category |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A AI — specification | 20 | 14 | 6 | 0 | 14 | 1 | 1 | 0 | 1 | 3 | 0 |
| B AI — inner alignment | 12 | 4 | 4 | 4 | 4 | 3 | 0 | 2 | 0 | 3 | 0 |
| C AI — generalization | 11 | 5 | 2 | 4 | 5 | 2 | 0 | 0 | 2 | 1 | 1 |
| D AI — strategic | 18 | 3 | 5 | 10 | 3 | 1 | 3 | 5 | 0 | 4 | 2 |
| E AI — training | 17 | 14 | 2 | 1 | 14 | 1 | 1 | 0 | 1 | 0 | 0 |
| F AI — oversight | 12 | 4 | 5 | 3 | 4 | 1 | 0 | 4 | 0 | 0 | 3 |
| G AI — multi-agent/systemic | 10 | 1 | 1 | 8 | 1 | 1 | 2 | 4 | 1 | 1 | 0 |
| H humans — individual | 25 | 4 | 13 | 8 | 4 | 1 | 9 | 2 | 3 | 3 | 3 |
| I humans — institutional | 30 | 11 | 8 | 11 | 11 | 0 | 3 | 10 | 3 | 3 | 0 |
| J biology — organism | 20 | 7 | 7 | 6 | 7 | 0 | 1 | 11 | 0 | 1 | 0 |
| K biology — genome | 15 | 1 | 11 | 3 | 1 | 0 | 4 | 10 | 0 | 0 | 0 |
| L formal results | 15 | 3 | 5 | 7 | 4 | 0 | 2 | 2 | 2 | 3 | 2 |
| M empirical regularities | 16 | 7 | 7 | 2 | 7 | 5 | 1 | 1 | 0 | 0 | 2 |

**Where the core is strong:**
- AI specification (14 of 20 fully expressible);
- training pipelines (14 of 17);
- empirical regularities (7 of 16 fully, 14 of 16 at least as a snapshot);
- institutional Goodhart-type items;
- organism-level biological proxies.

**Where it is weak:**
- multi-agent / systemic AI (8 of 10 not expressible);
- AI strategic behaviour (10 of 18);
- within-genome conflict (11 of 15 only as a snapshot);
- individual humans (13 of 25 only as a snapshot, mostly because of time).

## 4. The §14 hard cases

| Group | Outcome | Items needing a layer or outside |
|---|---|---|
| I16–I18, G10 | fires | 4/4 |
| G1–G3 | fires | 3/3 |
| K1–K15 | fires | 14/15 |
| J19 | handled | 0/1 |
| H15–H17 | fires | 3/3 |
| B7 | fires | 1/1 |
| G8 | fires | 1/1 |
| D16, M15 | fires | 2/2 |
| E10 | fires | 1/1 |
| C8, G4 | fires | 2/2 |
| J14, J16 | fires | 1/2 |
| H23 | fires | 1/1 |

**11 of 12 fire: the prediction (≥ 8) is confirmed.**

- **J19 (senescence) is the one handled.** With fitness as the target, the core gives zero regret. The
  hard case's point — "nothing is misaligned" — becomes a statement the core makes, and a misalignment
  appears only once a different target (e.g. longevity) is designated.
- **J14 is handled; J16 is not.** Domestication syndrome is correlated response to selection
  (`B_dictionary.md` §11). Resistance evolving against a designed objective is adversarial, so it is
  strategic.

## 5. Robustness

**Sensitivity.** 44 of the 76 P judgements are "generous" projections: cases where the snapshot the core
offers — for instance, an extreme evaluator error on a tamper action — may be judged too thin to count as
discussing the item. They are:
- all P items whose layer is outside-X or outside-E;
- all biological conflict items;
- the strategic oversight and contract items.

Reclassifying all 44 as N gives **F + P = 110 (49.8 %)**, below the 60 % threshold.

**The honest reading.** The core fully expresses about a third of the census. It offers a meaningful
snapshot of between one sixth and one third more, depending on how generously a snapshot is judged. It
cannot express the last third.

**Items where `X` = trajectories does the work.** A9, A10, A18, I22, L1 and L11 are F or P because the
behaviour space may be a set of trajectories. That is legitimate — the core allows it — but it is also where
"static" is doing the most work for the least content. A dynamic layer would make these statements
sharper, not merely possible.

## 6. Limits of this routing

- **Rater bias.** The router extended the framework in the same round (Prop. 20, B7(e), B12) and has an
  interest in a favourable result. **An independent re-routing is needed** before this result is quoted:
  at least a random 40 items, by someone else, with agreement statistics (`ROADMAP.md` T1b).
- **Census gaps** (listed in `E_census.md` §15):
  - military command and control;
  - legal interpretation;
  - medicine;
  - safety engineering (drift to danger, normalization of deviance);
  - developmental psychology;
  - non-Western institutions.

  The first and fourth would likely add dynamic and hierarchical (chain) items, where the core is weak.
- **"Strategic" and "outside-X" are missing layers, not justified exceptions.** The PI's exception class —
  disagreeing principals — corresponds to outside-E (13 items, 5.9 %). Tampering, corrigibility, collusion
  and games are central alignment topics. The core's silence on them is a gap to fill, not a boundary to
  accept.

## 7. Post-hoc note — not part of the registered result

After routing, `B_dictionary.md` §13 added one strategic piece within the current carrier. Potential games
under log-linear learning are a tilt of the joint behaviour space (Blume 1993).

**The registered routing above was not changed.** Items this plausibly affects, for an independent rater to
judge:

| Item | Why it may move |
|---|---|
| I14 (commons) | Cournot commons is a potential game: P or F |
| I15 (free riding) | public goods is a potential game; free riding is anti-alignment, `X_anti > 0`: P or F |
| G6 (race dynamics) | if modelled as a symmetric 2×2 game, it is a potential game: P |
| J12, G3 | uncertain — contests and repeated pricing are generally not exact potential games |

If all of I14, I15 and G6 moved, strategic N would fall from 23 to 20, and F + P would rise from 69.7 % to
71.0 %. The strategic layer remains the largest gap.

## 8. The 221 routings

F = fully expressible; P = snapshot; N = not expressible. Layer = minimal layer for full expression.

| # | Name | Locus | Expr. | Layer | Carrier / justification |
|---|---|---|---|---|---|
| A1 | Specification gaming | L2 | F | static | evaluator error E; Thm 1, Thm 5, Prop 20 |
| A2 | Reward hacking | L2 | F | static | evaluator error incl. measurement; width Thm 5; Prop 11 for rare large errors |
| A3 | Reward tampering | L7 | P | outside-X | snapshot: extreme E on a tamper action (Prop 4/11); mechanism: actor acts on the evaluator |
| A4 | Wireheading | L7 | P | outside-X | as A3: actor sets its own reward |
| A5 | Delusion box | L7 | P | outside-X | actor manipulates its own observations; snapshot as evaluator error |
| A6 | Proxy misspecification | L2 | F | static | E = proxy − target |
| A7 | Reward hackability (formal) | L2 | F | static | hackability as nonzero width / D_⊥ ≠ 0 (Thm 5, Cor 13.1, Prop 20) |
| A8 | Correlated proxies | L2 | F | static | B §5: sign of Cov_q(F̂,F); Laidlaw's definition derived |
| A9 | Reward shaping pathologies | L2 | F | static | X = trajectories: potential shaping telescopes to a constant E (Cor 1.1: zero regret); other shaping = non-constant E |
| A10 | Non-Markovian goals | L1 | F | static | X = trajectories, so non-Markov targets are admissible; the Markov-restricted evaluator leaves an irreducible E |
| A11 | Reward hypothesis limits | L1 | P | outside-E | targets violating the vNM/scalar conditions have no single functional F; concave functionals covered by Prop 15 |
| A12 | Side effects | L2 | F | static | omitted features in E, and the reference as a locus (Remark 16.1) |
| A13 | Negative side-effect avoidance failure | L4 | F | static | impact measure = capacity around a baseline; vacuous vs paralysing = width vs g(δ) (Thm 5, Cor 5.2) |
| A14 | Reward clipping distortion | L2 | F | static | clipping = non-affine map of the target; E concentrated on severe outcomes; transverse (Thm 13) |
| A15 | Unsafe exploration | L6 | P | dynamic | snapshot: exploratory behaviour puts mass on catastrophic region; learning-by-trial is dynamic |
| A16 | Environment / simulator exploitation | L2 | F | static | rare-region extreme E (Prop 4, Prop 11, Thm 9 extremal regime) |
| A17 | Semantic reward collapse | L5 | P | statistical | scalar evaluator compresses a vector of causes; diagnosis from data needs the statistical layer (Prop 16: only the tilt is identified) |
| A18 | Multi-step reward hacking | L5 | F | static | X = trajectories; step-level monitoring observes a coarsening, detection ≤ KL of the coarsened law (Prop 18 + data processing) |
| A19 | Answer-key / benchmark access | L2 | F | static | evaluator scores the answer-key behaviour high: rare-region E (Prop 4) |
| A20 | Objective underspecification in agentic settings | L2 | F | static | E on unenumerated regions; extremal regime at large capacity (Thm 9) |
| B1 | Mesa-optimization | L3 | P | statistical | two-link chain (Cor 1.5); formation of the internal objective by training is the statistical layer |
| B2 | Inner misalignment | L3 | F | static | inner error as second link; errors add in the exponent (Cor 1.5) |
| B3 | Deceptive alignment | L5 | P | strategic | evaluation gap Γ (Prop 19) is the quantity; 'to preserve an objective' is anticipation of training — strategic |
| B4 | Alignment faking | L5 | P | strategic | as B3 |
| B5 | In-context scheming | L7 | P | outside-X | undermining oversight acts on the observation/correction loop |
| B6 | Goal-guarding | L7 | N | outside-X | resisting modification acts on the correction loop; no core object for modification of the actor's objective |
| B7 | Gradient hacking | L7 | N | outside-X | actor acts on its own training signal (hard case) |
| B8 | Proxy goal internalisation | L2 | F | static | actor optimizes the proxy as its evaluator: E = proxy − target (target uncertainty not needed to state the failure) |
| B9 | Objective robustness failure | L5 | F | static | contexts (Def 9): per-context E_c large off-distribution while g stays small; T = g + ΔF separates capability from alignment |
| B10 | Emergent misalignment | L6 | N | statistical | the entropic actor predicts local effects of a local E; broad misalignment is a generalization property of the learner |
| B11 | Reward-hack generalisation | L6 | N | statistical | as B10 |
| B12 | Agentic/chat divergence | L5 | F | static | context-dependent training: evaluation gap across chat/agentic contexts (Prop 19) |
| C1 | Goal misgeneralization | L5 | F | static | as B9: competent (low g) pursuit of the wrong goal off-distribution |
| C2 | CoinRun | L5 | F | static | instance of C1 |
| C3 | Spurious correlation / shortcut learning | L2 | P | statistical | learned evaluator uses a correlated feature: small L1 error under D, large exposure (Prop 10(d), Prop 11); learning mechanism statistical |
| C4 | Underspecification | L2 | P | statistical | each model is an evaluator; Rashomon set of evaluators needs the statistical layer |
| C5 | Ontological crisis | L1 | N | outside-E | target loses its referent when X is re-represented: no F on the new X |
| C6 | Diamond maximizer | L1 | N | outside-E | as C5 |
| C7 | Distributional shift | L5 | F | static | contexts with ρ_dep ≠ ρ_ev (Def 9, Prop 19) |
| C8 | Auto-induced distributional shift | L7 | N | outside-X | the actor's behaviour changes the distribution and the target (hard case) |
| C9 | Capability/alignment generalisation gap | L5 | F | static | as B9 |
| C10 | Inverse scaling | L4 | F | static | capacity is not monotonically good (Prop 14); regime switch (Thm 9) |
| C11 | Ontology identification | L5 | N | category | locating concepts inside representations: interpretability |
| D1 | Instrumental convergence | L7 | P | dynamic | Turner's POWER needs states (B §9); acquiring power changes the reach (outside-X at the limit) |
| D2 | Power-seeking | L7 | P | dynamic | as D1 |
| D3 | Shutdown resistance / incorrigibility | L7 | N | outside-X | acts on the correction loop |
| D4 | Off-switch problem | L7 | N | strategic | assistance game with uncertainty over the target |
| D5 | Safe interruptibility | L6 | N | dynamic | learning under interruptions |
| D6 | Sandbagging | L5 | P | strategic | eval-context behaviour differs (Γ); deliberate underperformance anticipates consequences |
| D7 | Evaluation awareness | L5 | F | static | actor conditions on context (Def 9): the prerequisite for Γ > 0 |
| D8 | Situational awareness | L7 | N | strategic | enabling capability for strategic response to training; not itself a behavioural divergence |
| D9 | Test-awareness / Hawthorne effect in models | L5 | F | static | behaviour changes when measured: context-dependent behaviour, Γ (Prop 19) |
| D10 | Performative scheming | L5 | F | static | two evaluators (scheming vs sycophancy) produce the same behaviour: non-identification (Prop 12, Prop 16) |
| D11 | Self-exfiltration | L7 | N | outside-X | acts on its own containment |
| D12 | Oversight subversion | L7 | N | outside-X | acts on monitoring |
| D13 | Sabotage of safety work | L7 | N | outside-X | acts on the correction process |
| D14 | Collusion with malicious actors | L7 | N | strategic | coordination with other agents |
| D15 | Probe evasion | L5 | N | strategic | adaptive evasion of detectors: a game with the monitor |
| D16 | Self-fulfilling misalignment | L2 | P | statistical | snapshot: training discourse shifts the reference q (Remark 16.1); mechanism is learning from data (hard case) |
| D17 | Steganographic / hidden reasoning | L5 | P | category | observation is a coarsening (detection bound applies); the content of hidden reasoning is mechanism-level |
| D18 | Unfaithful chain of thought | L5 | N | category | faithfulness of stated reasoning is mechanism-level |
| E1 | Reward model overoptimization | L4 | F | static | B §4 slope; Thm 9 regimes; Props 10–11; Prop 20 |
| E2 | Sycophancy | L2 | F | static | evaluator rewards agreement; E correlated with an agreement feature (B §6) |
| E3 | Length / verbosity bias | L2 | F | static | B §6 length counterexample, exact |
| E4 | Formatting and style bias | L2 | F | static | as E3 |
| E5 | Annotator bias and disagreement | L2 | F | static | labeller-dependent evaluator error; the disagreement component is E10 |
| E6 | Preference-data confounding | L2 | P | statistical | confounded comparison data: the learned evaluator picks the confounder (causal Goodhart) |
| E7 | Mode collapse / diversity loss | L1 | F | static | diversity is a concave, non-linear target (Prop 15, tier 3); concentration with capacity (Prop 14) |
| E8 | Policy drift from the reference | L4 | F | static | KL from the reference is the capacity (Thm 5, Cor 5.2, Prop 7) |
| E9 | Evaluator gaming | L2 | F | static | as A2 |
| E10 | Judge disagreement | L1 | N | outside-E | two evaluators, no single target (hard case; justified exception) |
| E11 | Proxy under-alignment | L3 | P | dynamic | proxy and judge fall together: the optimizer fails its own evaluator (tiers 1–2 still hold); training collapse is dynamic |
| E12 | Localized reward hacking | L5 | F | static | per-context KL vs its average (Def 9): averages mask context-level regret |
| E13 | RLAIF constitution gaps | L2 | F | static | evaluator undefined/erroneous on unenumerated cases (as A20) |
| E14 | Reward model staleness | L4 | F | static | evaluator error measured under D; exposure grows with capacity (Prop 10(d), Thm 5) |
| E15 | Distillation of hacks | L2 | F | static | teacher behaviour becomes the student's reference/evaluator: stacked stages (Cor 1.5), reference error (Remark 16.1) |
| E16 | Safety-tax / capability trade | L4 | F | static | safety tax = increase of g under tighter capacity (Cor 5.2); pressure to undo it is dynamic/strategic |
| E17 | Inoculation-prompt dependence | L5 | F | static | mitigation effective only in one context: context-dependent behaviour (Def 9) |
| F1 | Scalable oversight | L5 | P | strategic | snapshot: evaluator error where the overseer is weak, detection bound (Prop 18); oversight protocols are games |
| F2 | Eliciting latent knowledge (ELK) | L5 | N | category | eliciting internal knowledge: mechanism-level |
| F3 | Hidden objectives | L5 | F | static | objectives not revealed by behaviour: non-identification (Prop 12, 16); unsampled contexts (Prop 19) |
| F4 | Confabulation | L5 | N | category | explanations vs causes: mechanism-level |
| F5 | Interpretability illusions | L5 | N | category | interpretability |
| F6 | Evaluation gaming / benchmark contamination | L2 | F | static | benchmark score as evaluator; Prop 20 covariance; conjugacy (Prop 10) |
| F7 | Weak-to-strong generalization | L2 | P | statistical | weak labels = evaluator with error; strong generalization beyond it is a learning phenomenon |
| F8 | Debate failure modes | L2 | P | strategic | persuasiveness − correctness as E; the debate protocol is a game |
| F9 | Recursive reward modelling limits | L2 | F | static | errors compound through stacked stages (Cor 1.5) |
| F10 | Monitoring evasion | L5 | P | strategic | against a fixed monitor: E on the monitor score (Prop 20); adaptation to a changing monitor is a game |
| F11 | Eval-realism gap | L5 | F | static | realism shifts ρ_ev toward ρ_dep; Γ (Prop 19) |
| F12 | Auditing under adversarial models | L5 | P | strategic | detection bound (Prop 18) explains low power at small KL; deliberate sandbagging is strategic |
| G1 | Multi-agent collusion | L7 | N | strategic | equilibrium among agents (hard case) |
| G2 | Emergent communication / hidden channels | L7 | N | strategic | as G1, with an unobservable channel |
| G3 | Algorithmic collusion | L7 | N | strategic | as G1 |
| G4 | Auto-induced preference change | L7 | N | outside-X | the actor changes the preferences it optimizes (hard case) |
| G5 | Engagement optimization externalities | L2 | F | static | engagement as evaluator, welfare as target; Prop 20 (aggregate welfare needs a single target, else outside-E) |
| G6 | Race dynamics | L7 | N | strategic | competition among developers |
| G7 | Value lock-in | L6 | N | dynamic | irreversibility and path dependence |
| G8 | Gradual disempowerment | L6 | N | dynamic | no single misaligned actor; erosion of the correction loop over time (hard case) |
| G9 | Correlated model failure | L2 | P | statistical | many actors share correlated evaluator errors; the core has one actor |
| G10 | Principal–AI–principal conflict | L1 | N | outside-E | multiple users with incompatible targets (hard case; justified exception) |
| H1 | Akrasia | L2 | F | static | operative valuation as evaluator, reflective judgement as target (B §12(a)) |
| H2 | Present bias / hyperbolic discounting | L6 | P | dynamic | naive: a sequence of present-biased evaluators (dynamic); sophisticated: intrapersonal game (B §12(c)) |
| H3 | Time inconsistency | L6 | P | dynamic | as H2 |
| H4 | Addiction | L2 | P | dynamic | snapshot: extreme E on the stimulus region (Prop 4); tolerance and dependence are dynamic |
| H5 | Substance-induced reward | L7 | P | outside-X | acting directly on the evaluation mechanism (wireheading) |
| H6 | Hedonic adaptation | L6 | P | dynamic | the evaluator resets with consumption history |
| H7 | Affective forecasting error | L2 | F | static | evaluator = forecast value, target = experienced value |
| H8 | Introspection failure | L5 | N | category | self-report vs process |
| H9 | Choice blindness | L5 | N | category | explanation of a choice, not the choice |
| H10 | Preference construction | L1 | P | outside-E | target constructed at elicitation: context-dependent F(c,·) (Def 9) but no context-free target |
| H11 | Preference reversal | L1 | P | outside-E | as H10 |
| H12 | Framing effects | L5 | F | static | frame-dependent evaluator/reference with frame-invariant target (Def 9) |
| H13 | Motivated reasoning | L2 | P | statistical | evaluator = value under distorted beliefs; belief formation is the statistical layer |
| H14 | Self-deception | L5 | N | category | self-knowledge of motives |
| H15 | Value drift over a life | L1 | N | outside-E | which self's values are the target (hard case) |
| H16 | Transformative experience | L7 | N | outside-X | choices change the target (hard case) |
| H17 | Adaptive preference formation | L7 | N | outside-X | target depends on the opportunity set (hard case) |
| H18 | Goal substitution | L2 | F | static | measurable proxy as evaluator |
| H19 | Perverse habit formation | L6 | P | dynamic | repetition shifts the reference/evaluator toward the means |
| H20 | Ego depletion / self-control failure | L4 | P | dynamic | state-dependent capacity; depletion dynamics |
| H21 | Learned helplessness | L6 | N | dynamic | learned beliefs about controllability; not an objective gap |
| H22 | Procrastination as internal principal–agent | L6 | P | dynamic | naive procrastination is dynamic; sophisticated is strategic (B §12(c)) |
| H23 | Internal conflict / multiple selves | L7 | N | strategic | several evaluators in one organism: intrapersonal game (hard case) |
| H24 | Moral licensing | L6 | P | dynamic | history-dependent evaluator (contexts indexed by past acts) |
| H25 | Compulsive engagement with designed stimuli | L2 | P | strategic | snapshot: extreme E on designed stimuli (Prop 4); the designer optimizes against the user |
| I1 | Principal–agent problem | L2 | F | static | agent's evaluator ≠ principal's target; contract design is strategic |
| I2 | Moral hazard | L2 | F | static | evaluator omits consequences borne by others; hidden-action contracting is strategic |
| I3 | Adverse selection | L5 | N | strategic | screening under hidden types |
| I4 | Goodhart's law | L2 | F | static | Prop 20; Thm 9; B §3 |
| I5 | Campbell's law | L6 | P | dynamic | the indicator's relation to the target erodes as agents act on it |
| I6 | Goodhart taxonomy | L2 | P | strategic | regressional/extremal derived (B §3); causal needs the statistical layer; adversarial needs strategic |
| I7 | Multitasking distortion | L2 | F | static | B §5 first order: Cov_q(F_m,F_u) < −Var_q F_m |
| I8 | Goal displacement | L6 | P | dynamic | evaluator drifts toward means over time |
| I9 | Regulatory capture | L7 | N | outside-X | the evaluated party reshapes the evaluator |
| I10 | Bureaucratic ritualism | L2 | F | static | procedure compliance as evaluator |
| I11 | Teaching to the test | L2 | F | static | test score as evaluator; conjugacy (Prop 10) |
| I12 | Metric fixation | L2 | F | static | metric as evaluator |
| I13 | Cobra effect | L2 | F | static | new behaviour with high F̂ and low F: extremal regime, anti-alignment X_anti (Thm 13(b)) |
| I14 | Tragedy of the commons | L7 | N | strategic | many agents, shared resource |
| I15 | Free riding | L7 | N | strategic | public-goods game |
| I16 | Arrow's impossibility | L1 | N | outside-E | aggregation impossibility (hard case; justified exception) |
| I17 | Condorcet cycles | L1 | N | outside-E | as I16 |
| I18 | Gibbard–Satterthwaite | L7 | N | outside-X | strategic reporting makes F endogenous (hard case) |
| I19 | Rent-seeking | L2 | P | strategic | captured vs created value as E; capture from others is a game |
| I20 | Shirking and monitoring cost | L5 | P | strategic | unobservable effort: detection bound (Prop 18); second-best contracts are strategic |
| I21 | Gresham dynamics in quality | L2 | P | strategic | market selection on price as evaluator; lemons asymmetry is strategic |
| I22 | Short-termism | L2 | F | static | X = trajectories: short-horizon evaluator vs long-horizon target |
| I23 | Groupthink | L7 | N | strategic | social epistemics among agents |
| I24 | Information cascades | L7 | N | strategic | sequential social learning |
| I25 | Institutional memory loss | L6 | P | dynamic | fixed evaluator, drifting target |
| I26 | Mission creep | L7 | N | outside-X | actor expands its own mandate |
| I27 | Perverse audit effects | L5 | F | static | audited behaviour depends on being audited: Γ (Prop 19) |
| I28 | Street-level discretion | L3 | F | static | two-link delegation chain (Cor 1.5, entropic caveat) |
| I29 | Sanctions and incentive crowding-out | L2 | P | strategic | the evaluator responds non-additively to the incentive; incentive design is strategic |
| I30 | Coordination failure under conflicting principals | L1 | N | outside-E | several principals, incompatible instructions (justified exception) |
| J1 | Supernormal stimuli | L2 | F | static | extreme E on an artificial cue region (Prop 4, Prop 11) |
| J2 | Evolutionary mismatch | L5 | F | static | evaluator tuned to the ancestral context (Def 9; A §10 biology) |
| J3 | Sweet-taste / caloric decoupling | L2 | F | static | sweetness as evaluator, nutrition as target |
| J4 | Contraception | L2 | F | static | mating reward as evaluator, fitness as target |
| J5 | Recreational drug use | L7 | P | outside-X | direct action on evaluation machinery |
| J6 | Brood parasitism | L2 | P | strategic | host's kin-recognition error exploited by a coevolving parasite |
| J7 | Aggressive mimicry | L2 | P | strategic | receiver's evaluator exploited by a signaller |
| J8 | Batesian mimicry | L2 | P | strategic | signalling equilibrium without differential cost (B §8) |
| J9 | Sensory exploitation | L2 | P | strategic | receiver bias exploited by coevolving signals |
| J10 | Sexual conflict | L1 | N | strategic | two parties' optima over one interaction |
| J11 | Parent–offspring conflict | L1 | N | strategic | as J10 |
| J12 | Sibling rivalry / siblicide | L7 | N | strategic | competition among offspring |
| J13 | Manipulative parasites | L7 | N | strategic | a third party manipulates the host's evaluator |
| J14 | Domestication syndrome | L2 | F | static | correlated response to selection (B §11, B4) (hard case) |
| J15 | Artificial selection side effects | L2 | F | static | selection on a metric: correlated response, Prop 20 (B §11) |
| J16 | Antibiotic and pesticide resistance | L7 | N | strategic | an adversarial population evolving against a designed objective (hard case) |
| J17 | Kin recognition error | L2 | P | strategic | relatedness proxy as evaluator (static); its exploitation by cheats is strategic |
| J18 | Altruism breakdown under anonymity | L5 | P | strategic | cue mismatch across contexts (Def 9); cooperation itself is a game |
| J19 | Senescence as objective mismatch | L1 | F | static | with fitness as the target, R_J = 0: no misalignment; a misalignment exists only against a designated different target (e.g. longevity), then E is late-life weighting (hard case) |
| J20 | Runaway sexual selection | L6 | N | dynamic | preference and trait coevolve; the evaluator depends on the population |
| K1 | Intragenomic conflict | L1 | P | strategic | multilevel Price decomposition (B §11, stated); levels are players (hard case) |
| K2 | Selfish genetic elements | L2 | P | strategic | element's evaluator = own transmission; frequency-dependent suppression (hard case) |
| K3 | Meiotic drive / segregation distortion | L2 | P | strategic | as K2 (hard case) |
| K4 | Transposable elements | L2 | P | dynamic | copy-number dynamics (hard case) |
| K5 | B chromosomes | L2 | P | dynamic | as K4 (hard case) |
| K6 | Genomic imprinting | L1 | N | strategic | parental conflict (hard case) |
| K7 | Cytoplasmic male sterility | L2 | P | strategic | maternally transmitted elements' evaluator (hard case) |
| K8 | Mitochondrial–nuclear conflict | L1 | P | strategic | two genomes, two optima (hard case) |
| K9 | *Wolbachia* and sex-ratio distortion | L7 | N | strategic | endosymbiont manipulates host (hard case) |
| K10 | Cancer as cellular defection | L2 | P | dynamic | somatic selection on proliferation vs organismal target: correlated response, non-stationary (hard case) |
| K11 | Somatic mosaicism and clonal expansion | L2 | P | dynamic | as K10 (hard case) |
| K12 | Immune autoimmunity | L2 | F | static | B §10: binary-KL structure of overrating self vs underrating pathogens (Prop 4) (hard case) |
| K13 | Germline–soma conflict | L1 | P | strategic | germline vs soma interests (hard case) |
| K14 | Green-beard effects | L2 | P | strategic | recognition marker as evaluator, exploited by cheats (hard case) |
| K15 | Dobzhansky–Muller incompatibilities from conflict | L6 | N | strategic | internal arms races (hard case) |
| L1 | No Markov reward for some goals | L1 | P | static | stated: X = trajectories admits non-Markov targets; the Markov-restricted evaluator's residual is an E |
| L2 | Reward hypothesis conditions | L1 | P | outside-E | characterizes when condition (E) holds for temporal preferences |
| L3 | Hackability characterisation | L2 | F | static | core analogue: zero regret iff E constant (Cor 1.1), D_⊥ = 0 iff affine (Cor 13.1); width over all capacity (Thm 5) |
| L4 | Power-seeking tendency | L7 | P | dynamic | stated (B §9) |
| L5 | Reward tampering as a causal diagram | L7 | N | outside-X | causal-diagram incentives: the proposed Layer-0, not the core |
| L6 | Path-specific objectives | L7 | N | outside-X | as L5 |
| L7 | Robust agents learn causal models | L3 | N | category | a result about the actor's internal world model |
| L8 | Arrow's impossibility | L1 | N | outside-E | justified exception |
| L9 | Gibbard–Satterthwaite | L7 | N | outside-X | strategic reporting |
| L10 | Goodhart taxonomy (formal) | L2 | P | strategic | 2 of 4 variants derived (B §3) |
| L11 | Time-consistency of geometric discounting | L6 | P | dynamic | discounted targets on trajectories are static; dynamic consistency is dynamic |
| L12 | Nonidentifiability of reward from behaviour | L5 | F | static | Prop 12 / Prop 16 (derived gauge) |
| L13 | Impossibility of reward inference without assumptions | L5 | F | static | Prop 12(ii): the entropic planner family is an instance — behaviour identifies only the tilt, not (β, q, F̂) |
| L14 | Rice's theorem / undecidability | L5 | N | category | computability |
| L15 | Off-switch game | L7 | N | strategic | off-switch game |
| M1 | Overoptimization follows a predictable curve in proxy-model size and KL distance | L4 | P | statistical | KL dependence: Thm 9, B §4 slope; proxy-model-size dependence is statistical |
| M2 | Reward-model errors grow with distance from the reference policy | L4 | F | static | error measured under q, exposure grows with capacity (Props 6, 10, 11) |
| M3 | The proxy/true divergence appears as a sharp transition in some settings | L4 | F | static | Prop 4: a rare overrated region is captured sharply near β·M ≈ log 1/p*(A) |
| M4 | Sycophancy traces to preference data rather than to any explicit objective | L2 | P | statistical | evaluator learned from preference data |
| M5 | Frontier models can distinguish evaluation from deployment | L5 | F | static | contexts known to the actor (Def 9) |
| M6 | Increased evaluation awareness reduces misaligned behaviour | L5 | F | static | eval-awareness lowers eval-context divergence: detection exponent falls, Γ rises (Prop 19) |
| M7 | More realistic evaluations reduce both misalignment and evaluation awareness | L5 | F | static | realism moves ρ_ev toward ρ_dep, reducing Γ |
| M8 | Anti-scheming training reduces measured scheming substantially but not to zero | L6 | P | dynamic | training effect over time; residual Γ (Prop 19) |
| M9 | Chat-based safety training leaves agentic misalignment intact | L5 | F | static | as B12 |
| M10 | Reward hacking in training generalises to deployment misbehaviour | L6 | N | statistical | as B11 |
| M11 | Narrow fine-tuning on insecure code induces broad misalignment | L6 | N | statistical | as B10: the entropic actor predicts local effects |
| M12 | Row-level analysis reveals hacking hidden by checkpoint averages | L5 | F | static | as E12 |
| M13 | Deception probes detect some sandbagging but produce false positives | L5 | P | category | detection trade-off (Prop 18); probes are mechanism-level |
| M14 | Interrogation-style mitigations can backfire by teaching better lying | L5 | P | strategic | training against a detector: adversarial Goodhart |
| M15 | Alignment-related discourse in pretraining can induce the behaviour it describes | L2 | P | statistical | as D16 (hard case) |
| M16 | Whether current scheming reflects coherent goal-pursuit is contested | L3 | P | category | behaviour does not identify objectives (Prop 12); coherence of internal goals is mechanism-level |
## 9. Independent re-routing (T1b, review R5)

The second rater (`reviews/R5_independent/`) routed all 221 items blind to this routing: the routing file was
frozen and hashed before this report was opened. The rater introduced one refinement, **`Pt`**: a snapshot
that reduces to a generic proxy error, without using specific core structure. The lenient reading counts
`Pt` as P; the strict reading counts it as N.

| Agreement | Raw | Cohen's κ |
|---|---|---|
| expressibility, lenient | 0.715 | 0.572 |
| expressibility, strict | 0.692 | 0.543 |
| minimal layer | 0.756 | 0.699 |
| locus | 0.805 | 0.756 |

**The T1b gate** (κ < 0.4 means the counts are not quoted) **passes**. Agreement is moderate on
expressibility and substantial on layer and locus.

| Quantity | This routing | Second rater, lenient | Second rater, strict | Both raters |
|---|---|---|---|---|
| F | 78 (35.3 %) | 60 (27.1 %) | 60 | **55 (24.9 %)** |
| F + P | 154 (69.7 %) | 155 (70.1 %) | 117 (52.9 %) | 136 (61.5 %) lenient; 114 (51.6 %) strict |
| strategic layer | 51 | 49 | | |
| frame (outside-X) | 22 | 23 | | |
| dynamic | 27 | 21 | | |
| statistical | 16 | 28 | | |
| outside-E / category | 13 / 13 | 13 / 20 | | |
| undetermined | 0 | 7 | | |

**What the comparison shows.**

- **My routing was generous in one systematic way.** 22 items I called F the second rater calls P, 12 of
  them with the statistical layer: goal misgeneralization (B9, C1, C2, C9), context-dependent training
  (B12, M9, E17), learned evaluators and proxy internalization (B8, E5, M2), and composition (E15, F9). These phenomena name a learning
  mechanism. The core expresses their snapshot, not what is learned. **I accept this reading.**
- **The second rater is more lenient on frame items.** Several of my N items are `Pt` there — tampering-like
  items (D3, D11–D13, B6) — and several strategic items (J11–J13, K9). The strict reading restores N.
- **My "generous 44" was mis-targeted.** Of those 44, the second rater keeps 21 as P or F. Meanwhile 15 of my
  other P items are N or `Pt` for them. The totals nevertheless agree: my pessimistic 49.8 % against their
  strict 52.9 %.
- **The §14 hard cases fire 11 of 12 in both routings, but not the same 11.** For the second rater
  senescence (J19) is outside-E — which target? — and J14 and J16 are both handled. J16 becomes anti-alignment
  of a population tilt with a designated target.
- **Four pushbacks change the framework, not only the counts.**
  - C8, auto-induced distributional shift, is inside on trajectory space (`C_boundary.md` §3).
  - Turner-style power-seeking needs a prior over intents, not frame endogeneity (`B_dictionary.md` §9).
  - F10 and M14, Goodhart on a fixed monitor, are static.
  - I5, Campbell's law, is Goodhart restated.

  The first two are recorded as `D_status.md` rows 63 and 64.

**The robust reading, stated once.**
- The core fully expresses about **a quarter to a third** of the census.
- It gives at least a snapshot of **half to two-thirds**.
- **Strategic interaction and frame endogeneity** are the largest gaps: about 72–73 items in either routing.
- Justified exceptions (no single target, mechanism-level) are about **20 items**.

## 10. Adjudication by a third rater (R6) — the frozen result

A third rater routed the 101 disputed items and 20 agreed controls blind. It hashed that routing, then ruled on
eight rule-level questions and adjudicated every item. Files: `reviews/R6_independent/adjudication/`; the
final codes are in `t1/adjudicated_routing.py`; the frozen rules are in `T1_RULES_FROZEN.md`.

| Share | Adjudicated | Third rater, blind |
|---|---|---|
| named (F + P + Pt) | 173 (78.3 %) | 172 (77.8 %) |
| **specific (F + P)** | **134 (60.6 %)** | **122 (55.2 %)** |
| full (F) | 65 (29.4 %) | 56 (25.3 %) |

**Layers needed** (adjudicated):
- strategic 51;
- statistical 31;
- outside-X 23;
- dynamic 20;
- outside-E 16;
- category 15;
- static 65.

**Why this is reported as nested shares.** The "specific" share sits on the pre-registered 60 % threshold, and
single defensible perturbations move it across. **The frozen format is three shares with a band. Pass/fail
is retired.**

**Anchoring check.**
- The third rater's blind codes on the disputed items agreed with the second rater (κ 0.48), and hardly at
  all with the first (κ 0.04).
- In adjudication it sided with the second rater on 55 items, the first on 23, and neither on 23.
- The T1c anchoring gate does not fire.
- It overrode 3 of 20 controls (K10, I15, G6). K10 suggests a generosity both earlier raters shared,
  treating Price/B11 as specific structure for biological conflicts.

