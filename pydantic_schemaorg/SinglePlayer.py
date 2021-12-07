from pydantic import Field
from pydantic_schemaorg.GamePlayMode import GamePlayMode


class SinglePlayer(GamePlayMode):
    """Play mode: SinglePlayer. Which is played by a lone player.

    See https://schema.org/SinglePlayer.

    """
    type_: str = Field("SinglePlayer", const=True, alias='@type')
    

SinglePlayer.update_forward_refs()
