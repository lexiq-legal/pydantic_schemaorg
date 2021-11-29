from pydantic import Field
from pydantic_schemaorg.GameServerStatus import GameServerStatus


class OfflinePermanently(GameServerStatus):
    """Game server status: OfflinePermanently. Server is offline and not available.

    See https://schema.org/OfflinePermanently.

    """

    locals().update({"@type": Field("OfflinePermanently", const=True)})


OfflinePermanently.update_forward_refs()
