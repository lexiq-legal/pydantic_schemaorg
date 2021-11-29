from pydantic import Field
from pydantic_schema_org.MusicAlbumReleaseType import MusicAlbumReleaseType


class BroadcastRelease(MusicAlbumReleaseType):
    """BroadcastRelease.

    See https://schema.org/BroadcastRelease.

    """

    locals().update({"@type": Field("BroadcastRelease", const=True)})


BroadcastRelease.update_forward_refs()
