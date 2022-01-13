from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.BroadcastChannel import BroadcastChannel


class RadioChannel(BroadcastChannel):
    """A unique instance of a radio BroadcastService on a CableOrSatelliteService lineup.

    See: https://schema.org/RadioChannel
    Model depth: 4
    """

    type_: str = Field("RadioChannel", const=True, alias="@type")


if TYPE_CHECKING:

    RadioChannel.update_forward_refs()
