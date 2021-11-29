from pydantic import Field
from pydantic_schemaorg.MusicAlbumProductionType import MusicAlbumProductionType
from typing import Any, Union, List, Optional
from pydantic_schemaorg.MusicAlbumReleaseType import MusicAlbumReleaseType
from pydantic_schemaorg.Person import Person
from pydantic_schemaorg.MusicPlaylist import MusicPlaylist


class MusicAlbum(MusicPlaylist):
    """A collection of music tracks.

    See https://schema.org/MusicAlbum.

    """

    albumProductionType: Optional[Union[List[MusicAlbumProductionType], MusicAlbumProductionType]] = Field(
        None,
        description="Classification of the album by it's type of content: soundtrack, live album, studio"
     "album, etc.",
    )
    albumReleaseType: Optional[Union[List[MusicAlbumReleaseType], MusicAlbumReleaseType]] = Field(
        None,
        description="The kind of release which this album is: single, EP or album.",
    )
    byArtist: Union[List[Union[Person, Any]], Union[Person, Any]] = Field(
        None,
        description="The artist that performed this album or recording.",
    )
    albumRelease: Any = Field(
        None,
        description="A release of this album.",
    )
    locals().update({"@type": Field("MusicAlbum", const=True)})


MusicAlbum.update_forward_refs()
