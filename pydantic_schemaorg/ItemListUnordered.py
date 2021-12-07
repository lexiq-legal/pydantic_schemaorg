from pydantic import Field
from pydantic_schemaorg.ItemListOrderType import ItemListOrderType


class ItemListUnordered(ItemListOrderType):
    """An ItemList ordered with no explicit order.

    See https://schema.org/ItemListUnordered.

    """
    type_: str = Field("ItemListUnordered", const=True, alias='@type')
    

ItemListUnordered.update_forward_refs()
