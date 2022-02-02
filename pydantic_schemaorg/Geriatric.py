from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty
from pydantic_schemaorg.MedicalBusiness import MedicalBusiness


class Geriatric(MedicalSpecialty, MedicalBusiness):
    """A specific branch of medical science that is concerned with the diagnosis and treatment"
     "of diseases, debilities and provision of care to the aged.

    See: https://schema.org/Geriatric
    Model depth: 5
    """
    type_: str = Field("Geriatric", alias='@type')
    

