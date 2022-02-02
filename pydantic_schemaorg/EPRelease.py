from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MusicAlbumReleaseType import MusicAlbumReleaseType


class EPRelease(MusicAlbumReleaseType):
    """EPRelease.

    See: https://schema.org/EPRelease
    Model depth: 5
    """
    type_: str = Field("EPRelease", alias='@type')
    

