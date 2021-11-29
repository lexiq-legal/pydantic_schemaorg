from pydantic import Field
from pydantic_schemaorg.BodyOfWater import BodyOfWater


class Canal(BodyOfWater):
    """A canal, like the Panama Canal.

    See https://schema.org/Canal.

    """

    locals().update({"@type": Field("Canal", const=True)})


Canal.update_forward_refs()
