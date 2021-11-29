from pydantic import Field
from pydantic_schemaorg.MusicAlbumReleaseType import MusicAlbumReleaseType


class AlbumRelease(MusicAlbumReleaseType):
    """AlbumRelease.

    See https://schema.org/AlbumRelease.

    """

    locals().update({"@type": Field("AlbumRelease", const=True)})


AlbumRelease.update_forward_refs()
