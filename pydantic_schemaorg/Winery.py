from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.FoodEstablishment import FoodEstablishment


class Winery(FoodEstablishment):
    """A winery.

    See: https://schema.org/Winery
    Model depth: 5
    """
    type_: str = Field("Winery", alias='@type')
    

