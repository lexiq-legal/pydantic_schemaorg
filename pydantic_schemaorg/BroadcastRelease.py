from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MusicAlbumReleaseType import MusicAlbumReleaseType


class BroadcastRelease(MusicAlbumReleaseType):
    """BroadcastRelease.

    See: https://schema.org/BroadcastRelease
    Model depth: 5
    """

    type_: str = Field("BroadcastRelease", const=True, alias="@type")


if TYPE_CHECKING:

    BroadcastRelease.update_forward_refs()
