from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty
from pydantic_schemaorg.MedicalBusiness import MedicalBusiness


class PublicHealth(MedicalSpecialty, MedicalBusiness):
    """Branch of medicine that pertains to the health services to improve and protect community"
     "health, especially epidemiology, sanitation, immunization, and preventive medicine.

    See: https://schema.org/PublicHealth
    Model depth: 5
    """
    type_: str = Field("PublicHealth", alias='@type')
    

