from pydantic import Field
from pydantic_schemaorg.MedicalStudyStatus import MedicalStudyStatus


class Recruiting(MedicalStudyStatus):
    """Recruiting participants.

    See https://schema.org/Recruiting.

    """
    type_: str = Field("Recruiting", const=True, alias='@type')
    

Recruiting.update_forward_refs()
