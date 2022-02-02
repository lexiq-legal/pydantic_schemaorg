from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MedicalStudyStatus import MedicalStudyStatus


class Terminated(MedicalStudyStatus):
    """Terminated.

    See: https://schema.org/Terminated
    Model depth: 6
    """
    type_: str = Field("Terminated", alias='@type')
    

