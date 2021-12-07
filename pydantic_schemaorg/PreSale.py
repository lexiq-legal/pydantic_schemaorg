from pydantic import Field
from pydantic_schemaorg.ItemAvailability import ItemAvailability


class PreSale(ItemAvailability):
    """Indicates that the item is available for ordering and delivery before general availability.

    See https://schema.org/PreSale.

    """
    type_: str = Field("PreSale", const=True, alias='@type')
    

PreSale.update_forward_refs()
