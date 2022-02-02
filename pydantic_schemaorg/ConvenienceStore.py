from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Store import Store


class ConvenienceStore(Store):
    """A convenience store.

    See: https://schema.org/ConvenienceStore
    Model depth: 5
    """
    type_: str = Field("ConvenienceStore", alias='@type')
    

