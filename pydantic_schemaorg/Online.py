from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.GameServerStatus import GameServerStatus


class Online(GameServerStatus):
    """Game server status: Online. Server is available.

    See: https://schema.org/Online
    Model depth: 6
    """
    type_: str = Field("Online", alias='@type')
    

