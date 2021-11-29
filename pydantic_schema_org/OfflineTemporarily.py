from pydantic import Field
from pydantic_schema_org.GameServerStatus import GameServerStatus


class OfflineTemporarily(GameServerStatus):
    """Game server status: OfflineTemporarily. Server is offline now but it can be online soon.

    See https://schema.org/OfflineTemporarily.

    """

    locals().update({"@type": Field("OfflineTemporarily", const=True)})


OfflineTemporarily.update_forward_refs()
