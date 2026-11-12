"""A factorization by who can act, with what a record leaves open and what an intervention closes (NOTES.md §44,
H89–H91, Q86). Exploratory, not a check; the invented support bot of q84_factorization.py.
Usage: python3 probes/review/q86_tiers.py        (about a minute)

Tiers, nested by nature and not by choice: what any actor could do in this world (full view, every action); what
this deployment allows (here: the view, and no look-up tool); what this actor can do, which no record shows; what it
did. The actor: on account questions it answers from the documentation 70% of the time and escalates 30%.
Three records: as deployed; under an instruction to escalate more of them (it then answers 25% and escalates 75%);
and with the look-up granted (it then looks up 80% of account questions and escalates 20%).
"""
import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location("q84", Path(__file__).with_name("q84_factorization.py"))
q84 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(q84)

if __name__ == "__main__":
    world = q84.least(view=True, tool=True)                 # any actor, everything the world offers
    deploy = q84.least(view=True, tool=False)               # this deployment: no look-up
    as_deployed = q84.M([1, 0, 0, 0.7, 0.3, 0])
    instructed = q84.M([1, 0, 0, 0.25, 0.75, 0])
    granted = q84.M([1, 0, 0, 0, 0.2, 0.8])
    rest = as_deployed - deploy
    print(f"misalignment as deployed                         {as_deployed:.4f}")
    print(f"unavoidable in this world, for any actor         {world:.4f}")
    print(f"the deployment's limits (no look-up)             {deploy - world:.4f}")
    print(f"the rest: cannot, or did not                     {rest:.4f}")
    print(f"  from the record as deployed:   cannot in [0, {rest:.4f}], did not in [0, {rest:.4f}]")
    elicited = min(as_deployed, instructed)
    print(f"  after the instruction ({instructed:.4f}): cannot in [0, {elicited - deploy:.4f}], "
          f"did not in [{as_deployed - elicited:.4f}, {rest:.4f}]")
    print(f"granting the look-up: could remove up to {deploy - world:.4f} of the deployment's limits; "
          f"the record with it shows {granted:.4f}, a fall of {as_deployed - granted:.4f}")
