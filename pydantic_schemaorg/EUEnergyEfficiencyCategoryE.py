from pydantic import Field
from pydantic_schemaorg.EUEnergyEfficiencyEnumeration import EUEnergyEfficiencyEnumeration


class EUEnergyEfficiencyCategoryE(EUEnergyEfficiencyEnumeration):
    """Represents EU Energy Efficiency Class E as defined in EU energy labeling regulations.

    See https://schema.org/EUEnergyEfficiencyCategoryE.

    """
    type_: str = Field("EUEnergyEfficiencyCategoryE", const=True, alias='@type')
    

EUEnergyEfficiencyCategoryE.update_forward_refs()
