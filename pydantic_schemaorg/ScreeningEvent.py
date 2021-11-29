from pydantic import Field
from typing import Any, Union, List, Optional
from pydantic_schemaorg.Event import Event


class ScreeningEvent(Event):
    """A screening of a movie or other video.

    See https://schema.org/ScreeningEvent.

    """

    workPresented: Any = Field(
        None,
        description="The movie presented during this event.",
    )
    subtitleLanguage: Union[List[Union[str, Any]], Union[str, Any]] = Field(
        None,
        description="Languages in which subtitles/captions are available, in [IETF BCP 47 standard format](http://tools.ietf.org/html/bcp47).",
    )
    videoFormat: Optional[Union[List[str], str]] = Field(
        None,
        description="The type of screening or video broadcast used (e.g. IMAX, 3D, SD, HD, etc.).",
    )
    locals().update({"@type": Field("ScreeningEvent", const=True)})


ScreeningEvent.update_forward_refs()
