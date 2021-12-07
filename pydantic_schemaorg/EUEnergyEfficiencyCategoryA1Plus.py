from pydantic import Field
from pydantic_schemaorg.EUEnergyEfficiencyEnumeration import EUEnergyEfficiencyEnumeration


class EUEnergyEfficiencyCategoryA1Plus(EUEnergyEfficiencyEnumeration):
    """Represents EU Energy Efficiency Class A+ as defined in EU energy labeling regulations.

    See https://schema.org/EUEnergyEfficiencyCategoryA1Plus.

    """
    type_: str = Field("EUEnergyEfficiencyCategoryA1Plus", const=True, alias='@type')
    

EUEnergyEfficiencyCategoryA1Plus.update_forward_refs()
