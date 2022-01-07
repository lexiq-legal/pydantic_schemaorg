from pydantic import Field
from pydantic_schemaorg.MusicAlbumProductionType import MusicAlbumProductionType
from typing import List, Optional, Union
from pydantic_schemaorg.MusicAlbumReleaseType import MusicAlbumReleaseType
from pydantic_schemaorg.MusicGroup import MusicGroup
from pydantic_schemaorg.Person import Person
from pydantic_schemaorg.MusicRelease import MusicRelease
from pydantic_schemaorg.MusicPlaylist import MusicPlaylist


class MusicAlbum(MusicPlaylist):
    """A collection of music tracks.

    See https://schema.org/MusicAlbum.

    """
    type_: str = Field("MusicAlbum", const=True, alias='@type')
    albumProductionType: Optional[Union[List[Union[MusicAlbumProductionType, str]], Union[MusicAlbumProductionType, str]]] = Field(
        None,
        description="Classification of the album by it's type of content: soundtrack, live album, studio"
     "album, etc.",
    )
    albumReleaseType: Optional[Union[List[Union[MusicAlbumReleaseType, str]], Union[MusicAlbumReleaseType, str]]] = Field(
        None,
        description="The kind of release which this album is: single, EP or album.",
    )
    byArtist: Optional[Union[List[Union[MusicGroup, Person, str]], Union[MusicGroup, Person, str]]] = Field(
        None,
        description="The artist that performed this album or recording.",
    )
    albumRelease: Optional[Union[List[Union[MusicRelease, str]], Union[MusicRelease, str]]] = Field(
        None,
        description="A release of this album.",
    )
    

MusicAlbum.update_forward_refs()
