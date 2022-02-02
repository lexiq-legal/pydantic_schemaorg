from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Store import Store


class HardwareStore(Store):
    """A hardware store.

    See: https://schema.org/HardwareStore
    Model depth: 5
    """
    type_: str = Field("HardwareStore", alias='@type')
    

