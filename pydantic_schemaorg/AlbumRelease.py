from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MusicAlbumReleaseType import MusicAlbumReleaseType


class AlbumRelease(MusicAlbumReleaseType):
    """AlbumRelease.

    See: https://schema.org/AlbumRelease
    Model depth: 5
    """
    type_: str = Field("AlbumRelease", alias='@type')
    

