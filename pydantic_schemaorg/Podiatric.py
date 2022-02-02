from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty
from pydantic_schemaorg.MedicalBusiness import MedicalBusiness


class Podiatric(MedicalSpecialty, MedicalBusiness):
    """Podiatry is the care of the human foot, especially the diagnosis and treatment of foot"
     "disorders.

    See: https://schema.org/Podiatric
    Model depth: 5
    """
    type_: str = Field("Podiatric", alias='@type')
    

