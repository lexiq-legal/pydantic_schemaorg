from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Store import Store


class FurnitureStore(Store):
    """A furniture store.

    See: https://schema.org/FurnitureStore
    Model depth: 5
    """
    type_: str = Field("FurnitureStore", alias='@type')
    

