from pydantic import Field
from pydantic_schemaorg.BodyOfWater import BodyOfWater


class SeaBodyOfWater(BodyOfWater):
    """A sea (for example, the Caspian sea).

    See https://schema.org/SeaBodyOfWater.

    """

    locals().update({"@type": Field("SeaBodyOfWater", const=True)})


SeaBodyOfWater.update_forward_refs()
