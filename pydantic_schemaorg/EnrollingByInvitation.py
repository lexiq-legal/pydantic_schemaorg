from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MedicalStudyStatus import MedicalStudyStatus


class EnrollingByInvitation(MedicalStudyStatus):
    """Enrolling participants by invitation only.

    See: https://schema.org/EnrollingByInvitation
    Model depth: 6
    """
    type_: str = Field("EnrollingByInvitation", alias='@type')
    

