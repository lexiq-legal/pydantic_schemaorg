from pydantic import Field
from pydantic_schemaorg.Enumeration import Enumeration


class OfferItemCondition(Enumeration):
    """A list of possible conditions for the item.

    See https://schema.org/OfferItemCondition.

    """
    type_: str = Field("OfferItemCondition", const=True, alias='@type')
    

OfferItemCondition.update_forward_refs()
