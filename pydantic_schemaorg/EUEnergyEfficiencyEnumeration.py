from pydantic import Field
from pydantic_schemaorg.EnergyEfficiencyEnumeration import EnergyEfficiencyEnumeration


class EUEnergyEfficiencyEnumeration(EnergyEfficiencyEnumeration):
    """Enumerates the EU energy efficiency classes A-G as well as A+, A++, and A+++ as defined"
     "in EU directive 2017/1369.

    See https://schema.org/EUEnergyEfficiencyEnumeration.

    """

    locals().update({"@type": Field("EUEnergyEfficiencyEnumeration", const=True)})


EUEnergyEfficiencyEnumeration.update_forward_refs()
