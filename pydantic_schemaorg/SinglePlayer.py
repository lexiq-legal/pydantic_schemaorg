from pydantic import Field
from pydantic_schemaorg.GamePlayMode import GamePlayMode


class SinglePlayer(GamePlayMode):
    """Play mode: SinglePlayer. Which is played by a lone player.

    See https://schema.org/SinglePlayer.

    """

    locals().update({"@type": Field("SinglePlayer", const=True)})


SinglePlayer.update_forward_refs()
