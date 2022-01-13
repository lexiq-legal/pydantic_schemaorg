from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MusicAlbumReleaseType import MusicAlbumReleaseType


class AlbumRelease(MusicAlbumReleaseType):
    """AlbumRelease.

    See: https://schema.org/AlbumRelease
    Model depth: 5
    """

    type_: str = Field("AlbumRelease", const=True, alias="@type")


if TYPE_CHECKING:

    AlbumRelease.update_forward_refs()
