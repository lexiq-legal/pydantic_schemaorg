from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MedicalEnumeration import MedicalEnumeration


class DrugPrescriptionStatus(MedicalEnumeration):
    """Indicates whether this drug is available by prescription or over-the-counter.

    See: https://schema.org/DrugPrescriptionStatus
    Model depth: 5
    """

    type_: str = Field("DrugPrescriptionStatus", const=True, alias="@type")


if TYPE_CHECKING:

    DrugPrescriptionStatus.update_forward_refs()
