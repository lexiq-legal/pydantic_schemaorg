from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.BodyOfWater import BodyOfWater


class Waterfall(BodyOfWater):
    """A waterfall, like Niagara.

    See: https://schema.org/Waterfall
    Model depth: 5
    """
    type_: str = Field(default="Waterfall", alias='@type', const=True)
    
