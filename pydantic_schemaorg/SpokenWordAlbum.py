from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MusicAlbumProductionType import MusicAlbumProductionType


class SpokenWordAlbum(MusicAlbumProductionType):
    """SpokenWordAlbum.

    See: https://schema.org/SpokenWordAlbum
    Model depth: 5
    """

    type_: str = Field("SpokenWordAlbum", const=True, alias="@type")


if TYPE_CHECKING:

    SpokenWordAlbum.update_forward_refs()
