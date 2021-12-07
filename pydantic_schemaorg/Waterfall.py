from pydantic import Field
from pydantic_schemaorg.BodyOfWater import BodyOfWater


class Waterfall(BodyOfWater):
    """A waterfall, like Niagara.

    See https://schema.org/Waterfall.

    """
    type_: str = Field("Waterfall", const=True, alias='@type')
    

Waterfall.update_forward_refs()
