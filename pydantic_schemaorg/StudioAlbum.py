from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MusicAlbumProductionType import MusicAlbumProductionType


class StudioAlbum(MusicAlbumProductionType):
    """StudioAlbum.

    See: https://schema.org/StudioAlbum
    Model depth: 5
    """

    type_: str = Field("StudioAlbum", const=True, alias="@type")


if TYPE_CHECKING:

    StudioAlbum.update_forward_refs()
