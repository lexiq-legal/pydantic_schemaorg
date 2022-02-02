from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.EventAttendanceModeEnumeration import EventAttendanceModeEnumeration


class OfflineEventAttendanceMode(EventAttendanceModeEnumeration):
    """OfflineEventAttendanceMode - an event that is primarily conducted offline.

    See: https://schema.org/OfflineEventAttendanceMode
    Model depth: 5
    """
    type_: str = Field("OfflineEventAttendanceMode", alias='@type')
    

