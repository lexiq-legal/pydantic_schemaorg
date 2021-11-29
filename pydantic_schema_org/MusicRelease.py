from pydantic import Field
from pydantic_schema_org.MusicAlbum import MusicAlbum
from typing import Any, Optional, Union, List
from pydantic_schema_org.MusicReleaseFormatType import MusicReleaseFormatType
from pydantic_schema_org.Person import Person
from pydantic_schema_org.Organization import Organization
from pydantic_schema_org.MusicPlaylist import MusicPlaylist


class MusicRelease(MusicPlaylist):
    """A MusicRelease is a specific release of a music album.

    See https://schema.org/MusicRelease.

    """

    releaseOf: Optional[Union[List[MusicAlbum], MusicAlbum]] = Field(
        None,
        description="The album this is a release of.",
    )
    duration: Any = Field(
        None,
        description="The duration of the item (movie, audio recording, event, etc.) in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601).",
    )
    catalogNumber: Optional[Union[List[str], str]] = Field(
        None,
        description="The catalog number for the release.",
    )
    musicReleaseFormat: Optional[Union[List[MusicReleaseFormatType], MusicReleaseFormatType]] = Field(
        None,
        description="Format of this release (the type of recording media used, ie. compact disc, digital media,"
     "LP, etc.).",
    )
    creditedTo: Optional[Union[List[Union[Person, Organization]], Union[Person, Organization]]] = Field(
        None,
        description="The group the release is credited to if different than the byArtist. For example, Red"
     "and Blue is credited to \"Stefani Germanotta Band\", but by Lady Gaga.",
    )
    recordLabel: Optional[Union[List[Organization], Organization]] = Field(
        None,
        description="The label that issued the release.",
    )
    locals().update({"@type": Field("MusicRelease", const=True)})


MusicRelease.update_forward_refs()
