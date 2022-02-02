from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Enumeration import Enumeration


class BookFormatType(Enumeration):
    """The publication format of the book.

    See: https://schema.org/BookFormatType
    Model depth: 4
    """
    type_: str = Field("BookFormatType", alias='@type')
    

