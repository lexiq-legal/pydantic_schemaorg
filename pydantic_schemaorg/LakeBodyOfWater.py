from pydantic import Field
from pydantic_schemaorg.BodyOfWater import BodyOfWater


class LakeBodyOfWater(BodyOfWater):
    """A lake (for example, Lake Pontrachain).

    See https://schema.org/LakeBodyOfWater.

    """

    locals().update({"@type": Field("LakeBodyOfWater", const=True)})


LakeBodyOfWater.update_forward_refs()
