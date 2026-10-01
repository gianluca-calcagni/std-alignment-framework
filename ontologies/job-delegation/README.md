# Ontology — job delegation from a manager to an employee

A manager asks an employee to do some work. The manager is the principal and the employee is the actor. The manager's
brief is the specification. A bonus, a target or a new template is an intervention. This ontology reframes a classic
lesson about incentives at work, "you get what you reward", and says what the core adds to it.

A running example is used throughout. One unit of the employee's time ends as one of four outcomes: a report written
carefully, a report rushed, an unmeasured task such as helping a colleague, and other work. The employee's current
practice is `p = (0.2, 0.1, 0.3, 0.4)`. Reports are counted, so the manager can pay per report, and a rushed report
takes half the time of a careful one. The manager values the four outcomes at `F = (2, 0.5, 1.5, 0)`, so
`E_p[F] = 0.9`.

## 1. Slots

| Slot | Core | In this discipline | Observed as | Fit |
|---|---|---|---|---|
| **outcomes** | [D1] | what one unit of the employee's time ends as: a task, and the way it is done | time sheets, task logs, audits of samples of work | approximate: time and quality are cut into a few classes |
| **contexts** | [D8] | the requests that arrive (which client, which kind of task), when the employee does not choose them | the request log | assumed: the manager decides which parts of an outcome count as given; none when the employee chooses their own work |
| **behaviour** | [D1] | the employee's allocation: how often each outcome occurs over their units of work in a period | the same logs, over a period | exact as a frequency, but one employee gives few units, so it is estimated with error |
| **sample** | [D11] | units of the employee's time, each logged as one outcome | time sheets, task logs, audits of sampled work | approximate: successive units of one person's time depend on each other (a task started is finished), so independence is a model; an audit draws units, and should draw them at random |
| **default** | [D2] | the employee's current practice: what they do before the brief or the change being judged | logs from a period before the brief | assumed: the manager declares it. Current practice was itself shaped by past incentives. An outcome never seen in that period needs a declared small mass, for full support |
| **objective** | [D2] | the manager's value of each outcome, for the team or the firm | values written in the brief | assumed: the manager states it, which in practice is rare |
| **evaluator** | [D10] | the measure the employee is paid on: an indicator `1_A`, or pay per report `u = (1, 2, 0, 0)` in the running example; otherwise revealed from the allocation | the bonus rule, as written | exact for the rule. An indicator has two level sets, `A` and the rest; pay per report has three, careful reports, rushed reports, and the unpaid outcomes together |
| **intensity** | [D2] | how hard the employee pursues what is asked, against the cost of changing their practice | never apart from the objective: only the product is identified | approximate: the cost of changing practice is modelled as KL ([P4]); contract theory usually uses other effort costs |
| **specification** | [D3] | the brief: the current practice, and "do more of what I value, at the pace you can" | the written brief, dated before the period judged | exact when the brief is written beforehand; a brief reconstructed afterwards breaks the rule of use of [D3] |
| **principal's resolution** | [D4] | what the manager declares not to care about: "I don't care how, as long as it is done well" groups the ways of reaching one deliverable | the brief | assumed; the finest resolution when the brief says nothing |
| **actor's resolution** | [D4] | what the employee cannot tell apart, such as which clients matter most, or which errors a customer notices | interviews, or changes of behaviour that separate outcomes ([P12](ii)) | assumed; identifiable from behaviour from one side only |
| **change** | [P2] | learning, feedback, a new target: the allocation moving from period to period | logs over consecutive periods | approximate: periods are discrete, and the revealed objective is read from successive allocations |
| **intervention** | [D6] | a bonus on a measured indicator, a target, or a new default such as a template or the order of a queue | the bonus rule, as written | exact when the rule is a known function of the outcome |
| **stakes** | [D5] | the manager's value, in money or in the units of the brief | the brief's values | exact, given the objective |

## 2. Known result

Kerr observed that organizations often reward one behaviour while hoping for another, and then get what they reward
[@kerr1975]. Holmström and Milgrom gave the observation a model [@holmstrom1991]: when an employee divides effort among
tasks and only some are measured, paying for the measured tasks draws effort away from the others. When the unmeasured
tasks matter enough, the best contract pays only weakly for the measured ones, or pays a fixed wage. Their model has a
risk-averse employee, an effort cost, and a cost of paying the bonus. Two further results frame the claims below. Any
signal that is informative about what the employee did has value in a contract, which is Holmström's informativeness
principle [@holmstrom1979]. External rewards can crowd out an employee's own motivation, and sometimes crowd it in
[@frey2001].

## 3. What the core says

In this section, `p` is the employee's practice, which is also the declared default, `F` is the manager's value, and the
bonus pays on a measured indicator `u`. The employee passes the bonus through with pass-through `φ` ([D6]).

- **Consequence** of [D6], [P1]: a bonus on a set `A` of measured outcomes, `u = 1_A`, passed through with `φ > 0`,
  multiplies the mass of every outcome in `A` by one factor, `e^φ/Z`, and the mass of every outcome outside `A` by
  another, `1/Z`, with `Z = E_p[e^{φ·u}] > 1`. Every unmeasured task loses the same share of its time. This is the
  substitution of effort that Holmström and Milgrom derive, in its simplest form, and its proportional form can be
  tested
  (the prediction below).
- **Consequence** of [P13]: at the start, the manager's average value moves at the rate
  `Cov_p(u, F) = p(A)·(E_p[F|A] − E_p[F])` per unit of pass-through. So rewarding `A` helps at first exactly when the
  rewarded outcomes are worth more, to the manager, than the employee's current average. Kerr's folly is the case
  `E_p[F|A] < E_p[F]`: the rewarded outcomes are worth less than what the employee already does on average. In the
  running example, a bonus that only a rushed report earns has `E_p[F|A] = 0.5 < 0.9`.
- **Consequence** of [P18], [P20]: a bonus on an indicator has no best size in between. The indicator `1_A` has two
  level sets, and a behaviour that follows it keeps the splits inside `A` and outside it ([P18](i)), so the manager's
  average is `p_φ(A)·E_p[F|A] + (1 − p_φ(A))·E_p[F|not A]`, which is monotone in `φ`: the best bonus is either none or
  the largest. A bonus on a graded measure is different. In the running example, pay per report gives the measure
  `u = (1, 2, 0, 0)` per unit of time, since a rushed report takes half the time. Its regression ([D10]) is `0.5` on
  rushed reports, `2` on careful ones and `0.45/0.7 ≈ 0.64` on the unpaid outcomes: it falls at the top. The manager's
  average rises from `0.9` to about `0.97` at `φ ≈ 0.79`, and then falls toward `0.5`, the regression at the measure's
  top value ([P20](ii)). The peak is where `Cov_{p_φ}(u, F) = 0` ([P20](i)): where the measure and the manager's value
  become uncorrelated under the behaviour that the bonus itself induces. So the core gives a reason for weak incentives
  with no risk aversion and no cost of pay: the measure stops tracking the value as the employee follows it.
- **Consequence** of [P11], [P8]: measured against the brief, the share of the employee's first response to a bonus
  `1_A` that is misaligned is `sin²θ`, with `cos θ` the correlation of `1_A` and `F` under `p`. When the rewarded
  outcomes are worth more than the rest, this share is the part of the variance of `F` that lies inside `A` and inside
  its complement, the part the indicator cannot see. The response to the bonus is limited to the resolution
  `{A, not A}` ([P8](i)), and the share is the small-effort share of [P8](iv).
- **Prediction** from [P12], [D6]: if the employee only adds the bonus to what they pursue, the ratios among the
  outcomes outside `A` do not change. In the running example, with pay for careful reports only, the ratio of helping a
  colleague to other work stays fixed. *Refuted if* those ratios move by more than their sampling error. The test needs
  at least two unmeasured outcomes. A refutation shows that the bonus changed more than what is paid: the employee's
  own objective, as in crowding out [@frey2001], or other things that came with it, such as closer monitoring.
- **Consequence** of [D6], [P1]: behaviour identifies only `φ = t·w`, the product of how hard the employee pursues and
  how much they value the bonus. No record of behaviour tells a weakly motivated employee who values money from a
  motivated employee who does not.
- **Consequence** of [P8]: an employee who cannot tell apart outcomes that the manager values differently, such as two
  clients of unequal importance, pursues at best the average of the manager's value over what they can tell apart
  ([P8](ii)). Unless the employee can see all of the variation of `F`, or none of it, they are misaligned at every
  effort ([P8](iv)). More effort does not remove this; telling the employee the distinction does, by refining their
  resolution. The part no effort can remove is the Jensen gap of [P8](iii).
- **Consequence** of [D4], [P7]: a manager who declares "I don't care how" forgives exactly the departure that happens
  within each deliverable ([P7](ii)). A brief that declares nothing is read at the finest resolution, so a change of
  method counts as departure that the brief must explain. A brief is complete only when it says what the manager does
  not care about.
- **Reading** with [P4]: a manager who sees only coarse records, such as counts per category, sees at most the
  misalignment at that resolution, which is never more than the misalignment at the finest one ([P4](iv)). This runs
  parallel to the informativeness principle [@holmstrom1979]: a finer record never hides more. The two are different
  statements, one about detection and one about the value of a contract.
- **Consequence** of [P24], [D11]: an audit that samples kinds of request in other proportions than they arrive
  measures a different misalignment. When the brief judges each kind of request on its own terms, the difference is
  the evaluation gap `Γ`, each kind's misalignment weighted by how much more often it arrives than it is audited. An
  audit that over-samples the kinds of request where the employee is closest to the brief understates their
  misalignment. When the brief asks for one pace across kinds, `Γ` does not apply, and both misalignments must be
  computed ([P24], Notes).

## 4. Limits

- The core has no wages, no risk aversion, no participation constraint and no career concerns. Holmström and Milgrom's
  conclusions about the best contract use all of these. The core recovers the substitution of effort, and a reason for
  weak incentives, but not their contract.
- The cost of changing one's practice is modelled as KL. Agreement with known qualitative results does not test that
  model; the prediction above, and the pursuit test of [P3] across bonuses of different sizes, do.
- The default is the employee's current practice, which past incentives shaped. "No pursuit" means "nothing new asked".
- One employee works few units in a period, so allocations are estimated with error. [P23] gives the law of the
  estimated misalignment for independent units ([D11]); units of one person's time are not independent, so its error
  bars are too narrow.
- Requests that the employee does not choose are contexts. The claims above hold within one kind of request; across
  kinds, [P15] separates avoidable from unavoidable misalignment (see Contexts in `../README.md`).
- The core needs the manager's values written down before the work is judged. Without them, it gives no verdict.

## 5. Open questions

- Chains of delegation. A manager is also someone's employee. Does misalignment compose along a chain, and does a gap in
  resolution at one link transmit to the next (main: the transmission gap, G2)?
- One pace across kinds of request. By [P15], the best feasible pursuit keeps one intensity across contexts, so an
  employee who works hard for one client and not at all for another is charged the difference as avoidable
  misalignment. Is that what managers mean by "do more of what I value"?
- Teams. With several employees sharing outcomes, the behaviour judged is joint; the core has no item for it.
- Crowding in. The prediction above detects a change of objective, but not its sign: crowding out and crowding in both
  show as ratios that move.
