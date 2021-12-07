from pydantic import Field
from pydantic_schemaorg.EnergyStarEnergyEfficiencyEnumeration import EnergyStarEnergyEfficiencyEnumeration


class EnergyStarCertified(EnergyStarEnergyEfficiencyEnumeration):
    """Represents EnergyStar certification.

    See https://schema.org/EnergyStarCertified.

    """
    type_: str = Field("EnergyStarCertified", const=True, alias='@type')
    

EnergyStarCertified.update_forward_refs()
