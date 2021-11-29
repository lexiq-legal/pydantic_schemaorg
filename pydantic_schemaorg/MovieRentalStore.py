from pydantic import Field
from pydantic_schemaorg.Store import Store


class MovieRentalStore(Store):
    """A movie rental store.

    See https://schema.org/MovieRentalStore.

    """

    locals().update({"@type": Field("MovieRentalStore", const=True)})


MovieRentalStore.update_forward_refs()
