from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MedicalEvidenceLevel import MedicalEvidenceLevel


class EvidenceLevelC(MedicalEvidenceLevel):
    """Only consensus opinion of experts, case studies, or standard-of-care.

    See: https://schema.org/EvidenceLevelC
    Model depth: 6
    """
    type_: str = Field("EvidenceLevelC", alias='@type')
    

