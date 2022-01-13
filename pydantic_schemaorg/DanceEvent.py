from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Event import Event


class DanceEvent(Event):
    """Event type: A social dance.

    See: https://schema.org/DanceEvent
    Model depth: 3
    """

    type_: str = Field("DanceEvent", const=True, alias="@type")


if TYPE_CHECKING:

    DanceEvent.update_forward_refs()
