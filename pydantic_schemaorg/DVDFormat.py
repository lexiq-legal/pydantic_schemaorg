from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MusicReleaseFormatType import MusicReleaseFormatType


class DVDFormat(MusicReleaseFormatType):
    """DVDFormat.

    See: https://schema.org/DVDFormat
    Model depth: 5
    """

    type_: str = Field("DVDFormat", const=True, alias="@type")


if TYPE_CHECKING:

    DVDFormat.update_forward_refs()
