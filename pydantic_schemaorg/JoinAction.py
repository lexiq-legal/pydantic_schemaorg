from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional

from pydantic_schemaorg.InteractAction import InteractAction


class JoinAction(InteractAction):
    """An agent joins an event/group with participants/friends at a location. Related actions:"
     "* [[RegisterAction]]: Unlike RegisterAction, JoinAction refers to joining a group/team"
     "of people. * [[SubscribeAction]]: Unlike SubscribeAction, JoinAction does not imply"
     "that you'll be receiving updates. * [[FollowAction]]: Unlike FollowAction, JoinAction"
     "does not imply that you'll be polling for updates.

    See: https://schema.org/JoinAction
    Model depth: 4
    """

    type_: str = Field("JoinAction", const=True, alias="@type")
    event: "Optional[Union[List[Union[Event, str]], Union[Event, str]]]" = Field(
        None,
        description="Upcoming or past event associated with this place, organization, or action.",
    )


if TYPE_CHECKING:

    from pydantic_schemaorg.Event import Event

    JoinAction.update_forward_refs()
