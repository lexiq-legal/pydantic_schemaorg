from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.EnergyEfficiencyEnumeration import EnergyEfficiencyEnumeration


class EnergyStarEnergyEfficiencyEnumeration(EnergyEfficiencyEnumeration):
    """Used to indicate whether a product is EnergyStar certified.

    See: https://schema.org/EnergyStarEnergyEfficiencyEnumeration
    Model depth: 5
    """

    type_: str = Field(
        "EnergyStarEnergyEfficiencyEnumeration", const=True, alias="@type"
    )


if TYPE_CHECKING:

    EnergyStarEnergyEfficiencyEnumeration.update_forward_refs()
