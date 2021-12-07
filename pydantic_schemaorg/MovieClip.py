from pydantic import Field
from pydantic_schemaorg.Clip import Clip


class MovieClip(Clip):
    """A short segment/part of a movie.

    See https://schema.org/MovieClip.

    """
    type_: str = Field("MovieClip", const=True, alias='@type')
    

MovieClip.update_forward_refs()
