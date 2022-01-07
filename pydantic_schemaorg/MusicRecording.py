from pydantic import Field
from pydantic_schemaorg.MusicPlaylist import MusicPlaylist
from typing import List, Optional, Any, Union
from pydantic_schemaorg.Duration import Duration
from pydantic_schemaorg.MusicGroup import MusicGroup
from pydantic_schemaorg.Person import Person
from pydantic_schemaorg.MusicAlbum import MusicAlbum
from pydantic_schemaorg.MusicComposition import MusicComposition
from pydantic_schemaorg.CreativeWork import CreativeWork


class MusicRecording(CreativeWork):
    """A music recording (track), usually a single song.

    See https://schema.org/MusicRecording.

    """
    type_: str = Field("MusicRecording", const=True, alias='@type')
    inPlaylist: Optional[Union[List[Union[MusicPlaylist, str]], Union[MusicPlaylist, str]]] = Field(
        None,
        description="The playlist to which this recording belongs.",
    )
    duration: Optional[Union[List[Union[Duration, str]], Union[Duration, str]]] = Field(
        None,
        description="The duration of the item (movie, audio recording, event, etc.) in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601).",
    )
    byArtist: Optional[Union[List[Union[MusicGroup, Person, str]], Union[MusicGroup, Person, str]]] = Field(
        None,
        description="The artist that performed this album or recording.",
    )
    inAlbum: Optional[Union[List[Union[MusicAlbum, str]], Union[MusicAlbum, str]]] = Field(
        None,
        description="The album to which this recording belongs.",
    )
    recordingOf: Optional[Union[List[Union[MusicComposition, str]], Union[MusicComposition, str]]] = Field(
        None,
        description="The composition this track is a recording of.",
    )
    isrcCode: Optional[Union[List[str], str]] = Field(
        None,
        description="The International Standard Recording Code for the recording.",
    )
    

MusicRecording.update_forward_refs()
