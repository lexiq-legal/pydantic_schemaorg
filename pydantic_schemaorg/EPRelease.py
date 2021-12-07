from pydantic import Field
from pydantic_schemaorg.MusicAlbumReleaseType import MusicAlbumReleaseType


class EPRelease(MusicAlbumReleaseType):
    """EPRelease.

    See https://schema.org/EPRelease.

    """
    type_: str = Field("EPRelease", const=True, alias='@type')
    

EPRelease.update_forward_refs()
