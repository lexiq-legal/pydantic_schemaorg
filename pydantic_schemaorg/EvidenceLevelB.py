from pydantic import Field
from pydantic_schemaorg.MedicalEvidenceLevel import MedicalEvidenceLevel


class EvidenceLevelB(MedicalEvidenceLevel):
    """Data derived from a single randomized trial, or nonrandomized studies.

    See https://schema.org/EvidenceLevelB.

    """
    type_: str = Field("EvidenceLevelB", const=True, alias='@type')
    

EvidenceLevelB.update_forward_refs()
