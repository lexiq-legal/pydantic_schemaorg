from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.CivicStructure import CivicStructure


class MusicVenue(CivicStructure):
    """A music venue.

    See: https://schema.org/MusicVenue
    Model depth: 4
    """
    type_: str = Field("MusicVenue", alias='@type')
    

