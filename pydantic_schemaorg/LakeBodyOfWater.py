from pydantic import Field
from pydantic_schemaorg.BodyOfWater import BodyOfWater


class LakeBodyOfWater(BodyOfWater):
    """A lake (for example, Lake Pontrachain).

    See https://schema.org/LakeBodyOfWater.

    """
    type_: str = Field("LakeBodyOfWater", const=True, alias='@type')
    

LakeBodyOfWater.update_forward_refs()
