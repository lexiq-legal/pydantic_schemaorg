from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.EUEnergyEfficiencyEnumeration import (
    EUEnergyEfficiencyEnumeration,
)


class EUEnergyEfficiencyCategoryB(EUEnergyEfficiencyEnumeration):
    """Represents EU Energy Efficiency Class B as defined in EU energy labeling regulations.

    See: https://schema.org/EUEnergyEfficiencyCategoryB
    Model depth: 6
    """

    type_: str = Field("EUEnergyEfficiencyCategoryB", const=True, alias="@type")


if TYPE_CHECKING:

    EUEnergyEfficiencyCategoryB.update_forward_refs()
