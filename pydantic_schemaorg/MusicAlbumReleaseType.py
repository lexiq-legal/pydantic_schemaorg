from pydantic import Field
from pydantic_schemaorg.Enumeration import Enumeration


class MusicAlbumReleaseType(Enumeration):
    """The kind of release which this album is: single, EP or album.

    See https://schema.org/MusicAlbumReleaseType.

    """
    type_: str = Field("MusicAlbumReleaseType", const=True, alias='@type')
    

MusicAlbumReleaseType.update_forward_refs()
