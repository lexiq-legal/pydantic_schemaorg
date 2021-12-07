from pydantic import Field
from pydantic_schemaorg.MedicalEnumeration import MedicalEnumeration


class MedicalAudienceType(MedicalEnumeration):
    """Target audiences types for medical web pages. Enumerated type.

    See https://schema.org/MedicalAudienceType.

    """
    type_: str = Field("MedicalAudienceType", const=True, alias='@type')
    

MedicalAudienceType.update_forward_refs()
