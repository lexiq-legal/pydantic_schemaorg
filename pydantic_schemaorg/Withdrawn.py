from pydantic import Field
from pydantic_schemaorg.MedicalStudyStatus import MedicalStudyStatus


class Withdrawn(MedicalStudyStatus):
    """Withdrawn.

    See https://schema.org/Withdrawn.

    """
    type_: str = Field("Withdrawn", const=True, alias='@type')
    

Withdrawn.update_forward_refs()
