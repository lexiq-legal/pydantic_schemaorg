from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.LocalBusiness import LocalBusiness


class ShoppingCenter(LocalBusiness):
    """A shopping center or mall.

    See: https://schema.org/ShoppingCenter
    Model depth: 4
    """
    type_: str = Field("ShoppingCenter", alias='@type')
    

