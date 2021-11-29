from pydantic import Field
from pydantic_schema_org.EventAttendanceModeEnumeration import EventAttendanceModeEnumeration


class OfflineEventAttendanceMode(EventAttendanceModeEnumeration):
    """OfflineEventAttendanceMode - an event that is primarily conducted offline.

    See https://schema.org/OfflineEventAttendanceMode.

    """

    locals().update({"@type": Field("OfflineEventAttendanceMode", const=True)})


OfflineEventAttendanceMode.update_forward_refs()
