from pydantic import Field
from pydantic_schemaorg.Event import Event
from typing import Any, Union, List, Optional
from pydantic_schemaorg.CommunicateAction import CommunicateAction


class InviteAction(CommunicateAction):
    """The act of asking someone to attend an event. Reciprocal of RsvpAction.

    See https://schema.org/InviteAction.

    """

    event: Optional[Union[List[Event], Event]] = Field(
        None,
        description="Upcoming or past event associated with this place, organization, or action.",
    )
    locals().update({"@type": Field("InviteAction", const=True)})


InviteAction.update_forward_refs()
