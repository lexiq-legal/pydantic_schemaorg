from pydantic import Field
from pydantic_schemaorg.EUEnergyEfficiencyEnumeration import EUEnergyEfficiencyEnumeration


class EUEnergyEfficiencyCategoryA3Plus(EUEnergyEfficiencyEnumeration):
    """Represents EU Energy Efficiency Class A+++ as defined in EU energy labeling regulations.

    See https://schema.org/EUEnergyEfficiencyCategoryA3Plus.

    """

    locals().update({"@type": Field("EUEnergyEfficiencyCategoryA3Plus", const=True)})


EUEnergyEfficiencyCategoryA3Plus.update_forward_refs()
