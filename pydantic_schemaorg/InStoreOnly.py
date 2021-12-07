from pydantic import Field
from pydantic_schemaorg.ItemAvailability import ItemAvailability


class InStoreOnly(ItemAvailability):
    """Indicates that the item is available only at physical locations.

    See https://schema.org/InStoreOnly.

    """
    type_: str = Field("InStoreOnly", const=True, alias='@type')
    

InStoreOnly.update_forward_refs()
