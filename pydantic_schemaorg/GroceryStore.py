from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Store import Store


class GroceryStore(Store):
    """A grocery store.

    See: https://schema.org/GroceryStore
    Model depth: 5
    """
    type_: str = Field("GroceryStore", alias='@type')
    

