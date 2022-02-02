from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.PlaceOfWorship import PlaceOfWorship


class BuddhistTemple(PlaceOfWorship):
    """A Buddhist temple.

    See: https://schema.org/BuddhistTemple
    Model depth: 5
    """
    type_: str = Field("BuddhistTemple", alias='@type')
    

