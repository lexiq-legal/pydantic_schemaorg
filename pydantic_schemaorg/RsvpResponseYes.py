from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.RsvpResponseType import RsvpResponseType


class RsvpResponseYes(RsvpResponseType):
    """The invitee will attend.

    See: https://schema.org/RsvpResponseYes
    Model depth: 5
    """

    type_: str = Field("RsvpResponseYes", const=True, alias="@type")


if TYPE_CHECKING:

    RsvpResponseYes.update_forward_refs()
