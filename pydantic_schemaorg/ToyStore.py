from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Store import Store


class ToyStore(Store):
    """A toy store.

    See: https://schema.org/ToyStore
    Model depth: 5
    """
    type_: str = Field("ToyStore", alias='@type')
    

