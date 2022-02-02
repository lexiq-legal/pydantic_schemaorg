from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MedicalStudyStatus import MedicalStudyStatus


class Recruiting(MedicalStudyStatus):
    """Recruiting participants.

    See: https://schema.org/Recruiting
    Model depth: 6
    """
    type_: str = Field("Recruiting", alias='@type')
    

