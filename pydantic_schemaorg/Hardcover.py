from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.BookFormatType import BookFormatType


class Hardcover(BookFormatType):
    """Book format: Hardcover.

    See: https://schema.org/Hardcover
    Model depth: 5
    """
    type_: str = Field("Hardcover", alias='@type')
    

