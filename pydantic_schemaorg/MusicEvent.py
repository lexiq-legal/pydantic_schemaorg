from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Event import Event


class MusicEvent(Event):
    """Event type: Music event.

    See: https://schema.org/MusicEvent
    Model depth: 3
    """

    type_: str = Field("MusicEvent", const=True, alias="@type")


if TYPE_CHECKING:

    MusicEvent.update_forward_refs()
