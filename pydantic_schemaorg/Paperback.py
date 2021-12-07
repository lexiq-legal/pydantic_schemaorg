from pydantic import Field
from pydantic_schemaorg.BookFormatType import BookFormatType


class Paperback(BookFormatType):
    """Book format: Paperback.

    See https://schema.org/Paperback.

    """
    type_: str = Field("Paperback", const=True, alias='@type')
    

Paperback.update_forward_refs()
