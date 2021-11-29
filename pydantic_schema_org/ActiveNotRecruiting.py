from pydantic import Field
from pydantic_schema_org.MedicalStudyStatus import MedicalStudyStatus


class ActiveNotRecruiting(MedicalStudyStatus):
    """Active, but not recruiting new participants.

    See https://schema.org/ActiveNotRecruiting.

    """

    locals().update({"@type": Field("ActiveNotRecruiting", const=True)})


ActiveNotRecruiting.update_forward_refs()
