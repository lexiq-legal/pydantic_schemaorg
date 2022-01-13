from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MusicAlbumProductionType import MusicAlbumProductionType


class LiveAlbum(MusicAlbumProductionType):
    """LiveAlbum.

    See: https://schema.org/LiveAlbum
    Model depth: 5
    """

    type_: str = Field("LiveAlbum", const=True, alias="@type")


if TYPE_CHECKING:

    LiveAlbum.update_forward_refs()
