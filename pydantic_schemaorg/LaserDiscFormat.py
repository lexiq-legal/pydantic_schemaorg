from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MusicReleaseFormatType import MusicReleaseFormatType


class LaserDiscFormat(MusicReleaseFormatType):
    """LaserDiscFormat.

    See: https://schema.org/LaserDiscFormat
    Model depth: 5
    """

    type_: str = Field("LaserDiscFormat", const=True, alias="@type")


if TYPE_CHECKING:

    LaserDiscFormat.update_forward_refs()
