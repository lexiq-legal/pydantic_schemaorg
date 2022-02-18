from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.OfferItemCondition import OfferItemCondition


class DamagedCondition(OfferItemCondition):
    """Indicates that the item is damaged.

    See: https://schema.org/DamagedCondition
    Model depth: 5
    """
    type_: str = Field(default="DamagedCondition", alias='@type', const=True)
    
