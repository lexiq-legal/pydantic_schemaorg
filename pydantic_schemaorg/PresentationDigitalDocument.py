from pydantic import Field
from pydantic_schemaorg.DigitalDocument import DigitalDocument


class PresentationDigitalDocument(DigitalDocument):
    """A file containing slides or used for a presentation.

    See https://schema.org/PresentationDigitalDocument.

    """

    locals().update({"@type": Field("PresentationDigitalDocument", const=True)})


PresentationDigitalDocument.update_forward_refs()
