from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List


from pydantic import Field
from pydantic_schemaorg.MusicPlaylist import MusicPlaylist


class MusicRelease(MusicPlaylist):
    """A MusicRelease is a specific release of a music album.

    See: https://schema.org/MusicRelease
    Model depth: 4
    """
    type_: str = Field("MusicRelease", alias='@type')
    releaseOf: Optional[Union[List[Union['MusicAlbum', str]], 'MusicAlbum', str]] = Field(
        None,
        description="The album this is a release of.",
    )
    duration: Optional[Union[List[Union['Duration', str]], 'Duration', str]] = Field(
        None,
        description="The duration of the item (movie, audio recording, event, etc.) in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601).",
    )
    catalogNumber: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="The catalog number for the release.",
    )
    musicReleaseFormat: Optional[Union[List[Union['MusicReleaseFormatType', str]], 'MusicReleaseFormatType', str]] = Field(
        None,
        description="Format of this release (the type of recording media used, ie. compact disc, digital media,"
     "LP, etc.).",
    )
    creditedTo: Optional[Union[List[Union['Organization', 'Person', str]], 'Organization', 'Person', str]] = Field(
        None,
        description="The group the release is credited to if different than the byArtist. For example, Red"
     "and Blue is credited to \"Stefani Germanotta Band\", but by Lady Gaga.",
    )
    recordLabel: Optional[Union[List[Union['Organization', str]], 'Organization', str]] = Field(
        None,
        description="The label that issued the release.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.MusicAlbum import MusicAlbum
    from pydantic_schemaorg.Duration import Duration
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.MusicReleaseFormatType import MusicReleaseFormatType
    from pydantic_schemaorg.Organization import Organization
    from pydantic_schemaorg.Person import Person
