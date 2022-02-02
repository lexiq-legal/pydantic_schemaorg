from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.ItemListOrderType import ItemListOrderType


class ItemListUnordered(ItemListOrderType):
    """An ItemList ordered with no explicit order.

    See: https://schema.org/ItemListUnordered
    Model depth: 5
    """
    type_: str = Field("ItemListUnordered", alias='@type')
    

