from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Clip import Clip


class MovieClip(Clip):
    """A short segment/part of a movie.

    See: https://schema.org/MovieClip
    Model depth: 4
    """
    type_: str = Field("MovieClip", alias='@type')
    

