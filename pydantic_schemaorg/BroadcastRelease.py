from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MusicAlbumReleaseType import MusicAlbumReleaseType


class BroadcastRelease(MusicAlbumReleaseType):
    """BroadcastRelease.

    See: https://schema.org/BroadcastRelease
    Model depth: 5
    """
    type_: str = Field("BroadcastRelease", alias='@type')
    

