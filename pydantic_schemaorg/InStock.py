from pydantic import Field
from pydantic_schemaorg.ItemAvailability import ItemAvailability


class InStock(ItemAvailability):
    """Indicates that the item is in stock.

    See https://schema.org/InStock.

    """
    type_: str = Field("InStock", const=True, alias='@type')
    

InStock.update_forward_refs()
