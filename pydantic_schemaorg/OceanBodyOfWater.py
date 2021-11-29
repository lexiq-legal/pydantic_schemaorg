from pydantic import Field
from pydantic_schemaorg.BodyOfWater import BodyOfWater


class OceanBodyOfWater(BodyOfWater):
    """An ocean (for example, the Pacific).

    See https://schema.org/OceanBodyOfWater.

    """

    locals().update({"@type": Field("OceanBodyOfWater", const=True)})


OceanBodyOfWater.update_forward_refs()
