from pydantic import Field
from pydantic_schemaorg.EnergyEfficiencyEnumeration import EnergyEfficiencyEnumeration


class EnergyStarEnergyEfficiencyEnumeration(EnergyEfficiencyEnumeration):
    """Used to indicate whether a product is EnergyStar certified.

    See https://schema.org/EnergyStarEnergyEfficiencyEnumeration.

    """
    type_: str = Field("EnergyStarEnergyEfficiencyEnumeration", const=True, alias='@type')
    

EnergyStarEnergyEfficiencyEnumeration.update_forward_refs()
