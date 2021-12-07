from pydantic import Field
from pydantic_schemaorg.Enumeration import Enumeration


class BookFormatType(Enumeration):
    """The publication format of the book.

    See https://schema.org/BookFormatType.

    """
    type_: str = Field("BookFormatType", const=True, alias='@type')
    

BookFormatType.update_forward_refs()
