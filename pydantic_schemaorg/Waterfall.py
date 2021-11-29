from pydantic import Field
from pydantic_schemaorg.BodyOfWater import BodyOfWater


class Waterfall(BodyOfWater):
    """A waterfall, like Niagara.

    See https://schema.org/Waterfall.

    """

    locals().update({"@type": Field("Waterfall", const=True)})


Waterfall.update_forward_refs()
