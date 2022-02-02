from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, List, Optional


from pydantic import Field
from pydantic_schemaorg.InteractAction import InteractAction


class LeaveAction(InteractAction):
    """An agent leaves an event / group with participants/friends at a location. Related actions:"
     "* [[JoinAction]]: The antonym of LeaveAction. * [[UnRegisterAction]]: Unlike UnRegisterAction,"
     "LeaveAction implies leaving a group/team of people rather than a service.

    See: https://schema.org/LeaveAction
    Model depth: 4
    """
    type_: str = Field("LeaveAction", alias='@type')
    event: Optional[Union[List[Union['Event', str]], 'Event', str]] = Field(
        None,
        description="Upcoming or past event associated with this place, organization, or action.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Event import Event
