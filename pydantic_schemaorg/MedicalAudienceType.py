from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MedicalEnumeration import MedicalEnumeration


class MedicalAudienceType(MedicalEnumeration):
    """Target audiences types for medical web pages. Enumerated type.

    See: https://schema.org/MedicalAudienceType
    Model depth: 5
    """
    type_: str = Field("MedicalAudienceType", alias='@type')
    

