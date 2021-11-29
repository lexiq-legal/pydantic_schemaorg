from pydantic import Field
from pydantic_schemaorg.EUEnergyEfficiencyEnumeration import EUEnergyEfficiencyEnumeration


class EUEnergyEfficiencyCategoryC(EUEnergyEfficiencyEnumeration):
    """Represents EU Energy Efficiency Class C as defined in EU energy labeling regulations.

    See https://schema.org/EUEnergyEfficiencyCategoryC.

    """

    locals().update({"@type": Field("EUEnergyEfficiencyCategoryC", const=True)})


EUEnergyEfficiencyCategoryC.update_forward_refs()
