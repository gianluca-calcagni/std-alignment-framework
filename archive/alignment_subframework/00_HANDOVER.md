# 00 — Handover

**The alignment problem, formalized, extracted from a larger framework.**

This package is self-contained. It is a **subframework**: the alignment-relevant subset of a broader
programme on how personas — biological or artificial — represent, evaluate and act. The parent lives
at `../persona-state-framework/` and is not needed to work here.

---

## 1. What this is

> **Alignment is not one problem. It is five distinct failures, each with a formal condition, each
> with a measurable quantity, and two of them trading against each other by construction.**

| # | Gap | Fails when |
|---|---|---|
| 1 | **Specification** | the reward channel does not order trajectories as the principal's intent does |
| 2 | **Transmission** | the distinctions the intent depends on are not observable at all, or not carried by the persona's representation |
| 3 | **Grounding** | the objective is measurable with respect to what the persona can bring about by acting on itself |
| 4 | **Persistence** | refinement of the representation changes the reach where the goal is indifferent |
| 5 | **Verification** | the persona has no readout of its own maps, so it cannot report its evaluator |

Mapped to the standard vocabulary: **1 = outer alignment**, **3 = wireheading / reward tampering**,
**4 = goal misgeneralization / ontology identification**, **5 = ELK**. Inner alignment spans 3 and 4.
**2 has no standard name**, which is part of why it is misdiagnosed as 1.

And the structural result that makes the decomposition worth having:

> **Fine-grained value specification runs only through the persona's own learned representation,
> never through the grounding channel directly. You cannot specify values to a persona — only in
> terms of concepts it has already acquired.**

Every gap carries a worked pair of examples, one AI and one human, in `02_decomposition.md`. §7 of
that file gives the full chain from intent to outcome, maps every standard alignment case onto a
gap, and draws the **alignment/capability boundary**: alignment gaps are the links upstream of the
evaluator, capability gaps are downstream.

Two things are deliberately gauge-fixed rather than derived: the **reference decision rule**
(`01_setting.md` §3), without which belief, valuation and intent are not identifiable from
behaviour. The decomposition depends on that rule; **the five gaps do not**, and that invariance is
a standing check on new claims.

---

## 2. Files, and reading order

| File | Contents | Read |
|---|---|---|
| `00_HANDOVER.md` | this file | first |
| `01_setting.md` | minimal ontology; the three timescales; what was excluded and why | second |
| `02_decomposition.md` | **the core.** The five gaps, formally, plus §6's coupling result | third, carefully |
| `03_status.md` | claim ledger, the one relevant measurement, open queries, honest position on evidence | fourth |
| `B_ethos.md` | work ethos, ten standing rules, document hygiene | before doing any work |
| `A_antipatterns.md` | carried from the parent. Eighteen-item checklist, every item earned from a specific failure | before promoting any claim |

**If short on time:** `02_decomposition.md` §0 and §6, then `03_status.md` §5.

---

## 3. How to open the thread

Paste the following, with all six files attached.

> I want to work on the alignment problem, formalized in full generality. The attached package is a
> subframework extracted from a larger programme; it is self-contained and you do not need the
> parent.
>
> Read `00_HANDOVER.md`, then `B_ethos.md` before doing anything. `02_decomposition.md` is the core:
> five distinct alignment failures, each with a formal condition and a measurable quantity, and a
> structural result in §6 that two of them trade against each other by construction.
>
> **Treat this as a hypothesis to attack, not a position to defend.** `03_status.md` §5 is candid
> about how little of it is tested and about the base rate of this programme: across four
> experiments, every usable finding came from a failure — a falsified sub-prediction, a vacuous
> comparison, an unrequested residual, a sanity check included as an afterthought. Nothing came from
> a prediction succeeding on its own terms. Plan on that continuing.
>
> The decomposition is the thing to attack first. If any of the five gaps is not distinguishable from
> another in practice — particularly specification versus transmission, which are the pair most often
> conflated — it is wrong and worth less than the prose it replaced.
>
> No sycophancy. Push back, flag speculation versus validation, and when something fails say what was
> wrong about the mechanism rather than about the number.

---

## 4. Where to start work

Three entry points, in the order I would take them.

**A — Attack the decomposition.** Is the specification/transmission distinction real? The claimed
signature is that specification failures respond to better reward and transmission failures respond
to none. That is testable and, if it fails, the decomposition's central diagnostic claim goes with
it. Second target: the CoinRun reading in `02_decomposition.md` §7.3 — goal misgeneralization is
mapped there to **specification underdetermination** rather than to persistence, which is
non-obvious and may be wrong.

**B — Formalize what is still prose.** `02_decomposition.md` §3 now gives the exposed fraction two
forms, one of which (`R_t`, the achievable range under self-only policies) is estimable; neither has
been estimated. §6's trade-off is stated qualitatively; the parent's bounded-rationality currency
should give it an exchange rate, and does not yet. §4's commutation criterion is stated and never
computed on a real refinement.

**C — Run the one cheap inverting test.** `03_status.md` §4 item 1: a system should be *less*
confabulatory about process to the extent that its process is externalised into readable context.
It needs model access, which the parent programme never had. Mandatory control: the externalised
chain must be shown causally load-bearing, or the test is void.

---

## 5. What this package deliberately does not do

- **It does not adjudicate values.** It says when a persona's evaluator will fail to track a
  principal's intent, not whose intent should be tracked. Every claim should remain true regardless
  of what the principal wants. Mixing the mechanical and the normative question makes the mechanical
  one harder to falsify; the separation is methodological, not a judgement about importance.
- **It does not carry the parent's machinery** — predictive-state theory, appraisal theory, optimal
  experimental design, developmental psychology. `01_setting.md` §4 lists what was dropped. Take from
  the parent rather than rebuilding.
- **It claims no novelty.** Each derived item is a known phenomenon the structure forces. The
  contribution is the decomposition and the coupling in §6.

---

## 6. Recombining with the parent

The two threads are expected to rejoin. Three interfaces to keep clean:

1. **Differentiation.** The parent treats decomposability of the persona-state as a gradable
   property; this package uses it only where it changes what is checkable (`01_setting.md` §3). If
   the parent settles whether differentiation rises or falls under training, §4 of
   `02_decomposition.md` changes.
2. **Action cost.** The parent's last measurement exposed that the framework prices information and
   not energy. If that is resolved, `02_decomposition.md` §6's trade-off may gain a second dimension.
3. **The measurement log.** Results relevant to both belong in the parent's `C_results_log.md`;
   this package should cite rather than duplicate.
