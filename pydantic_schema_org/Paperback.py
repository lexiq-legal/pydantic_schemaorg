from pydantic import Field
from pydantic_schema_org.BookFormatType import BookFormatType


class Paperback(BookFormatType):
    """Book format: Paperback.

    See https://schema.org/Paperback.

    """

    locals().update({"@type": Field("Paperback", const=True)})


Paperback.update_forward_refs()
