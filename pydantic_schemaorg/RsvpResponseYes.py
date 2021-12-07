from pydantic import Field
from pydantic_schemaorg.RsvpResponseType import RsvpResponseType


class RsvpResponseYes(RsvpResponseType):
    """The invitee will attend.

    See https://schema.org/RsvpResponseYes.

    """
    type_: str = Field("RsvpResponseYes", const=True, alias='@type')
    

RsvpResponseYes.update_forward_refs()
