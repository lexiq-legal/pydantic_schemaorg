from pydantic import Field
from typing import Any, Optional, Union, List
from pydantic_schemaorg.CreativeWork import CreativeWork


class MusicPlaylist(CreativeWork):
    """A collection of music tracks in playlist form.

    See https://schema.org/MusicPlaylist.

    """
    type_: str = Field("MusicPlaylist", const=True, alias='@type')
    numTracks: Optional[Union[List[int], int]] = Field(
        None,
        description="The number of tracks in this album or playlist.",
    )
    tracks: Any = Field(
        None,
        description="A music recording (track)&#x2014;usually a single song.",
    )
    track: Any = Field(
        None,
        description="A music recording (track)&#x2014;usually a single song. If an ItemList is given, the"
     "list should contain items of type MusicRecording.",
    )
    

MusicPlaylist.update_forward_refs()
