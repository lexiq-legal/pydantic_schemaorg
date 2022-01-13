from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.DigitalDocument import DigitalDocument


class NoteDigitalDocument(DigitalDocument):
    """A file containing a note, primarily for the author.

    See: https://schema.org/NoteDigitalDocument
    Model depth: 4
    """

    type_: str = Field("NoteDigitalDocument", const=True, alias="@type")


if TYPE_CHECKING:

    NoteDigitalDocument.update_forward_refs()
