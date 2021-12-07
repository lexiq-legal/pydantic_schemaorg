from pydantic import Field
from pydantic_schemaorg.MedicalEnumeration import MedicalEnumeration


class MedicalStudyStatus(MedicalEnumeration):
    """The status of a medical study. Enumerated type.

    See https://schema.org/MedicalStudyStatus.

    """
    type_: str = Field("MedicalStudyStatus", const=True, alias='@type')
    

MedicalStudyStatus.update_forward_refs()
