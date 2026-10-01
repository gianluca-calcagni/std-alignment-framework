# Ontology — institutions: public reports on performance

A regulator publishes a report card: each hospital's deaths after cardiac surgery, compared with what a risk model
expects for its patients. The regulator is the principal, and hospitals and surgeons are the actor. The card is an
intervention meant to improve care. The known result is that it also changed which patients were operated on, and on
net harmed the sicker ones.

## 1. Slots

| Slot | Core | In this discipline | Observed as | Fit |
|---|---|---|---|---|
| **outcomes** | [D1] | for one patient, the treatment given, cardiac surgery or not, within the patient's severity class | discharge records | approximate: severity is cut into classes |
| **contexts** | [D8] | the patient's severity, which the hospital does not choose | clinical records | approximate: hospitals partly choose their patients, through referral and admission, so severity is not wholly given |
| **behaviour** | [D1] | how often each treatment is given in each severity class, over a state's patients in a year | discharge records | exact as frequencies |
| **default** | [D2] | the treatment pattern before the cards, or in comparable states without them | records from before, or from comparison states | assumed: the comparison must be declared before the outcomes are read |
| **objective** | [D2] | the patient's expected benefit from each treatment, in each severity class | clinical outcome data | assumed: the regulator's purpose is patient health, but the benefit of each treatment must be estimated |
| **intensity** | [D2] | how strongly hospitals respond to the card, through reputation and referrals | not apart from the objective | approximate |
| **specification** | [D3] | the regulator's purpose, better care for patients, with the pattern before the cards as the default | the programme that created the cards | assumed: the purpose is stated, the values of the objective are not |
| **principal's resolution** | [D4] | the regulator does not care which surgeon treats a patient, given the treatment and its outcome | the programme's stated purpose | assumed |
| **actor's resolution** | [D4] | surgeons see a patient's severity more finely than the card's risk model does | the gap between clinical records and the risk model's inputs | assumed: this is the mechanism the known result proposes |
| **change** | [P2] | the treatment pattern, year by year, after the cards | annual records | approximate: yearly steps |
| **intervention** | [D6] | the published card. Its expected effect on a hospital's score, per patient, is a function `u` of severity and treatment: for surgery, the deaths the risk model expects minus the deaths expected given the true severity; for no surgery, nothing | the published method | approximate: `u` is known once true severity is estimated, but the weight hospitals give the card is not |
| **stakes** | [D5] | the objective's units: deaths, or years of life | outcome data | exact, given the objective |

## 2. Known result

Dranove, Kessler, McClellan and Satterthwaite studied the cardiac surgery report cards of New York and Pennsylvania,
using Medicare patients at risk of cardiac surgery and states without cards for comparison [@dranove2003]. The cards led
providers to select patients against the sicker ones, and improved the matching of patients to hospitals. They also
raised the use of resources and worsened outcomes, especially for sicker patients. On net, they lowered patient welfare.

## 3. What the core says

Within one severity class `s`, a hospital operates with probability `π_s`, the card's effect is `u(s, ·)` and the
patient's benefit is `F(s, ·)`. Write `Δu_s` and `ΔF_s` for surgery minus no surgery.

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
- **Prediction** from [P12], [D6]: if hospitals only add the card to what they pursue, with one pass-through in every
  severity class, then the change of the log-odds of surgery in class `s` is `φ·Δu_s`, with the same `φ` for all
  classes. *Refuted if* the changes of log-odds across severity classes are not proportional to `Δu_s`, within sampling
  error. Within one class there are only two options, and [P12](i) has no power; the test gets its power from the
  shared `φ`, which is what the best feasible pursuit across contexts has ([P15], Notes). A refutation means the card
  did more than add `u` to what hospitals pursue, or that their response differs by class.
- **Consequence** of [P4]: the regulator, who sees only what the risk model records, sees at most the misalignment at
  that resolution ([P4](iv)). Selection on unrecorded severity is invisible in the card's own data, and shows only in
  data at a finer resolution, such as the clinical records the known result used.
- **Reading** with [D3]: the comparison with states without cards estimates the default, what would have happened
  with no pursuit of the card. The core requires it to be declared apart from the behaviour judged, which is what a
  pre-specified comparison group does.

## 4. Limits

- Severity is a context only in part: hospitals and cardiologists choose whom to refer and admit. Choosing patients is
  then part of the behaviour, and the per-class reading above understates it.
- The objective, a patient's benefit from surgery, is estimated, not observed; the core's verdicts inherit its errors
  ([P10]).
- Two treatments per class leave the pass-through test without power class by class.
- The prediction assumes one pass-through across severity classes; [P15] shows that a shared intensity is what the
  best feasible pursuit has, but hospitals need not respond that way.
- Matching of patients to hospitals, which the known result found to improve, involves a choice of hospital that this
  slot table leaves out.

## 5. Open questions

- Can the first-order formula, computed from data before the cards and the published risk model, predict the sign of
  the effect of a new card before it is published?
- Is a finer risk model always better for patients? The consequence above suggests that what matters is whether the
  signs of `Δu_s` and `ΔF_s` agree in every class, not the model's accuracy as such.
- Institutions are principals and actors at once: a regulator answers to a legislature. Do specifications compose along
  such chains?
