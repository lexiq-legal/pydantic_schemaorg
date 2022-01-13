from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Enumeration import Enumeration


class MusicAlbumProductionType(Enumeration):
    """Classification of the album by it's type of content: soundtrack, live album, studio"
     "album, etc.

    See: https://schema.org/MusicAlbumProductionType
    Model depth: 4
    """

    type_: str = Field("MusicAlbumProductionType", const=True, alias="@type")


if TYPE_CHECKING:

    MusicAlbumProductionType.update_forward_refs()
