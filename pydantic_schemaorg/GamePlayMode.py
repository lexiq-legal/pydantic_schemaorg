from pydantic import Field
from pydantic_schemaorg.Enumeration import Enumeration


class GamePlayMode(Enumeration):
    """Indicates whether this game is multi-player, co-op or single-player.

    See https://schema.org/GamePlayMode.

    """

    locals().update({"@type": Field("GamePlayMode", const=True)})


GamePlayMode.update_forward_refs()
