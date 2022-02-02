from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Store import Store


class JewelryStore(Store):
    """A jewelry store.

    See: https://schema.org/JewelryStore
    Model depth: 5
    """
    type_: str = Field("JewelryStore", alias='@type')
    

