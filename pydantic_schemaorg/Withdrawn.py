from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MedicalStudyStatus import MedicalStudyStatus


class Withdrawn(MedicalStudyStatus):
    """Withdrawn.

    See: https://schema.org/Withdrawn
    Model depth: 6
    """
    type_: str = Field(default="Withdrawn", alias='@type', const=True)
    
