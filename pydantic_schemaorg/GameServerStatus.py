from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.StatusEnumeration import StatusEnumeration


class GameServerStatus(StatusEnumeration):
    """Status of a game server.

    See: https://schema.org/GameServerStatus
    Model depth: 5
    """
    type_: str = Field("GameServerStatus", alias='@type')
    

