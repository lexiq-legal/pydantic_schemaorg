from pydantic import Field
from pydantic_schemaorg.DigitalDocument import DigitalDocument


class TextDigitalDocument(DigitalDocument):
    """A file composed primarily of text.

    See https://schema.org/TextDigitalDocument.

    """

    locals().update({"@type": Field("TextDigitalDocument", const=True)})


TextDigitalDocument.update_forward_refs()
