from pydantic import Field
from pydantic_schemaorg.DigitalDocument import DigitalDocument


class SpreadsheetDigitalDocument(DigitalDocument):
    """A spreadsheet file.

    See https://schema.org/SpreadsheetDigitalDocument.

    """
    type_: str = Field("SpreadsheetDigitalDocument", const=True, alias='@type')
    

SpreadsheetDigitalDocument.update_forward_refs()
