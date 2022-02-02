from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.EnergyEfficiencyEnumeration import EnergyEfficiencyEnumeration


class EnergyStarEnergyEfficiencyEnumeration(EnergyEfficiencyEnumeration):
    """Used to indicate whether a product is EnergyStar certified.

    See: https://schema.org/EnergyStarEnergyEfficiencyEnumeration
    Model depth: 5
    """
    type_: str = Field("EnergyStarEnergyEfficiencyEnumeration", alias='@type')
    

