from pydantic import Field
from pydantic_schemaorg.MedicalStudyStatus import MedicalStudyStatus


class NotYetRecruiting(MedicalStudyStatus):
    """Not yet recruiting.

    See https://schema.org/NotYetRecruiting.

    """
    type_: str = Field("NotYetRecruiting", const=True, alias='@type')
    

NotYetRecruiting.update_forward_refs()
