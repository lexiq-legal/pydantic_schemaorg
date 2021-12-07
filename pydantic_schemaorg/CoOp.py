from pydantic import Field
from pydantic_schemaorg.GamePlayMode import GamePlayMode


class CoOp(GamePlayMode):
    """Play mode: CoOp. Co-operative games, where you play on the same team with friends.

    See https://schema.org/CoOp.

    """
    type_: str = Field("CoOp", const=True, alias='@type')
    

CoOp.update_forward_refs()
