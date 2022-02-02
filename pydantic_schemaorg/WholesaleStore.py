from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Store import Store


class WholesaleStore(Store):
    """A wholesale store.

    See: https://schema.org/WholesaleStore
    Model depth: 5
    """
    type_: str = Field("WholesaleStore", alias='@type')
    

