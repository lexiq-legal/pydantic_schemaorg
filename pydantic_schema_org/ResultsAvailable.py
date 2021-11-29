from pydantic import Field
from pydantic_schema_org.MedicalStudyStatus import MedicalStudyStatus


class ResultsAvailable(MedicalStudyStatus):
    """Results are available.

    See https://schema.org/ResultsAvailable.

    """

    locals().update({"@type": Field("ResultsAvailable", const=True)})


ResultsAvailable.update_forward_refs()
