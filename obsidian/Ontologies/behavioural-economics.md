# Ontology — behavioural economics: choices under defaults and incentives

People choose among options: how much to save, whether to come on time. An employer, a regulator or an institution
wants some choices more than others and changes what people face: a fine, a matching contribution, a default option.
That institution is the principal, and the people choosing are the actor. Two known results are reframed: a default
option that changed saving, and a fine that increased the behaviour it was meant to reduce.

## 1. Slots

| Slot | Core | In this discipline | Observed as | Fit |
|---|---|---|---|---|
| **outcomes** | [[D1 — Outcomes, behaviours, divergence and tilt\|D1]] | the options of one decision: contribution rates to a retirement plan, or whether a parent arrives late | administrative records | exact for a menu of options; approximate when a continuum, such as minutes late, is cut into classes |
| **contexts** | [[D8 — Conditions, responses and views\|D8]] | the person's circumstances, fixed before they choose: age, pay, tenure | records | assumed: the analyst decides which circumstances count as given; none when a whole population is treated as one actor |
| **behaviour** | [[D1 — Outcomes, behaviours, divergence and tilt\|D1]] | how often each option is chosen, in a population or by one person over many occasions | administrative records | exact as frequencies, but a population's frequencies are not any one person's behaviour |
| **sample** | [[D11 — Sample and evidence\|D11]] | recorded decisions: one employee's enrolment and contribution rate, or one pick-up on one day | administrative records | approximate: independence fits decisions of different people better than one person's decisions on successive days, which habit links; parents at one centre may also influence each other |
| **default** | [[D2 — Pursuit of an objective\|D2]] | the choice frequencies before the change judged, in the same population or a comparable one | records from before the change | assumed: the analyst declares it. It is not the "default option" of behavioural economics: an option that everyone takes is a point mass, without full support, so the core treats a change of default option as an intervention ([[D6 — Intervention and pass-through\|D6]]) |
| **objective** | [[D2 — Pursuit of an objective\|D2]] | what the principal wants: retirement saving, punctuality, or a person's own stated intention | a stated goal or a stated intention | assumed: which objective is a person's own welfare is contested, and the core does not settle it |
| **evaluator** | [[D10 — Evaluator, regression and residual\|D10]] | what people are observed to pursue: revealed from choice frequencies; or, as a hypothesis, their earlier evaluator plus a rule added to it, such as a fine | choice frequencies before and after a change; the rule, as written | assumed: a known rule is only part of what people pursue, and the fine study shows that adding it can change the rest (section 3). A fine on lateness has two values: with minutes late cut into classes, its level set "late" groups them all |
| **intensity** | [[D2 — Pursuit of an objective\|D2]] | how strongly people pursue it: attention and deliberation | not apart from the objective | approximate: logit choice and quantal response [[References\|@mckelvey1995]] have this form, with a scale estimated from data |
| **specification** | [[D3 — Specification, declaration and misalignment\|D3]] | the principal's stated goal, and the behaviour before the change as the default | a policy document or a pre-registration | assumed |
| **principal's resolution** | [[D4 — Resolution\|D4]] | what the principal declares not to care about, such as which fund a contribution goes to | the policy document | assumed; the finest resolution unless declared |
| **actor's resolution** | [[D4 — Resolution\|D4]] | the options a person does not tell apart, such as funds they never compare | choices that never move apart, which bound it from one side only ([[P12 — What interventions reveal\|P12]](ii)) | assumed |
| **change** | [[P2 — Every change of behaviour follows a replicator equation\|P2]] | choices drifting over time, such as people leaving a default option as their tenure grows | records over periods | approximate: read from cohorts or periods |
| **intervention** | [[D6 — Intervention and pass-through\|D6]] | a fine, a matching contribution, or a new default option | the rule, as written | exact for a fine or a match, which are known functions of the option chosen; approximate for a new default option, modelled as a bonus on it, and rejected between two defaults (section 3) |
| **stakes** | [[D5 — Stakes\|D5]] | the units of the objective: money saved, minutes late | records | exact, given the objective |

## 2. Known result

Madrian and Shea studied a large US company whose retirement plan switched from enrolment on request to automatic
enrolment, in which employees are enrolled unless they opt out [[References|@madrian2001]]. Participation was much higher among
employees hired after the switch, and many of them kept both the default contribution rate and the default fund. The
authors attribute this to inertia, and to employees reading the default as advice.

Gneezy and Rustichini introduced a fine for parents who picked up their children late, in six of ten day-care centres in
Haifa, over twenty weeks [[References|@gneezy2000]]. The number of late parents increased. When the fine was removed, it stayed at
the higher level.

**Data.** Madrian and Shea report the distribution of contribution rates in each cohort in their figures. v7.10 read
them, with Choi et al.'s table and figure for three more companies and Beshears et al.'s figure for a fourth (T7-2, 2b,
2d), so these data are seen. Gneezy and Rustichini report the number of late parents in each centre and week; a public
copy is reported (`NOTES.md` §3.2, D1) and has not been verified. Field experiments in economics increasingly publish
replication files with counts per option, which is what the slots need.

## 3. What the core says

- **Consequence** of [[D6 — Intervention and pass-through|D6]], [[P1 — Every behaviour is a tilt of any other|P1]]: the fine. With two outcomes, late or on time, every change of behaviour passes the
  fine through ([[P12 — What interventions reveal|P12]] Notes), so the rise in lateness is a negative pass-through, `φ < 0`, for the fine
  `u = −c·[late]`. Removing the fine is the intervention `−u`. A parent who kept their objective, default and
  intensity, and only added the fine to what they pursue, would pass the removal through with the same `φ`, and by
  [[P1 — Every behaviour is a tilt of any other|P1]](iii) return to their behaviour before the fine. The reported persistence means the removal was passed through
  with `φ` close to `0`. So no fixed actor that adds the fine to what it pursues fits both changes: the fine changed the
  parents, either what they pursue or what they do by default. This is the core's form of "a fine is a price", and it
  needs only the two-outcome counts that were reported. Two outcomes cannot tell which of the two changed.
- **Prediction** (empirical) from [[P12 — What interventions reveal|P12]], [[D6 — Intervention and pass-through|D6]]: automatic enrolment. Moving the default option from not participating to
  a default rate `d` removes the effort of acting for those who take `d`, and adds it for those who stay out. If that is
  all it does, it is the intervention `u = 1_d − 1_0`, a bonus on the new default option and a penalty on the old one.
  If people only added it to what they pursue, every other contribution rate would keep its share relative to every
  other: for example, the ratio of employees at 6% to employees at 10% would be the same in both cohorts. *Refuted if*
  those ratios differ by more than their sampling error, in cohorts comparable in tenure and pay. A refutation shows
  that the default did more than favour one option, for example by pulling nearby rates toward it as advice would. The
  test needs the full distribution of contribution rates in both cohorts. *Tested in v7.10, before this ontology was
  written* (T7-2, T7-2b, T7-2d; data read from published tables and figures, without sampling errors, so a registered
  tolerance `log 1.5` stood in for them). Against enrolment on request it held loosely. T7-2's registered test pooled
  two companies and held (median `|δ|` 0.265, where `δ` is the difference of the log-ratios of the two non-default
  categories), though one of them, taken alone, exceeds the tolerance (0.454, computed from the same table, not
  registered). Of two further companies, Madrian and Shea's was within it (0.271) and the other was not (0.876, on a
  cell of very few employees). Between two automatic-enrolment defaults, 3% and 6% in one company (Beshears, Choi,
  Laibson and Madrian, NBER w12009), it failed: the log-ratios of the other rates were `+0.65`, `+1.83`, `−0.27`,
  `−0.05` and `−0.56`, and the higher default moved some employees down. **Refuted in its two-default form.** Every one
  of these datasets has been seen, so a further test on them is exploratory; a confirmatory test needs a company not yet
  used.
- **Consequence** of [[P13 — What the start of a change gains|P13]]: if the new default is passed through, which the two-default data above reject, the average
  of any objective `F`, such as savings at retirement, changes at first at the rate
  `Cov_p(u, F) = p(d)·(F(d) − E_p[F]) + p(0)·(E_p[F] − F(0))` per unit of pass-through, where `p` is the behaviour
  before the switch. The second term is the gain from enrolling people who were not saving. The first is a loss when the
  default rate is worth less than the current average, because the switch also draws people away from higher rates. The
  sign of the sum can be computed before the switch, from the behaviour before it and a declared `F`: a check on the
  choice of the default rate.
- **Reading** with [[D4 — Resolution|D4]], [[P8 — An actor that cannot tell outcomes apart|P8]]: keeping the default fund. A person who does not tell the funds apart is limited, inside
  the cell "contributes at rate `x`", to the default's split among funds: inside an actor's cells, the default decides
  ([[D4 — Resolution|D4]]). The plan's default allocation, all in one fund, is a point mass; the reading holds in the limit of a default
  that puts almost all of each cell's mass on that fund. Under an objective that cares about funds, such a person is
  then charged the Jensen gap of [[P8 — An actor that cannot tell outcomes apart|P8]](iii), which no effort spent on the contribution rate removes.

## 4. Limits

- A population's choice frequencies are treated as one behaviour. Claims about individuals need data on individuals.
- The core's tests need comparable groups before and after a change, which field data provide only in part.
- With two outcomes, [[P12 — What interventions reveal|P12]](i) has no power. The fine study counts late parents, so only the pair of changes, the fine
  and its removal, carries information.
- The fine study's counts are weekly counts of late parents in ten centres: few samples, and not independent if
  lateness is a habit. Error bars that assume independent draws ([[D11 — Sample and evidence|D11]], [[P23 — The estimated misalignment of an actor that pursues the objective|P23]]) are then too narrow.
- Which objective is a person's own welfare is contested. The core needs one to be declared, and does not choose it.
- The default option of behavioural economics is not the core's default; the two must not be confused.
- A new default option is not a known bonus on it ([[D6 — Intervention and pass-through|D6]]): the two-default test of section 3 rejects that model, while a
  fine or a match is a known function of the option chosen. The rejection bears on defaults, not on explicit incentives
  such as the fine here or the measures of the medical-sciences ontology.

## 5. Open questions

- Can a person be their own principal, with a stated intention as the specification and the gap between intention and
  behaviour as misalignment?
- Is the drift away from a default option with tenure the pursuit of one fixed objective? [[P3 — A fixed objective is visible in the changes of behaviour|P3]] tests this on panel
  data.
- Across circumstances (contexts), [[P15 — Misalignment splits into what the actor could avoid and what it could not|P15]] takes the best feasible pursuit to share one intensity. Is the response to a
  default consistent across ages and pay levels, or is part of it avoidable inconsistency?
