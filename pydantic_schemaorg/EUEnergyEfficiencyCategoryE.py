from pydantic import Field
from pydantic_schemaorg.EUEnergyEfficiencyEnumeration import EUEnergyEfficiencyEnumeration


class EUEnergyEfficiencyCategoryE(EUEnergyEfficiencyEnumeration):
    """Represents EU Energy Efficiency Class E as defined in EU energy labeling regulations.

    See https://schema.org/EUEnergyEfficiencyCategoryE.

    """

    locals().update({"@type": Field("EUEnergyEfficiencyCategoryE", const=True)})


EUEnergyEfficiencyCategoryE.update_forward_refs()
