from pydantic import Field
from pydantic_schemaorg.Enumeration import Enumeration


class ItemListOrderType(Enumeration):
    """Enumerated for values for itemListOrder for indicating how an ordered ItemList is organized.

    See https://schema.org/ItemListOrderType.

    """
    type_: str = Field("ItemListOrderType", const=True, alias='@type')
    

ItemListOrderType.update_forward_refs()
