from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MusicAlbumProductionType import MusicAlbumProductionType


class MixtapeAlbum(MusicAlbumProductionType):
    """MixtapeAlbum.

    See: https://schema.org/MixtapeAlbum
    Model depth: 5
    """

    type_: str = Field("MixtapeAlbum", const=True, alias="@type")


if TYPE_CHECKING:

    MixtapeAlbum.update_forward_refs()
