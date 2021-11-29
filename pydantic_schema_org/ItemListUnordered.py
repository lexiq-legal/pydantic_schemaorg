from pydantic import Field
from pydantic_schema_org.ItemListOrderType import ItemListOrderType


class ItemListUnordered(ItemListOrderType):
    """An ItemList ordered with no explicit order.

    See https://schema.org/ItemListUnordered.

    """

    locals().update({"@type": Field("ItemListUnordered", const=True)})


ItemListUnordered.update_forward_refs()
