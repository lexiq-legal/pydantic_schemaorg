from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.PlaceOfWorship import PlaceOfWorship


class HinduTemple(PlaceOfWorship):
    """A Hindu temple.

    See: https://schema.org/HinduTemple
    Model depth: 5
    """
    type_: str = Field("HinduTemple", alias='@type')
    

