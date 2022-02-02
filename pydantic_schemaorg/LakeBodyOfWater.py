from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.BodyOfWater import BodyOfWater


class LakeBodyOfWater(BodyOfWater):
    """A lake (for example, Lake Pontrachain).

    See: https://schema.org/LakeBodyOfWater
    Model depth: 5
    """
    type_: str = Field("LakeBodyOfWater", alias='@type')
    

