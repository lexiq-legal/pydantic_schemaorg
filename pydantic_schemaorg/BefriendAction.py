from pydantic import Field
from pydantic_schemaorg.InteractAction import InteractAction


class BefriendAction(InteractAction):
    """The act of forming a personal connection with someone (object) mutually/bidirectionally/symmetrically."
     "Related actions: * [[FollowAction]]: Unlike FollowAction, BefriendAction implies"
     "that the connection is reciprocal.

    See https://schema.org/BefriendAction.

    """

    locals().update({"@type": Field("BefriendAction", const=True)})


BefriendAction.update_forward_refs()
