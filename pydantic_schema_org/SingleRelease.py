from pydantic import Field
from pydantic_schema_org.MusicAlbumReleaseType import MusicAlbumReleaseType


class SingleRelease(MusicAlbumReleaseType):
    """SingleRelease.

    See https://schema.org/SingleRelease.

    """

    locals().update({"@type": Field("SingleRelease", const=True)})


SingleRelease.update_forward_refs()
