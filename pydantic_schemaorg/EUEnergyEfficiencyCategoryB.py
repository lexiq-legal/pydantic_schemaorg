from pydantic import Field
from pydantic_schemaorg.EUEnergyEfficiencyEnumeration import EUEnergyEfficiencyEnumeration


class EUEnergyEfficiencyCategoryB(EUEnergyEfficiencyEnumeration):
    """Represents EU Energy Efficiency Class B as defined in EU energy labeling regulations.

    See https://schema.org/EUEnergyEfficiencyCategoryB.

    """
    type_: str = Field("EUEnergyEfficiencyCategoryB", const=True, alias='@type')
    

EUEnergyEfficiencyCategoryB.update_forward_refs()
