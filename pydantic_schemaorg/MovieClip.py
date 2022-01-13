from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Clip import Clip


class MovieClip(Clip):
    """A short segment/part of a movie.

    See: https://schema.org/MovieClip
    Model depth: 4
    """

    type_: str = Field("MovieClip", const=True, alias="@type")


if TYPE_CHECKING:

    MovieClip.update_forward_refs()
