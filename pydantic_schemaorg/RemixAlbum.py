from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MusicAlbumProductionType import MusicAlbumProductionType


class RemixAlbum(MusicAlbumProductionType):
    """RemixAlbum.

    See: https://schema.org/RemixAlbum
    Model depth: 5
    """

    type_: str = Field("RemixAlbum", const=True, alias="@type")


if TYPE_CHECKING:

    RemixAlbum.update_forward_refs()
