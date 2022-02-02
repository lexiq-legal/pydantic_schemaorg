from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Landform import Landform


class BodyOfWater(Landform):
    """A body of water, such as a sea, ocean, or lake.

    See: https://schema.org/BodyOfWater
    Model depth: 4
    """
    type_: str = Field("BodyOfWater", alias='@type')
    

