from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Enumeration import Enumeration


class EnergyEfficiencyEnumeration(Enumeration):
    """Enumerates energy efficiency levels (also known as \"classes\" or \"ratings\") and"
     "certifications that are part of several international energy efficiency standards.

    See: https://schema.org/EnergyEfficiencyEnumeration
    Model depth: 4
    """
    type_: str = Field("EnergyEfficiencyEnumeration", alias='@type')
    

