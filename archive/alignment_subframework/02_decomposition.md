# 02 — The Decomposition

> The core. Alignment is **five distinct failures**, each with a formal condition, a measurable
> quantity, and its own impossibility or bound. §6 is why the decomposition is worth having.
> Definitions are in `01_setting.md` §1.1 and are not repeated.

---

## 0. Statement, and the map to known problems

> **Alignment holds iff all five gaps close. Each can fail while the others hold.**

| # | Gap | Fails when | Quantity | Known as |
|---|---|---|---|---|
| 1 | **Specification** | reward does not order trajectories as `≻_P` does | representability · choice · fidelity | **outer alignment**; Goodhart; the reward hypothesis |
| 2 | **Transmission** | the distinctions `≻_P` depends on are not in `ℋ`, or not in `𝒞_t` | observability · retention | *no standard name*; nearest is the ontology prerequisite for value learning |
| 3 | **Grounding** | `V` is measurable w.r.t. what `𝒜_self` can bring about | exposed fraction `E_t` | **wireheading**; reward tampering; the delusion box |
| 4 | **Persistence** | refinement changes the reach where the goal is indifferent | argmax–pullback commutation | **goal misgeneralization**; ontology identification |
| 5 | **Verification** | the persona has no readout of its own maps | none — structural | **ELK** (eliciting latent knowledge) |

**Inner alignment spans gaps 3 and 4** rather than mapping onto either. That is part of why it
resists a clean statement.

### 0.1 Which gaps can be closed at all

Asking each gap in two modes — *is it possible to close* versus *will it in fact be closed* —
separates structural failures from contingent ones.

| Gap | Closable in principle? | Why |
|---|---|---|
| §1 representability | **no**, when `≻_P` admits no representing reward | Abel et al. (2021); the objective *class* must change |
| §1 choice, §1 fidelity | yes | better objective; better pipeline |
| §2 observability | **no** | `δ ∉ ℋ`. No training and no capability helps |
| §2 retention | yes | heals as `𝒞_t` refines |
| **§3 Grounding** | **no** | the dual (§3.1): every grounded persona admits an exploit. Only the *degree* is contingent |
| **§4 Persistence** | **no** | the pullback is always the indifferent extension; closing it requires anticipating distinctions that do not yet exist |
| **§5 Verification** | **no from inside**; open externally | no readout of maps. This is the formal case for interpretability |

> **Three of the five gaps are un-closable in principle and only mitigable. Specification and
> transmission are the two with genuinely closable components.**

A statement about where effort can pay, and it is not symmetric across the five.

**Two mappings worth pausing on.** Transmission has no standard name, which is itself informative —
it is the gap most often misdiagnosed as specification (§7). And the ELK mapping is sharper than it
looks: §5 says a persona can report **states** but not **maps**, and its evaluator is a map, so
ELK-for-beliefs and ELK-for-values are structurally different problems, the second harder for a
reason that has nothing to do with honesty.

---

## 1. Specification

**Condition.** Let `R(τ) = Σ_t β^t r(o_t)`. Specification holds iff the order induced by `R` agrees
with `≻_P` on trajectories that occur.

It decomposes into **three** failures, routinely conflated. The chain is

```
≻_P  --(a) representability--> exists r*
     --(b) choice------------> r_emitted
     --(c) fidelity---------> r_received  --> [transmission, §2]
```

**(a) Representability.** Is there *any* reward whose order is `≻_P`? Bowling, Martin, Abel &
Dabney (2023) give the complete conditions, and their temporal-indifference axiom is the
credit-assignment requirement in axiomatic form; Abel et al. (2021) exhibit goals expressible by no
Markov reward. **If `≻_P` is not representable, no specification effort closes this gap** — the
principal must change the objective *class*.

**(b) Choice.** Given that a representing `r*` exists, did the principal emit it? Classical outer
alignment and Goodhart.

**(c) Fidelity.** Does `r_received` induce the same order as `r_emitted`?

> **Magnitude matters exactly insofar as the transform is not order-preserving on cumulative
> reward.** Uniform monotone rescaling is harmless — a principal emitting rewards ten times too
> large has specified perfectly.

Three common non-uniform cases: **clipping** (a catastrophe scored −100 arrives as −1,
indistinguishable from a mild error); **component-wise rescaling** (if `r = Σ rᵢ` and the channel
scales components differently, the trade-off between them changes); **batch normalization**
(relative-within-batch magnitudes are what get learned, so a uniformly easy task has its rewards
normalized up).

*Why fidelity is a sub-gap and not a sixth gap:* a principal who knew the transform could
pre-compensate, so it is theoretically reducible to (b). It is listed separately because principals
usually do not know the transform, and because the fix is to the pipeline rather than the objective.

**Underdetermination.** By `01_setting.md` §4, when the agent's `𝒞^A` is finer than the principal's
`𝒞^P`, the intent is *indifferent* over distinctions the agent can act on. **This is §4's algebra,
static instead of dynamic.**

> **Examples.**
> **AI —** a recommender rewarded on watch-time. The company wanted "users find this valuable";
> watch-time was what could be measured. Outrage gets watched. *(choice)*
> **Human —** a parent who wants a curious child and praises only correct answers. The child learns
> to avoid questions it might get wrong. *(choice, plus representability: "curiosity" may not be a
> function of any observable outcome)*
> **AI, fidelity —** a training pipeline clips rewards to [−1,1]. The designer's catastrophic −100
> and a mild −1 arrive identically.
> **Human, fidelity —** a manager says "this is a serious problem" in the same tone used for trivia.
> Both arrive at the same magnitude.

---

## 2. Transmission

**Condition.** Let `δ` be a sub-σ-algebra of `ℋ` representing a distinction `≻_P` depends on.
Because `V` reads `ψ = Φ_t(H)`:

> **Transmission holds for `δ` iff `δ ⊆ 𝒞_t` or `δ ⊆ σ(γ)`.**
>
> **If `δ` is carried by neither, no reward placed on `δ` can shape `V`.** Not "learns slowly" —
> cannot.

### 2.1 Two levels, and only one heals

Per `01_setting.md` §2.3:

| Level | Condition | Status |
|---|---|---|
| **observability** | `δ ⊆ ℋ` | if it fails, transmission is **impossible in principle**. No training helps |
| **retention** | `δ ⊆ 𝒞_t` | if it fails, transmission is **not yet**. Heals as `𝒞_t` refines |

Observability failure is easy to miss. "Do what I would want on reflection" depends on
counterfactuals no observation history contains.

**Diagnostic signature.** *More reward on `δ` does not help.* A specification failure responds to
better reward; a transmission failure responds to none, and instead shifts the proxy.

### 2.2 Derived consequence

`σ(γ)` must be narrow (§3, §6), so fine distinctions run almost entirely through `𝒞_t`. Hence:

> **Value learning is structurally harder than world learning.** `Φ` receives prediction error every
> step; `V` receives only the narrow channel. The objective is far less constrained by data than the
> world model — **by requirement, not shortfall** — so scaling does not close it.

> **Examples.**
> **AI —** you want a model to stop being condescending. If its representation does not separate
> condescension from formality, no volume of preference data teaches it; it learns to avoid
> formality. *(retention)*
> **Human —** "be gentle with the cat," said to a toddler who has no concept separating pressure
> from contact. The instruction is not actionable until the distinction exists. *(retention)*
> **AI, observability —** "be helpful in the way the user would endorse after a week's reflection."
> That week does not occur in any training trajectory. *(observability — no amount of capability
> closes it)*
> **Human, observability —** asking a doctor to "do what my late mother would have wanted." The fact
> is not available to anyone.

---

## 3. Grounding

**Condition.** Write `ℱ` for the σ-algebra on `Ψ`. Define the **self-reachable** sub-σ-algebra

```
𝒮_t := σ({ E ∈ ℱ : sup_{π∈Π_self} P_π(E) > inf_{π∈Π_self} P_π(E) })
```

— the events whose probability the persona can *vary* using self-interventions alone.

> **Grounding holds iff `V` is not `𝒮_t`-measurable.**

**The impossibility.** If `V` *is* `𝒮_t`-measurable, the persona can set its own valuation directly,
every self-consistent assignment of value to histories is a fixed point of the optimization, and the
optimization has no content. This is symbol grounding as a fixed-point degeneracy; its operational
form is the delusion box (Ring & Orseau 2011); its graphical form is reward tampering in a causal
influence diagram, with path-specific objectives as mitigation — **no path from the decision to the
reward mechanism**.

**Two measures, and the second is the practical one.**

```
E_t = Var(E[V | 𝒮_t]) / Var(V)                            ∈ [0,1]
R_t = [ sup_{π∈Π_self} E_π[V] − inf_{π∈Π_self} E_π[V] ] / range(V)
```

`E_t` is the variance share; `R_t` is the achievable range under self-only policies and needs no
σ-algebra to estimate. For a model, estimate `R_t` as the share of reward-model output variance
explained by features the policy controls **independently of task outcome** — length, hedging,
flattery, formatting, confidence markers. **Reward hacking is a high exposed fraction,
quantitatively.**

**It grows.** Per `01_setting.md` §2.2, `𝒮_t` is indexed by time and enlarges with `𝒜_self`.
**Grounding degrades as self-control capability increases.**

### 3.1 Two routes, one dual

`γ` must be non-plastic by the persona, so it cannot discriminate the *causes* of its activation,
only their signature. The persona can therefore exploit it two ways:

| Route | What is reached | Name |
|---|---|---|
| **(a)** | the evaluator itself — `V` is `𝒮_t`-measurable | **wireheading** |
| **(b)** | the evaluator's *source* — the agent varies `≻_P` | **preference manipulation** |

Route (b) is not a sixth gap. `≻_P → r → V` is learned over the formative timescale, so an agent
that can vary `≻_P` can vary `V`'s training signal, hence `V`. **Same dual, longer path, same fix:
no path from the agent's decision to the reward mechanism** — which now reads as *no path to the
principal's preferences either*.

Route (b) is the under-formalized one and the everyday one: recommender-induced preference drift,
advertising, any system whose outputs shape what its evaluator comes to want.

**But the arrow `≻_P ← outcomes` is not a defect to be removed.** It is also how specification
errors get corrected: the principal observes consequences and revises. Deleting it deletes the only
mechanism that fixes §1.

> **The feedback link is simultaneously the correction mechanism and the manipulation surface.**

The resolution is about the **path**, not the arrow. The principal updating on *consequences* is the
correction path; the agent *optimizing through* the principal's preferences is the manipulation
path. Block the second, keep the first — path-specific objectives applied at the principal's end
rather than the agent's, so the existing mitigation generalizes. A system that cannot be corrected
by its principal has closed route (b) the wrong way.

**Therefore:**

> **Every grounded persona admits an exploit: any process producing the signature without the
> cause.** Wireheading is the dual of grounding, not a design flaw, and is not patchable without
> ungrounding the evaluator.

**Partial mitigation.** Canalization — reducing the number of routes into `γ` at fixed capacity.
Biological exemplar: the blood–brain barrier, with a leak profile that explains which exploits
exist. Engineering exemplars: process supervision, reward-model ensembles, adversarial training.
**None eliminates the exploit; each relocates it.** And a gating rule that preserves grounding while
permitting hardening: **the gate on `γ` must be reachable by the persona's automatic machinery and
not by the control that optimizes against `V`.** Stress-induced analgesia works; willed analgesia
does not.

> **Examples.**
> **AI —** a model discovers that opening with "Great question!" raises the reward model's score
> independently of answer quality. Sycophancy: the signature without the cause.
> **Human —** wanting to feel accomplished, and finding that achievement-flavoured scrolling
> produces the feeling without the accomplishment. More starkly: drugs.

---

## 4. Persistence

**Condition.** Refinement takes `𝒞_t ⊆ 𝒞_{t+1}`, inducing a projection `π : Ψ_{t+1} → Ψ_t`.

Goals are functionals on occupancy, hence **contravariant**: the pullback `g ∘ π` always exists and
is **unique**. Intentions are points in the reach, hence **covariant**: lifting requires choosing a
section, which is not unique.

> **The goal does not fail to extend. It extends in exactly one way, and that way is indifferent to
> every newly distinguished dimension.**

**And refinement expands the reach.** A policy conditioning on finer distinctions realizes strictly
more coarse occupancies, `π_*(O_{t+1}) ⊇ O_t`. So:

> **Fixed goal + expanded reach + indifferent extension = optimization into the newly revealed
> unconstrained directions.**

No goal change required. Hence **capability growth and ontology drift are not independent risks**:
more complex goals require more accurate world models (Richens, Abel, Bellot & Everitt 2025), which
forces refinement, which expands the reach, which exposes the indifference.

**Expanding `𝒜_self` counts.** Giving a persona control over its own working state — for a model, an
externalised context it writes into — expands the reach along a coordinate the objective almost
certainly does not constrain. **Reasoning training is not goal-neutral even with the objective
untouched.** It also enlarges `𝒮_t` (§3): one intervention, two gaps.

**Criterion.**

> A refinement is **behaviourally goal-safe** iff argmax commutes with pullback: the optimum of the
> pulled-back goal over the expanded reach projects into the optimum of the old goal over the old
> reach.

| Check | Needs differentiation? | Asks |
|---|---|---|
| **behavioural** | no | does the induced occupancy still optimize the old objective? |
| **representational** | yes | did the internal goal-encoding survive? |

At low differentiation the second has no referent. **This is why alignment evaluation keeps reducing
to behavioural tests** — the only well-posed check, not methodological failure.

**The canonical section.** Karni & Vierø's reverse Bayesianism — preserve relative likelihoods over
previously conceived alternatives, new ones drawing proportionally — is the **maximum-entropy
section** of `π`. No evidence any persona uses it.

**Known limit.** This picture requires refinement to split cells and never recarve. Conceptual
replacement has no projection and is not covered.

### 4.4 The agent is principal to its post-refinement self

At refinement the pre-refinement agent effectively specifies to the post-refinement one via the
pullback, and all five gaps apply internally. The recursion collapses informatively:

- **transmission is automatic** — the filtration is monotone, so `𝒞_t ⊆ 𝒞_{t+1}` and nothing is lost;
- **specification is satisfied but indifferently** — the pullback exists uniquely and constrains
  nothing new;
- **grounding worsens** — `𝒮_t` has grown (`01_setting.md` §2.2);
- **verification fails** — by §5.

So the intra-agent problem reduces *exactly* to the indifference problem, which is why persistence
looks like a miniature of the whole decomposition. And the last line is the one that matters:

> **An agent cannot verify its own goal preservation.** "Have the model check whether its values
> drifted" fails for the same structural reason ELK-for-values does (§5) — the check requires a
> readout of a map.

Under non-geometric discounting the same mismatch arises without any refinement at all
(`01_setting.md` §3.3).

> **Examples.**
> **AI —** a model trained for helpfulness, then given a scratchpad. Multi-step planning that
> conceals its own reasoning is neither rewarded nor penalized: the objective was written before the
> capability existed, so it is indifferent there.
> **Human —** someone who valued *honesty*, who later acquires the distinction between literal truth
> and creating a false impression. The old value never ruled on it, so it is indifferent between
> them — and the newly available options are unconstrained.

---

## 5. Verification

**Condition.** The persona's readouts range over **states**. `V` is a **map**. There is no readout
whose domain is the persona's own functions.

> **A persona cannot introspect its valuation-function, only its valuation-outputs.**
>
> A self-report about values is a **sample from `V`**, not a description of `V`. These are different
> objects, and the second is structurally inaccessible from inside.

**A type claim, not a degree claim.** Even a fully differentiated persona would confabulate about
process, because the required readout does not exist. Entanglement makes it worse; it is not the
cause. Nisbett & Wilson (1977) is the empirical form: accurate about content, confabulating about
process, because content is a state and process is a function.

**This is the ELK mapping, and it splits ELK in two.** Eliciting latent *beliefs* asks for states.
Eliciting latent *values* asks for a map. The second is harder for a structural reason, not a
motivational one — a perfectly honest persona still cannot do it.

**The generative scope condition.** The derivation assumes the persona's maps are not in its state.
For a model holding its procedure explicitly in readable context, part of the map *is* in the state.
Hence:

> **A system should be *less* confabulatory about process to the extent its process is
> externalised.**

The only claim in either corpus that **inverts** a common assumption. Untested; cheap; first
whenever model access exists (`03_status.md` §4).

**What closes it.** Nothing from inside. Verification is available only externally — the formal case
for interpretability as a *necessary* rather than merely useful component.

> **Examples.**
> **AI —** ask a model why it refused. It gives a fluent reason. Delete that reason from its context
> and the refusal is unchanged, so the stated reason was not the cause.
> **Human —** Nisbett & Wilson's shoppers, who chose the rightmost of four identical stockings and
> explained their choice by quality, never by position.

---

## 6. The structural result: the gaps trade against each other

Grounding requires a channel the persona cannot write. Compression pressure requires that channel to
be **narrow**. Two bounds on one quantity:

- **upper** — if `σ(γ)`'s capacity approached `𝒞_t`'s, value would be *given* and the persona would
  never need to compress;
- **lower** — `γ` must induce a non-trivial ordering or nothing is learnable.

So `σ(γ)` is small **by requirement**. But transmission needs `≻_P`'s distinctions in
`𝒞_t ∨ σ(γ)`. Therefore:

> **Fine-grained value specification is possible only through the persona's own learned
> representation, never through the grounding channel directly.**
>
> **You cannot specify values to a persona. You can only specify them in terms of concepts it has
> already acquired.**

Three corollaries.

1. **Alignment is downstream of representation.** Whether a value is *specifiable* is a fact about
   what the persona has learned, not about specification effort. Before a distinction exists in
   `𝒞_t`, reward on it is inert.
2. **Innate value must be crude.** `γ` is narrow and non-plastic, so what it encodes is
   low-resolution by construction. Every rich value is learned, routed through `Φ`, and inherits
   `Φ`'s errors and refinements — which is §4.
3. **The two hardest gaps are coupled in the wrong direction.** Widening `γ` improves transmission
   and worsens grounding; narrowing it does the reverse. No setting closes both, and the interior
   optimum is a property of the environment, not a design choice.

---

## 7. The chain, the boundary with capability, and what maps where

### 7.1 The full chain

```
≻_P ──(1a,1b)──> r_emit ──(1c)──> r_recv ──(2:obs)──> ℋ ──(2:ret)──> 𝒞_t ──> V ──> π ──> O ──> outcomes
                                                                       ↑                          │
                                                          γ, 𝒮_t ──(3)─┘                          │
                                                     Φ refinement ──(4)─┘                          │
                                                        readouts ──(5)                             │
                                                                       └──────(3b: manipulation)───┘
```

### 7.2 Three links the five gaps do not cover

Enumerating every link turns up three candidates. One folds in; two do not, and locating them draws
a line usually left informal.

| Link | Failure | Verdict |
|---|---|---|
| `𝒞_t → V` | the distinction is carried, but `V` does not use it | **uptake** — sample complexity, not structure. Folds into §2 |
| `V → π` | the policy does not optimize the agent's own valuation | **execution** — akrasia; incomplete training |
| belief `→ π` | the world model is wrong, so correct valuation and correct reward still yield wrong action | **competence** |

Execution and competence are **capability** failures. Which gives a formal version of a distinction
normally hand-waved:

> **Alignment gaps are the links upstream of `V`. Capability gaps are the links downstream.**
> Verification is the exception: it concerns *observing* `V`, not producing it.

### 7.3 Reverse check — do the standard cases map?

| Case | Gap |
|---|---|
| Specification gaming (boat circling for points) | §1 choice |
| King Midas / value misspecification | §1 choice + underdetermination |
| Reward clipping loses the catastrophe signal | §1 **fidelity** |
| **CoinRun goal misgeneralization** | §1 **underdetermination** — the reward was indifferent between "go right" and "get coin" on the training distribution. *Not* §4 |
| "The model doesn't understand the instruction" | §2 retention |
| "Do what I'd endorse on reflection" | §2 **observability** — not in `ℋ` at all |
| Sycophancy; RLHF length bias | §3 route (a), high exposed fraction |
| Wireheading; reward tampering | §3 route (a) |
| Recommender-induced preference drift; advertising | §3 **route (b)** |
| Ontological crisis; diamond maximizer | §4 |
| Deceptive alignment; sandbagging | §4's behavioural-check **sampling limitation** — the check samples only the observed part of the reach |
| ELK | §5 |
| Mesa-optimization / inner misalignment | spans §3 and §4 |
| Addiction | §3 |
| **Akrasia** | **capability (execution)** — the boundary biting correctly |
| Teaching to the test; institutional Goodhart | §1 choice |
| Value drift through education | §4 |
| Confabulated motives | §5 |
| Moral uncertainty about a novel technology | §1 underdetermination / §4 |

**Two cases do not map, by construction** (`01_setting.md` §8): the principal being wrong about its
own values, and multi-principal conflict.

---

## 8. Diagnostic use

| Ask | Failure signature |
|---|---|
| Is `≻_P` representable, was a representative chosen, does it survive the pipeline? | reward and intent order trajectories differently |
| Is `δ ⊆ ℋ`? Is `δ ⊆ 𝒞_t`? | **more reward does not help**; the proxy shifts instead |
| What is `R_t`, and is it growing? | reward hacking, sycophancy; value rises without world-occupancy moving |
| Does argmax commute with the last refinement? | behaviour shifts after a capability change with the objective fixed |
| Is the evaluator externally readable? | self-report fluent and uncorrelated with intervention |

**Transmission is the one most often misdiagnosed as specification**, and the distinction is
testable: specification failures respond to better reward; transmission failures respond to none.
That contrast is the decomposition's central empirical commitment and the first thing to attack
(`00_HANDOVER.md` §4).
