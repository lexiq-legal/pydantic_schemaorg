from pydantic import Field
from pydantic_schemaorg.Store import Store


class BookStore(Store):
    """A bookstore.

    See https://schema.org/BookStore.

    """

    locals().update({"@type": Field("BookStore", const=True)})


BookStore.update_forward_refs()
