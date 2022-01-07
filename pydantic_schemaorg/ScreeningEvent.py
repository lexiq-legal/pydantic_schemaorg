from pydantic import Field
from pydantic_schemaorg.Movie import Movie
from typing import List, Optional, Any, Union
from pydantic_schemaorg.Language import Language
from pydantic_schemaorg.Event import Event


class ScreeningEvent(Event):
    """A screening of a movie or other video.

    See https://schema.org/ScreeningEvent.

    """
    type_: str = Field("ScreeningEvent", const=True, alias='@type')
    workPresented: Optional[Union[List[Union[Movie, str]], Union[Movie, str]]] = Field(
        None,
        description="The movie presented during this event.",
    )
    subtitleLanguage: Optional[Union[List[Union[str, Language]], Union[str, Language]]] = Field(
        None,
        description="Languages in which subtitles/captions are available, in [IETF BCP 47 standard format](http://tools.ietf.org/html/bcp47).",
    )
    videoFormat: Optional[Union[List[str], str]] = Field(
        None,
        description="The type of screening or video broadcast used (e.g. IMAX, 3D, SD, HD, etc.).",
    )
    

ScreeningEvent.update_forward_refs()
