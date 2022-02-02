from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Store import Store


class MusicStore(Store):
    """A music store.

    See: https://schema.org/MusicStore
    Model depth: 5
    """
    type_: str = Field("MusicStore", alias='@type')
    

