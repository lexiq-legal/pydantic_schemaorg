from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.DigitalDocument import DigitalDocument


class TextDigitalDocument(DigitalDocument):
    """A file composed primarily of text.

    See: https://schema.org/TextDigitalDocument
    Model depth: 4
    """
    type_: str = Field("TextDigitalDocument", alias='@type')
    

