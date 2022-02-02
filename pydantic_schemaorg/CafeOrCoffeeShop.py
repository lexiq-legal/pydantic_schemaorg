from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.FoodEstablishment import FoodEstablishment


class CafeOrCoffeeShop(FoodEstablishment):
    """A cafe or coffee shop.

    See: https://schema.org/CafeOrCoffeeShop
    Model depth: 5
    """
    type_: str = Field("CafeOrCoffeeShop", alias='@type')
    

