from pydantic import AnyUrl, Field
from typing import Any, Optional, Union, List
from pydantic_schema_org.MusicAlbum import MusicAlbum
from pydantic_schema_org.MusicRecording import MusicRecording
from pydantic_schema_org.ItemList import ItemList
from pydantic_schema_org.Person import Person
from pydantic_schema_org.PerformingGroup import PerformingGroup


class MusicGroup(PerformingGroup):
    """A musical group, such as a band, an orchestra, or a choir. Can also be a solo musician.

    See https://schema.org/MusicGroup.

    """

    genre: Optional[Union[List[Union[AnyUrl, str]], Union[AnyUrl, str]]] = Field(
        None,
        description="Genre of the creative work, broadcast channel or group.",
    )
    album: Optional[Union[List[MusicAlbum], MusicAlbum]] = Field(
        None,
        description="A music album.",
    )
    tracks: Optional[Union[List[MusicRecording], MusicRecording]] = Field(
        None,
        description="A music recording (track)&#x2014;usually a single song.",
    )
    track: Optional[Union[List[Union[ItemList, MusicRecording]], Union[ItemList, MusicRecording]]] = Field(
        None,
        description="A music recording (track)&#x2014;usually a single song. If an ItemList is given, the"
     "list should contain items of type MusicRecording.",
    )
    albums: Optional[Union[List[MusicAlbum], MusicAlbum]] = Field(
        None,
        description="A collection of music albums.",
    )
    musicGroupMember: Optional[Union[List[Person], Person]] = Field(
        None,
        description="A member of a music group&#x2014;for example, John, Paul, George, or Ringo.",
    )
    locals().update({"@type": Field("MusicGroup", const=True)})


MusicGroup.update_forward_refs()
