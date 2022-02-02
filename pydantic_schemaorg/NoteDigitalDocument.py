from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.DigitalDocument import DigitalDocument


class NoteDigitalDocument(DigitalDocument):
    """A file containing a note, primarily for the author.

    See: https://schema.org/NoteDigitalDocument
    Model depth: 4
    """
    type_: str = Field("NoteDigitalDocument", alias='@type')
    

