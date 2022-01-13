from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.GameServerStatus import GameServerStatus


class OfflineTemporarily(GameServerStatus):
    """Game server status: OfflineTemporarily. Server is offline now but it can be online soon.

    See: https://schema.org/OfflineTemporarily
    Model depth: 6
    """

    type_: str = Field("OfflineTemporarily", const=True, alias="@type")


if TYPE_CHECKING:

    OfflineTemporarily.update_forward_refs()
