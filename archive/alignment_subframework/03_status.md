# 03 — Status and Open Queries

> What each claim rests on, what measurement has touched, and what is genuinely open.
> Honesty about evidence is the point of this file; read §5 before citing anything from §1.

---

## 1. Claim ledger

**Derived** — the framework forbids the negation.

| Claim | Where |
|---|---|
| Grounding is a fixed-point impossibility: if `V` is `𝒮`-measurable the optimization has no content | `02` §3 |
| Wireheading is the dual of grounding; every grounded persona admits an exploit | `02` §3 |
| Nothing motivates except as retained, or via `γ` | `02` §2 |
| Value learning is structurally harder than world learning — by requirement, not shortfall | `02` §2 |
| Goals pull back uniquely, and the pullback is the indifferent extension | `02` §4 |
| Refinement expands the reach | `02` §4 |
| Expanding `A_self` is a capability increase; reasoning training is not goal-neutral | `02` §4 |
| A persona cannot introspect its valuation-function, only its outputs | `02` §5 |
| Innate value must be crude | `02` §6 |
| The exposed fraction **grows** as the self-control repertoire grows, so grounding degrades over training | `01` §2.2, `02` §3 |
| Principal-coarseness is the static analogue of refinement-induced indifference | `01` §4 |
| Transmission splits into observability (never heals) and retention (heals with learning) | `02` §2.1 |
| ELK splits: eliciting beliefs asks for states, eliciting values asks for a map | `02` §5 |
| Alignment is a property of a (principal, agent, **environment**) triple | `01` §2.3 |
| Preference manipulation is grounding by a longer path, not a sixth gap | `02` §3.1 |
| An agent cannot verify its own goal preservation | `02` §4.4 |
| Non-geometric discounting is an intra-agent alignment failure of the same form | `01` §3.3 |
| Alignment gaps are upstream of `V`; capability gaps are downstream | `02` §7.2 |
| The alignment claims are gauge-invariant; the belief/valuation/intent split is not | `01` §3.2 |
| §6's trade-off implies an **irreducible floor** on total failure | `02` §6 — existence only; no functional forms, so the floor is not located |
| **Three of five gaps are un-closable in principle**; only specification and transmission have closable components | `02` §0.1 |
| The principal-feedback arrow is both the correction mechanism and the manipulation surface; the fix is path-specific, not arrow-deletion | `02` §3.1 |
| **Fine-grained value specification runs only through `σ(Φ)`, never through `γ`** | `02` §6 |

**Imported as theorem** — not ours, and load-bearing.

| Import | Buys |
|---|---|
| Bowling, Martin, Abel & Dabney (2023) | when a goal reduces to Markov reward; the subjective/objective goal split |
| Abel et al. (2021) | goals expressible by no Markov reward |
| Richens & Everitt (2024); Richens, Abel, Bellot & Everitt (2025) | competence forces a world model, extractable from policy, accuracy scaling in goal complexity |
| Ring & Orseau (2011) | delusion box |
| Everitt, Hutter, Kumar & Krakovna; Farquhar, Carey & Everitt | reward tampering as a CID; path-specific objectives |
| Ortega & Braun | the utility/information conversion law, axiomatically |
| Karni & Vierø (2013) | reverse Bayesianism as the maximum-entropy section |
| Nisbett & Wilson (1977) | the content/process introspection split |

**Speculative** — flagged, not promoted.

- **Action cost.** The parent's measurement showed the design criterion under-penalises how much
  effect a unit of command buys. The framework prices *information* (KL from a prior policy) and does
  not price *energy*. Two costs imply two exchange rates. There is a standing neuromodulator
  candidate. **Not promoted**: it has the exact shape of the over-unification anti-pattern, and the
  tempting identification with a measured interior optimum is wrong, because that experiment ran with
  matched power and therefore had no energy cost at all.

---

## 2. One named disagreement with a live competitor

LeCun's architecture for autonomous machine intelligence maps near-isomorphically onto the parent
framework, and **its cost module independently reproduces the split this subframework calls `γ`
versus learned valuation**: a hard-wired *intrinsic cost* plus a trainable *critic*. Two designs, two
motivations, same partition — the strongest convergence either corpus found.

**Two disagreements remain.**

- **Its cost is a single scalar; this framework's valuation is two-dimensional** (target and the
  temperature at which it is pursued). If the scalar version is right, part of the parent's account
  of evaluative state is wrong.
- **Its configurator — the module that reconfigures the others — is widely regarded as the proposal's
  most under-specified component.** This framework says why: choosing among self-interventions
  requires predicting their effects on oneself, and that predictive partner is absent from the
  architecture. **Prediction: any working implementation will be forced to build a self-model,
  whether or not it is named one.** Watch for it appearing implicitly.

---

## 3. What measurement has touched

Three rounds in the parent programme. Only one result bears on this subframework.

> **Reward-dependence tracks capacity, not exactness, and saturates.** Representation divergence
> between two disjoint reward structures falls monotonically with capacity (ρ = −0.893, p = 0.007)
> but **never reaches the same-task floor at any capacity tested** — and over a range where
> reconstruction error falls ~10×, it does not fall at all.

**Why it matters here.** It partly falsifies the parent's claim that reward-independence is a
*corollary of exactness*. What survives is that compression is reward-dependent whenever capacity
binds. For this subframework the consequence is `01_setting.md` §3: **error localization is
conditional on differentiation and does not become available merely by adding capacity**, so `02`
§4's representational goal-safety check may be permanently unavailable rather than temporarily so.

**One artifact explanation is open and cheap to settle.** The metric measures the whole
representation, including directions the task does not constrain, which at excess capacity may be
filled task-specifically. Discriminating run: divergence restricted to the task-relevant subspace.
Not done.

---

## 4. Open queries, ranked

1. **The externalised-process introspection test.** `02` §5's scope condition predicts a system
   should be *less* confabulatory about process to the extent its process sits in readable context.
   The only claim in either corpus that **inverts** a common assumption; cheap; needs model access;
   never run. **First whenever access exists.** Mandatory control: the externalised chain must be
   shown causally load-bearing — edit it and check the answer moves — or the test is void.
2. **Is the exposed fraction estimable, and does it predict hacking?** `02` §3 turns a judgement call
   into a number. Severe confound: exposed fraction and reward-model accuracy correlate naturally and
   must be varied independently.
3. **Is behavioural goal-safety enough?** `02` §4. A behaviourally safe refinement can still have
   moved internal structure in ways that matter off-distribution, with no check available at low
   differentiation. This is the deceptive-alignment worry reached from a different direction.
4. **Does differentiation increase or decrease under training?** Determines whether the
   representational/behavioural gap narrows or widens with scale. Distinct pressures on distinct
   readouts should favour separation; capacity pressure favours entanglement. Unknown, and
   consequential.
5. **The subspace-restricted divergence measurement** (§3). Cheap, and it decides whether a parent
   claim survives.
6. **Does the growth of `𝒮_t` have a bound?** `01` §2.2 says grounding degrades as self-control
   capability grows, and says nothing about how fast or whether it saturates. If it does not
   saturate, grounding is not a property a system *has* but one it *loses*, and the mitigation
   question changes shape.
7. **Where is the irreducible floor?** `02` §6 shows widening `γ` worsens grounding and narrowing
   worsens transmission, so total failure has a minimum over channel capacity. **Existence is
   argued; the location is not,** and it needs functional forms neither corpus has. Until then the
   floor is a shape claim, not a quantity.
8. **Is the specification/transmission contrast empirically separable?** The decomposition's central
   commitment: specification failures respond to better reward, transmission failures respond to
   none. Untested, and the first thing to attack.
9. **Does the parent's action-cost gap change `02` §6?** If `γ` must price energy as well as
   information, the capacity interval has a second dimension and the trade-off in §6 may not be
   one-dimensional. Unexamined.

---

## 5. The honest position

**Nothing in this subframework is novel to the world.** Each derived item is a known phenomenon the
structure forces. The contribution is the **decomposition** — that these are five distinct failures
with distinct signatures, and that two of them trade against each other by construction. That
framing is the thing to attack.

**Almost none of it is tested.** The parent programme ran four specified experiments; three of them
could not answer their own question, and all three failures were checkable in advance by algebra
nobody did. Only one result touches this subframework, and it went partly against the theory.

**Coherence is not evidence.** The parent corpus became more internally coherent every session, which
is also the trajectory a well-constructed wrong theory follows. This subframework is more compact and
will therefore feel more convincing. Discount accordingly.

**The base rate, and it is the most reliable thing either thread has produced:** across every round,
content came from a falsified sub-prediction, a vacuous comparison, an unrequested residual, and a
sanity check included as an afterthought. **Nothing came from a prediction succeeding on its own
terms.** Plan work on the assumption that this continues.
