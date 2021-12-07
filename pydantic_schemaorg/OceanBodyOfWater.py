from pydantic import Field
from pydantic_schemaorg.BodyOfWater import BodyOfWater


class OceanBodyOfWater(BodyOfWater):
    """An ocean (for example, the Pacific).

    See https://schema.org/OceanBodyOfWater.

    """
    type_: str = Field("OceanBodyOfWater", const=True, alias='@type')
    

OceanBodyOfWater.update_forward_refs()
