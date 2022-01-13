from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.BroadcastService import BroadcastService


class RadioBroadcastService(BroadcastService):
    """A delivery service through which radio content is provided via broadcast over the air"
     "or online.

    See: https://schema.org/RadioBroadcastService
    Model depth: 5
    """

    type_: str = Field("RadioBroadcastService", const=True, alias="@type")


if TYPE_CHECKING:

    RadioBroadcastService.update_forward_refs()
