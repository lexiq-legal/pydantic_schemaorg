from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.ItemAvailability import ItemAvailability


class PreSale(ItemAvailability):
    """Indicates that the item is available for ordering and delivery before general availability.

    See: https://schema.org/PreSale
    Model depth: 5
    """
    type_: str = Field("PreSale", alias='@type')
    

