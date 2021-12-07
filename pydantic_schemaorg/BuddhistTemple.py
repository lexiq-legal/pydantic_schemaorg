from pydantic import Field
from pydantic_schemaorg.PlaceOfWorship import PlaceOfWorship


class BuddhistTemple(PlaceOfWorship):
    """A Buddhist temple.

    See https://schema.org/BuddhistTemple.

    """
    type_: str = Field("BuddhistTemple", const=True, alias='@type')
    

BuddhistTemple.update_forward_refs()
