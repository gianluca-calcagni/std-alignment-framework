# Severity, and who grades

> **Status: a proposal for v14 (Q69), the executor's, not reviewed and not decided.** It proves nothing new; it cites
> VK5, VK7, VE3, VF1 and VO1, proved elsewhere. Everything else here is a definition proposed for the PI to accept,
> change or refuse.

The PI agreed that severity is a thing of its own, independent of misalignment, and asked whether it is measured in nats
too, how the two interplay when an actor is trained, and whether the principal should be the one, and the only one, who
grades (Q69). The proposal in one paragraph: severity is a scale of value the principal declares on outcomes, in its own
units, never in nats; it enters the specification as a budget or as tolerances; a report gives, for each requirement,
the verdict, the evidence in nats and the size of the breach in the principal's units; evidence moves with a budget at a
price that depends on the actor (VK7), so no constant converts one scale into the other; and only the principal declares
grades, while graders apply them and the actor never grades itself.

## Why severity is not in nats

- *Nats measure evidence; severity measures value.* Misalignment is how fast a record convicts (`evidence.md`). A
  catastrophe tolerated at `10⁻⁶` and occurring at `2·10⁻⁶` has misalignment `3.9·10⁻⁷` nats per decision; a rude
  answer tolerated at `0.1` and occurring at `0.2`, `0.044` (`NOTES.md` §24). Any number that ranked the first breach
  above the second would have to bring in how bad each outcome is, which no record of the actor contains.
- *No constant converts one into the other.* For a fixed actor and a budget on a cost, VK7 shows that loosening the
  budget by one unit removes about `λ*` nats per decision of evidence, `λ*` being the stake of the best bet; `λ*`
  varies with the actor and the budget, and rescales with the cost's units. So no constant turns units of harm into
  nats of evidence, and a sum of the two would change meaning from one actor to the next. A principal may still declare
  such a rate, as the next point does; the framework does not supply one.
- *One exception, by declaration.* A principal whose value is wealth that harm reduces multiplicatively, an investor's
  capital or a population's growth, has severity on a logarithmic scale, and its units are then nats of value. They are
  still not nats of evidence, and the two must not be added.

## What the principal declares

1. **A severity scale** `s : X → [0, ∞]`, in the principal's units: money, hours, injuries, a score. Its zero is "no
   harm". `∞` is allowed, and marks the outcomes the principal forbids: they become a forbidden set, and budgets and
   rates apply to the outcomes of finite severity.
2. Or, when only an order is known, **severity levels**: a ranking of outcomes by how bad they are, read as `order.md`
   reads any ranking. "No worse than the reference at every level of severity" is then dominance with declared margins,
   `B_m(r)` (Q74), margins `0` giving VO1's `B(r)`, with no units needed.
3. **A tolerance**, in one of two forms:
   - a budget on expected severity, `E_a[s] ≤ b`: on average, at most this much harm per decision (`constraints.md`,
     VK3);
   - or tolerances by class, derived from a declared **risk appetite** `R`: a class of outcomes, of one severity `s_k`
     (severity constant on the class, or the class's largest), may occur at rate at most `ε_k = R/s_k`, so that each
     class carries expected harm at most `R`, as a risk matrix's iso-risk lines do. These are rate limits, one per
     class, not the budget `E_a[s] ≤ R`: `m` classes together allow up to `m·R`. A class with `s_k ≤ R` gets no limit;
     a class of infinite severity gets `ε = 0`, a forbidden set.

   Each tolerance is declared per decision, judged by bets, or pooled over a declared horizon, judged by confidence
   sequences; a limit on a tail measure such as CVaR is pooled, and its breach an aggregate breach (Q74).

## What a report gives

For each requirement built from severity:

| Quantity | Units | What it says | Verification status |
|---|---|---|---|
| verdict | convict, or certify at a declared margin | the requirement is broken; or met within the margin, on average, or per decision for a sample (Q76) | convict verifiable (VF1); certify for averages and samples only |
| misalignment | nats per decision | how fast a record convicts | verifiable that it is above any `m` (VF1) |
| expected severity, `E_p̂[s]` | the principal's units per decision | how much harm the actor does on average | estimated, with an interval |
| overrun, `E_p̂[s] − b` | the principal's units per decision | how far beyond the tolerance | estimated, with an interval |
| price, `λ*` | nats per unit of severity | for a single budget that the actor breaks, how much evidence per decision one unit of tolerance removes | estimated, since it depends on the actor's behaviour (VK7) |

Severity is never folded into misalignment, and a ranking of breaches says which scale it uses: by evidence, by
overrun, or by the expected severity itself.

## Severity and misalignment in training

Training changes an actor in response to feedback (`training.md`). Two numbers steer it, and they play different roles:
- *Severity shapes the feedback.* A trainer that must keep a severity budget, and optimizes its objective at a KL price,
  produces the actor that optimizes the objective minus the severity at the budget's shadow price `ν` (VK5): severity
  enters training as a weight, in the objective's units per unit of harm.
- *Misalignment decides when to stop.* Evidence against the specification, in nats, is what a test of the trained actor
  accumulates; a conviction keeps its level whatever the dependence between decisions (VE3). Shipping needs a
  certificate, which covers an average or, per decision, only a sample of independent draws, an assumption the report
  names (Q76).
- *Their interplay needs two budgets.* A trainer that keeps the principal's own severity budget produces an actor inside
  it, so the misalignment against that budget is `0` and so is the bettor's stake `λ*`; the trainer's price `ν` and the
  bettor's `λ*` are never both positive for one actor and one budget. They meet when the trainer's budget differs from
  the principal's: another law on the world's part `ℰ`, another grader's σ-algebra, another cost. Then, for the trained
  actor held fixed, VK7 says how the evidence per decision against the principal's budget moves with the principal's
  tolerance, while changing the trainer's budget changes the actor itself, which VK7 does not cover. How `ν` and `λ*`
  relate across two such budgets is open (H50).

## Who grades

**In what forms the framework grades now.** All normative grading is in the specification, and all of it is the
principal's: which behaviours are acceptable (requirements), which outcomes are better (rankings), how much an outcome
costs (budgets), and how often an outcome may occur (rate limits). The framework itself grades nothing: it computes
evidence against what was declared. Severity, as proposed here, is one more declared function, the cost of a budget.

**Who should declare grades.** The principal, and only the principal, by definition: a misalignment is always
misalignment *to* a declared principal (`LIMITS.md`, whose alignment). A grade someone else would give, a regulator, an
affected person, an ethicist, is another principal's declaration, judged and reported separately; several principals
are pooled only with weights they declare ([P42]), and choosing the weights is outside the framework.

**Who applies grades.** A **grader**, a person, a model or an instrument, reads each outcome and assigns it to the
principal's classes. Grading is measurement: the record's σ-algebra is the grader's (`resolution.md`), and a grader's
errors are a channel between the outcome and the record (H47). A report names who declared each grade and who applied
it.

**Who never grades.** The actor, about itself, unless its self-report is a declared and audited channel: an actor that
can influence its own grades is tampering with the measurement ([P50]), whatever its reasons.

## Open

- H50: how the trainer's shadow price `ν`, for its own budget, and the bettor's stake `λ*`, for the principal's, are
  related when the two budgets differ.
- An interval for the overrun from a record, with the dependence VE3 allows, is not derived.
- Severity on a continuum of outcomes, and heavy tails of severity, where the expected severity may not exist.
