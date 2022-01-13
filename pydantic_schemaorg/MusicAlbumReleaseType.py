from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Enumeration import Enumeration


class MusicAlbumReleaseType(Enumeration):
    """The kind of release which this album is: single, EP or album.

    See: https://schema.org/MusicAlbumReleaseType
    Model depth: 4
    """

    type_: str = Field("MusicAlbumReleaseType", const=True, alias="@type")


if TYPE_CHECKING:

    MusicAlbumReleaseType.update_forward_refs()
