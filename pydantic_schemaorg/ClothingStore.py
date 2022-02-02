from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Store import Store


class ClothingStore(Store):
    """A clothing store.

    See: https://schema.org/ClothingStore
    Model depth: 5
    """
    type_: str = Field("ClothingStore", alias='@type')
    

