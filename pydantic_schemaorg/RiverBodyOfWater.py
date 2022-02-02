from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.BodyOfWater import BodyOfWater


class RiverBodyOfWater(BodyOfWater):
    """A river (for example, the broad majestic Shannon).

    See: https://schema.org/RiverBodyOfWater
    Model depth: 5
    """
    type_: str = Field("RiverBodyOfWater", alias='@type')
    

