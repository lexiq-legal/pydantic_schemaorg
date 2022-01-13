from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional

from pydantic_schemaorg.Intangible import Intangible


class GameServer(Intangible):
    """Server that provides game interaction in a multiplayer game.

    See: https://schema.org/GameServer
    Model depth: 3
    """

    type_: str = Field("GameServer", const=True, alias="@type")
    serverStatus: "Optional[Union[List[Union[GameServerStatus, str]], Union[GameServerStatus, str]]]" = Field(
        None,
        description="Status of a game server.",
    )
    playersOnline: "Optional[Union[List[Union[int, str]], Union[int, str]]]" = Field(
        None,
        description="Number of players on the server.",
    )
    game: "Optional[Union[List[Union[VideoGame, str]], Union[VideoGame, str]]]" = Field(
        None,
        description="Video game which is played on this server.",
    )


if TYPE_CHECKING:

    from pydantic_schemaorg.GameServerStatus import GameServerStatus

    from pydantic_schemaorg.VideoGame import VideoGame

    GameServer.update_forward_refs()
