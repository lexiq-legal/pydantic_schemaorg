from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MedicalObservationalStudyDesign import MedicalObservationalStudyDesign


class Observational(MedicalObservationalStudyDesign):
    """An observational study design.

    See: https://schema.org/Observational
    Model depth: 6
    """
    type_: str = Field("Observational", alias='@type')
    

