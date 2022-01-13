from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Enumeration import Enumeration


class MusicReleaseFormatType(Enumeration):
    """Format of this release (the type of recording media used, ie. compact disc, digital media,"
     "LP, etc.).

    See: https://schema.org/MusicReleaseFormatType
    Model depth: 4
    """

    type_: str = Field("MusicReleaseFormatType", const=True, alias="@type")


if TYPE_CHECKING:

    MusicReleaseFormatType.update_forward_refs()
