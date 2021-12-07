from pydantic import Field
from pydantic_schemaorg.RsvpResponseType import RsvpResponseType


class RsvpResponseMaybe(RsvpResponseType):
    """The invitee may or may not attend.

    See https://schema.org/RsvpResponseMaybe.

    """
    type_: str = Field("RsvpResponseMaybe", const=True, alias='@type')
    

RsvpResponseMaybe.update_forward_refs()
