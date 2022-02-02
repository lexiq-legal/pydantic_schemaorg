from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.SportsActivityLocation import SportsActivityLocation
from pydantic_schemaorg.CivicStructure import CivicStructure


class StadiumOrArena(SportsActivityLocation, CivicStructure):
    """A stadium.

    See: https://schema.org/StadiumOrArena
    Model depth: 4
    """
    type_: str = Field("StadiumOrArena", alias='@type')
    

