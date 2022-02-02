from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.LocalBusiness import LocalBusiness


class Store(LocalBusiness):
    """A retail good store.

    See: https://schema.org/Store
    Model depth: 4
    """
    type_: str = Field("Store", alias='@type')
    

