from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MusicReleaseFormatType import MusicReleaseFormatType


class CassetteFormat(MusicReleaseFormatType):
    """CassetteFormat.

    See: https://schema.org/CassetteFormat
    Model depth: 5
    """

    type_: str = Field("CassetteFormat", const=True, alias="@type")


if TYPE_CHECKING:

    CassetteFormat.update_forward_refs()
