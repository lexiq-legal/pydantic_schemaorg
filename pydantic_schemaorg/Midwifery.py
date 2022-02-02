from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty
from pydantic_schemaorg.MedicalBusiness import MedicalBusiness


class Midwifery(MedicalSpecialty, MedicalBusiness):
    """A nurse-like health profession that deals with pregnancy, childbirth, and the postpartum"
     "period (including care of the newborn), besides sexual and reproductive health of women"
     "throughout their lives.

    See: https://schema.org/Midwifery
    Model depth: 5
    """
    type_: str = Field("Midwifery", alias='@type')
    

