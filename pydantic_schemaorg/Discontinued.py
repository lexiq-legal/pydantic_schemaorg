from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.ItemAvailability import ItemAvailability


class Discontinued(ItemAvailability):
    """Indicates that the item has been discontinued.

    See: https://schema.org/Discontinued
    Model depth: 5
    """
    type_: str = Field("Discontinued", alias='@type')
    

