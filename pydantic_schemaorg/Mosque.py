from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.PlaceOfWorship import PlaceOfWorship


class Mosque(PlaceOfWorship):
    """A mosque.

    See: https://schema.org/Mosque
    Model depth: 5
    """
    type_: str = Field("Mosque", alias='@type')
    

