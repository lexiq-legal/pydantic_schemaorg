from pydantic import Field
from pydantic_schema_org.BookFormatType import BookFormatType


class EBook(BookFormatType):
    """Book format: Ebook.

    See https://schema.org/EBook.

    """

    locals().update({"@type": Field("EBook", const=True)})


EBook.update_forward_refs()
