from pydantic import Field
from pydantic_schemaorg.MedicalEnumeration import MedicalEnumeration


class MedicalAudienceType(MedicalEnumeration):
    """Target audiences types for medical web pages. Enumerated type.

    See https://schema.org/MedicalAudienceType.

    """

    locals().update({"@type": Field("MedicalAudienceType", const=True)})


MedicalAudienceType.update_forward_refs()
