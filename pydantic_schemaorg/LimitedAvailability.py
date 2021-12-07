from pydantic import Field
from pydantic_schemaorg.ItemAvailability import ItemAvailability


class LimitedAvailability(ItemAvailability):
    """Indicates that the item has limited availability.

    See https://schema.org/LimitedAvailability.

    """
    type_: str = Field("LimitedAvailability", const=True, alias='@type')
    

LimitedAvailability.update_forward_refs()
