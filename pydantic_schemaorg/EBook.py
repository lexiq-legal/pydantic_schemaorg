from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.BookFormatType import BookFormatType


class EBook(BookFormatType):
    """Book format: Ebook.

    See: https://schema.org/EBook
    Model depth: 5
    """

    type_: str = Field("EBook", const=True, alias="@type")


if TYPE_CHECKING:

    EBook.update_forward_refs()
