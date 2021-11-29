from pydantic import Field
from pydantic_schemaorg.BodyOfWater import BodyOfWater


class RiverBodyOfWater(BodyOfWater):
    """A river (for example, the broad majestic Shannon).

    See https://schema.org/RiverBodyOfWater.

    """

    locals().update({"@type": Field("RiverBodyOfWater", const=True)})


RiverBodyOfWater.update_forward_refs()
