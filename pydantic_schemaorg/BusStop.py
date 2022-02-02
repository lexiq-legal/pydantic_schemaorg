from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.CivicStructure import CivicStructure


class BusStop(CivicStructure):
    """A bus stop.

    See: https://schema.org/BusStop
    Model depth: 4
    """
    type_: str = Field("BusStop", alias='@type')
    

