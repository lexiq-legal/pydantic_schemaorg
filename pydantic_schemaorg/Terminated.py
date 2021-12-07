from pydantic import Field
from pydantic_schemaorg.MedicalStudyStatus import MedicalStudyStatus


class Terminated(MedicalStudyStatus):
    """Terminated.

    See https://schema.org/Terminated.

    """
    type_: str = Field("Terminated", const=True, alias='@type')
    

Terminated.update_forward_refs()
