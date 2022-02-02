from __future__ import annotations
from typing import TYPE_CHECKING

from decimal import Decimal
from typing import Union, Optional, List


from pydantic import Field
from pydantic_schemaorg.InformAction import InformAction


class RsvpAction(InformAction):
    """The act of notifying an event organizer as to whether you expect to attend the event.

    See: https://schema.org/RsvpAction
    Model depth: 6
    """
    type_: str = Field("RsvpAction", alias='@type')
    additionalNumberOfGuests: Optional[Union[List[Union[Decimal, 'Number', str]], Decimal, 'Number', str]] = Field(
        None,
        description="If responding yes, the number of guests who will attend in addition to the invitee.",
    )
    comment: Optional[Union[List[Union['Comment', str]], 'Comment', str]] = Field(
        None,
        description="Comments, typically from users.",
    )
    rsvpResponse: Optional[Union[List[Union['RsvpResponseType', str]], 'RsvpResponseType', str]] = Field(
        None,
        description="The response (yes, no, maybe) to the RSVP.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Number import Number
    from pydantic_schemaorg.Comment import Comment
    from pydantic_schemaorg.RsvpResponseType import RsvpResponseType
