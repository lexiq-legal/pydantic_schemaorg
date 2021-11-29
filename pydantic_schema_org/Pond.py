from pydantic import Field
from pydantic_schema_org.BodyOfWater import BodyOfWater


class Pond(BodyOfWater):
    """A pond.

    See https://schema.org/Pond.

    """

    locals().update({"@type": Field("Pond", const=True)})


Pond.update_forward_refs()
