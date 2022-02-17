from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.AutomotiveBusiness import AutomotiveBusiness
from pydantic_schemaorg.Store import Store


class AutoPartsStore(AutomotiveBusiness, Store):
    """An auto parts store.

    See: https://schema.org/AutoPartsStore
    Model depth: 5
    """
    type_: str = Field("AutoPartsStore", alias='@type')
    

