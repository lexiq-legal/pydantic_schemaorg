from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.BodyOfWater import BodyOfWater


class Pond(BodyOfWater):
    """A pond.

    See: https://schema.org/Pond
    Model depth: 5
    """
    type_: str = Field("Pond", alias='@type')
    

