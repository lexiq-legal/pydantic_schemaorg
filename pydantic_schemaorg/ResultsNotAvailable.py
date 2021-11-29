from pydantic import Field
from pydantic_schemaorg.MedicalStudyStatus import MedicalStudyStatus


class ResultsNotAvailable(MedicalStudyStatus):
    """Results are not available.

    See https://schema.org/ResultsNotAvailable.

    """

    locals().update({"@type": Field("ResultsNotAvailable", const=True)})


ResultsNotAvailable.update_forward_refs()
