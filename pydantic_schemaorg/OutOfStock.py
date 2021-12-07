from pydantic import Field
from pydantic_schemaorg.ItemAvailability import ItemAvailability


class OutOfStock(ItemAvailability):
    """Indicates that the item is out of stock.

    See https://schema.org/OutOfStock.

    """
    type_: str = Field("OutOfStock", const=True, alias='@type')
    

OutOfStock.update_forward_refs()
