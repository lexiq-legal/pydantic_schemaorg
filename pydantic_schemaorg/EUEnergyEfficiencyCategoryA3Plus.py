from pydantic import Field
from pydantic_schemaorg.EUEnergyEfficiencyEnumeration import EUEnergyEfficiencyEnumeration


class EUEnergyEfficiencyCategoryA3Plus(EUEnergyEfficiencyEnumeration):
    """Represents EU Energy Efficiency Class A+++ as defined in EU energy labeling regulations.

    See https://schema.org/EUEnergyEfficiencyCategoryA3Plus.

    """
    type_: str = Field("EUEnergyEfficiencyCategoryA3Plus", const=True, alias='@type')
    

EUEnergyEfficiencyCategoryA3Plus.update_forward_refs()
