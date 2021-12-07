from pydantic import Field
from pydantic_schemaorg.OfferItemCondition import OfferItemCondition


class UsedCondition(OfferItemCondition):
    """Indicates that the item is used.

    See https://schema.org/UsedCondition.

    """
    type_: str = Field("UsedCondition", const=True, alias='@type')
    

UsedCondition.update_forward_refs()
