from pydantic import Field
from pydantic_schemaorg.MedicalEnumeration import MedicalEnumeration


class MedicalEvidenceLevel(MedicalEnumeration):
    """Level of evidence for a medical guideline. Enumerated type.

    See https://schema.org/MedicalEvidenceLevel.

    """

    locals().update({"@type": Field("MedicalEvidenceLevel", const=True)})


MedicalEvidenceLevel.update_forward_refs()
