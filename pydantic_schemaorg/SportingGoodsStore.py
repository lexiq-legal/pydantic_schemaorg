from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Store import Store


class SportingGoodsStore(Store):
    """A sporting goods store.

    See: https://schema.org/SportingGoodsStore
    Model depth: 5
    """
    type_: str = Field("SportingGoodsStore", alias='@type')
    

