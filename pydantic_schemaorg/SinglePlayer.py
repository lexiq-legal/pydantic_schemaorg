from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.GamePlayMode import GamePlayMode


class SinglePlayer(GamePlayMode):
    """Play mode: SinglePlayer. Which is played by a lone player.

    See: https://schema.org/SinglePlayer
    Model depth: 5
    """
    type_: str = Field("SinglePlayer", alias='@type')
    

