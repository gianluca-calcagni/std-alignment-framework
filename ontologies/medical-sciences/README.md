# Ontology — medical sciences: performance measures in health care

A health system judges its providers by measures: a time target in emergency departments, a report card of deaths after
surgery. The ministry or regulator is the principal; hospitals and their clinicians are the actor. A measure is an
evaluator ([D10]), introduced as an intervention ([D6]); patient welfare is the objective. Medicine records what
providers do as counts, such as attendances by time in the department or patients by treatment and severity, so
behaviour is observed as frequencies and a diagnosis is a computation. Two known results are reframed: the four-hour
target in English emergency departments, and cardiac surgery report cards.

## 1. Slots

| Slot | Core | In this discipline | Observed as | Fit |
|---|---|---|---|---|
| **outcomes** | [D1] | for the target, one attendance's time in the department, in three intervals: under 3 hours 40 minutes, the last twenty minutes, four hours or more. For the cards, one patient's treatment, cardiac surgery or not, within a severity class | attendance and discharge records | approximate: time and severity are cut into classes |
| **contexts** | [D8] | the patient's state on arrival: for the target, whether the patient will need admission, and age; for the cards, severity | clinical records | approximate: admission and the choice of patients are partly the provider's decisions, so they are not wholly given |
| **behaviour** | [D1] | the share of attendances in each interval, or of patients given each treatment in each class, per hospital and year | hospital records | exact as frequencies |
| **sample** | [D11] | one attendance, or one patient | hospital records | approximate: one department's attendances share its staff and its crowding on the day, so draws are clustered by department and day |
| **default** | [D2] | the distribution before the measure: in the target's case, the first year studied; for the cards, the pattern before them or in comparable states without them | records from before, or from comparison states | assumed: the comparison must be declared before the outcomes are read |
| **objective** | [D2] | patient welfare: timely and appropriate care, or the benefit of each treatment in each severity class | clinical outcome data | assumed: welfare is estimated, not observed |
| **evaluator** | [D10] | the measure. The target is pass or breach: two level sets, so its regression is the objective's average over passing and over breaching attendances. For the cards, what hospitals pursued before plus the card's effect `u` (the intervention slot) | the published rule | exact for the target's rule; assumed for the weight hospitals give a card. Within one severity class the two treatments score differently unless the card is indifferent between them |
| **intensity** | [D2] | how strongly providers respond: management pressure, penalties, reputation, referrals | not apart from the objective | approximate |
| **specification** | [D3] | the principal's stated aim, timely and good care, with the behaviour before the measure as the default; or, read literally, the measure itself | the policy that created the measure | assumed: which of the two is declared decides what counts as misalignment (section 3) |
| **principal's resolution** | [D4] | a target declared as such does not say when, within four hours, a patient should leave: its cells are pass and breach. For the cards, the regulator does not care which surgeon treats a patient, given the treatment | the target's definition; the programme's stated purpose | exact for the target as written; assumed for the cards |
| **actor's resolution** | [D4] | clinicians see more than the measure records: the time left before a breach, a patient's severity beyond the risk model's inputs | the gap between clinical records and the measure's inputs | assumed: this is the mechanism both known results propose |
| **change** | [P2] | the distribution, year by year, after the measure | annual records | approximate: yearly steps |
| **intervention** | [D6] | the measure, as a known function `u` of the outcome: for the target, `u = 1` on the two passing intervals and `0` on a breach; for the cards, the card's expected effect on a hospital's score, per patient: for surgery, the deaths the risk model expects minus those expected given the true severity, and nothing for no surgery | the published rule and method | exact for the target; approximate for the cards: `u` is known once true severity is estimated |
| **stakes** | [D5] | the objective's units: hours of waiting, deaths, years of life | outcome data | exact, given the objective |

## 2. Known result

England set its emergency departments a target: admit, transfer or discharge every patient within four hours of
arrival. Mason, Weber, Coster, Freeman and Locker analysed 735,588 attendances at fifteen hospital trusts, in May and
June of 2003 to 2006, with the time in the department classified into three intervals: under 3 hours 40 minutes, the
last twenty minutes before four hours, and four hours or more [@mason2012]. The share of attendances ending within four
hours rose from 83.9% to 96.3%, and after the target more patients left in the last twenty minutes before it, notably
older patients. Their title asks whether this was hitting the target but missing the point.

Dranove, Kessler, McClellan and Satterthwaite studied the cardiac surgery report cards of New York and Pennsylvania,
using Medicare patients at risk of cardiac surgery, with states without cards for comparison [@dranove2003]. The cards
led providers to select patients against the sicker ones, and improved the matching of patients to hospitals. They also
raised the use of resources and worsened outcomes, especially for sicker patients. On net, they lowered patient welfare.

**Data.** Mason et al. classified every attendance into the three intervals, for each of the four years, from the
trusts' records; their tables have not been read here. NHS England publishes monthly counts of attendances within and
beyond four hours for every trust: the evaluator's pass rate, without the split inside the passing cell. NHS England
Digital publishes annual statistics on accident and emergency activity, and a House of Commons Library briefing on A&E
statistics charts the minute at which patients leave the department, with a spike just before four hours. Dranove et al.
used Medicare records, which are not public; the New York and Pennsylvania cards themselves are published.

## 3. What the core says

For the target, write `e`, `l` and `b` for the three intervals (early, the last twenty minutes, breach), `q` for the
shares before the target and `p̂` for the shares after.

- **Consequence** of [D6], [P1]: if departments only add the target to what they pursue, with pass-through `φ`, then
  `p̂ = tilt(q, φ·u)` multiplies the early and the last-twenty-minute shares by one factor, so
  `p̂(l)/p̂(e) = q(l)/q(e)`. Any change of that ratio is a departure the target does not explain: the revealed objective
  ([P1]) gives the last twenty minutes a weight of its own, `log((p̂(l)/q(l))/(p̂(e)/q(e)))` nats beyond the target's.
- **Consequence** of [P5], [P7]: measured against the target itself, the standard specification of `F = u`, the
  misalignment of departments that pass more often than before is the within-cell departure of [P7](ii),
  `p̂(pass)·KL(p̂(·|pass)‖q(·|pass))`, computable from the three shares before and after. Under the target as declared,
  whose principal's resolution has only the cells pass and breach, the same departure is forgiven ([P7]): every
  behaviour that passes at least as often as before has misalignment `0`. "Hitting the target but missing the point" is
  exactly the departure that this resolution forgives. A principal who cares when, within the four hours, patients leave
  must declare the finer resolution.
- **Consequence** of [P19], [P20]: with welfare as the objective and the target as the evaluator, suppose that under the
  default, passing attendances are better for patients on average than breaching ones. Then the target's regression,
  which has two values, rises with it, and departments that only pursue the target cannot lower welfare on average
  ([P19]); as their pursuit grows, welfare's average moves toward its average over passing attendances under the default
  ([P20](ii)). So any harm the target does comes from changes the measure does not see: inside the passing cell, such as
  departures moved into the last twenty minutes, or inside the breach, which three intervals do not divide, such as
  longer waits once four hours have passed and leaving sooner no longer counts. The core says where to look, not what is
  there.
- **Prediction** (empirical) from [P1], [D6]: in a health system that introduces a time target, if departments only
  pursue the target, the ratio of departures in the last twenty minutes before the threshold to departures before them
  is the same before and after the target. *Refuted if* the ratio changes by more than its sampling error, in
  departments compared with themselves. A refutation shows that departments timed departures to the threshold, and the
  second consequence gives the size of that timing in nats. The English data of the known result are seen in summary:
  it reports more departures in the last twenty minutes, but the ratio has not been computed here, and a test on those
  data would be exploratory. A confirmatory test needs a system whose data have not been read.

For the cards, within one severity class `s`, a hospital operates with probability `π_s`, the card's effect is `u(s, ·)`
and the patient's benefit is `F(s, ·)`. Write `Δu_s` and `ΔF_s` for surgery minus no surgery.

- **Consequence** of [P13], [D6]: if hospitals pass the card through with pass-through `φ`, then within each severity
  class the average benefit changes at first at the rate `φ·π_s·(1 − π_s)·Δu_s·ΔF_s`, because with two options the
  covariance of [P13](i) is `π·(1 − π)` times the product of the two differences. So in each class the card helps at
  first exactly when it rewards surgery where surgery benefits the patient, and harms where the signs disagree. Across
  classes, the first-order effect is the average of these terms, weighted by how often each class occurs.
- **Consequence** of [D4], [P13]: when the risk model sees severity only coarsely, its expected deaths for a patient
  are the average over the patient's coarse class. Then, inside each coarse class, the card rewards surgery on the less
  sick (`Δu_s > 0`) and penalizes it on the sicker (`Δu_s < 0`). Where surgery benefits the sicker patients more, the
  signs of `Δu_s` and `ΔF_s` disagree for them, and the card pushes surgeons away from exactly those patients. This is
  the known result's mechanism, read as a gap between the actor's resolution and the resolution of the principal's
  measurement: the actor acts on distinctions the card does not record.
- **Prediction** (empirical) from [P12], [D6]: if hospitals only add the card to what they pursue, with one pass-through
  in every severity class, then the change of the log-odds of surgery in class `s` is `φ·Δu_s`, with the same `φ` for
  all classes. *Refuted if* the changes of log-odds across severity classes are not proportional to `Δu_s`, within
  sampling error. Within one class there are only two options, and [P12](i) has no power; the test gets its power from
  the shared `φ`, which is what the best feasible pursuit across contexts has ([P15], Notes). A refutation means the
  card did more than add `u` to what hospitals pursue, or that their response differs by class.
- **Consequence** of [P4]: a principal who sees only what a measure records sees at most the misalignment at that
  resolution ([P4](iv)). Selection on unrecorded severity is invisible in a card's own data, and timing within the
  passing cell is invisible in the target's pass rate; both show only in data at a finer resolution, such as the
  clinical records the card study used, or the time intervals of the target study.
- **Reading** with [D3]: a comparison group, states without cards or the year before a target, estimates the default:
  what would have happened with no pursuit of the measure. The core requires it to be declared apart from the behaviour
  judged, which is what a pre-specified comparison group does.

## 4. Limits

- Three intervals see little of the timing: grouping only hides misalignment ([P4](iv)), so the departure measured
  inside the passing cell is a lower bound on the departure at a finer resolution, such as minutes.
- A decision to admit a patient can be taken to stop the clock. The slots treat admission as a context, which
  understates what departments choose.
- Welfare, and a patient's benefit from surgery, are estimated, not observed; the core's verdicts about them inherit
  the errors of the estimates ([P10]).
- Attendances in one department on one day, and patients of one hospital, are not independent draws ([D11]): error bars
  that assume independence are too narrow, and should be computed by department or hospital.
- Severity is a context only in part: hospitals and cardiologists choose whom to refer and admit, so the per-class
  reading of the cards understates the choice of patients.
- Two treatments per class leave the cards' pass-through test without power class by class; it assumes one pass-through
  across classes, which [P15] shows the best feasible pursuit has, but hospitals need not respond that way.

## 5. Open questions

- Does the departure inside the passing cell carry a cost to patients, such as admissions decided in the last twenty
  minutes that a later review judges unneeded? The core locates where to measure it; the clinical records would say.
- Can the first-order formula for a card, computed from data before the card and its published risk model, predict the
  sign of its effect before it is published?
- Is a finer risk model always better for patients? The consequence above suggests that what matters is whether the
  signs of `Δu_s` and `ΔF_s` agree in every class, not the model's accuracy as such.
- A regulator answers to a government, and a department to its hospital. Do specifications compose along such chains?
