from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MedicalAudienceType import MedicalAudienceType


class Clinician(MedicalAudienceType):
    """Medical clinicians, including practicing physicians and other medical professionals"
     "involved in clinical practice.

    See: https://schema.org/Clinician
    Model depth: 6
    """
    type_: str = Field("Clinician", alias='@type')
    

