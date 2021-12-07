from pydantic import Field
from pydantic_schemaorg.GameServerStatus import GameServerStatus
from typing import Any, Optional, Union, List
from pydantic_schemaorg.VideoGame import VideoGame
from pydantic_schemaorg.Intangible import Intangible


class GameServer(Intangible):
    """Server that provides game interaction in a multiplayer game.

    See https://schema.org/GameServer.

    """
    type_: str = Field("GameServer", const=True, alias='@type')
    serverStatus: Optional[Union[List[GameServerStatus], GameServerStatus]] = Field(
        None,
        description="Status of a game server.",
    )
    playersOnline: Optional[Union[List[int], int]] = Field(
        None,
        description="Number of players on the server.",
    )
    game: Optional[Union[List[VideoGame], VideoGame]] = Field(
        None,
        description="Video game which is played on this server.",
    )
    

GameServer.update_forward_refs()
