from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MusicAlbumReleaseType import MusicAlbumReleaseType


class EPRelease(MusicAlbumReleaseType):
    """EPRelease.

    See: https://schema.org/EPRelease
    Model depth: 5
    """

    type_: str = Field("EPRelease", const=True, alias="@type")


if TYPE_CHECKING:

    EPRelease.update_forward_refs()
