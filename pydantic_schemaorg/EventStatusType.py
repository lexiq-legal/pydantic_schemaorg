from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.StatusEnumeration import StatusEnumeration


class EventStatusType(StatusEnumeration):
    """EventStatusType is an enumeration type whose instances represent several states that"
     "an Event may be in.

    See: https://schema.org/EventStatusType
    Model depth: 5
    """

    type_: str = Field("EventStatusType", const=True, alias="@type")


if TYPE_CHECKING:

    EventStatusType.update_forward_refs()
