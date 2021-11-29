from pydantic import Field
from pydantic_schemaorg.RsvpResponseType import RsvpResponseType


class RsvpResponseYes(RsvpResponseType):
    """The invitee will attend.

    See https://schema.org/RsvpResponseYes.

    """

    locals().update({"@type": Field("RsvpResponseYes", const=True)})


RsvpResponseYes.update_forward_refs()
