from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MedicalStudyStatus import MedicalStudyStatus


class Completed(MedicalStudyStatus):
    """Completed.

    See: https://schema.org/Completed
    Model depth: 6
    """
    type_: str = Field("Completed", alias='@type')
    

