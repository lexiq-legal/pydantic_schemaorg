from pydantic import Field
from pydantic_schemaorg.ItemAvailability import ItemAvailability


class Discontinued(ItemAvailability):
    """Indicates that the item has been discontinued.

    See https://schema.org/Discontinued.

    """
    type_: str = Field("Discontinued", const=True, alias='@type')
    

Discontinued.update_forward_refs()
