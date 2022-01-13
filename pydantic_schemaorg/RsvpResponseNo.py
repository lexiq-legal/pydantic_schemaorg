from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.RsvpResponseType import RsvpResponseType


class RsvpResponseNo(RsvpResponseType):
    """The invitee will not attend.

    See: https://schema.org/RsvpResponseNo
    Model depth: 5
    """

    type_: str = Field("RsvpResponseNo", const=True, alias="@type")


if TYPE_CHECKING:

    RsvpResponseNo.update_forward_refs()
