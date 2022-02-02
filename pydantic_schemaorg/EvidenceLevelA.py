from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MedicalEvidenceLevel import MedicalEvidenceLevel


class EvidenceLevelA(MedicalEvidenceLevel):
    """Data derived from multiple randomized clinical trials or meta-analyses.

    See: https://schema.org/EvidenceLevelA
    Model depth: 6
    """
    type_: str = Field("EvidenceLevelA", alias='@type')
    

