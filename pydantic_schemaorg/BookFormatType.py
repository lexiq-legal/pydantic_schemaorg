from pydantic import Field
from pydantic_schemaorg.Enumeration import Enumeration


class BookFormatType(Enumeration):
    """The publication format of the book.

    See https://schema.org/BookFormatType.

    """

    locals().update({"@type": Field("BookFormatType", const=True)})


BookFormatType.update_forward_refs()
