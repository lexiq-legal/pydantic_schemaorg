from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.BookFormatType import BookFormatType


class Paperback(BookFormatType):
    """Book format: Paperback.

    See: https://schema.org/Paperback
    Model depth: 5
    """

    type_: str = Field("Paperback", const=True, alias="@type")


if TYPE_CHECKING:

    Paperback.update_forward_refs()
