from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.PlaceOfWorship import PlaceOfWorship


class Synagogue(PlaceOfWorship):
    """A synagogue.

    See: https://schema.org/Synagogue
    Model depth: 5
    """
    type_: str = Field("Synagogue", alias='@type')
    

