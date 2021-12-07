from pydantic import Field
from pydantic_schemaorg.BodyOfWater import BodyOfWater


class Canal(BodyOfWater):
    """A canal, like the Panama Canal.

    See https://schema.org/Canal.

    """
    type_: str = Field("Canal", const=True, alias='@type')
    

Canal.update_forward_refs()
