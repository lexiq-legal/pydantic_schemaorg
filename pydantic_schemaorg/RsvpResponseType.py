from pydantic import Field
from pydantic_schemaorg.Enumeration import Enumeration


class RsvpResponseType(Enumeration):
    """RsvpResponseType is an enumeration type whose instances represent responding to an"
     "RSVP request.

    See https://schema.org/RsvpResponseType.

    """
    type_: str = Field("RsvpResponseType", const=True, alias='@type')
    

RsvpResponseType.update_forward_refs()
