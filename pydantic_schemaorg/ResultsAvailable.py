from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MedicalStudyStatus import MedicalStudyStatus


class ResultsAvailable(MedicalStudyStatus):
    """Results are available.

    See: https://schema.org/ResultsAvailable
    Model depth: 6
    """
    type_: str = Field("ResultsAvailable", alias='@type')
    

