from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MedicalAudienceType import MedicalAudienceType


class MedicalResearcher(MedicalAudienceType):
    """Medical researchers.

    See: https://schema.org/MedicalResearcher
    Model depth: 6
    """
    type_: str = Field("MedicalResearcher", alias='@type')
    

