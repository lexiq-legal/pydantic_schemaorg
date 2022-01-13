from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.EUEnergyEfficiencyEnumeration import (
    EUEnergyEfficiencyEnumeration,
)


class EUEnergyEfficiencyCategoryA(EUEnergyEfficiencyEnumeration):
    """Represents EU Energy Efficiency Class A as defined in EU energy labeling regulations.

    See: https://schema.org/EUEnergyEfficiencyCategoryA
    Model depth: 6
    """

    type_: str = Field("EUEnergyEfficiencyCategoryA", const=True, alias="@type")


if TYPE_CHECKING:

    EUEnergyEfficiencyCategoryA.update_forward_refs()
