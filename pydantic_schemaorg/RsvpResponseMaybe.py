from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.RsvpResponseType import RsvpResponseType


class RsvpResponseMaybe(RsvpResponseType):
    """The invitee may or may not attend.

    See: https://schema.org/RsvpResponseMaybe
    Model depth: 5
    """
    type_: str = Field("RsvpResponseMaybe", alias='@type')
    

