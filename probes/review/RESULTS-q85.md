# Output of the probe of Q85 (`NOTES.md` §43)

Run on 2026-11-12, with the pins of `requirements.txt`, on the default floating-point path. Exploratory: an invented
instance, no registered prediction, and no result rests on it.

## `python3 probes/review/q85_stages.py`

```text
== part A ==
against the overall limit: 0.0494; its nearest rates per condition: 0.0107, 0.1418
allocation (open, account)         open  account      sum
equal (0.0500, 0.0500)           0.0000   0.1324   0.1324
looser on account (0.0300, 0.0967)   0.0000   0.0724   0.0724
the nearest rates (0.0107, 0.1418)   0.0076   0.0418   0.0494
least sum over 20,001 allocations: 0.0494

== part B ==
perception                 decisions               percep.   decis.      sum    joint  isolated
exact                      with the look-up         0.0000   0.0000   0.0000   0.0000    0.0000
exact                      no look-up, escalates    0.0000   0.3612   0.3612   0.3612    0.3612
exact                      sloppy                   0.0000   0.2447   0.2447   0.2447    0.2447
20% of account read open   with the look-up         0.0894   0.0000   0.0894   0.0894    0.0000
20% of account read open   no look-up, escalates    0.0894   0.2890   0.3784   0.3784    0.3612
20% of account read open   sloppy                   0.0894   0.1999   0.2893   0.2893    0.2447
blind                      with the look-up         1.1736   0.0000   1.1736   1.1736    0.0000
blind                      no look-up, escalates    1.1736   0.0000   1.1736   1.1736    0.3612
blind                      sloppy                   1.1736   0.0207   1.1943   1.1943    0.2447
largest gap between the sum of the two terms and the joint misalignment: 4.9e-10
```
