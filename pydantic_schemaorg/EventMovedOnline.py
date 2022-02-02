from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.EventStatusType import EventStatusType


class EventMovedOnline(EventStatusType):
    """Indicates that the event was changed to allow online participation. See [[eventAttendanceMode]]"
     "for specifics of whether it is now fully or partially online.

    See: https://schema.org/EventMovedOnline
    Model depth: 6
    """
    type_: str = Field("EventMovedOnline", alias='@type')
    

