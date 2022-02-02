from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty
from pydantic_schemaorg.MedicalBusiness import MedicalBusiness


class Otolaryngologic(MedicalSpecialty, MedicalBusiness):
    """A specific branch of medical science that is concerned with the ear, nose and throat and"
     "their respective disease states.

    See: https://schema.org/Otolaryngologic
    Model depth: 5
    """
    type_: str = Field("Otolaryngologic", alias='@type')
    

