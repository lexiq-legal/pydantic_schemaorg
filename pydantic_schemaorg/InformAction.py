from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.CommunicateAction import CommunicateAction


class InformAction(CommunicateAction):
    """The act of notifying someone of information pertinent to them, with no expectation of"
     "a response.

    See: https://schema.org/InformAction
    Model depth: 5
    """
    type_: str = Field(default="InformAction", alias='@type', const=True)
    event: Optional[Union[List[Union['Event', str]], 'Event', str]] = Field(
        default=None,
        description="Upcoming or past event associated with this place, organization, or action.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Event import Event
