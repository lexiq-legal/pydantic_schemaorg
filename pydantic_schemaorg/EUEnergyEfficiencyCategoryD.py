from pydantic import Field
from pydantic_schemaorg.EUEnergyEfficiencyEnumeration import EUEnergyEfficiencyEnumeration


class EUEnergyEfficiencyCategoryD(EUEnergyEfficiencyEnumeration):
    """Represents EU Energy Efficiency Class D as defined in EU energy labeling regulations.

    See https://schema.org/EUEnergyEfficiencyCategoryD.

    """
    type_: str = Field("EUEnergyEfficiencyCategoryD", const=True, alias='@type')
    

EUEnergyEfficiencyCategoryD.update_forward_refs()
