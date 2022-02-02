from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MusicAlbumReleaseType import MusicAlbumReleaseType


class SingleRelease(MusicAlbumReleaseType):
    """SingleRelease.

    See: https://schema.org/SingleRelease
    Model depth: 5
    """
    type_: str = Field("SingleRelease", alias='@type')
    

