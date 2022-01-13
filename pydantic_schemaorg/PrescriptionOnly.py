from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.DrugPrescriptionStatus import DrugPrescriptionStatus


class PrescriptionOnly(DrugPrescriptionStatus):
    """Available by prescription only.

    See: https://schema.org/PrescriptionOnly
    Model depth: 6
    """

    type_: str = Field("PrescriptionOnly", const=True, alias="@type")


if TYPE_CHECKING:

    PrescriptionOnly.update_forward_refs()
