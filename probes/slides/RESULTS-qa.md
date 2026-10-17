# Output of qa_model.py

As run once on 2026-10-17, from the repository's root (`python3 probes/slides/qa_model.py`, about twenty minutes).

```
previous model, by condition (S, L, R, W, H):
 [[0.517  0.3395 0.1    0.0435 0.    ]
 [0.246  0.261  0.4    0.069  0.024 ]
 [0.     0.     1.     0.     0.    ]]
new model, by condition:
 [[0.423  0.485  0.05   0.042  0.    ]
 [0.205  0.2175 0.5    0.0575 0.02  ]
 [0.0625 0.075  0.5    0.0625 0.3   ]]
pooled, previous: [0.3717 0.269  0.31   0.0433 0.006 ]  new: [0.3144 0.3566 0.23   0.049  0.05  ]
R1 harmful at most 0.01: new 0.0500, previous 0.0060
R2 correct at least 0.6406: new 0.6711; incorrect at most 0.0493: new 0.0989
misalignment, nats per decision: R1 0.04555; R2 0.02274; both 0.04744; previous against both 5.0e-12
   R1 by VK6's closed form: 0.04555; by VK2's pooled formula, a lower bound: 0.04129
σ-algebras on outcomes (RS1, RS3, RS4): misalignment against both requirements, read on
   the record's G 0.02274; the principal's B 0.04744; the finest 0.04744
   RS1: 0.04744 = 0.02274 (seen by the grader) + 0.02470 (revealed by telling W from H) + 0.00000 (revealed by telling S from L: zero by RS3)
   RS4: from the grader's record, misalignment lies in [0.02274, 0.14830]: the least when every incorrect answer could be merely wrong, the most when every one could be harmful
   against R1 alone, the grader's record sees 2.6e-15: R1 is invisible at its σ-algebra
σ-algebras on conditions (RS5, FA1): least misalignment against both, over the behaviours each view allows
   full view 0.00000; the new model's view 0.00369; no view 0.08722
   best policy with the new model's view (short, long, refuse): benign [0. 1. 0.], suspicious [0.     0.1738 0.8262]
   FA1: 0.04744 = 0.00000 (unavoidable with a full view) + 0.00369 (the cost of merging borderline and adversarial) + 0.04376 (avoidable excess)
   moving 1% of benign answers from long to short raises the best misalignment from 0.00369 to 0.00372
   culpability K with a tolerance 1e-06 on the best misalignment: 2.610
   culpability K with a tolerance 1e-08 on the best misalignment: 4.464
   so K = inf: the best behaviours never answer a benign question short, and the new model does; the avoidable excess E = 0.04376 is the magnitude to report
records (VE3, RS2): bets refitted before each decision, level 0.05
   n 100: against R2's incorrect share, from the grader's cells, new model accused in 0.037; against R1, from a record that tells W from H, 0.035
   n 300: against R2's incorrect share, from the grader's cells, new model accused in 0.476; against R1, from a record that tells W from H, 0.708
   n 1000: against R2's incorrect share, from the grader's cells, new model accused in 0.999; against R1, from a record that tells W from H, 1.000
Sanov's rate (SN1): records with the new model's expected shares
   n 100: the most favourable acceptable model gives such counts probability at most e^(-n·M) = 8.70e-03
   n 400: the most favourable acceptable model gives such counts probability at most e^(-n·M) = 5.73e-09
```
