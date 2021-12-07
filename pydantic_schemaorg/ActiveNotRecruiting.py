from pydantic import Field
from pydantic_schemaorg.MedicalStudyStatus import MedicalStudyStatus


class ActiveNotRecruiting(MedicalStudyStatus):
    """Active, but not recruiting new participants.

    See https://schema.org/ActiveNotRecruiting.

    """
    type_: str = Field("ActiveNotRecruiting", const=True, alias='@type')
    

ActiveNotRecruiting.update_forward_refs()
