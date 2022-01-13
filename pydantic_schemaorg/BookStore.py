from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Store import Store


class BookStore(Store):
    """A bookstore.

    See: https://schema.org/BookStore
    Model depth: 5
    """

    type_: str = Field("BookStore", const=True, alias="@type")


if TYPE_CHECKING:

    BookStore.update_forward_refs()
