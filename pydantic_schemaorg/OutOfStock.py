from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.ItemAvailability import ItemAvailability


class OutOfStock(ItemAvailability):
    """Indicates that the item is out of stock.

    See: https://schema.org/OutOfStock
    Model depth: 5
    """
    type_: str = Field("OutOfStock", alias='@type')
    

