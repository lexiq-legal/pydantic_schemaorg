from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.EventStatusType import EventStatusType


class EventCancelled(EventStatusType):
    """The event has been cancelled. If the event has multiple startDate values, all are assumed"
     "to be cancelled. Either startDate or previousStartDate may be used to specify the event's"
     "cancelled date(s).

    See: https://schema.org/EventCancelled
    Model depth: 6
    """
    type_: str = Field("EventCancelled", alias='@type')
    

