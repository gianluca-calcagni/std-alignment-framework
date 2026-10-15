# Output of v14_probe.py

As run once on 2026-10-15, from the repository's root (`python3 probes/v14/v14_probe.py`).

```
VE1  the best bet against a convex set: h* = p/a* is a bet, and E_p[log h*] = M
  ordinal cone, 300 instances (104 with outcomes the actor never uses): largest E_a[h*] − 1 over its extreme points 4.4e-16

VE2  records hold an actor to the convex hull
  half intensity 0, half intensity 3: misalignment against the ray 0.0546 (t = 0.645); against the ordinal cone 0.0e+00
  share of records of 400 decisions accused at level 0.05: bet vs cone, count test vs cone, count test vs ray
    each decision intensity 0 or 3, at random     0.0185  0.0000  0.6890   (2000 records)
    intensity 8 after the best outcome, else 0    0.0120  0.0000  0.1570   (2000 records)
    pursues −F at intensity 1                     1.0000  1.0000  1.0000   (300 records)

VK2  rate limit a(C) ≤ ε: M = kl(p(C)‖ε) when p(C) > ε
  35 instances: largest |numerical minimum − kl(p(C)‖ε)|: 2.3e-12

VK3  budget E_a[g] ≤ b: M = max over 0 ≤ λ ≤ 1/(b − min g) of E_p[log(1 + λ(g − b))]
  80 instances: largest |dual − numerical minimum| 1.4e-08; the constructed a* is a behaviour within the budget and attains it within 3.7e-08; 37 instances at the edge λ* = 1/(b − min g)

VK4  several budgets: the best affine bet against the numerical minimum
  two budgets, 22 of 30 instances with a behaviour that keeps both: largest |best affine bet − numerical minimum| 4.9e-13

VK5  the constrained optimizer is tilt(q, t·(F − ν·g)), and ν is the budget's shadow price
  29 instances (0 where the solver failed from every start): largest |numerical optimum − value of the tilt| 2.1e-09; largest |d value/d b − ν| 1.7e-08
  forbidden set: total variation between tilt(q, 2(F − 40·1_C)) and the pursuit on the allowed outcomes 3.5e-18

VO3  three verdicts: a decoder always at level 8 of 10 levels, uniform reference
  better for every reading: False; worse for every reading: False; its rank's average 0.889 against the reference's 0.500
```
