from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MusicAlbumProductionType import MusicAlbumProductionType


class SoundtrackAlbum(MusicAlbumProductionType):
    """SoundtrackAlbum.

    See: https://schema.org/SoundtrackAlbum
    Model depth: 5
    """

    type_: str = Field("SoundtrackAlbum", const=True, alias="@type")


if TYPE_CHECKING:

    SoundtrackAlbum.update_forward_refs()
