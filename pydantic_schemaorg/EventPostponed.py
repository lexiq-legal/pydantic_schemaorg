from pydantic import Field
from pydantic_schemaorg.EventStatusType import EventStatusType


class EventPostponed(EventStatusType):
    """The event has been postponed and no new date has been set. The event's previousStartDate"
     "should be set.

    See https://schema.org/EventPostponed.

    """

    locals().update({"@type": Field("EventPostponed", const=True)})


EventPostponed.update_forward_refs()
