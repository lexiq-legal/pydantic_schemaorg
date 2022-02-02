from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty
from pydantic_schemaorg.MedicalBusiness import MedicalBusiness


class DietNutrition(MedicalSpecialty, MedicalBusiness):
    """Dietetic and nutrition as a medical specialty.

    See: https://schema.org/DietNutrition
    Model depth: 5
    """
    type_: str = Field("DietNutrition", alias='@type')
    

