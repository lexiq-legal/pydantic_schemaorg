from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MedicalObservationalStudyDesign import MedicalObservationalStudyDesign


class Registry(MedicalObservationalStudyDesign):
    """A registry-based study design.

    See: https://schema.org/Registry
    Model depth: 6
    """
    type_: str = Field("Registry", alias='@type')
    

