from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.GamePlayMode import GamePlayMode


class MultiPlayer(GamePlayMode):
    """Play mode: MultiPlayer. Requiring or allowing multiple human players to play simultaneously.

    See: https://schema.org/MultiPlayer
    Model depth: 5
    """

    type_: str = Field("MultiPlayer", const=True, alias="@type")


if TYPE_CHECKING:

    MultiPlayer.update_forward_refs()
