from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.FoodEstablishment import FoodEstablishment


class BarOrPub(FoodEstablishment):
    """A bar or pub.

    See: https://schema.org/BarOrPub
    Model depth: 5
    """
    type_: str = Field("BarOrPub", alias='@type')
    

