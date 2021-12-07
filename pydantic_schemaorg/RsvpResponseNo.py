from pydantic import Field
from pydantic_schemaorg.RsvpResponseType import RsvpResponseType


class RsvpResponseNo(RsvpResponseType):
    """The invitee will not attend.

    See https://schema.org/RsvpResponseNo.

    """
    type_: str = Field("RsvpResponseNo", const=True, alias='@type')
    

RsvpResponseNo.update_forward_refs()
