from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MedicalEnumeration import MedicalEnumeration


class MedicalEvidenceLevel(MedicalEnumeration):
    """Level of evidence for a medical guideline. Enumerated type.

    See: https://schema.org/MedicalEvidenceLevel
    Model depth: 5
    """

    type_: str = Field("MedicalEvidenceLevel", const=True, alias="@type")


if TYPE_CHECKING:

    MedicalEvidenceLevel.update_forward_refs()
