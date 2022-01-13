from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.EventAttendanceModeEnumeration import (
    EventAttendanceModeEnumeration,
)


class MixedEventAttendanceMode(EventAttendanceModeEnumeration):
    """MixedEventAttendanceMode - an event that is conducted as a combination of both offline"
     "and online modes.

    See: https://schema.org/MixedEventAttendanceMode
    Model depth: 5
    """

    type_: str = Field("MixedEventAttendanceMode", const=True, alias="@type")


if TYPE_CHECKING:

    MixedEventAttendanceMode.update_forward_refs()
