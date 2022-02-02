from __future__ import annotations
from typing import TYPE_CHECKING

from pydantic import AnyUrl
from typing import Union, Optional, List


from pydantic import Field
from pydantic_schemaorg.PerformingGroup import PerformingGroup


class MusicGroup(PerformingGroup):
    """A musical group, such as a band, an orchestra, or a choir. Can also be a solo musician.

    See: https://schema.org/MusicGroup
    Model depth: 4
    """
    type_: str = Field("MusicGroup", alias='@type')
    genre: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text']], AnyUrl, 'URL', str, 'Text']] = Field(
        None,
        description="Genre of the creative work, broadcast channel or group.",
    )
    album: Optional[Union[List[Union['MusicAlbum', str]], 'MusicAlbum', str]] = Field(
        None,
        description="A music album.",
    )
    tracks: Optional[Union[List[Union['MusicRecording', str]], 'MusicRecording', str]] = Field(
        None,
        description="A music recording (track)&#x2014;usually a single song.",
    )
    track: Optional[Union[List[Union['MusicRecording', 'ItemList', str]], 'MusicRecording', 'ItemList', str]] = Field(
        None,
        description="A music recording (track)&#x2014;usually a single song. If an ItemList is given, the"
     "list should contain items of type MusicRecording.",
    )
    albums: Optional[Union[List[Union['MusicAlbum', str]], 'MusicAlbum', str]] = Field(
        None,
        description="A collection of music albums.",
    )
    musicGroupMember: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        None,
        description="A member of a music group&#x2014;for example, John, Paul, George, or Ringo.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.MusicAlbum import MusicAlbum
    from pydantic_schemaorg.MusicRecording import MusicRecording
    from pydantic_schemaorg.ItemList import ItemList
    from pydantic_schemaorg.Person import Person
