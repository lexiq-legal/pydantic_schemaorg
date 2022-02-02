from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty
from pydantic_schemaorg.MedicalBusiness import MedicalBusiness


class Dermatology(MedicalSpecialty, MedicalBusiness):
    """A specific branch of medical science that pertains to diagnosis and treatment of disorders"
     "of skin.

    See: https://schema.org/Dermatology
    Model depth: 5
    """
    type_: str = Field("Dermatology", alias='@type')
    

