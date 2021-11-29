from pydantic import StrictBool, Field
from typing import Any, Optional, Union, List
from pydantic_schema_org.Language import Language
from pydantic_schema_org.Event import Event
from pydantic_schema_org.PublicationEvent import PublicationEvent


class BroadcastEvent(PublicationEvent):
    """An over the air or online broadcast event.

    See https://schema.org/BroadcastEvent.

    """

    isLiveBroadcast: Optional[Union[List[StrictBool], StrictBool]] = Field(
        None,
        description="True if the broadcast is of a live event.",
    )
    subtitleLanguage: Optional[Union[List[Union[str, Language]], Union[str, Language]]] = Field(
        None,
        description="Languages in which subtitles/captions are available, in [IETF BCP 47 standard format](http://tools.ietf.org/html/bcp47).",
    )
    videoFormat: Optional[Union[List[str], str]] = Field(
        None,
        description="The type of screening or video broadcast used (e.g. IMAX, 3D, SD, HD, etc.).",
    )
    broadcastOfEvent: Optional[Union[List[Event], Event]] = Field(
        None,
        description="The event being broadcast such as a sporting event or awards ceremony.",
    )
    locals().update({"@type": Field("BroadcastEvent", const=True)})


BroadcastEvent.update_forward_refs()
