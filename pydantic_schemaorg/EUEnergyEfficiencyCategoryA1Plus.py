from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.EUEnergyEfficiencyEnumeration import (
    EUEnergyEfficiencyEnumeration,
)


class EUEnergyEfficiencyCategoryA1Plus(EUEnergyEfficiencyEnumeration):
    """Represents EU Energy Efficiency Class A+ as defined in EU energy labeling regulations.

    See: https://schema.org/EUEnergyEfficiencyCategoryA1Plus
    Model depth: 6
    """

    type_: str = Field("EUEnergyEfficiencyCategoryA1Plus", const=True, alias="@type")


if TYPE_CHECKING:

    EUEnergyEfficiencyCategoryA1Plus.update_forward_refs()
