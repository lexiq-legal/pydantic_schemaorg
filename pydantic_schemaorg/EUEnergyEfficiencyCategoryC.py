from pydantic import Field
from pydantic_schemaorg.EUEnergyEfficiencyEnumeration import EUEnergyEfficiencyEnumeration


class EUEnergyEfficiencyCategoryC(EUEnergyEfficiencyEnumeration):
    """Represents EU Energy Efficiency Class C as defined in EU energy labeling regulations.

    See https://schema.org/EUEnergyEfficiencyCategoryC.

    """
    type_: str = Field("EUEnergyEfficiencyCategoryC", const=True, alias='@type')
    

EUEnergyEfficiencyCategoryC.update_forward_refs()
