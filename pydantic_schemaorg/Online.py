from pydantic import Field
from pydantic_schemaorg.GameServerStatus import GameServerStatus


class Online(GameServerStatus):
    """Game server status: Online. Server is available.

    See https://schema.org/Online.

    """

    locals().update({"@type": Field("Online", const=True)})


Online.update_forward_refs()
