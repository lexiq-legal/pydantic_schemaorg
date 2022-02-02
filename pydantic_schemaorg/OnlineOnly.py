from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.ItemAvailability import ItemAvailability


class OnlineOnly(ItemAvailability):
    """Indicates that the item is available only online.

    See: https://schema.org/OnlineOnly
    Model depth: 5
    """
    type_: str = Field("OnlineOnly", alias='@type')
    

