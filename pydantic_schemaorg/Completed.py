from pydantic import Field
from pydantic_schemaorg.MedicalStudyStatus import MedicalStudyStatus


class Completed(MedicalStudyStatus):
    """Completed.

    See https://schema.org/Completed.

    """
    type_: str = Field("Completed", const=True, alias='@type')
    

Completed.update_forward_refs()
