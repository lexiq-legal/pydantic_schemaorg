from pydantic import Field
from pydantic_schemaorg.MedicalStudyStatus import MedicalStudyStatus


class EnrollingByInvitation(MedicalStudyStatus):
    """Enrolling participants by invitation only.

    See https://schema.org/EnrollingByInvitation.

    """
    type_: str = Field("EnrollingByInvitation", const=True, alias='@type')
    

EnrollingByInvitation.update_forward_refs()
