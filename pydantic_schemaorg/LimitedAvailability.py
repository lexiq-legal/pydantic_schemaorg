from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.ItemAvailability import ItemAvailability


class LimitedAvailability(ItemAvailability):
    """Indicates that the item has limited availability.

    See: https://schema.org/LimitedAvailability
    Model depth: 5
    """
    type_: str = Field("LimitedAvailability", alias='@type')
    

