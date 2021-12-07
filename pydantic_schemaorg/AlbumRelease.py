from pydantic import Field
from pydantic_schemaorg.MusicAlbumReleaseType import MusicAlbumReleaseType


class AlbumRelease(MusicAlbumReleaseType):
    """AlbumRelease.

    See https://schema.org/AlbumRelease.

    """
    type_: str = Field("AlbumRelease", const=True, alias='@type')
    

AlbumRelease.update_forward_refs()
