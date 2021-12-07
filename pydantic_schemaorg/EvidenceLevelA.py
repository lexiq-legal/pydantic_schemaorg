from pydantic import Field
from pydantic_schemaorg.MedicalEvidenceLevel import MedicalEvidenceLevel


class EvidenceLevelA(MedicalEvidenceLevel):
    """Data derived from multiple randomized clinical trials or meta-analyses.

    See https://schema.org/EvidenceLevelA.

    """
    type_: str = Field("EvidenceLevelA", const=True, alias='@type')
    

EvidenceLevelA.update_forward_refs()
