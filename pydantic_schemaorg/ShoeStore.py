from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Store import Store


class ShoeStore(Store):
    """A shoe store.

    See: https://schema.org/ShoeStore
    Model depth: 5
    """
    type_: str = Field("ShoeStore", alias='@type')
    

