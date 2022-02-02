from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.CivicStructure import CivicStructure


class BusStation(CivicStructure):
    """A bus station.

    See: https://schema.org/BusStation
    Model depth: 4
    """
    type_: str = Field("BusStation", alias='@type')
    

