from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.BookFormatType import BookFormatType


class EBook(BookFormatType):
    """Book format: Ebook.

    See: https://schema.org/EBook
    Model depth: 5
    """
    type_: str = Field("EBook", alias='@type')
    

