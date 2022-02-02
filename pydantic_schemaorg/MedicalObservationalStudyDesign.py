from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MedicalEnumeration import MedicalEnumeration


class MedicalObservationalStudyDesign(MedicalEnumeration):
    """Design models for observational medical studies. Enumerated type.

    See: https://schema.org/MedicalObservationalStudyDesign
    Model depth: 5
    """
    type_: str = Field("MedicalObservationalStudyDesign", alias='@type')
    

