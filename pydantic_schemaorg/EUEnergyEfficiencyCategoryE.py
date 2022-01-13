from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.EUEnergyEfficiencyEnumeration import (
    EUEnergyEfficiencyEnumeration,
)


class EUEnergyEfficiencyCategoryE(EUEnergyEfficiencyEnumeration):
    """Represents EU Energy Efficiency Class E as defined in EU energy labeling regulations.

    See: https://schema.org/EUEnergyEfficiencyCategoryE
    Model depth: 6
    """

    type_: str = Field("EUEnergyEfficiencyCategoryE", const=True, alias="@type")


if TYPE_CHECKING:

    EUEnergyEfficiencyCategoryE.update_forward_refs()
