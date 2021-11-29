from pydantic import Field
from typing import Any, Union, List, Optional
from pydantic_schemaorg.InteractAction import InteractAction


class JoinAction(InteractAction):
    """An agent joins an event/group with participants/friends at a location. Related actions:"
     "* [[RegisterAction]]: Unlike RegisterAction, JoinAction refers to joining a group/team"
     "of people. * [[SubscribeAction]]: Unlike SubscribeAction, JoinAction does not imply"
     "that you'll be receiving updates. * [[FollowAction]]: Unlike FollowAction, JoinAction"
     "does not imply that you'll be polling for updates.

    See https://schema.org/JoinAction.

    """

    event: Any = Field(
        None,
        description="Upcoming or past event associated with this place, organization, or action.",
    )
    locals().update({"@type": Field("JoinAction", const=True)})


JoinAction.update_forward_refs()
