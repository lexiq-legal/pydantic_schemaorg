from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.BodyOfWater import BodyOfWater


class Canal(BodyOfWater):
    """A canal, like the Panama Canal.

    See: https://schema.org/Canal
    Model depth: 5
    """
    type_: str = Field("Canal", alias='@type')
    

