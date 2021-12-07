from pydantic import Field
from pydantic_schemaorg.StatusEnumeration import StatusEnumeration


class GameServerStatus(StatusEnumeration):
    """Status of a game server.

    See https://schema.org/GameServerStatus.

    """
    type_: str = Field("GameServerStatus", const=True, alias='@type')
    

GameServerStatus.update_forward_refs()
