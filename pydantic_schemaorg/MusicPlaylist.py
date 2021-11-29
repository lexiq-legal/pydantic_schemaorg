from pydantic import Field
from typing import Any, Union, List, Optional
from pydantic_schemaorg.CreativeWork import CreativeWork


class MusicPlaylist(CreativeWork):
    """A collection of music tracks in playlist form.

    See https://schema.org/MusicPlaylist.

    """

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
    locals().update({"@type": Field("MusicPlaylist", const=True)})


MusicPlaylist.update_forward_refs()
