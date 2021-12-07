from pydantic import Field
from pydantic_schemaorg.MedicalStudyStatus import MedicalStudyStatus


class ResultsAvailable(MedicalStudyStatus):
    """Results are available.

    See https://schema.org/ResultsAvailable.

    """
    type_: str = Field("ResultsAvailable", const=True, alias='@type')
    

ResultsAvailable.update_forward_refs()
