from pydantic import Field
from pydantic_schemaorg.EventAttendanceModeEnumeration import EventAttendanceModeEnumeration


class OnlineEventAttendanceMode(EventAttendanceModeEnumeration):
    """OnlineEventAttendanceMode - an event that is primarily conducted online.

    See https://schema.org/OnlineEventAttendanceMode.

    """

    locals().update({"@type": Field("OnlineEventAttendanceMode", const=True)})


OnlineEventAttendanceMode.update_forward_refs()
