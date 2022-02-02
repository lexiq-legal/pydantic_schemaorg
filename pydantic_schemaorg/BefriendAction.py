from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.InteractAction import InteractAction


class BefriendAction(InteractAction):
    """The act of forming a personal connection with someone (object) mutually/bidirectionally/symmetrically."
     "Related actions: * [[FollowAction]]: Unlike FollowAction, BefriendAction implies"
     "that the connection is reciprocal.

    See: https://schema.org/BefriendAction
    Model depth: 4
    """
    type_: str = Field("BefriendAction", alias='@type')
    

