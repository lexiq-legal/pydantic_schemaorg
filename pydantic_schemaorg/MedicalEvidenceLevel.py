from pydantic import Field
from pydantic_schemaorg.MedicalEnumeration import MedicalEnumeration


class MedicalEvidenceLevel(MedicalEnumeration):
    """Level of evidence for a medical guideline. Enumerated type.

    See https://schema.org/MedicalEvidenceLevel.

    """
    type_: str = Field("MedicalEvidenceLevel", const=True, alias='@type')
    

MedicalEvidenceLevel.update_forward_refs()
