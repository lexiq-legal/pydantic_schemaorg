from pydantic import Field
from pydantic_schemaorg.Event import Event
from typing import List, Optional, Union
from pydantic_schemaorg.CommunicateAction import CommunicateAction


class InviteAction(CommunicateAction):
    """The act of asking someone to attend an event. Reciprocal of RsvpAction.

    See https://schema.org/InviteAction.

    """
    type_: str = Field("InviteAction", const=True, alias='@type')
    event: Optional[Union[List[Union[Event, str]], Union[Event, str]]] = Field(
        None,
        description="Upcoming or past event associated with this place, organization, or action.",
    )
    

InviteAction.update_forward_refs()
