from pydantic import Field
from pydantic_schema_org.Landform import Landform


class BodyOfWater(Landform):
    """A body of water, such as a sea, ocean, or lake.

    See https://schema.org/BodyOfWater.

    """

    locals().update({"@type": Field("BodyOfWater", const=True)})


BodyOfWater.update_forward_refs()
