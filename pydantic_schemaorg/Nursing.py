from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty
from pydantic_schemaorg.MedicalBusiness import MedicalBusiness


class Nursing(MedicalSpecialty, MedicalBusiness):
    """A health profession of a person formally educated and trained in the care of the sick or"
     "infirm person.

    See: https://schema.org/Nursing
    Model depth: 5
    """
    type_: str = Field("Nursing", alias='@type')
    

