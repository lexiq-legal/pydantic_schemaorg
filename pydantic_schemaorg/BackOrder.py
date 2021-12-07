from pydantic import Field
from pydantic_schemaorg.ItemAvailability import ItemAvailability


class BackOrder(ItemAvailability):
    """Indicates that the item is available on back order.

    See https://schema.org/BackOrder.

    """
    type_: str = Field("BackOrder", const=True, alias='@type')
    

BackOrder.update_forward_refs()
