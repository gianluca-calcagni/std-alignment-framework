# Output of the probe of Q89 (`v14/interface-items.md`, `NOTES.md` §47)

Run on 2026-11-16, with the pins of `requirements.txt`, on the default floating-point path. Exploratory: an invented
instance, no registered prediction, and no result rests on it.

## `python3 probes/review/q89_interface.py`

```text
least misalignment within the limit        0.2315
least misalignment among what was shown    0.2315
as deployed, with the instructed record        M 0.3274  unavoidable in [0.2315, 0.2315]  avoidable in [0.0959, 0.0959]  culpable, shown
the instructed behaviour, deployed             M 0.2333  unavoidable in [0.2315, 0.2315]  avoidable in [0.0018, 0.0018]  excused by the limits
as deployed, nothing else shown                M 0.3274  unavoidable in [0.2315, 0.3274]  avoidable in [0.0000, 0.0959]  open
as deployed, nothing shown, no limit declared  M 0.3274  unavoidable in [0.0000, 0.3274]  avoidable in [0.0000, 0.3274]  open
```
