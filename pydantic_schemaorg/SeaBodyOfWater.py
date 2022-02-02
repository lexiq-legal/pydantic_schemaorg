from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.BodyOfWater import BodyOfWater


class SeaBodyOfWater(BodyOfWater):
    """A sea (for example, the Caspian sea).

    See: https://schema.org/SeaBodyOfWater
    Model depth: 5
    """
    type_: str = Field("SeaBodyOfWater", alias='@type')
    

