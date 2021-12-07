from pydantic import Field
from pydantic_schemaorg.BookFormatType import BookFormatType


class EBook(BookFormatType):
    """Book format: Ebook.

    See https://schema.org/EBook.

    """
    type_: str = Field("EBook", const=True, alias='@type')
    

EBook.update_forward_refs()
