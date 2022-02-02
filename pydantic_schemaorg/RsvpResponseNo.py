from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.RsvpResponseType import RsvpResponseType


class RsvpResponseNo(RsvpResponseType):
    """The invitee will not attend.

    See: https://schema.org/RsvpResponseNo
    Model depth: 5
    """
    type_: str = Field("RsvpResponseNo", alias='@type')
    

