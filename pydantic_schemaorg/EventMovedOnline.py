from pydantic import Field
from pydantic_schemaorg.EventStatusType import EventStatusType


class EventMovedOnline(EventStatusType):
    """Indicates that the event was changed to allow online participation. See [[eventAttendanceMode]]"
     "for specifics of whether it is now fully or partially online.

    See https://schema.org/EventMovedOnline.

    """
    type_: str = Field("EventMovedOnline", const=True, alias='@type')
    

EventMovedOnline.update_forward_refs()
