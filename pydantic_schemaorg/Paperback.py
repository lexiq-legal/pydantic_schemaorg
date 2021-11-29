from pydantic import Field
from pydantic_schemaorg.BookFormatType import BookFormatType


class Paperback(BookFormatType):
    """Book format: Paperback.

    See https://schema.org/Paperback.

    """

    locals().update({"@type": Field("Paperback", const=True)})


Paperback.update_forward_refs()
