from pydantic import Field
from pydantic_schemaorg.EUEnergyEfficiencyEnumeration import EUEnergyEfficiencyEnumeration


class EUEnergyEfficiencyCategoryG(EUEnergyEfficiencyEnumeration):
    """Represents EU Energy Efficiency Class G as defined in EU energy labeling regulations.

    See https://schema.org/EUEnergyEfficiencyCategoryG.

    """
    type_: str = Field("EUEnergyEfficiencyCategoryG", const=True, alias='@type')
    

EUEnergyEfficiencyCategoryG.update_forward_refs()
