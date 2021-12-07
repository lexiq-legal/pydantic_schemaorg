from pydantic import Field
from pydantic_schemaorg.MusicAlbumReleaseType import MusicAlbumReleaseType


class SingleRelease(MusicAlbumReleaseType):
    """SingleRelease.

    See https://schema.org/SingleRelease.

    """
    type_: str = Field("SingleRelease", const=True, alias='@type')
    

SingleRelease.update_forward_refs()
