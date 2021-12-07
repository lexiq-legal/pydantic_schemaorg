from pydantic import Field
from pydantic_schemaorg.EventAttendanceModeEnumeration import EventAttendanceModeEnumeration


class MixedEventAttendanceMode(EventAttendanceModeEnumeration):
    """MixedEventAttendanceMode - an event that is conducted as a combination of both offline"
     "and online modes.

    See https://schema.org/MixedEventAttendanceMode.

    """
    type_: str = Field("MixedEventAttendanceMode", const=True, alias='@type')
    

MixedEventAttendanceMode.update_forward_refs()
