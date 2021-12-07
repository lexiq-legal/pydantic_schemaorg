from pydantic import Field
from pydantic_schemaorg.ItemAvailability import ItemAvailability


class OnlineOnly(ItemAvailability):
    """Indicates that the item is available only online.

    See https://schema.org/OnlineOnly.

    """
    type_: str = Field("OnlineOnly", const=True, alias='@type')
    

OnlineOnly.update_forward_refs()
