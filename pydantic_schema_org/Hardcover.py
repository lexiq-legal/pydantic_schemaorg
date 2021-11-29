from pydantic import Field
from pydantic_schema_org.BookFormatType import BookFormatType


class Hardcover(BookFormatType):
    """Book format: Hardcover.

    See https://schema.org/Hardcover.

    """

    locals().update({"@type": Field("Hardcover", const=True)})


Hardcover.update_forward_refs()
