from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List


from pydantic import Field
from pydantic_schemaorg.Action import Action


class PlayAction(Action):
    """The act of playing/exercising/training/performing for enjoyment, leisure, recreation,"
     "Competition or exercise. Related actions: * [[ListenAction]]: Unlike ListenAction"
     "(which is under ConsumeAction), PlayAction refers to performing for an audience or"
     "at an event, rather than consuming music. * [[WatchAction]]: Unlike WatchAction (which"
     "is under ConsumeAction), PlayAction refers to showing/displaying for an audience"
     "or at an event, rather than consuming visual content.

    See: https://schema.org/PlayAction
    Model depth: 3
    """
    type_: str = Field("PlayAction", alias='@type')
    audience: Optional[Union[List[Union['Audience', str]], 'Audience', str]] = Field(
        None,
        description="An intended audience, i.e. a group for whom something was created.",
    )
    event: Optional[Union[List[Union['Event', str]], 'Event', str]] = Field(
        None,
        description="Upcoming or past event associated with this place, organization, or action.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Audience import Audience
    from pydantic_schemaorg.Event import Event
