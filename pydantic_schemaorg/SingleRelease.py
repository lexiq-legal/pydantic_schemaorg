from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MusicAlbumReleaseType import MusicAlbumReleaseType


class SingleRelease(MusicAlbumReleaseType):
    """SingleRelease.

    See: https://schema.org/SingleRelease
    Model depth: 5
    """

    type_: str = Field("SingleRelease", const=True, alias="@type")


if TYPE_CHECKING:

    SingleRelease.update_forward_refs()
