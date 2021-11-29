from pydantic import Field
from pydantic_schemaorg.MedicalEvidenceLevel import MedicalEvidenceLevel


class EvidenceLevelB(MedicalEvidenceLevel):
    """Data derived from a single randomized trial, or nonrandomized studies.

    See https://schema.org/EvidenceLevelB.

    """

    locals().update({"@type": Field("EvidenceLevelB", const=True)})


EvidenceLevelB.update_forward_refs()
