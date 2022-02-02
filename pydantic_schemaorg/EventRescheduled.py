from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.EventStatusType import EventStatusType


class EventRescheduled(EventStatusType):
    """The event has been rescheduled. The event's previousStartDate should be set to the old"
     "date and the startDate should be set to the event's new date. (If the event has been rescheduled"
     "multiple times, the previousStartDate property may be repeated).

    See: https://schema.org/EventRescheduled
    Model depth: 6
    """
    type_: str = Field("EventRescheduled", alias='@type')
    

