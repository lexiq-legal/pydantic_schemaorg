from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Event import Event


class FoodEvent(Event):
    """Event type: Food event.

    See: https://schema.org/FoodEvent
    Model depth: 3
    """

    type_: str = Field("FoodEvent", const=True, alias="@type")


if TYPE_CHECKING:

    FoodEvent.update_forward_refs()
