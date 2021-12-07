from pydantic import Field
from pydantic_schemaorg.MedicalStudyStatus import MedicalStudyStatus


class Suspended(MedicalStudyStatus):
    """Suspended.

    See https://schema.org/Suspended.

    """
    type_: str = Field("Suspended", const=True, alias='@type')
    

Suspended.update_forward_refs()
