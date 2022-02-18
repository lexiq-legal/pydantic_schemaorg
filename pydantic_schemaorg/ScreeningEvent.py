from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.Event import Event


class ScreeningEvent(Event):
    """A screening of a movie or other video.

    See: https://schema.org/ScreeningEvent
    Model depth: 3
    """
    type_: str = Field(default="ScreeningEvent", alias='@type', const=True)
    workPresented: Optional[Union[List[Union['Movie', str]], 'Movie', str]] = Field(
        default=None,
        description="The movie presented during this event.",
    )
    subtitleLanguage: Optional[Union[List[Union[str, 'Text', 'Language']], str, 'Text', 'Language']] = Field(
        default=None,
        description="Languages in which subtitles/captions are available, in [IETF BCP 47 standard format](http://tools.ietf.org/html/bcp47).",
    )
    videoFormat: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The type of screening or video broadcast used (e.g. IMAX, 3D, SD, HD, etc.).",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Movie import Movie
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Language import Language
