from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Store import Store


class LiquorStore(Store):
    """A shop that sells alcoholic drinks such as wine, beer, whisky and other spirits.

    See: https://schema.org/LiquorStore
    Model depth: 5
    """
    type_: str = Field("LiquorStore", alias='@type')
    

