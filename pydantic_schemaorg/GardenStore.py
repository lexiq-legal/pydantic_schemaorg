from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Store import Store


class GardenStore(Store):
    """A garden store.

    See: https://schema.org/GardenStore
    Model depth: 5
    """
    type_: str = Field("GardenStore", alias='@type')
    

