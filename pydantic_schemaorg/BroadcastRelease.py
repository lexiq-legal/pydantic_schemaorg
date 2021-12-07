from pydantic import Field
from pydantic_schemaorg.MusicAlbumReleaseType import MusicAlbumReleaseType


class BroadcastRelease(MusicAlbumReleaseType):
    """BroadcastRelease.

    See https://schema.org/BroadcastRelease.

    """
    type_: str = Field("BroadcastRelease", const=True, alias='@type')
    

BroadcastRelease.update_forward_refs()
