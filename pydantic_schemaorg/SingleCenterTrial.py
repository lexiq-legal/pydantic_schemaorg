from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MedicalTrialDesign import MedicalTrialDesign


class SingleCenterTrial(MedicalTrialDesign):
    """A trial that takes place at a single center.

    See: https://schema.org/SingleCenterTrial
    Model depth: 6
    """
    type_: str = Field("SingleCenterTrial", alias='@type')
    

