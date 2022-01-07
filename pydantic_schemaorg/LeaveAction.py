from pydantic import Field
from pydantic_schemaorg.Event import Event
from typing import List, Optional, Union
from pydantic_schemaorg.InteractAction import InteractAction


class LeaveAction(InteractAction):
    """An agent leaves an event / group with participants/friends at a location. Related actions:"
     "* [[JoinAction]]: The antonym of LeaveAction. * [[UnRegisterAction]]: Unlike UnRegisterAction,"
     "LeaveAction implies leaving a group/team of people rather than a service.

    See https://schema.org/LeaveAction.

    """
    type_: str = Field("LeaveAction", const=True, alias='@type')
    event: Optional[Union[List[Union[Event, str]], Union[Event, str]]] = Field(
        None,
        description="Upcoming or past event associated with this place, organization, or action.",
    )
    

LeaveAction.update_forward_refs()
