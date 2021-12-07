from pydantic import Field
from pydantic_schemaorg.EUEnergyEfficiencyEnumeration import EUEnergyEfficiencyEnumeration


class EUEnergyEfficiencyCategoryF(EUEnergyEfficiencyEnumeration):
    """Represents EU Energy Efficiency Class F as defined in EU energy labeling regulations.

    See https://schema.org/EUEnergyEfficiencyCategoryF.

    """
    type_: str = Field("EUEnergyEfficiencyCategoryF", const=True, alias='@type')
    

EUEnergyEfficiencyCategoryF.update_forward_refs()
