from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.ItemAvailability import ItemAvailability


class BackOrder(ItemAvailability):
    """Indicates that the item is available on back order.

    See: https://schema.org/BackOrder
    Model depth: 5
    """
    type_: str = Field("BackOrder", alias='@type')
    

