from pydantic import Field
from pydantic_schemaorg.DigitalDocument import DigitalDocument


class NoteDigitalDocument(DigitalDocument):
    """A file containing a note, primarily for the author.

    See https://schema.org/NoteDigitalDocument.

    """
    type_: str = Field("NoteDigitalDocument", const=True, alias='@type')
    

NoteDigitalDocument.update_forward_refs()
