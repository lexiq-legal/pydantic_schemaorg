from pydantic import Field
from pydantic_schemaorg.EnergyEfficiencyEnumeration import EnergyEfficiencyEnumeration


class EnergyStarEnergyEfficiencyEnumeration(EnergyEfficiencyEnumeration):
    """Used to indicate whether a product is EnergyStar certified.

    See https://schema.org/EnergyStarEnergyEfficiencyEnumeration.

    """

    locals().update({"@type": Field("EnergyStarEnergyEfficiencyEnumeration", const=True)})


EnergyStarEnergyEfficiencyEnumeration.update_forward_refs()
