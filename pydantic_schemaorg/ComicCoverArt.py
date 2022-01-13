from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.CoverArt import CoverArt

from pydantic_schemaorg.ComicStory import ComicStory


class ComicCoverArt(CoverArt, ComicStory):
    """The artwork on the cover of a comic.

    See: https://schema.org/ComicCoverArt
    Model depth: 4
    """

    type_: str = Field("ComicCoverArt", const=True, alias="@type")


if TYPE_CHECKING:

    ComicCoverArt.update_forward_refs()
