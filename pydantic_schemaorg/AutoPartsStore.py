from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Store import Store
from pydantic_schemaorg.AutomotiveBusiness import AutomotiveBusiness


class AutoPartsStore(Store, AutomotiveBusiness):
    """An auto parts store.

    See: https://schema.org/AutoPartsStore
    Model depth: 5
    """
    type_: str = Field("AutoPartsStore", alias='@type')
    

