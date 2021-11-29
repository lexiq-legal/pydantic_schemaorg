from pydantic import Field
from pydantic_schemaorg.MedicalEvidenceLevel import MedicalEvidenceLevel


class EvidenceLevelA(MedicalEvidenceLevel):
    """Data derived from multiple randomized clinical trials or meta-analyses.

    See https://schema.org/EvidenceLevelA.

    """

    locals().update({"@type": Field("EvidenceLevelA", const=True)})


EvidenceLevelA.update_forward_refs()
