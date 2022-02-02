from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Enumeration import Enumeration


class GamePlayMode(Enumeration):
    """Indicates whether this game is multi-player, co-op or single-player.

    See: https://schema.org/GamePlayMode
    Model depth: 4
    """
    type_: str = Field("GamePlayMode", alias='@type')
    

