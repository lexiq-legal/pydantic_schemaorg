from pydantic import Field
from pydantic_schemaorg.BodyOfWater import BodyOfWater


class Pond(BodyOfWater):
    """A pond.

    See https://schema.org/Pond.

    """
    type_: str = Field("Pond", const=True, alias='@type')
    

Pond.update_forward_refs()
