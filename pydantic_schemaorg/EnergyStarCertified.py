from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.EnergyStarEnergyEfficiencyEnumeration import EnergyStarEnergyEfficiencyEnumeration


class EnergyStarCertified(EnergyStarEnergyEfficiencyEnumeration):
    """Represents EnergyStar certification.

    See: https://schema.org/EnergyStarCertified
    Model depth: 6
    """
    type_: str = Field("EnergyStarCertified", alias='@type')
    

