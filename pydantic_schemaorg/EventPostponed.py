from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.EventStatusType import EventStatusType


class EventPostponed(EventStatusType):
    """The event has been postponed and no new date has been set. The event's previousStartDate"
     "should be set.

    See: https://schema.org/EventPostponed
    Model depth: 6
    """

    type_: str = Field("EventPostponed", const=True, alias="@type")


if TYPE_CHECKING:

    EventPostponed.update_forward_refs()
