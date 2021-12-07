from pydantic import Field
from pydantic_schemaorg.GameServerStatus import GameServerStatus


class Online(GameServerStatus):
    """Game server status: Online. Server is available.

    See https://schema.org/Online.

    """
    type_: str = Field("Online", const=True, alias='@type')
    

Online.update_forward_refs()
