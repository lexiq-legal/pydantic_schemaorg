from pydantic import Field
from pydantic_schemaorg.EventAttendanceModeEnumeration import EventAttendanceModeEnumeration


class OnlineEventAttendanceMode(EventAttendanceModeEnumeration):
    """OnlineEventAttendanceMode - an event that is primarily conducted online.

    See https://schema.org/OnlineEventAttendanceMode.

    """
    type_: str = Field("OnlineEventAttendanceMode", const=True, alias='@type')
    

OnlineEventAttendanceMode.update_forward_refs()
