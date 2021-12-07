from pydantic import Field
from pydantic_schemaorg.BookFormatType import BookFormatType


class Hardcover(BookFormatType):
    """Book format: Hardcover.

    See https://schema.org/Hardcover.

    """
    type_: str = Field("Hardcover", const=True, alias='@type')
    

Hardcover.update_forward_refs()
