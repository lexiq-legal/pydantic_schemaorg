from pydantic import Field
from pydantic_schemaorg.MedicalAudienceType import MedicalAudienceType


class Clinician(MedicalAudienceType):
    """Medical clinicians, including practicing physicians and other medical professionals"
     "involved in clinical practice.

    See https://schema.org/Clinician.

    """
    type_: str = Field("Clinician", const=True, alias='@type')
    

Clinician.update_forward_refs()
