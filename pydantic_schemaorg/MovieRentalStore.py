from pydantic import Field
from pydantic_schemaorg.Store import Store


class MovieRentalStore(Store):
    """A movie rental store.

    See https://schema.org/MovieRentalStore.

    """
    type_: str = Field("MovieRentalStore", const=True, alias='@type')
    

MovieRentalStore.update_forward_refs()
