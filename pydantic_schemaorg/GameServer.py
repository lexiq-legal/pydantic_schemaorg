from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List


from pydantic import Field
from pydantic_schemaorg.Intangible import Intangible


class GameServer(Intangible):
    """Server that provides game interaction in a multiplayer game.

    See: https://schema.org/GameServer
    Model depth: 3
    """
    type_: str = Field("GameServer", alias='@type')
    serverStatus: Optional[Union[List[Union['GameServerStatus', str]], 'GameServerStatus', str]] = Field(
        None,
        description="Status of a game server.",
    )
    playersOnline: Optional[Union[List[Union[int, 'Integer', str]], int, 'Integer', str]] = Field(
        None,
        description="Number of players on the server.",
    )
    game: Optional[Union[List[Union['VideoGame', str]], 'VideoGame', str]] = Field(
        None,
        description="Video game which is played on this server.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.GameServerStatus import GameServerStatus
    from pydantic_schemaorg.Integer import Integer
    from pydantic_schemaorg.VideoGame import VideoGame
