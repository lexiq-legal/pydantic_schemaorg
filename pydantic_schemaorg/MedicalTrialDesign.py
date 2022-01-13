from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MedicalEnumeration import MedicalEnumeration


class MedicalTrialDesign(MedicalEnumeration):
    """Design models for medical trials. Enumerated type.

    See: https://schema.org/MedicalTrialDesign
    Model depth: 5
    """

    type_: str = Field("MedicalTrialDesign", const=True, alias="@type")


if TYPE_CHECKING:

    MedicalTrialDesign.update_forward_refs()
