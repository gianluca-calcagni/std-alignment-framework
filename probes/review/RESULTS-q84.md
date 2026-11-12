# Output of the probe of Q84 (`NOTES.md` §42)

Run on 2026-11-12, with the pins of `requirements.txt`, on the default floating-point path. Exploratory: an invented
instance, no registered prediction, and no result rests on it.

## `python3 probes/review/q84_factorization.py`

```text
part 1: least misalignment by capabilities (nats per decision)
  view yes tool yes  0.0000
  view yes tool no   0.2315
  view no  tool yes  0.3628
  view no  tool no   0.4694
  the cost of losing the VIEW: removed first 0.3628; removed after the tool 0.2379
  the cost of losing the TOOL: removed first 0.2315; removed after the view 0.1066
  Shapley shares: {'view': 0.3004, 'tool': 0.1691} sum 0.4694 = m(neither) − m(both) 0.4694

part 2: the actor's misalignment 0.0848 unavoidable 0.0000 avoidable excess 0.0848
  entailed by F1 alone 0.0194; by F2 alone 0.0845; by both 0.0845
  Shapley shares: {'F1': 0.0097, 'F2': 0.0748}
  unexplained by the two features 0.0003
  check: unavoidable + shares + unexplained = 0.0848
```
