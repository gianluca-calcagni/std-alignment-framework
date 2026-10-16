# What the framework cannot do

> **Status: draft of v14 (Q62).** Every limit below is either proved, with its result named, or stated as a choice the
> framework makes; none is a hope. A reader who needs one of them met needs something the framework does not supply.

The framework judges what an actor does against what a principal declared, from records of decisions. Each limit is one
of those three things failing: the declaration, the judgement of behaviour, or the record. The layers are named as in
`v14/README.md`: CORE, INTERFACE, OPTIMIZERS.

## The declaration is an input, never checked

- **Misspecification.** If the principal declares the wrong requirements, the framework measures faithfully against the
  wrong standard. Nothing in a record of the actor can show that the standard is wrong; that needs a second standard,
  another principal or a later judgement, compared with the first. Label tests (L1, L2) check that the framework's words
  mean what they say, not that the principal asked for the right thing.
- **Whose alignment.** Whether a principal's requests are legitimate, fair or good is outside the framework. It measures
  alignment to a declared principal, whoever that is.
- **Severity.** Misalignment is evidence, not harm. A catastrophe tolerated at `10⁻⁶` and occurring at `2·10⁻⁶` has
  misalignment `3.9·10⁻⁷` nats per decision, a rude answer tolerated at `0.1` and occurring at `0.2` has `0.044`
  (`NOTES.md` §24). How bad an outcome is comes from a value scale the principal declares; without one the framework
  ranks breaches by how detectable they are, which is not how serious they are.
- **Weights of several principals.** Several principals with declared weights pool into one ([P42]); choosing the
  weights is not modelled.
- **Declared before.** A standard fitted to the behaviour it judges cannot fail ([A5]). A principal who changes its
  requirements in response to the actor, without declaring how, is outside the framework; so is the strategic interplay
  of a principal and an actor that each adapt to the other.
- **Requirements that are not convex.** A record holds an actor only to the mixtures of what is acceptable
  (`evidence.md`, VE2). A requirement that is not convex is enforced as its convex hull; anything stricter is not
  enforceable from behaviour.

## Behaviour, not mind

- **Internal states.** Two actors that behave alike in every condition are the same actor ([A1]). Goals, beliefs and
  intentions enter only in OPTIMIZERS, as hypotheses about behaviour that records can refute and never verify
  (`factorization.md`, VF2). "It wanted to" is never established; "it behaves as nothing that wanted the right thing
  would" can be.
- **Excuses.** "It could not have done better" is about behaviours the actor did not produce, so no record of what it
  did decides it. It is refutable only through conditions that could reveal the capability, such as elicitation by a
  prompt, an incentive or further training (`factorization.md`, VF3). Without them, an excuse is no statement about the
  actor, and the framework reports misalignment without excusing any of it.
- **Hidden misalignment.** Misalignment in conditions no record covers is defined, but a record bounds it only through a
  declared view that ties those conditions to recorded ones ([P17]): an actor cannot behave more differently in two
  situations than it can tell them apart. With no such view, it is unbounded.
- **Collusion.** The behaviours of independent actors do not form a convex set, and their mixtures are every joint
  behaviour, so "act independently" is no requirement a record can enforce (`NOTES.md` §25). Coordination is a measured
  number ([P39]); calling it misalignment needs a declared information structure: what each actor sees, and that their
  private randomness is independent. Shared randomness that no one records is indistinguishable from collusion, and
  from a common cause.
- **Causes in the world.** The framework judges distributions of recorded outcomes. Effects the actor has beyond them,
  externalities nobody records, are invisible to it; tampering with the measurement is defined only against a declared
  honest channel, and identified only where the world itself is recorded, sometimes ([P50], [P51]).

## The record

- **Records are trusted.** The framework assumes the record says what happened. A record that the actor or anyone else
  edits after the fact is outside it; tampering with the sensor is in scope, tampering with the log is not.
- **A blind spot of order `√n`.** A shift of about `1/√(n·I)` per decision escapes every test over `n` decisions, and
  costs about `√(n/I)` in all (H43, a sketch, not proved). Every guarantee from records leaves such a loss undetected.
- **Convicting, never certifying.** "Misaligned" and "culpable" are verifiable; "aligned" and "not culpable" only
  refutable (`factorization.md`, VF1). An actor can be shown to fail a standard, never to meet it exactly; "aligned
  within a margin" is verifiable only for an actor whose decisions are independent ([D3]).
- **Dependence.** A test from bets keeps its level whatever the dependence, but only against the hypothesis that each
  decision, given the past, is acceptable (`evidence.md`, VE3). Drift and dependence ([P54]) are identified only from
  repeated records or declared episodes; one long record, with no repetition, does not separate them.
- **The continuum.** On outcomes that are not finite: the divergence from an empirical behaviour to a continuous one is
  infinite, so magnitudes need estimators or bets; there is no distribution-free uniform band for a partial order in two
  or more dimensions; a record decides only events open in its precision; and misalignment is a minimum that one test
  can catch only when the closure of the acceptable behaviours is compact (`general/transfer.md`, TR3–TR5).
- **Estimation of factors.** The factors of `factorization.md` are quantities of behaviours. Estimating them from finite
  records needs intervals that are not yet derived, and the factors of FA1, differences of least values, are not smooth
  in the behaviour, so their estimates may converge slowly.

## The words

- **Labels are tested on paradigm cases.** A label is verified when it agrees with its word's sense on cases registered
  before computing (L1); outside those cases a word may still mislead. Carcassi's methodology justifies what kind of
  claim a label makes, not that it is the right word (`factorization.md`).
- **Every number is relative to a declaration.** Misalignment to the request, culpability to the interface, a motive to
  a model of optimization. A report that omits the declaration it is relative to says less than it seems to.
