from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Store import Store


class ElectronicsStore(Store):
    """An electronics store.

    See: https://schema.org/ElectronicsStore
    Model depth: 5
    """
    type_: str = Field("ElectronicsStore", alias='@type')
    

