from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Enumeration import Enumeration


class RsvpResponseType(Enumeration):
    """RsvpResponseType is an enumeration type whose instances represent responding to an"
     "RSVP request.

    See: https://schema.org/RsvpResponseType
    Model depth: 4
    """

    type_: str = Field("RsvpResponseType", const=True, alias="@type")


if TYPE_CHECKING:

    RsvpResponseType.update_forward_refs()
