from pydantic import Field
from pydantic_schemaorg.DigitalDocument import DigitalDocument


class TextDigitalDocument(DigitalDocument):
    """A file composed primarily of text.

    See https://schema.org/TextDigitalDocument.

    """
    type_: str = Field("TextDigitalDocument", const=True, alias='@type')
    

TextDigitalDocument.update_forward_refs()
