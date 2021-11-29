from pydantic import Field
from pydantic_schemaorg.ItemListOrderType import ItemListOrderType


class ItemListOrderDescending(ItemListOrderType):
    """An ItemList ordered with higher values listed first.

    See https://schema.org/ItemListOrderDescending.

    """

    locals().update({"@type": Field("ItemListOrderDescending", const=True)})


ItemListOrderDescending.update_forward_refs()
