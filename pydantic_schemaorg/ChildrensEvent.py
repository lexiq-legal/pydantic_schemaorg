from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Event import Event


class ChildrensEvent(Event):
    """Event type: Children's event.

    See: https://schema.org/ChildrensEvent
    Model depth: 3
    """

    type_: str = Field("ChildrensEvent", const=True, alias="@type")


if TYPE_CHECKING:

    ChildrensEvent.update_forward_refs()
