from pydantic import Field
from pydantic_schemaorg.Landform import Landform


class BodyOfWater(Landform):
    """A body of water, such as a sea, ocean, or lake.

    See https://schema.org/BodyOfWater.

    """
    type_: str = Field("BodyOfWater", const=True, alias='@type')
    

BodyOfWater.update_forward_refs()
