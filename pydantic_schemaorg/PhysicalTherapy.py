from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MedicalTherapy import MedicalTherapy


class PhysicalTherapy(MedicalTherapy):
    """A process of progressive physical care and rehabilitation aimed at improving a health"
     "condition.

    See: https://schema.org/PhysicalTherapy
    Model depth: 6
    """

    type_: str = Field("PhysicalTherapy", const=True, alias="@type")


if TYPE_CHECKING:

    PhysicalTherapy.update_forward_refs()
