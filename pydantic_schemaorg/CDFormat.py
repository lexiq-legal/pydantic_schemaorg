from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MusicReleaseFormatType import MusicReleaseFormatType


class CDFormat(MusicReleaseFormatType):
    """CDFormat.

    See: https://schema.org/CDFormat
    Model depth: 5
    """

    type_: str = Field("CDFormat", const=True, alias="@type")


if TYPE_CHECKING:

    CDFormat.update_forward_refs()
