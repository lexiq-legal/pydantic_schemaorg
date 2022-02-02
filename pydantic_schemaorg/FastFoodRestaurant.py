from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.FoodEstablishment import FoodEstablishment


class FastFoodRestaurant(FoodEstablishment):
    """A fast-food restaurant.

    See: https://schema.org/FastFoodRestaurant
    Model depth: 5
    """
    type_: str = Field("FastFoodRestaurant", alias='@type')
    

