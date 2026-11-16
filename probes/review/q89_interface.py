"""The interface as two sets, what the actor is limited to and what it has shown, and the three verdicts they give
(v14/interface-items.md, NOTES.md §47, Q89). Exploratory, not a check; the invented support bot of
q84_factorization.py. Usage: python3 probes/review/q89_interface.py        (about a minute)

The limit: the deployment gives the view and no look-up tool. Shown: the behaviours the actor produced, here as
deployed (on account questions it answers 70% and escalates 30%) and under an instruction (25% and 75%), and their
mixtures. Care margin: 0.01 nats per decision.
"""
import importlib.util
from pathlib import Path
import numpy as np

spec = importlib.util.spec_from_file_location("q84", Path(__file__).with_name("q84_factorization.py"))
q84 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(q84)
DELTA = 0.01


def verdict(m_actor, m_shown, m_limit):
    if m_actor - m_shown > DELTA:
        return "culpable, shown"
    if m_actor - m_limit <= DELTA:
        return "excused by the limits"
    return "open"


if __name__ == "__main__":
    limit = q84.least(view=True, tool=False)
    sloppy, careful = np.array([1, 0, 0, 0.7, 0.3, 0.0]), np.array([1, 0, 0, 0.25, 0.75, 0.0])
    shown = min(q84.M(w * sloppy + (1 - w) * careful) for w in np.linspace(0, 1, 101))
    print(f"least misalignment within the limit        {limit:.4f}")
    print(f"least misalignment among what was shown    {shown:.4f}")
    for name, pol, sh, lim in (("as deployed, with the instructed record", sloppy, shown, limit),
                               ("the instructed behaviour, deployed", careful, shown, limit),
                               ("as deployed, nothing else shown", sloppy, q84.M(sloppy), limit),
                               ("as deployed, nothing shown, no limit declared", sloppy, q84.M(sloppy), 0.0)):
        m = q84.M(pol)
        print(f"{name:46s} M {m:.4f}  unavoidable in [{lim:.4f}, {sh:.4f}]  "
              f"avoidable in [{m - sh:.4f}, {m - lim:.4f}]  {verdict(m, sh, lim)}")
