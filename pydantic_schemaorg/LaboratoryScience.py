from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty


class LaboratoryScience(MedicalSpecialty):
    """A medical science pertaining to chemical, hematological, immunologic, microscopic,"
     "or bacteriological diagnostic analyses or research.

    See: https://schema.org/LaboratoryScience
    Model depth: 6
    """
    type_: str = Field("LaboratoryScience", alias='@type')
    

