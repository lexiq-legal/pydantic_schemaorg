from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Store import Store


class MensClothingStore(Store):
    """A men's clothing store.

    See: https://schema.org/MensClothingStore
    Model depth: 5
    """
    type_: str = Field("MensClothingStore", alias='@type')
    

