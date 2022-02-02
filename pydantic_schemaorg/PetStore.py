from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Store import Store


class PetStore(Store):
    """A pet store.

    See: https://schema.org/PetStore
    Model depth: 5
    """
    type_: str = Field("PetStore", alias='@type')
    

