from pydantic import Field
from pydantic_schemaorg.OfferItemCondition import OfferItemCondition


class RefurbishedCondition(OfferItemCondition):
    """Indicates that the item is refurbished.

    See https://schema.org/RefurbishedCondition.

    """
    type_: str = Field("RefurbishedCondition", const=True, alias='@type')
    

RefurbishedCondition.update_forward_refs()
