from pydantic import Field
from pydantic_schemaorg.GameServerStatus import GameServerStatus
from typing import List, Optional, Union
from pydantic_schemaorg.VideoGame import VideoGame
from pydantic_schemaorg.Intangible import Intangible


class GameServer(Intangible):
    """Server that provides game interaction in a multiplayer game.

    See https://schema.org/GameServer.

    """
    type_: str = Field("GameServer", const=True, alias='@type')
    serverStatus: Optional[Union[List[Union[GameServerStatus, str]], Union[GameServerStatus, str]]] = Field(
        None,
        description="Status of a game server.",
    )
    playersOnline: Optional[Union[List[Union[int, str]], Union[int, str]]] = Field(
        None,
        description="Number of players on the server.",
    )
    game: Optional[Union[List[Union[VideoGame, str]], Union[VideoGame, str]]] = Field(
        None,
        description="Video game which is played on this server.",
    )
    

GameServer.update_forward_refs()
