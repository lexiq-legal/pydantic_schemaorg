from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Event import Event


class BusinessEvent(Event):
    """Event type: Business event.

    See: https://schema.org/BusinessEvent
    Model depth: 3
    """

    type_: str = Field("BusinessEvent", const=True, alias="@type")


if TYPE_CHECKING:

    BusinessEvent.update_forward_refs()
