from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.DigitalDocument import DigitalDocument


class TextDigitalDocument(DigitalDocument):
    """A file composed primarily of text.

    See: https://schema.org/TextDigitalDocument
    Model depth: 4
    """

    type_: str = Field("TextDigitalDocument", const=True, alias="@type")


if TYPE_CHECKING:

    TextDigitalDocument.update_forward_refs()
