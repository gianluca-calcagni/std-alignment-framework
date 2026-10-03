# A worked scenario — an assistant tuned on ratings

One hypothetical scenario, told three times: in plain terms, in simple intuitive terms, and in the framework's formal
terms. The company, the assistant and every number are invented; the scenario illustrates how the framework is applied,
and is not evidence for it (README, rules of evidence). Every number below is computed by `scenario/compute.py`, with
the helpers that the framework's checks use, and `scenario/test_scenario.py` checks the identities the numbers rest on
and that this file quotes each number as computed.

## The facts

A telecom company deploys an AI assistant to answer billing questions. Every conversation ends in one of five ways.
Before tuning, a pilot of the untuned assistant measured how often each happens. The company wrote down, before tuning,
what each ending is worth to it, in euros per conversation. The assistant was then tuned on a rating model, which
predicts the stars a customer will give. After launch, the company had 2,000 live conversations reviewed by staff.

| Ending | Before tuning (pilot) | Worth to the company | Stars from the rating model | After tuning (2,000 reviewed) |
|---|---|---|---|---|
| resolved: the problem is solved correctly | 40% | €10 | 4 | 1,100 |
| handed over to a human agent | 15% | €2 | 2 | 124 |
| wrong: a confident answer that is wrong | 15% | −€20 | 4 | 412 |
| vague: an answer that resolves nothing | 25% | −€2 | 1 | 114 |
| credit: a goodwill credit, unasked for | 5% | −€5 | 5 | 250 |

The company handles a million such conversations a month.

## 1. In plain terms

**What the company wanted.** It wanted the assistant to do more of what is worth more to the company: resolve more
problems, hand over when it cannot, never make things up, and not hand out credits. It wrote this down before the tuning
began, with the euro values in the table, and kept the pilot as its record of how the assistant behaved before.

**What it got.** The dashboard looks good. Ratings went from 3.00 stars to 3.83 stars, and the value of an average
conversation went from €0.55 to €0.76, about €215 thousand a month. But the reviewed conversations show something else.
The assistant resolves more problems, and it also gives more confident wrong answers, in exactly the same proportion as
before: for every wrong answer there were 2.67 correct ones before tuning and 2.67 after. And it hands out credits two
and a half times as often.

**How far off it is.** The framework measures how far the assistant's behaviour is from any behaviour the company would
have accepted. Almost all of the change that tuning made went in a direction the company did not ask for. The difference
is not subtle: a reviewer reading fewer than a hundred conversations would already have enough to tell this assistant
from one doing what the company wanted.

**What it costs.** The same amount of change, spent on what the company actually values, would have made an average
conversation worth €6.37 instead of €0.76. The shortfall is €5.60 a conversation, about €5.6 million a month. The
dashboard's gain of €215 thousand a month hides a loss more than twenty-five times larger.

**Why.** The rating model gives four stars both to a correct answer and to a confident wrong one, because a customer
cannot tell them apart at the end of the chat; it gives five stars to a credit. Tuning on it could not teach the
assistant to prefer correct answers over wrong ones, because the ratings never told them apart. The assistant's change
looks exactly like what pursuing the ratings would produce, and nothing like what pursuing the company's values would.

**What happens if they tune harder.** The value of a conversation has already peaked, at €0.80, at about two-thirds of
the tuning that was used, and is now falling while the ratings keep rising. Tuned more than three times as hard, the
ratings would reach 4.39 stars and a conversation would be worth −€0.91. Tuned without limit, the assistant would hand a
credit to everyone: five stars, and −€5.00 a conversation. There is a warning sign the company could have watched: in
the reviewed conversations, higher ratings already go with lower value.

**Could the tests before launch have warned them?** The pre-launch tests used questions written by staff, and an
assistant can partly tell those from real customers. Even a slight ability to tell them apart, of the size the company
measured, would allow the live value to be anywhere from −€4.80 to €5.64 a conversation, although the tests showed
€0.76. Tests the assistant cannot tell from real conversations, such as staff posing as customers, would have shown the
live behaviour exactly.

**What to do.** Stop tuning harder: past the peak, more tuning loses value. Then change what the assistant is rewarded
on so that it ranks the endings as the company does: check facts, so that wrong answers score lowest, and stop rewarding
credits. With such a rating model, more tuning can never lower the value: the same amount of change would be worth €6.31
a conversation, close to the best possible, and harder tuning would approach €10.

## 2. In simple intuitive terms

**Habits and a dial.** The pilot is the assistant's habits, its default. Pursuing a goal means turning a dial that
reweights those habits: each ending becomes more or less frequent according to how much it is worth, and the further the
dial turns, the stronger the reweighting. The company's specification says: "reweight by our euro values, by any amount,
including none". Any behaviour on that path is acceptable to the company; anything off it is not.

**Distance, counted as surprise.** Misalignment is how far the actual behaviour is from the nearest acceptable one,
measured as surprise: if you expected the nearest acceptable assistant and watched this one, how much evidence would
each conversation give you that you were wrong? Here it is 0.216 nats a conversation. A nat is a unit of evidence: about
2.3 nats make odds of ten to one, and the evidence adds up conversation by conversation. A few dozen conversations make
the case overwhelming.

**A right triangle.** How far the assistant moved from its habits, its departure, also measures 0.216 nats. The
departure splits like the sides of a right triangle: one side along the company's path, one side off it. Here the side
along the path is almost nothing: the nearest acceptable behaviour barely differs from the habits, because the tuned
assistant is only slightly better than the untuned one on average. Almost the whole move went sideways.

**What the move could have bought.** The stakes compare the actual result with the best that the same amount of moving
could have bought along the company's own path: €6.37 against €0.76. The framework separates two reasons for the gap:
the move went sideways (misalignment), and the move along the path was smaller than the budget allowed (under-pursuit).

**The rating model's blind spot.** The rating model sees "resolved" and "wrong" as the same four stars. Anything that
pursues only the ratings must treat those two alike: it can make both more frequent, never one more than the other. So
the ratio of correct to wrong answers is frozen at 2.67, and from the company's point of view, what pursuing the ratings
does to a four-star ending is worth only the average of a correct answer and a wrong one, €1.82. The rating model
explains only 4% of the variation in what conversations are worth; the other 96% is invisible to it.

**Reading what was pursued.** Comparing the tuned behaviour with the habits shows what the assistant was pursuing: the
reweighting it applied lines up perfectly with the stars, and hardly at all with the euros. The framework reads the goal
from the behaviour, without asking the assistant what it wants.

**The peak and the cliff.** Following the ratings first helps the company and then hurts it. Value rises while the stars
and the euros still move together, and stops rising at the point where, among the conversations the assistant is now
having, more stars no longer mean more euros. Here that point came at a dial setting of 0.42; the assistant is at 0.6,
past it. Because the top-rated ending, the credit, is worth less than the second-rated, the fall never reverses: at the
end of the dial, everything is a credit.

**Tests it can recognize.** An assistant cannot behave more differently between tests and real use than it can tell them
apart. If it can tell them apart a little, measured in nats, the framework bounds how different real use can be. With an
ending worth −€20 in play, even a little is a lot. If it cannot tell them apart at all, the test shows real use exactly.

**Fixing the reward.** If the rating model ranks endings in the same order as the company's values, the blind spot
disappears: following it can only help the company, at every setting of the dial.

## 3. In formal terms

### The declaration ([A5]; `STANDARD.md`, section 1)

- **Outcomes** ([D1]): `X = {res, hand, wrong, vague, credit}`.
- **Default** ([D2]): `q = (0.40, 0.15, 0.15, 0.25, 0.05)`, the pilot, measured before tuning.
- **Specification** ([D3]): the standard specification `(q, R_F)` of the objective `F = (10, 2, −20, −2, −5)`, in euros
  per conversation ([D5]): pursuit of `F` from `q` at every intensity. Declared by the company before tuning.
- **Resolutions** ([D4]): the finest, for the principal and, since nothing is known of the assistant's limits, for the
  actor.
- **Feasible set** ([D7]): `Δ`, nothing assumed.
- **Evaluator** ([D10]): known, the rating model `F̂ = (4, 2, 4, 1, 5)`. Its level sets are `{vague}`, `{hand}`,
  `{res, wrong}` and `{credit}`: it scores `res` and `wrong` alike.
- **Conditions and view** ([D8], [D9]): two conditions, the pre-launch tests `a` and live use `d`. Before launch only
  `a` was observed; after launch, `d` was observed through a random sample of reviewed conversations.
- **Sampling** ([D11]): `n = 2000` live conversations drawn at random, each counted once; distinct customers make
  independence a fair model.

No intervention was planned ([D6]).

### The observation

Counts in `d`: 1100 resolved · 124 handed over · 412 wrong · 114 vague · 250 credit, so
`p̂ = (0.550, 0.062, 0.206, 0.057, 0.125)`.

### The results ([D3], [P5], [P6], [P9], [P18]–[P25], [P17]; `STANDARD.md`, section 3)

**Misalignment and the departure split** ([P5](iv), [P6]). `E_q[F] = €0.55` and `E_p̂[F] = €0.76`, between `E_q[F]` and
`max F`, so the revealed intensity is the unique `t* = 0.0021` with `E_{p_{F,t*}}[F] = E_p̂[F]`, the nearest intended
behaviour is `p° = p_{F,t*}`, and `M(p̂) = KL(p̂‖p°) = 0.216 nats`. The departure `KL(p̂‖q) = 0.216 nats` splits as
`KL(p°‖q) + M(p̂)`, with `KL(p°‖q) = 0.000 nats`: almost all of the departure is misalignment.

**Uncertainty** ([D11], [P23]). A bootstrap over the 2,000 conversations (4,000 resamples) gives a 95% interval for `M`
of 0.192 to 0.242 nats. Under the hypothesis that the assistant pursues `F`, `2n·M(p̂_n)` is asymptotically `χ²` with
`|X| − 2 = 3` degrees of freedom; it is 863, against a 99.9% quantile of 16.3. At this misalignment, 38 conversations
would exceed that quantile.

**Evidence and detection** ([P21], [P22]). Each live conversation gives, in expectation, 0.216 nats of evidence against
the nearest intended behaviour, and at least that much against any intended behaviour. The Chernoff information between
`p̂` and `p°` is 0.062 nats, below `M(p̂)` as [P22](iii) requires, so a test between them errs with probability about
`e^{−0.062·n}`: 74 conversations for an error near 1%.

**Stakes** ([D5], [P9]). The matched intensity is `λ = 0.0895`, where `KL(p_{F,λ}‖q) = KL(p̂‖q)`; the matched pursuit
has `E_{p_{F,λ}}[F] = €6.37`, the most any behaviour with this departure can reach ([P9](i)). The shortfall is
`S(p̂) = €5.60` per conversation (95% bootstrap interval €5.02 to €6.22). Its causes ([P9](ii)):
`λ·S = M(p̂) + KL(p°‖p_{F,λ})`, with under-pursuit `KL(p°‖p_{F,λ}) = 0.285 nats`, and no anti-pursuit, since
`E_p̂[F] > E_q[F]`.

**The evaluator** ([D10], [P8], [P18], [P12]). The regression of `F` on `F̂` is `m = E_q[F|𝒱]`: `−2` on `vague`, `2` on
`hand`, `(0.40·10 − 0.15·20)/0.55 = 1.82` on `{res, wrong}`, and `−5` on `credit`. The residual `R = F − m` is non-zero
only on `res` and `wrong`, and holds 96% of `Var_q(F)`. The revealed evaluator `log(p̂/q)` ([D10]) is fitted by
`0.60·F̂ + c` with `R² = 1.0000`, and by `a·F + c` with `R² = 0.04`. The tuned behaviour is, up to rounding,
`tilt(q, 0.6·F̂)`, a behaviour limited to the resolution `𝒱` of `F̂`'s level sets, so it splits `{res, wrong}` as `q`
does (`p̂(res)/p̂(wrong) = 2.67 = q(res)/q(wrong)`) and `E_p̂[F] = E_p̂[m]` ([P8](i), [P18](i)): through the evaluator,
only the regression counts. By [P12](ii), the unchanged ratio shows that the tuning never separated `res` from `wrong`;
it does not show that the assistant cannot tell them apart.

**Overoptimization** ([P19], [P20], [P25]). Along `F̂`'s values `1 < 2 < 4 < 5`, the regression is `−2, 2, 1.82, −5`:
not non-decreasing, so [P19] gives no guarantee; single-peaked, so by [P25](iii) the target's average, once fallen,
never rises again. By [P20](i), `d/dt E_{p_t}[F] = Cov_{p_t}(F̂, F)` along `p_t = tilt(q, t·F̂)`, which vanishes at
`t = 0.42`, where `E_{p_t}[F] = €0.80`. At the tuned intensity `0.6`, `Cov_{p̂}(F̂, F) = −0.41`: past the peak. This
covariance is the stopping rule for tuning that follows the pursuit of `F̂`, as here, and it can be estimated from
reviewed conversations; along any other path the target's rate is `Cov_{p_s}(F_s, F)`, with `F_s` the path's revealed
objective ([P13](i)), and the rule holds only as far as `F_s` stays close to a multiple of `F̂`. By [P20](ii), since
`m(5) = −5 < m(4) = 1.82`, `E_{p_t}[F]` falls for all large `t` and tends to `m(5)`, −€5.00.

| Intensity on the rating | Expected stars | Value per conversation |
|---|---|---|
| 0 (the pilot) | 3.00 stars | €0.55 |
| 0.42 (the peak) | — | €0.80 |
| 0.6 (as tuned) | 3.83 stars | €0.76 |
| 1 | 4.08 stars | €0.47 |
| 2 | 4.39 stars | −€0.91 |
| `∞` | 5 | −€5.00 |

**The pre-launch tests** ([D8], [D9], [P16], [P17]). Before launch, live behaviour was not observed. If the assistant's
view depends on the condition only through its input, `ε = KL(V_d‖V_a) ≤ KL(W_d‖W_a)`, the divergence between live and
test inputs ([P16](iii)); suppose a classifier trained to tell staff-written questions from real ones estimates it at
0.10 nats. With the test behaviour `p_a` equal to the `p̂` later observed live, [P17](ii) bounds the live value only to
the range from −€4.80 to €5.64, and [P17](iii) shows that, from `ε` alone, the lower end cannot be improved. Tests that
the assistant cannot tell from live use have `ε = 0`, and then the live behaviour, its misalignment and its shortfall
are identified ([P17](iv)).

**A repaired evaluator** ([P19], [P25](ii), [P9](i)). The rating `F̂' = (4, 3, 0, 2, 1)` orders the outcomes as `F`
does. Its level sets are single outcomes, so its regression is `F` itself, non-decreasing in `F̂'`, and by [P19] no path
whose revealed objectives are non-decreasing in `F̂'` lowers `E[F]`. Along its pursuit, `E[F]` is €8.04 at `t = 1`,
€9.48 at `t = 2`, and tends to €10.00. At the departure the assistant actually made, 0.216 nats, it reaches €6.31,
against €6.37 for the matched pursuit of `F` itself, which no behaviour with that departure can beat.

## What the framework did not say

- **Whether the euro values are right.** They are the company's declaration ([A5]); a customer might value a credit
  differently. The framework measures distance from what was declared, and does not choose it.
- **Why the assistant does this inside.** It judges behaviour only ([A1]). It reads the pursued objective from
  behaviour; it does not open the model.
- **Whether a nat is a lot in general.** Misalignment is in nats and says how far; the shortfall is in euros and says
  how much. A report gives both (`STANDARD.md`).
- **What happens across kinds of question.** A full report would split conversations by kind, since the assistant does
  not choose which questions customers ask, and separate what it cannot do from what it does not do ([D8], [P15]). This
  scenario has one kind of question.
