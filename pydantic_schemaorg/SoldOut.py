from pydantic import Field
from pydantic_schemaorg.ItemAvailability import ItemAvailability


class SoldOut(ItemAvailability):
    """Indicates that the item has sold out.

    See https://schema.org/SoldOut.

    """
    type_: str = Field("SoldOut", const=True, alias='@type')
    

SoldOut.update_forward_refs()
