from pydantic import Field
from pydantic_schemaorg.ItemListOrderType import ItemListOrderType


class ItemListOrderAscending(ItemListOrderType):
    """An ItemList ordered with lower values listed first.

    See https://schema.org/ItemListOrderAscending.

    """

    locals().update({"@type": Field("ItemListOrderAscending", const=True)})


ItemListOrderAscending.update_forward_refs()
