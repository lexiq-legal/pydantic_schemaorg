from pydantic import Field
from pydantic_schemaorg.MusicAlbumReleaseType import MusicAlbumReleaseType


class BroadcastRelease(MusicAlbumReleaseType):
    """BroadcastRelease.

    See https://schema.org/BroadcastRelease.

    """

    locals().update({"@type": Field("BroadcastRelease", const=True)})


BroadcastRelease.update_forward_refs()
