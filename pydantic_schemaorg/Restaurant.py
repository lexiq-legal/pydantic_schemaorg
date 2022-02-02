from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.FoodEstablishment import FoodEstablishment


class Restaurant(FoodEstablishment):
    """A restaurant.

    See: https://schema.org/Restaurant
    Model depth: 5
    """
    type_: str = Field("Restaurant", alias='@type')
    

