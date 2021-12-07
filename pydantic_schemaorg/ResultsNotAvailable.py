from pydantic import Field
from pydantic_schemaorg.MedicalStudyStatus import MedicalStudyStatus


class ResultsNotAvailable(MedicalStudyStatus):
    """Results are not available.

    See https://schema.org/ResultsNotAvailable.

    """
    type_: str = Field("ResultsNotAvailable", const=True, alias='@type')
    

ResultsNotAvailable.update_forward_refs()
