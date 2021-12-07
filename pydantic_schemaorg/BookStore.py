from pydantic import Field
from pydantic_schemaorg.Store import Store


class BookStore(Store):
    """A bookstore.

    See https://schema.org/BookStore.

    """
    type_: str = Field("BookStore", const=True, alias='@type')
    

BookStore.update_forward_refs()
