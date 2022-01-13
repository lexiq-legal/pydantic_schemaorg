from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.DigitalDocument import DigitalDocument


class PresentationDigitalDocument(DigitalDocument):
    """A file containing slides or used for a presentation.

    See: https://schema.org/PresentationDigitalDocument
    Model depth: 4
    """

    type_: str = Field("PresentationDigitalDocument", const=True, alias="@type")


if TYPE_CHECKING:

    PresentationDigitalDocument.update_forward_refs()
