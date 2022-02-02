from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.ItemAvailability import ItemAvailability


class PreOrder(ItemAvailability):
    """Indicates that the item is available for pre-order.

    See: https://schema.org/PreOrder
    Model depth: 5
    """
    type_: str = Field("PreOrder", alias='@type')
    

