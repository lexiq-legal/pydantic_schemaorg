from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.BookFormatType import BookFormatType


class Hardcover(BookFormatType):
    """Book format: Hardcover.

    See: https://schema.org/Hardcover
    Model depth: 5
    """

    type_: str = Field("Hardcover", const=True, alias="@type")


if TYPE_CHECKING:

    Hardcover.update_forward_refs()
