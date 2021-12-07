from pydantic import Field
from pydantic_schemaorg.Enumeration import Enumeration


class ItemAvailability(Enumeration):
    """A list of possible product availability options.

    See https://schema.org/ItemAvailability.

    """
    type_: str = Field("ItemAvailability", const=True, alias='@type')
    

ItemAvailability.update_forward_refs()
