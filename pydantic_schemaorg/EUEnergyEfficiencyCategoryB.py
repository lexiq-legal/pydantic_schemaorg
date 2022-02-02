from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.EUEnergyEfficiencyEnumeration import EUEnergyEfficiencyEnumeration


class EUEnergyEfficiencyCategoryB(EUEnergyEfficiencyEnumeration):
    """Represents EU Energy Efficiency Class B as defined in EU energy labeling regulations.

    See: https://schema.org/EUEnergyEfficiencyCategoryB
    Model depth: 6
    """
    type_: str = Field("EUEnergyEfficiencyCategoryB", alias='@type')
    

