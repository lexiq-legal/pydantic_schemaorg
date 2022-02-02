from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Store import Store


class TireShop(Store):
    """A tire shop.

    See: https://schema.org/TireShop
    Model depth: 5
    """
    type_: str = Field("TireShop", alias='@type')
    

