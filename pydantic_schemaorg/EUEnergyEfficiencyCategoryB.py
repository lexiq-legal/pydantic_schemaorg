from pydantic import Field
from pydantic_schemaorg.EUEnergyEfficiencyEnumeration import EUEnergyEfficiencyEnumeration


class EUEnergyEfficiencyCategoryB(EUEnergyEfficiencyEnumeration):
    """Represents EU Energy Efficiency Class B as defined in EU energy labeling regulations.

    See https://schema.org/EUEnergyEfficiencyCategoryB.

    """

    locals().update({"@type": Field("EUEnergyEfficiencyCategoryB", const=True)})


EUEnergyEfficiencyCategoryB.update_forward_refs()
