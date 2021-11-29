from pydantic import Field
from pydantic_schemaorg.EUEnergyEfficiencyEnumeration import EUEnergyEfficiencyEnumeration


class EUEnergyEfficiencyCategoryD(EUEnergyEfficiencyEnumeration):
    """Represents EU Energy Efficiency Class D as defined in EU energy labeling regulations.

    See https://schema.org/EUEnergyEfficiencyCategoryD.

    """

    locals().update({"@type": Field("EUEnergyEfficiencyCategoryD", const=True)})


EUEnergyEfficiencyCategoryD.update_forward_refs()
