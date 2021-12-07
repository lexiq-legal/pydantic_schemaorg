from pydantic import Field
from pydantic_schemaorg.ItemAvailability import ItemAvailability


class PreOrder(ItemAvailability):
    """Indicates that the item is available for pre-order.

    See https://schema.org/PreOrder.

    """
    type_: str = Field("PreOrder", const=True, alias='@type')
    

PreOrder.update_forward_refs()
