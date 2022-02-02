from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.DigitalDocument import DigitalDocument


class PresentationDigitalDocument(DigitalDocument):
    """A file containing slides or used for a presentation.

    See: https://schema.org/PresentationDigitalDocument
    Model depth: 4
    """
    type_: str = Field("PresentationDigitalDocument", alias='@type')
    

