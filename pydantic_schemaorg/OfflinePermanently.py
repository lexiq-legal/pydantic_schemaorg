from pydantic import Field
from pydantic_schemaorg.GameServerStatus import GameServerStatus


class OfflinePermanently(GameServerStatus):
    """Game server status: OfflinePermanently. Server is offline and not available.

    See https://schema.org/OfflinePermanently.

    """
    type_: str = Field("OfflinePermanently", const=True, alias='@type')
    

OfflinePermanently.update_forward_refs()
