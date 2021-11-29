from pydantic import Field
from pydantic_schemaorg.BodyOfWater import BodyOfWater


class Reservoir(BodyOfWater):
    """A reservoir of water, typically an artificially created lake, like the Lake Kariba reservoir.

    See https://schema.org/Reservoir.

    """

    locals().update({"@type": Field("Reservoir", const=True)})


Reservoir.update_forward_refs()
