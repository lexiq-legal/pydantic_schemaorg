from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MedicalStudyStatus import MedicalStudyStatus


class ActiveNotRecruiting(MedicalStudyStatus):
    """Active, but not recruiting new participants.

    See: https://schema.org/ActiveNotRecruiting
    Model depth: 6
    """
    type_: str = Field("ActiveNotRecruiting", alias='@type')
    

