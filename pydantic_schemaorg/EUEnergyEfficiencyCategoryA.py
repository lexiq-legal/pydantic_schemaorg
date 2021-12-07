from pydantic import Field
from pydantic_schemaorg.EUEnergyEfficiencyEnumeration import EUEnergyEfficiencyEnumeration


class EUEnergyEfficiencyCategoryA(EUEnergyEfficiencyEnumeration):
    """Represents EU Energy Efficiency Class A as defined in EU energy labeling regulations.

    See https://schema.org/EUEnergyEfficiencyCategoryA.

    """
    type_: str = Field("EUEnergyEfficiencyCategoryA", const=True, alias='@type')
    

EUEnergyEfficiencyCategoryA.update_forward_refs()
