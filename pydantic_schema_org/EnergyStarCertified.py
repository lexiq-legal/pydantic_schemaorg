from pydantic import Field
from pydantic_schema_org.EnergyStarEnergyEfficiencyEnumeration import EnergyStarEnergyEfficiencyEnumeration


class EnergyStarCertified(EnergyStarEnergyEfficiencyEnumeration):
    """Represents EnergyStar certification.

    See https://schema.org/EnergyStarCertified.

    """

    locals().update({"@type": Field("EnergyStarCertified", const=True)})


EnergyStarCertified.update_forward_refs()
