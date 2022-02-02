from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.EUEnergyEfficiencyEnumeration import EUEnergyEfficiencyEnumeration


class EUEnergyEfficiencyCategoryF(EUEnergyEfficiencyEnumeration):
    """Represents EU Energy Efficiency Class F as defined in EU energy labeling regulations.

    See: https://schema.org/EUEnergyEfficiencyCategoryF
    Model depth: 6
    """
    type_: str = Field("EUEnergyEfficiencyCategoryF", alias='@type')
    

