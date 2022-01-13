from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional

from pydantic_schemaorg.CommunicateAction import CommunicateAction


class InviteAction(CommunicateAction):
    """The act of asking someone to attend an event. Reciprocal of RsvpAction.

    See: https://schema.org/InviteAction
    Model depth: 5
    """

    type_: str = Field("InviteAction", const=True, alias="@type")
    event: "Optional[Union[List[Union[Event, str]], Union[Event, str]]]" = Field(
        None,
        description="Upcoming or past event associated with this place, organization, or action.",
    )


if TYPE_CHECKING:

    from pydantic_schemaorg.Event import Event

    InviteAction.update_forward_refs()
