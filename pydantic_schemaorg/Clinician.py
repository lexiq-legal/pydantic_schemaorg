from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MedicalAudienceType import MedicalAudienceType


class Clinician(MedicalAudienceType):
    """Medical clinicians, including practicing physicians and other medical professionals"
     "involved in clinical practice.

    See: https://schema.org/Clinician
    Model depth: 6
    """

    type_: str = Field("Clinician", const=True, alias="@type")


if TYPE_CHECKING:

    Clinician.update_forward_refs()
