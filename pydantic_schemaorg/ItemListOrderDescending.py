from pydantic import Field
from pydantic_schemaorg.ItemListOrderType import ItemListOrderType


class ItemListOrderDescending(ItemListOrderType):
    """An ItemList ordered with higher values listed first.

    See https://schema.org/ItemListOrderDescending.

    """
    type_: str = Field("ItemListOrderDescending", const=True, alias='@type')
    

ItemListOrderDescending.update_forward_refs()
