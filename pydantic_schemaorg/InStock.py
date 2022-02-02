from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.ItemAvailability import ItemAvailability


class InStock(ItemAvailability):
    """Indicates that the item is in stock.

    See: https://schema.org/InStock
    Model depth: 5
    """
    type_: str = Field("InStock", alias='@type')
    

