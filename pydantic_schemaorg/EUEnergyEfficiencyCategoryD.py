from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.EUEnergyEfficiencyEnumeration import EUEnergyEfficiencyEnumeration


class EUEnergyEfficiencyCategoryD(EUEnergyEfficiencyEnumeration):
    """Represents EU Energy Efficiency Class D as defined in EU energy labeling regulations.

    See: https://schema.org/EUEnergyEfficiencyCategoryD
    Model depth: 6
    """
    type_: str = Field("EUEnergyEfficiencyCategoryD", alias='@type')
    

