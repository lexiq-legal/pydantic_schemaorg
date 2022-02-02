from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MedicalEvidenceLevel import MedicalEvidenceLevel


class EvidenceLevelB(MedicalEvidenceLevel):
    """Data derived from a single randomized trial, or nonrandomized studies.

    See: https://schema.org/EvidenceLevelB
    Model depth: 6
    """
    type_: str = Field("EvidenceLevelB", alias='@type')
    

