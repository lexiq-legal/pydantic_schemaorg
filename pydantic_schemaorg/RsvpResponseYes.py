from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.RsvpResponseType import RsvpResponseType


class RsvpResponseYes(RsvpResponseType):
    """The invitee will attend.

    See: https://schema.org/RsvpResponseYes
    Model depth: 5
    """
    type_: str = Field("RsvpResponseYes", alias='@type')
    

