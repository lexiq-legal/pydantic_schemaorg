from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.OfferItemCondition import OfferItemCondition


class UsedCondition(OfferItemCondition):
    """Indicates that the item is used.

    See: https://schema.org/UsedCondition
    Model depth: 5
    """
    type_: str = Field("UsedCondition", alias='@type')
    

