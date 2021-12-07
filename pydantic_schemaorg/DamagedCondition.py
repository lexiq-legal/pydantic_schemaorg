from pydantic import Field
from pydantic_schemaorg.OfferItemCondition import OfferItemCondition


class DamagedCondition(OfferItemCondition):
    """Indicates that the item is damaged.

    See https://schema.org/DamagedCondition.

    """
    type_: str = Field("DamagedCondition", const=True, alias='@type')
    

DamagedCondition.update_forward_refs()
