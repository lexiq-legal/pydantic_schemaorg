from pydantic import Field
from pydantic_schemaorg.OfferItemCondition import OfferItemCondition


class NewCondition(OfferItemCondition):
    """Indicates that the item is new.

    See https://schema.org/NewCondition.

    """
    type_: str = Field("NewCondition", const=True, alias='@type')
    

NewCondition.update_forward_refs()
