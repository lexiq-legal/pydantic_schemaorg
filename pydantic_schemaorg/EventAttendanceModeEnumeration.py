from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Enumeration import Enumeration


class EventAttendanceModeEnumeration(Enumeration):
    """An EventAttendanceModeEnumeration value is one of potentially several modes of organising"
     "an event, relating to whether it is online or offline.

    See: https://schema.org/EventAttendanceModeEnumeration
    Model depth: 4
    """

    type_: str = Field("EventAttendanceModeEnumeration", const=True, alias="@type")


if TYPE_CHECKING:

    EventAttendanceModeEnumeration.update_forward_refs()
