from pydantic import Field
from pydantic_schemaorg.Clip import Clip


class MovieClip(Clip):
    """A short segment/part of a movie.

    See https://schema.org/MovieClip.

    """

    locals().update({"@type": Field("MovieClip", const=True)})


MovieClip.update_forward_refs()
