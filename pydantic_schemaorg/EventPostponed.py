from pydantic import Field
from pydantic_schemaorg.EventStatusType import EventStatusType


class EventPostponed(EventStatusType):
    """The event has been postponed and no new date has been set. The event's previousStartDate"
     "should be set.

    See https://schema.org/EventPostponed.

    """
    type_: str = Field("EventPostponed", const=True, alias='@type')
    

EventPostponed.update_forward_refs()
