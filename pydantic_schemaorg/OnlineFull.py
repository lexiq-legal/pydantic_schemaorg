from pydantic import Field
from pydantic_schemaorg.GameServerStatus import GameServerStatus


class OnlineFull(GameServerStatus):
    """Game server status: OnlineFull. Server is online but unavailable. The maximum number"
     "of players has reached.

    See https://schema.org/OnlineFull.

    """

    locals().update({"@type": Field("OnlineFull", const=True)})


OnlineFull.update_forward_refs()
