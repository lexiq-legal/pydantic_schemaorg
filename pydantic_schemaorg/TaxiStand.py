from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.CivicStructure import CivicStructure


class TaxiStand(CivicStructure):
    """A taxi stand.

    See: https://schema.org/TaxiStand
    Model depth: 4
    """
    type_: str = Field("TaxiStand", alias='@type')
    

