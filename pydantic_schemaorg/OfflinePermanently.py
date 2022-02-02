from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.GameServerStatus import GameServerStatus


class OfflinePermanently(GameServerStatus):
    """Game server status: OfflinePermanently. Server is offline and not available.

    See: https://schema.org/OfflinePermanently
    Model depth: 6
    """
    type_: str = Field("OfflinePermanently", alias='@type')
    

