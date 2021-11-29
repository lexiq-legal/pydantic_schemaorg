from pydantic import Field
from pydantic_schemaorg.Enumeration import Enumeration


class ItemListOrderType(Enumeration):
    """Enumerated for values for itemListOrder for indicating how an ordered ItemList is organized.

    See https://schema.org/ItemListOrderType.

    """

    locals().update({"@type": Field("ItemListOrderType", const=True)})


ItemListOrderType.update_forward_refs()
