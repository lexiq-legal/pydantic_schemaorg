from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.PriceComponentTypeEnumeration import PriceComponentTypeEnumeration


class Subscription(PriceComponentTypeEnumeration):
    """Represents the subscription pricing component of the total price for an offered product.

    See: https://schema.org/Subscription
    Model depth: 5
    """
    type_: str = Field("Subscription", alias='@type')
    

