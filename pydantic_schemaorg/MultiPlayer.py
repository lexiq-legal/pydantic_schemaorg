from pydantic import Field
from pydantic_schemaorg.GamePlayMode import GamePlayMode


class MultiPlayer(GamePlayMode):
    """Play mode: MultiPlayer. Requiring or allowing multiple human players to play simultaneously.

    See https://schema.org/MultiPlayer.

    """

    locals().update({"@type": Field("MultiPlayer", const=True)})


MultiPlayer.update_forward_refs()
