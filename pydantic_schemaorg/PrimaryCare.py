from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty
from pydantic_schemaorg.MedicalBusiness import MedicalBusiness


class PrimaryCare(MedicalSpecialty, MedicalBusiness):
    """The medical care by a physician, or other health-care professional, who is the patient's"
     "first contact with the health-care system and who may recommend a specialist if necessary.

    See: https://schema.org/PrimaryCare
    Model depth: 5
    """
    type_: str = Field("PrimaryCare", alias='@type')
    

