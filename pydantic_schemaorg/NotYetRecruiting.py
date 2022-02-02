from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MedicalStudyStatus import MedicalStudyStatus


class NotYetRecruiting(MedicalStudyStatus):
    """Not yet recruiting.

    See: https://schema.org/NotYetRecruiting
    Model depth: 6
    """
    type_: str = Field("NotYetRecruiting", alias='@type')
    

