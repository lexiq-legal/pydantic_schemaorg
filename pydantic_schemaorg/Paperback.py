from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.BookFormatType import BookFormatType


class Paperback(BookFormatType):
    """Book format: Paperback.

    See: https://schema.org/Paperback
    Model depth: 5
    """
    type_: str = Field("Paperback", alias='@type')
    

