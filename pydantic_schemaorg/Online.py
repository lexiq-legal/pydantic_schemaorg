from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.GameServerStatus import GameServerStatus


class Online(GameServerStatus):
    """Game server status: Online. Server is available.

    See: https://schema.org/Online
    Model depth: 6
    """

    type_: str = Field("Online", const=True, alias="@type")


if TYPE_CHECKING:

    Online.update_forward_refs()
