from pydantic import Field
from pydantic_schemaorg.MusicPlaylist import MusicPlaylist
from typing import Any, Union, List, Optional
from pydantic_schemaorg.Person import Person
from pydantic_schemaorg.MusicAlbum import MusicAlbum
from pydantic_schemaorg.CreativeWork import CreativeWork


class MusicRecording(CreativeWork):
    """A music recording (track), usually a single song.

    See https://schema.org/MusicRecording.

    """

    inPlaylist: Optional[Union[List[MusicPlaylist], MusicPlaylist]] = Field(
        None,
        description="The playlist to which this recording belongs.",
    )
    duration: Any = Field(
        None,
        description="The duration of the item (movie, audio recording, event, etc.) in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601).",
    )
    byArtist: Union[List[Union[Person, Any]], Union[Person, Any]] = Field(
        None,
        description="The artist that performed this album or recording.",
    )
    inAlbum: Optional[Union[List[MusicAlbum], MusicAlbum]] = Field(
        None,
        description="The album to which this recording belongs.",
    )
    recordingOf: Any = Field(
        None,
        description="The composition this track is a recording of.",
    )
    isrcCode: Optional[Union[List[str], str]] = Field(
        None,
        description="The International Standard Recording Code for the recording.",
    )
    locals().update({"@type": Field("MusicRecording", const=True)})


MusicRecording.update_forward_refs()
