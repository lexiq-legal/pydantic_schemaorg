from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.OfferItemCondition import OfferItemCondition


class NewCondition(OfferItemCondition):
    """Indicates that the item is new.

    See: https://schema.org/NewCondition
    Model depth: 5
    """
    type_: str = Field("NewCondition", alias='@type')
    

