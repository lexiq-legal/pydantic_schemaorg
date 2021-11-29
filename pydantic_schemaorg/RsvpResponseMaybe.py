from pydantic import Field
from pydantic_schemaorg.RsvpResponseType import RsvpResponseType


class RsvpResponseMaybe(RsvpResponseType):
    """The invitee may or may not attend.

    See https://schema.org/RsvpResponseMaybe.

    """

    locals().update({"@type": Field("RsvpResponseMaybe", const=True)})


RsvpResponseMaybe.update_forward_refs()
