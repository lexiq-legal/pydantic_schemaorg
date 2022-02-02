from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.EventAttendanceModeEnumeration import EventAttendanceModeEnumeration


class OnlineEventAttendanceMode(EventAttendanceModeEnumeration):
    """OnlineEventAttendanceMode - an event that is primarily conducted online.

    See: https://schema.org/OnlineEventAttendanceMode
    Model depth: 5
    """
    type_: str = Field("OnlineEventAttendanceMode", alias='@type')
    

