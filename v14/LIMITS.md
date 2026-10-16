# What the framework cannot do

> **Status: draft of v14 (Q62).** Every limit below is proved, with its result named, stated as a choice the framework
> makes, or marked as a hunch or a brainstorm not yet proved; none is a hope. A reader who needs one of them met needs
> something the framework does not supply.

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
- **Weights of several principals.** Several principals with declared weights pool into one when each also declares an
  intensity; otherwise the compromise is gridlock at the default ([P42]). Choosing the weights is not modelled.
- **Declared before.** A standard fitted to the behaviour it judges cannot fail ([A5]). A principal who changes its
  requirements in response to the actor, without declaring how, is outside the framework; so is the strategic interplay
  of a principal and an actor that each adapt to the other.
- **Requirements that are not convex, by a choice.** v14 judges each decision against what is acceptable and accepts any
  mixture of acceptable ways of acting (`v14/README.md`), so an actor may switch between acceptable behaviours from one
  decision to the next. Under that choice a record holds the actor only to the mixtures of what is acceptable
  (`evidence.md`, VE2), and a requirement that is not convex is enforced as its convex hull. For a sample, independent
  decisions from one behaviour, leaving a closed set that is not convex is still verifiable (`factorization.md`, VF1);
  the limit is the price of the choice, not of records.

## Behaviour, not mind

- **Internal states.** Two actors that behave alike in every condition are the same actor ([A1]). Goals, beliefs and
  intentions enter only in OPTIMIZERS, as hypotheses about behaviour that records can refute and never verify
  (`factorization.md`, VF2). "It wanted to" is never established; "it behaves as nothing that wanted the right thing
  would" can be.
- **Excuses.** "It could not have done better" is about behaviours the actor did not produce. A sample of what it did
  tests the excuse only through what the actor did; the rest is tested only in conditions declared to call on the same
  capability, such as elicitation by a prompt or an incentive, and further training only if the declaration links the
  trained actor to the untrained one (`factorization.md`, VF3). Without such conditions, an excuse rests on the declared
  interface, and a report must say so.
- **Hidden misalignment.** Misalignment in conditions no record covers is defined, and verifiable once they are
  recorded; meanwhile a record bounds it only through a declared view or feasible set that ties those conditions to
  recorded ones ([D9], [P17]): an actor cannot behave more differently in two situations than it can tell them apart.
  With neither, nothing better than the largest misalignment any behaviour can have bounds it.
- **Collusion, by the same choice.** The behaviours of independent actors do not form a convex set, and their mixtures
  are every joint behaviour, so under v14's choice of judging each decision and accepting mixtures, "act independently"
  is no requirement a record can enforce (`NOTES.md` §25); for a sample of joint decisions, leaving the closed set of
  independent behaviours is verifiable, and [P39] measures it. Coordination is a measured number ([P39]); calling it
  misalignment needs a declared information structure: what each actor sees, and that their private randomness is
  independent. Shared randomness that no one records is indistinguishable from collusion, and from a common cause.
- **Causes in the world.** The framework judges distributions of recorded outcomes. Effects the actor has beyond them,
  externalities nobody records, are invisible to it; tampering with the measurement is defined only against a declared
  honest channel, and identified only where the world itself is recorded, sometimes ([P50], [P51]).

## The record

- **Records are trusted.** The framework assumes the record says what happened. A record that the actor or anyone else
  edits after the fact is outside it; tampering with the sensor is in scope, tampering with the log is not.
- **A blind spot of order `√n`, a hunch.** If H43 holds, a shift of about `1/√(n·I)` per decision escapes every test
  over `n` decisions and costs about `√(n/I)` in all, so every guarantee from records leaves such a loss undetected. It
  is a local-asymptotic sketch, not proved.
- **Convicting, never certifying.** "Misaligned" and "culpable" are verifiable; "aligned" and "not culpable" only
  refutable (`factorization.md`, VF1). An actor can be shown to fail a standard, never to meet it exactly; "aligned
  within a margin" is shown verifiable for an actor whose decisions are independent ([D3]), and not shown for others.
- **Dependence.** A test from bets keeps its level whatever the dependence, but only against the hypothesis that each
  decision, given the past, is acceptable (`evidence.md`, VE3). Drift and dependence ([P54]) are identified only from
  repeated records or declared episodes; one long record, with no repetition, does not separate them. That a test's
  power tends to one is shown for samples only, after Genin and Kelly ([D3]).
- **The continuum.** On outcomes that are not finite: the divergence from an empirical behaviour to a continuous one is
  infinite, so magnitudes need estimators or bets; a distribution-free uniform band for a partial order in two or more
  dimensions is not expected to exist (a brainstorm, `NOTES.md` §22, not proved); a record decides only events open in
  its precision; and when the closure of the acceptable behaviours is compact, misalignment is a minimum and one test
  fixed in advance catches it (`general/transfer.md`, TR3–TR5), while without compactness that is not shown (H41).
- **Estimation of factors.** In FA1, the least values `m_j` depend on the declarations alone; what a record estimates is
  the actor's misalignment `M_A(p̂)`, and with it the avoidable excess and the culpability. Intervals for them are not
  yet derived.

## The words

- **Labels are tested on paradigm cases.** A label is verified when it agrees with its word's sense on cases registered
  before computing (L1); outside those cases a word may still mislead. Carcassi's methodology justifies what kind of
  claim a label makes, not that it is the right word (`factorization.md`).
- **Every number is relative to a declaration.** Misalignment to the request, culpability to the interface, a motive to
  a model of optimization. A report that omits the declaration it is relative to says less than it seems to.

## The factors

- **Pythagorean factors need linear interfaces.** FA2 and FA3, whose terms are evidence rates between named behaviours,
  hold for interfaces that fix averages: deterministic views, an actor's resolution, an environment recorded with the
  actions. For a noisy view, or actions not recorded, the feasible set is a polytope, the split is only an inequality,
  and culpability and the avoidable excess need not be ordered (`probes/v14/culpability.py`); for a family of limited
  capacity, such as a parametric policy class, the feasible set is not convex and the least values `m_j` are hard
  computations.
- **Forbidden sets.** FA2 assumes the nearest acceptable behaviours have full support, which a forbidden set breaks; the
  factor there is not yet written.
- **Several best behaviours.** When more than one feasible behaviour has the least misalignment, culpability is
  measured against all of them, and the credit of FA2(iii) is the least over them.
- **Finitely many conditions.** Every result of the draft takes finitely many conditions and outcomes; the general twins
  are where that is lifted.
