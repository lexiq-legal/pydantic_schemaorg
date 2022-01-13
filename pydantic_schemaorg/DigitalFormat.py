from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MusicReleaseFormatType import MusicReleaseFormatType


class DigitalFormat(MusicReleaseFormatType):
    """DigitalFormat.

    See: https://schema.org/DigitalFormat
    Model depth: 5
    """

    type_: str = Field("DigitalFormat", const=True, alias="@type")


if TYPE_CHECKING:

    DigitalFormat.update_forward_refs()
