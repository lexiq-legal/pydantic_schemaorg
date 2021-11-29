from pydantic import Field
from pydantic_schemaorg.EUEnergyEfficiencyEnumeration import EUEnergyEfficiencyEnumeration


class EUEnergyEfficiencyCategoryA(EUEnergyEfficiencyEnumeration):
    """Represents EU Energy Efficiency Class A as defined in EU energy labeling regulations.

    See https://schema.org/EUEnergyEfficiencyCategoryA.

    """

    locals().update({"@type": Field("EUEnergyEfficiencyCategoryA", const=True)})


EUEnergyEfficiencyCategoryA.update_forward_refs()
