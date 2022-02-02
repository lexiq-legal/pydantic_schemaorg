from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.EUEnergyEfficiencyEnumeration import EUEnergyEfficiencyEnumeration


class EUEnergyEfficiencyCategoryG(EUEnergyEfficiencyEnumeration):
    """Represents EU Energy Efficiency Class G as defined in EU energy labeling regulations.

    See: https://schema.org/EUEnergyEfficiencyCategoryG
    Model depth: 6
    """
    type_: str = Field("EUEnergyEfficiencyCategoryG", alias='@type')
    

