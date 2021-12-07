from pydantic import Field
from pydantic_schemaorg.BodyOfWater import BodyOfWater


class RiverBodyOfWater(BodyOfWater):
    """A river (for example, the broad majestic Shannon).

    See https://schema.org/RiverBodyOfWater.

    """
    type_: str = Field("RiverBodyOfWater", const=True, alias='@type')
    

RiverBodyOfWater.update_forward_refs()
