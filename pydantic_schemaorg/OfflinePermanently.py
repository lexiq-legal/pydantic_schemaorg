from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.GameServerStatus import GameServerStatus


class OfflinePermanently(GameServerStatus):
    """Game server status: OfflinePermanently. Server is offline and not available.

    See: https://schema.org/OfflinePermanently
    Model depth: 6
    """

    type_: str = Field("OfflinePermanently", const=True, alias="@type")


if TYPE_CHECKING:

    OfflinePermanently.update_forward_refs()
