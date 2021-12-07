from pydantic import Field
from pydantic_schemaorg.PlaceOfWorship import PlaceOfWorship


class HinduTemple(PlaceOfWorship):
    """A Hindu temple.

    See https://schema.org/HinduTemple.

    """
    type_: str = Field("HinduTemple", const=True, alias='@type')
    

HinduTemple.update_forward_refs()
