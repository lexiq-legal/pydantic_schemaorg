from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.EnergyEfficiencyEnumeration import EnergyEfficiencyEnumeration


class EUEnergyEfficiencyEnumeration(EnergyEfficiencyEnumeration):
    """Enumerates the EU energy efficiency classes A-G as well as A+, A++, and A+++ as defined"
     "in EU directive 2017/1369.

    See: https://schema.org/EUEnergyEfficiencyEnumeration
    Model depth: 5
    """

    type_: str = Field("EUEnergyEfficiencyEnumeration", const=True, alias="@type")


if TYPE_CHECKING:

    EUEnergyEfficiencyEnumeration.update_forward_refs()
