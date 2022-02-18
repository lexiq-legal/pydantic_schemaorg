from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Store import Store


class BikeStore(Store):
    """A bike store.

    See: https://schema.org/BikeStore
    Model depth: 5
    """
    type_: str = Field(default="BikeStore", alias='@type', const=True)
    
