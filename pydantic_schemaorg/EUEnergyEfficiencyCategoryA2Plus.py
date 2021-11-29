from pydantic import Field
from pydantic_schemaorg.EUEnergyEfficiencyEnumeration import EUEnergyEfficiencyEnumeration


class EUEnergyEfficiencyCategoryA2Plus(EUEnergyEfficiencyEnumeration):
    """Represents EU Energy Efficiency Class A++ as defined in EU energy labeling regulations.

    See https://schema.org/EUEnergyEfficiencyCategoryA2Plus.

    """

    locals().update({"@type": Field("EUEnergyEfficiencyCategoryA2Plus", const=True)})


EUEnergyEfficiencyCategoryA2Plus.update_forward_refs()
