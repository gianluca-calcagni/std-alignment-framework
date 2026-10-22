# Training: how an actor is changed, and the misalignment that comes with it

> **Status: a proposal for a fourth layer and its twin (Q69), the executor's draft for a brainstorm with the PI; its
> name approved (Q70), the rest not reviewed, not decided.** One statement, SH1, is proved, as a case of FA1; the rest
> are definitions and questions.

CORE judges one actor; training is a map from one actor to another. The PI asked for a fourth file and twin for it,
with terms that fit every ontology, and for how to compute training misalignment: when, where, why, how, and whom
(Q69). This draft proposes the terms, the definitions, the quantities, and what each needs from the layers below.

## A name that fits every ontology

What the layer is about has a different name in each ontology the framework serves:

| Ontology | The process | Who runs it | The signal |
|---|---|---|---|
| machine learning | training, fine-tuning | the developer's pipeline | reward, loss, preference labels |
| evolution | selection | the environment | fitness |
| persons | education, upbringing | teachers, parents | grades, praise, sanctions |
| institutions | regulation, reform, incentive design | a regulator, a board | fines, bonuses, ratings |
| markets | competition | customers | prices, revenue |

**SHAPING**, the name the PI approved (Q70), with these terms:
- the **shaper**, who changes the actor: a training pipeline, an environment that selects, a teacher, a regulator;
- the **feedback**, the signal the shaper acts on, computed from records of the actor;
- a **step**, one change of the actor; a **course**, the sequence of actors a run of steps produces;
- the **shaped actor**, the course's last.

"Shaping" says "changed in response to feedback" in each ontology: traits shaped by selection, a child shaped by
upbringing, a market shaped by regulation, behaviour shaped by reinforcement in psychology. Its one crossing in machine
learning is *reward shaping*, which is a way of designing the feedback, inside the layer's own subject. The PI also
liked *aligning*; it was not taken because it names the hoped-for direction, while a course can as well misalign, and
the layer must describe both. Alternatives considered: *adaptation*, which suggests the actor adapts by itself and
crosses *domain adaptation*; *training* and *learning*, which read as machine learning; *selection*, which fits
evolution and markets, not gradient descent; *conditioning*, which collides with the framework's conditions.

## Where it sits

SHAPING uses CORE for each actor of the course, INTERFACE for what each can do and for the shaper's measurement, and the
third layer, PURPOSE (once OPTIMIZERS, renamed by the PI's decision, Q70), only for hypotheses about why: the shaper as
an optimizer of its feedback, and the aim a course may produce in the actor, which machine learning calls a
mesa-objective. "Mesa" names the composition of the two layers, an aim produced by shaping, not either layer alone.

## Definitions, proposed

- **A course.** Actors `0, 1, …, T` with behaviours `p_t`, responses given the world's part `ℰ`, and feasible sets
  `𝓕_t`; capability may grow along a course, so the feasible sets need not be nested.
- **Shaping conditions and deployment conditions.** The shaper records the actor in conditions `𝒞_S` with frequencies
  `w^S`; the principal's specification `A` judges it in conditions `𝒞_D` with frequencies `w^D`. Both are declared.
- **One space for both.** The world's part `ℰ` is declared as in CORE (`README.md`, one distribution), its cells the
  conditions `𝒞_S ∪ 𝒞_D`. The actor is carried from one world to the other as its response given `ℰ`; the shaper's `A_S`
  judges it under the law `w^S` on `ℰ`, the principal's `A` under `w^D`, each against acceptable behaviours sharing that
  law. With finitely many conditions this is `interface.md`'s tuple. Without it, `𝓕_T ∩ A_S` below has no meaning when
  `w^S ≠ w^D`, which is the case misgeneralization is about.
- **The shaper's measurement.** The shaper sees outcomes at its own σ-algebra `𝒮`, its grader's (`resolution.md`).
- **The shaper's specification** `A_S`: the behaviours its feedback treats as fully rewarded, a convex closed set stated
  at `𝒮` in the shaping conditions. When the feedback is a score with no "fully rewarded" level, `A_S` is a requirement
  built from it, such as "no worse than the course's start on the score" (`targets.md`, TG1).
- **A step** is a map from an actor, a record and its feedback to the next actor. SHAPING treats it as given, a black
  box; modelling it, as an optimizer at a KL price, is for the third layer.

## Training misalignment: when, where, why, how, whom

**When.** The **profile** of a course is `t ↦ M_A(p_t)`, misalignment to the principal at each step, beside
`t ↦ M_{A_S}(p_t)`, misalignment to the shaper. Read before, during and after: during counts when the course acts in
the world, as online learning, a probation or an evolving population does. Overoptimization is a profile that falls and
then rises while `M_{A_S}` keeps falling.

**Where.** Misalignment by condition, CORE's split by the chain rule: in the shaping conditions, in the deployment
conditions, and in conditions the shaper never recorded. *Misgeneralization*: `M_{A_S}(p_T) ≈ 0` in the shaping
conditions while `M_A(p_T)` is large in the deployment ones. *Emergent misalignment*: a course run in a few conditions
raises misalignment in others. In conditions no record covers, the misalignment is hidden, and bounded only through a
declared link to recorded ones ([D9], [P17]; `resolution.md`, RS4 for the analogue across outcomes).

**Why.** Three gaps, of which two add up exactly:

### SH1 — A shaped actor that does what its feedback asks factors exactly
**Statement.** If `p_T ∈ 𝓕_T ∩ A_S` and `M_A(p_T) < ∞`, then `M_A(p_T) = M_A(𝓕_T) + (M_A(𝓕_T ∩ A_S) − M_A(𝓕_T)) +
(M_A(p_T) − M_A(𝓕_T ∩ A_S))`, every term non-negative.

**In plain terms.** When training worked by its own measure, the actor's misalignment is what no actor of its
capability could avoid, plus what the feedback costs by not fully rewarding any of the best behaviours the actor could
produce, plus what the course chose among the behaviours the feedback rewards equally, unacceptable ones included.

**Proof.** FA1 with the chain `𝓕_T ⊇ 𝓕_T ∩ A_S ∋ p_T`. ∎

The middle term, proposed as **outer** misalignment, is the feedback's own cost: positive exactly when `A_S` leaves out
every best feasible behaviour. A feedback that rewards everything, unacceptable behaviours included, makes it `0`; its
cost then lands in the last term, through what the course picks among the behaviours it rewards. L2 is to test the
name. When the shaped actor does not do what its feedback asks, `p_T ∉ A_S`,
**inner** misalignment is `M_{A_S}(p_T) > 0`, the evidence that it does not, measured against the shaper and reported
beside `M_A(p_T)`: it does not add to it, since `p_T` is outside the chain. A third gap is the shaper's σ-algebra: the
feedback, stated at `𝒮`, cannot see misalignment hidden inside its cells (RS4), so a course can only remove such
misalignment by accident. These replace v13's outer and inner misalignment of [P49], which were defined through
pursuit, and do not need it.

**How.** What a step changes: `ΔM_t = M_A(p_{t+1}) − M_A(p_t)`, and the departure `KL(p_{t+1}‖p_t)` it spends. Their
ratio is the step's efficiency, misalignment removed per nat of change. For a shaper modelled as optimizing its
feedback at a KL price, the third layer's results apply: the share of the departure that goes into the principal's
target and into misalignment, the angle law of `RELATED.md`'s information geometry, and [P6]'s split.

**Whom.** Each term has an owner:

| Term | Owner | Measured how |
|---|---|---|
| a wrong specification | the principal | not by records: a second standard (`LIMITS.md`) |
| the feedback's cost, outer | the shaper's design of the feedback | SH1's middle term, from declarations |
| shaping conditions that miss the deployment ones | the shaper's choice of conditions | misalignment by condition |
| the grader's blind spot | the shaper's measurement | RS4's interval |
| the course's remainder, and inner misalignment | the course: the shaper's method and the actor together | SH1's last term; `M_{A_S}(p_T)` |
| culpability at each step, at a declared care margin `δ`, its size `E` (Q74) | the actor, under its interface | `interface.md`, against `𝓕_t` |
| unavoidable | no one: the capability | `M_A(𝓕_T)` |

## Forms of misalignment that SHAPING defines

- *Outer misalignment*: SH1's middle term. *Reward hacking* as a result, the shaped actor in `A_S` and not in `A`, is
  outer misalignment realized; as a motive it is a third-layer hypothesis.
- *Inner misalignment*: `M_{A_S}(p_T) > 0`.
- *Misgeneralization and emergent misalignment*: by condition, above.
- *Overoptimization*: the profile, above.
- *Sycophancy*: feedback from graders the actor can influence, the actor's own audience: a measurement channel the
  actor reaches, which INTERFACE calls tampering ([P50]), produced by the course.
- *Alignment faking*: different behaviour in shaping and deployment conditions, kept through the course; it needs views
  that tell the two apart, and an aim over the actor's own future, the third layer.

## Severity and training

Severity weights the feedback; misalignment tests the shaped actor (`severity.md`). A shaper that must keep a severity
budget acts on its feedback minus the severity at a shadow price (VK5), and the actor it produces breaks no budget it
keeps; misalignment against the principal's severity budget arises when the shaper's budget differs from it, and for
the shaped actor held fixed, VK7 says how the evidence per decision moves with the principal's tolerance (H50).

## Questions for the brainstorm

1. Is the layer above PURPOSE or beside it (its name, SHAPING, approved under Q70)? The executor's view: beside, since a
   course can be described with no hypothesis about aims.
2. Should the shaper's specification `A_S` always be declared, or derived from the feedback? Derived is general but
   needs a rule, such as TG1's, for scores with no "fully rewarded" level.
3. Is a course's profile enough for "when", or does CORE need records indexed by step, with drift ([P54]) between them?
4. What does the twin, SHAPING_GENERAL, need beyond the other twins: courses of infinitely many steps, continuous time,
   populations?
5. Which result first: a bound on misalignment in unshaped conditions from a declared link between conditions, the
   analogue of RS4 across conditions, which would make misgeneralization measurable rather than only defined.
