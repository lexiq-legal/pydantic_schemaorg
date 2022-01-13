from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Event import Event


class TheaterEvent(Event):
    """Event type: Theater performance.

    See: https://schema.org/TheaterEvent
    Model depth: 3
    """

    type_: str = Field("TheaterEvent", const=True, alias="@type")


if TYPE_CHECKING:

    TheaterEvent.update_forward_refs()
