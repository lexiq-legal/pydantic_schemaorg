from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MedicalTrialDesign import MedicalTrialDesign


class RandomizedTrial(MedicalTrialDesign):
    """A randomized trial design.

    See: https://schema.org/RandomizedTrial
    Model depth: 6
    """
    type_: str = Field("RandomizedTrial", alias='@type')
    

