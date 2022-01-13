from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Event import Event


class ComedyEvent(Event):
    """Event type: Comedy event.

    See: https://schema.org/ComedyEvent
    Model depth: 3
    """

    type_: str = Field("ComedyEvent", const=True, alias="@type")


if TYPE_CHECKING:

    ComedyEvent.update_forward_refs()
