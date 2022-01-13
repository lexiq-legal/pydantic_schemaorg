from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.StatusEnumeration import StatusEnumeration


class GameServerStatus(StatusEnumeration):
    """Status of a game server.

    See: https://schema.org/GameServerStatus
    Model depth: 5
    """

    type_: str = Field("GameServerStatus", const=True, alias="@type")


if TYPE_CHECKING:

    GameServerStatus.update_forward_refs()
