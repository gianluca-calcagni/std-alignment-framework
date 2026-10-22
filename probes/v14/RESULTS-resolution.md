# Output of resolution.py

As run once on 2026-10-17, from the repository's root (`python3 probes/v14/resolution.py`, under a minute).

```
RS1, RS2, RS3, RS4 on random instances: six outcomes, two budgets, a chain of three partitions
  RS1: least increment along the chain -1.8e-15 (non-negative up to solver tolerance)
  RS2: the best coarse bet costs at most 1 + 8.6e-07 under the acceptable set; its growth equals the coarse misalignment within 0.0e+00
  RS3: a requirement stated at the middle resolution: full and middle misalignment agree within 5.0e-14
  RS4: the split of the coarse cells as a* splits them has full misalignment equal to the coarse one within 6.4e-14; other splits of the same coarse masses hide up to 0.289 nats more (median over instances 0.030)

RS5 and FA1: an actor's view as a partition of conditions (actions are the outcomes themselves)
  least misalignment: full view 0.00000; merging conditions 1 and 2 0.18975; seeing nothing 0.98982
  an actor that sees nothing: misalignment 7.14863 = 0.00000 + 0.18975 + 0.80007 + 6.15881 (FA1: every term non-negative)

TG2: two targets in tension, pursued one at a time, against 'no worse on any target'
  pursuit of G1 at intensity 0.25: E[G1] 1.8071 (q: 1.5000), E[G2] 1.2703 (q: 1.5000)
  pursuit of G1 at intensity 0.5: E[G1] 2.0846 (q: 1.5000), E[G2] 1.0945 (q: 1.5000)
  pursuit of G1 at intensity 1.0: E[G1] 2.4927 (q: 1.5000), E[G2] 0.9144 (q: 1.5000)
  covariance of G1 and G2 under q: -1.0000
  [P53](iv) as TG2(iv): misalignment against the pursuits of a two-target cone equals the departure beyond 'no worse than the actor on either target', within 4.3e-14 on 30 instances

SN1: the most favourable acceptable behaviour's probability of the record's counts, against e^{-nM}
  n 20: log sup probability -5.352; -nM -1.036; -nM - log k_n -8.515
  n 100: log sup probability -11.845; -nM -5.180; -nM - log k_n -17.263
  n 500: log sup probability -34.965; -nM -25.899; -nM - log k_n -42.763
  two acceptable behaviours, an actor at their midpoint: Sanov's rate against the pair 0.3307; the best bet's growth, against their hull, 0.0000

VK6: a pooled rate limit with the conditions' frequencies fixed
  closed form against numerical minimization: within 4.8e-11 on 40 instances; the pooled formula of VK2 is below it by 1.9e-05 to 0.1892
  the support bot (probes/slides): wrong answers per condition 0.0291, 0.3534; pooled 0.1264; VK6 0.04956; VK2's pooled formula 0.04396

VK7: how misalignment moves with the budget
  the derivative of M in the budget against minus the best stake: within 3.3e-08 on 30 instances
  M(b') - (M(b) - log(1 + λ*(b' - b))) on a grid of b': least value 0.0e+00 (non-negative up to tolerance)
```
