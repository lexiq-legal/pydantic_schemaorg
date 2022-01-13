from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.EventStatusType import EventStatusType


class EventMovedOnline(EventStatusType):
    """Indicates that the event was changed to allow online participation. See [[eventAttendanceMode]]"
     "for specifics of whether it is now fully or partially online.

    See: https://schema.org/EventMovedOnline
    Model depth: 6
    """

    type_: str = Field("EventMovedOnline", const=True, alias="@type")


if TYPE_CHECKING:

    EventMovedOnline.update_forward_refs()
