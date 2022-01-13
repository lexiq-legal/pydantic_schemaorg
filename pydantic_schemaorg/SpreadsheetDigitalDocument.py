from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.DigitalDocument import DigitalDocument


class SpreadsheetDigitalDocument(DigitalDocument):
    """A spreadsheet file.

    See: https://schema.org/SpreadsheetDigitalDocument
    Model depth: 4
    """

    type_: str = Field("SpreadsheetDigitalDocument", const=True, alias="@type")


if TYPE_CHECKING:

    SpreadsheetDigitalDocument.update_forward_refs()
