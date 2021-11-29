from pydantic import Field
from pydantic_schemaorg.Audience import Audience
from typing import Any, Union, List, Optional
from pydantic_schemaorg.Event import Event
from pydantic_schemaorg.Action import Action


class PlayAction(Action):
    """The act of playing/exercising/training/performing for enjoyment, leisure, recreation,"
     "Competition or exercise. Related actions: * [[ListenAction]]: Unlike ListenAction"
     "(which is under ConsumeAction), PlayAction refers to performing for an audience or"
     "at an event, rather than consuming music. * [[WatchAction]]: Unlike WatchAction (which"
     "is under ConsumeAction), PlayAction refers to showing/displaying for an audience"
     "or at an event, rather than consuming visual content.

    See https://schema.org/PlayAction.

    """

    audience: Optional[Union[List[Audience], Audience]] = Field(
        None,
        description="An intended audience, i.e. a group for whom something was created.",
    )
    event: Optional[Union[List[Event], Event]] = Field(
        None,
        description="Upcoming or past event associated with this place, organization, or action.",
    )
    locals().update({"@type": Field("PlayAction", const=True)})


PlayAction.update_forward_refs()
