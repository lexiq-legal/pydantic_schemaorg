from pydantic import Field
from pydantic_schemaorg.Event import Event
from typing import Any, Union, List, Optional
from pydantic_schemaorg.InteractAction import InteractAction


class LeaveAction(InteractAction):
    """An agent leaves an event / group with participants/friends at a location. Related actions:"
     "* [[JoinAction]]: The antonym of LeaveAction. * [[UnRegisterAction]]: Unlike UnRegisterAction,"
     "LeaveAction implies leaving a group/team of people rather than a service.

    See https://schema.org/LeaveAction.

    """

    event: Optional[Union[List[Event], Event]] = Field(
        None,
        description="Upcoming or past event associated with this place, organization, or action.",
    )
    locals().update({"@type": Field("LeaveAction", const=True)})


LeaveAction.update_forward_refs()
