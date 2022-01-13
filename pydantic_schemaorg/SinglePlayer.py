from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.GamePlayMode import GamePlayMode


class SinglePlayer(GamePlayMode):
    """Play mode: SinglePlayer. Which is played by a lone player.

    See: https://schema.org/SinglePlayer
    Model depth: 5
    """

    type_: str = Field("SinglePlayer", const=True, alias="@type")


if TYPE_CHECKING:

    SinglePlayer.update_forward_refs()
