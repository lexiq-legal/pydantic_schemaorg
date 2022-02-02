from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.ItemListOrderType import ItemListOrderType


class ItemListOrderAscending(ItemListOrderType):
    """An ItemList ordered with lower values listed first.

    See: https://schema.org/ItemListOrderAscending
    Model depth: 5
    """
    type_: str = Field("ItemListOrderAscending", alias='@type')
    

