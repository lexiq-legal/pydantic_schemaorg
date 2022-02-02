from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.FoodEstablishment import FoodEstablishment


class IceCreamShop(FoodEstablishment):
    """An ice cream shop.

    See: https://schema.org/IceCreamShop
    Model depth: 5
    """
    type_: str = Field("IceCreamShop", alias='@type')
    

