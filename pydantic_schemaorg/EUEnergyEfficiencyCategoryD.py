from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.EUEnergyEfficiencyEnumeration import (
    EUEnergyEfficiencyEnumeration,
)


class EUEnergyEfficiencyCategoryD(EUEnergyEfficiencyEnumeration):
    """Represents EU Energy Efficiency Class D as defined in EU energy labeling regulations.

    See: https://schema.org/EUEnergyEfficiencyCategoryD
    Model depth: 6
    """

    type_: str = Field("EUEnergyEfficiencyCategoryD", const=True, alias="@type")


if TYPE_CHECKING:

    EUEnergyEfficiencyCategoryD.update_forward_refs()
