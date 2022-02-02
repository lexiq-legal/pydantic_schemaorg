from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.PlaceOfWorship import PlaceOfWorship


class Church(PlaceOfWorship):
    """A church.

    See: https://schema.org/Church
    Model depth: 5
    """
    type_: str = Field("Church", alias='@type')
    

