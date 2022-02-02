from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.DigitalDocument import DigitalDocument


class SpreadsheetDigitalDocument(DigitalDocument):
    """A spreadsheet file.

    See: https://schema.org/SpreadsheetDigitalDocument
    Model depth: 4
    """
    type_: str = Field("SpreadsheetDigitalDocument", alias='@type')
    

