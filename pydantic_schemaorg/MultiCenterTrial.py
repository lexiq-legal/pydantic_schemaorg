from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MedicalTrialDesign import MedicalTrialDesign


class MultiCenterTrial(MedicalTrialDesign):
    """A trial that takes place at multiple centers.

    See: https://schema.org/MultiCenterTrial
    Model depth: 6
    """
    type_: str = Field("MultiCenterTrial", alias='@type')
    

