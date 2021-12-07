from pydantic import Field
from pydantic_schemaorg.InteractAction import InteractAction


class BefriendAction(InteractAction):
    """The act of forming a personal connection with someone (object) mutually/bidirectionally/symmetrically."
     "Related actions: * [[FollowAction]]: Unlike FollowAction, BefriendAction implies"
     "that the connection is reciprocal.

    See https://schema.org/BefriendAction.

    """
    type_: str = Field("BefriendAction", const=True, alias='@type')
    

BefriendAction.update_forward_refs()
