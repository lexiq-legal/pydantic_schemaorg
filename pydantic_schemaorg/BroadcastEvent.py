from __future__ import annotations
from typing import TYPE_CHECKING

from pydantic import StrictBool
from typing import Union, Optional, List


from pydantic import Field
from pydantic_schemaorg.PublicationEvent import PublicationEvent


class BroadcastEvent(PublicationEvent):
    """An over the air or online broadcast event.

    See: https://schema.org/BroadcastEvent
    Model depth: 4
    """
    type_: str = Field("BroadcastEvent", alias='@type')
    isLiveBroadcast: Optional[Union[List[Union[StrictBool, 'Boolean', str]], StrictBool, 'Boolean', str]] = Field(
        None,
        description="True if the broadcast is of a live event.",
    )
    subtitleLanguage: Optional[Union[List[Union[str, 'Text', 'Language']], str, 'Text', 'Language']] = Field(
        None,
        description="Languages in which subtitles/captions are available, in [IETF BCP 47 standard format](http://tools.ietf.org/html/bcp47).",
    )
    videoFormat: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="The type of screening or video broadcast used (e.g. IMAX, 3D, SD, HD, etc.).",
    )
    broadcastOfEvent: Optional[Union[List[Union['Event', str]], 'Event', str]] = Field(
        None,
        description="The event being broadcast such as a sporting event or awards ceremony.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Boolean import Boolean
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Language import Language
    from pydantic_schemaorg.Event import Event
