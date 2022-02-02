from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.FoodEstablishment import FoodEstablishment


class Bakery(FoodEstablishment):
    """A bakery.

    See: https://schema.org/Bakery
    Model depth: 5
    """
    type_: str = Field("Bakery", alias='@type')
    

