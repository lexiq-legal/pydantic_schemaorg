from pydantic import Field
from pydantic_schemaorg.Enumeration import Enumeration


class EnergyEfficiencyEnumeration(Enumeration):
    """Enumerates energy efficiency levels (also known as \"classes\" or \"ratings\") and"
     "certifications that are part of several international energy efficiency standards.

    See https://schema.org/EnergyEfficiencyEnumeration.

    """

    locals().update({"@type": Field("EnergyEfficiencyEnumeration", const=True)})


EnergyEfficiencyEnumeration.update_forward_refs()
