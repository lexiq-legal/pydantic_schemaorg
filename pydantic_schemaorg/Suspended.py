from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MedicalStudyStatus import MedicalStudyStatus


class Suspended(MedicalStudyStatus):
    """Suspended.

    See: https://schema.org/Suspended
    Model depth: 6
    """
    type_: str = Field("Suspended", alias='@type')
    

