from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Store import Store


class OutletStore(Store):
    """An outlet store.

    See: https://schema.org/OutletStore
    Model depth: 5
    """
    type_: str = Field("OutletStore", alias='@type')
    

