from pydantic import Field
from pydantic_schemaorg.MedicalEvidenceLevel import MedicalEvidenceLevel


class EvidenceLevelC(MedicalEvidenceLevel):
    """Only consensus opinion of experts, case studies, or standard-of-care.

    See https://schema.org/EvidenceLevelC.

    """
    type_: str = Field("EvidenceLevelC", const=True, alias='@type')
    

EvidenceLevelC.update_forward_refs()
