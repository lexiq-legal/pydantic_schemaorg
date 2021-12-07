from pydantic import Field
from pydantic_schemaorg.BodyOfWater import BodyOfWater


class Reservoir(BodyOfWater):
    """A reservoir of water, typically an artificially created lake, like the Lake Kariba reservoir.

    See https://schema.org/Reservoir.

    """
    type_: str = Field("Reservoir", const=True, alias='@type')
    

Reservoir.update_forward_refs()
