from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Store import Store


class MovieRentalStore(Store):
    """A movie rental store.

    See: https://schema.org/MovieRentalStore
    Model depth: 5
    """
    type_: str = Field("MovieRentalStore", alias='@type')
    

