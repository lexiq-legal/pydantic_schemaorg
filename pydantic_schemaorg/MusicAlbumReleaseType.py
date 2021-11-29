from pydantic import Field
from pydantic_schemaorg.Enumeration import Enumeration


class MusicAlbumReleaseType(Enumeration):
    """The kind of release which this album is: single, EP or album.

    See https://schema.org/MusicAlbumReleaseType.

    """

    locals().update({"@type": Field("MusicAlbumReleaseType", const=True)})


MusicAlbumReleaseType.update_forward_refs()
